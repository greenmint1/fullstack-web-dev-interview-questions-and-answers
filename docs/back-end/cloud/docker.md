# Docker Interview Questions and Answers

_Last updated: October 28, 2026_

450 Docker interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target current Docker: Docker Engine 29, Docker Compose v2 and later (the `docker compose` plugin, current releases are v5), BuildKit and Buildx, and Docker Desktop. Older things like Compose v1 (`docker-compose`), the `version` key in Compose files and the legacy builder are mentioned where they still matter, since you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Docker?](#1-what-is-docker)
- [2: What problem does Docker solve?](#2-what-problem-does-docker-solve)
- [3: What is a container?](#3-what-is-a-container)
- [4: What is a Docker image?](#4-what-is-a-docker-image)
- [5: What is the difference between an image and a container?](#5-what-is-the-difference-between-an-image-and-a-container)
- [6: What is the difference between a container and a virtual machine?](#6-what-is-the-difference-between-a-container-and-a-virtual-machine)
- [7: What is a Dockerfile?](#7-what-is-a-dockerfile)
- [8: What is Docker Hub?](#8-what-is-docker-hub)
- [9: What is a container registry?](#9-what-is-a-container-registry)
- [10: How do you install Docker?](#10-how-do-you-install-docker)
- [11: What does docker run do?](#11-what-does-docker-run-do)
- [12: What are the most common options for docker run?](#12-what-are-the-most-common-options-for-docker-run)
- [13: How do you list running containers?](#13-how-do-you-list-running-containers)
- [14: How do you stop and start a container?](#14-how-do-you-stop-and-start-a-container)
- [15: What is the difference between docker stop and docker kill?](#15-what-is-the-difference-between-docker-stop-and-docker-kill)
- [16: How do you remove a container?](#16-how-do-you-remove-a-container)
- [17: How do you list and remove images?](#17-how-do-you-list-and-remove-images)
- [18: What does docker pull do?](#18-what-does-docker-pull-do)
- [19: What is an image tag?](#19-what-is-an-image-tag)
- [20: What is the latest tag?](#20-what-is-the-latest-tag)
- [21: How do you build an image?](#21-how-do-you-build-an-image)
- [22: What is the build context?](#22-what-is-the-build-context)
- [23: What is a .dockerignore file?](#23-what-is-a-dockerignore-file)
- [24: What does the FROM instruction do?](#24-what-does-the-from-instruction-do)
- [25: What does the RUN instruction do?](#25-what-does-the-run-instruction-do)
- [26: What does the CMD instruction do?](#26-what-does-the-cmd-instruction-do)
- [27: What does the ENTRYPOINT instruction do?](#27-what-does-the-entrypoint-instruction-do)
- [28: What is the difference between CMD and ENTRYPOINT?](#28-what-is-the-difference-between-cmd-and-entrypoint)
- [29: What is the difference between the exec form and the shell form?](#29-what-is-the-difference-between-the-exec-form-and-the-shell-form)
- [30: What does COPY do?](#30-what-does-copy-do)
- [31: What is the difference between COPY and ADD?](#31-what-is-the-difference-between-copy-and-add)
- [32: What does WORKDIR do?](#32-what-does-workdir-do)
- [33: What does ENV do?](#33-what-does-env-do)
- [34: What does ARG do?](#34-what-does-arg-do)
- [35: What is the difference between ARG and ENV?](#35-what-is-the-difference-between-arg-and-env)
- [36: What does EXPOSE do?](#36-what-does-expose-do)
- [37: How do you publish a port?](#37-how-do-you-publish-a-port)
- [38: How do you see the logs of a container?](#38-how-do-you-see-the-logs-of-a-container)
- [39: How do you run a command inside a running container?](#39-how-do-you-run-a-command-inside-a-running-container)
- [40: What is the difference between docker exec and docker attach?](#40-what-is-the-difference-between-docker-exec-and-docker-attach)
- [41: How do you get detailed information about a container?](#41-how-do-you-get-detailed-information-about-a-container)
- [42: What is a volume?](#42-what-is-a-volume)
- [43: What is a bind mount?](#43-what-is-a-bind-mount)
- [44: What is the difference between a volume and a bind mount?](#44-what-is-the-difference-between-a-volume-and-a-bind-mount)
- [45: What is a tmpfs mount?](#45-what-is-a-tmpfs-mount)
- [46: What happens to data inside a container when it is removed?](#46-what-happens-to-data-inside-a-container-when-it-is-removed)
- [47: What is the difference between -v and --mount?](#47-what-is-the-difference-between--v-and---mount)
- [48: How do you list and remove volumes?](#48-how-do-you-list-and-remove-volumes)
- [49: What is Docker Compose?](#49-what-is-docker-compose)
- [50: What is the difference between docker-compose and docker compose?](#50-what-is-the-difference-between-docker-compose-and-docker-compose)
- [51: What is the compose.yaml file?](#51-what-is-the-composeyaml-file)
- [52: Do you still need the version field in a Compose file?](#52-do-you-still-need-the-version-field-in-a-compose-file)
- [53: What are the most common docker compose commands?](#53-what-are-the-most-common-docker-compose-commands)
- [54: What is the difference between docker compose up and docker compose start?](#54-what-is-the-difference-between-docker-compose-up-and-docker-compose-start)
- [55: What does docker compose down do?](#55-what-does-docker-compose-down-do)
- [56: What is a service in Docker Compose?](#56-what-is-a-service-in-docker-compose)
- [57: How do containers in the same Compose project talk to each other?](#57-how-do-containers-in-the-same-compose-project-talk-to-each-other)
- [58: What is the official image of a technology on Docker Hub?](#58-what-is-the-official-image-of-a-technology-on-docker-hub)
- [59: What is a base image?](#59-what-is-a-base-image)
- [60: What is an Alpine image and why is it popular?](#60-what-is-an-alpine-image-and-why-is-it-popular)
- [61: What does slim mean in image tags like python:3.13-slim?](#61-what-does-slim-mean-in-image-tags-like-python313-slim)
- [62: How do you tag an image?](#62-how-do-you-tag-an-image)
- [63: How do you push an image to a registry?](#63-how-do-you-push-an-image-to-a-registry)
- [64: What is the full name of an image?](#64-what-is-the-full-name-of-an-image)
- [65: What is a dangling image?](#65-what-is-a-dangling-image)
- [66: How do you check how much disk space Docker uses?](#66-how-do-you-check-how-much-disk-space-docker-uses)
- [67: What does docker system prune do?](#67-what-does-docker-system-prune-do)
- [68: What is a restart policy?](#68-what-is-a-restart-policy)
- [69: What is the difference between restart always and unless-stopped?](#69-what-is-the-difference-between-restart-always-and-unless-stopped)
- [70: How do you pass environment variables to a container?](#70-how-do-you-pass-environment-variables-to-a-container)
- [71: What is the .env file in Docker Compose?](#71-what-is-the-env-file-in-docker-compose)
- [72: How do you rename a container?](#72-how-do-you-rename-a-container)
- [73: What is a container ID?](#73-what-is-a-container-id)
- [74: How do you copy files between a container and the host?](#74-how-do-you-copy-files-between-a-container-and-the-host)
- [75: How do you see resource usage of containers?](#75-how-do-you-see-resource-usage-of-containers)
- [76: How do you limit the memory and CPU of a container?](#76-how-do-you-limit-the-memory-and-cpu-of-a-container)
- [77: What does docker run -it do?](#77-what-does-docker-run--it-do)
- [78: What does docker run --rm do?](#78-what-does-docker-run---rm-do)
- [79: What is the default network for docker run?](#79-what-is-the-default-network-for-docker-run)
- [80: What network drivers does Docker have?](#80-what-network-drivers-does-docker-have)
- [81: How do you create a network and connect containers to it?](#81-how-do-you-create-a-network-and-connect-containers-to-it)
- [82: What is the host network mode?](#82-what-is-the-host-network-mode)
- [83: What is the docker version command and how is it different from docker info?](#83-what-is-the-docker-version-command-and-how-is-it-different-from-docker-info)
- [84: What is Docker Desktop?](#84-what-is-docker-desktop)
- [85: Why does Docker on macOS and Windows need a virtual machine?](#85-why-does-docker-on-macos-and-windows-need-a-virtual-machine)
- [86: What is a layer in a Docker image?](#86-what-is-a-layer-in-a-docker-image)
- [87: What is the build cache?](#87-what-is-the-build-cache)
- [88: How do you build without using the cache?](#88-how-do-you-build-without-using-the-cache)
- [89: What does docker image history show?](#89-what-does-docker-image-history-show)
- [90: What does docker commit do and should you use it?](#90-what-does-docker-commit-do-and-should-you-use-it)
- [91: How do you save an image to a file and load it back?](#91-how-do-you-save-an-image-to-a-file-and-load-it-back)
- [92: What is the difference between docker save and docker export?](#92-what-is-the-difference-between-docker-save-and-docker-export)
- [93: What is a healthcheck?](#93-what-is-a-healthcheck)
- [94: What does the USER instruction do?](#94-what-does-the-user-instruction-do)
- [95: What does the LABEL instruction do?](#95-what-does-the-label-instruction-do)
- [96: What does the VOLUME instruction do?](#96-what-does-the-volume-instruction-do)
- [97: What is a multi-stage build?](#97-what-is-a-multi-stage-build)
- [98: Why should a container run only one main process?](#98-why-should-a-container-run-only-one-main-process)
- [99: What is the difference between docker create and docker run?](#99-what-is-the-difference-between-docker-create-and-docker-run)
- [100: How do you see which ports a container publishes?](#100-how-do-you-see-which-ports-a-container-publishes)
- [101: What is the Docker daemon?](#101-what-is-the-docker-daemon)
- [102: How does the Docker CLI talk to the daemon?](#102-how-does-the-docker-cli-talk-to-the-daemon)
- [103: What is a Docker context?](#103-what-is-a-docker-context)
- [104: Why do you need sudo for docker commands on Linux?](#104-why-do-you-need-sudo-for-docker-commands-on-linux)
- [105: What is the docker group?](#105-what-is-the-docker-group)
- [106: What does docker run -d mean and how do you get back to the container?](#106-what-does-docker-run--d-mean-and-how-do-you-get-back-to-the-container)
- [107: How do you pause and unpause a container?](#107-how-do-you-pause-and-unpause-a-container)
- [108: What container states exist?](#108-what-container-states-exist)
- [109: What does the exit code of a container mean?](#109-what-does-the-exit-code-of-a-container-mean)
- [110: How do you run a one-off command with docker run?](#110-how-do-you-run-a-one-off-command-with-docker-run)
- [111: How do you override the entrypoint of an image?](#111-how-do-you-override-the-entrypoint-of-an-image)
- [112: What is the scratch image?](#112-what-is-the-scratch-image)
- [113: What is a distroless image?](#113-what-is-a-distroless-image)
- [114: How do you name a container and why does it matter?](#114-how-do-you-name-a-container-and-why-does-it-matter)
- [115: What happens if you run docker run twice with the same name?](#115-what-happens-if-you-run-docker-run-twice-with-the-same-name)
- [116: How do you view the processes inside a container?](#116-how-do-you-view-the-processes-inside-a-container)
- [117: What is the docker events command?](#117-what-is-the-docker-events-command)
- [118: How do you filter docker ps output?](#118-how-do-you-filter-docker-ps-output)
- [119: What does docker run --env-file do?](#119-what-does-docker-run---env-file-do)
- [120: What is an anonymous volume?](#120-what-is-an-anonymous-volume)
- [121: Where does Docker store volumes on Linux?](#121-where-does-docker-store-volumes-on-linux)
- [122: How do you make a mount read-only?](#122-how-do-you-make-a-mount-read-only)
- [123: How do you see the networks on a host?](#123-how-do-you-see-the-networks-on-a-host)
- [124: How do you remove a network?](#124-how-do-you-remove-a-network)
- [125: What is port mapping and why do you need it?](#125-what-is-port-mapping-and-why-do-you-need-it)
- [126: What does 0.0.0.0 mean in port mappings?](#126-what-does-0000-mean-in-port-mappings)
- [127: How do you start a database for local development with Docker?](#127-how-do-you-start-a-database-for-local-development-with-docker)
- [128: What is the depends_on option in Compose?](#128-what-is-the-depends_on-option-in-compose)
- [129: How do you build images with Compose?](#129-how-do-you-build-images-with-compose)
- [130: How do you define volumes in Compose?](#130-how-do-you-define-volumes-in-compose)
- [131: How do you define ports and environment variables in Compose?](#131-how-do-you-define-ports-and-environment-variables-in-compose)
- [132: How do you see logs for all services in Compose?](#132-how-do-you-see-logs-for-all-services-in-compose)
- [133: What is a Compose project name?](#133-what-is-a-compose-project-name)
- [134: How do you run a one-off command in a Compose service?](#134-how-do-you-run-a-one-off-command-in-a-compose-service)
- [135: What is the image digest?](#135-what-is-the-image-digest)
- [136: How do you see the IP address of a container?](#136-how-do-you-see-the-ip-address-of-a-container)
- [137: What is the difference between docker image ls and docker images?](#137-what-is-the-difference-between-docker-image-ls-and-docker-images)
- [138: What is the hello-world image?](#138-what-is-the-hello-world-image)
- [139: What is a Dockerfile comment and a parser directive?](#139-what-is-a-dockerfile-comment-and-a-parser-directive)
- [140: Can a Dockerfile have more than one CMD?](#140-can-a-dockerfile-have-more-than-one-cmd)
- [141: What does the SHELL instruction do?](#141-what-does-the-shell-instruction-do)
- [142: What is the STOPSIGNAL instruction?](#142-what-is-the-stopsignal-instruction)
- [143: How do you update an image to a newer version?](#143-how-do-you-update-an-image-to-a-newer-version)
- [144: What is Docker Swarm?](#144-what-is-docker-swarm)
- [145: What is the relationship between Docker and Kubernetes?](#145-what-is-the-relationship-between-docker-and-kubernetes)
- [146: What is OCI?](#146-what-is-oci)
- [147: What are some alternatives to Docker?](#147-what-are-some-alternatives-to-docker)
- [148: How do you log in to a registry?](#148-how-do-you-log-in-to-a-registry)
- [149: How do you check the Docker Compose version?](#149-how-do-you-check-the-docker-compose-version)
- [150: What is docker init?](#150-what-is-docker-init)

### Moderate Questions (151-300)

- [151: How do you write a good Dockerfile for a Node.js app?](#151-how-do-you-write-a-good-dockerfile-for-a-nodejs-app)
- [152: How do you order Dockerfile instructions to get the most out of the cache?](#152-how-do-you-order-dockerfile-instructions-to-get-the-most-out-of-the-cache)
- [153: How does Docker decide whether a cached layer can be reused?](#153-how-does-docker-decide-whether-a-cached-layer-can-be-reused)
- [154: Why should you combine apt-get update and apt-get install in one RUN?](#154-why-should-you-combine-apt-get-update-and-apt-get-install-in-one-run)
- [155: How do you make images smaller?](#155-how-do-you-make-images-smaller)
- [156: What is BuildKit?](#156-what-is-buildkit)
- [157: What is Buildx?](#157-what-is-buildx)
- [158: How do you build an image for a different CPU architecture?](#158-how-do-you-build-an-image-for-a-different-cpu-architecture)
- [159: What is a multi-platform image?](#159-what-is-a-multi-platform-image)
- [160: How do you pass secrets to a build safely?](#160-how-do-you-pass-secrets-to-a-build-safely)
- [161: What is a cache mount?](#161-what-is-a-cache-mount)
- [162: What is an SSH mount in a build?](#162-what-is-an-ssh-mount-in-a-build)
- [163: What is a bind mount in a RUN instruction?](#163-what-is-a-bind-mount-in-a-run-instruction)
- [164: How do you build only one stage of a multi-stage Dockerfile?](#164-how-do-you-build-only-one-stage-of-a-multi-stage-dockerfile)
- [165: How do you use a named stage as a base for another stage?](#165-how-do-you-use-a-named-stage-as-a-base-for-another-stage)
- [166: How can you copy files from another image in a Dockerfile?](#166-how-can-you-copy-files-from-another-image-in-a-dockerfile)
- [167: What is the difference between docker build --pull and a normal build?](#167-what-is-the-difference-between-docker-build---pull-and-a-normal-build)
- [168: How do you write a Python Dockerfile?](#168-how-do-you-write-a-python-dockerfile)
- [169: Why does my app work inside the container but not from the host?](#169-why-does-my-app-work-inside-the-container-but-not-from-the-host)
- [170: How do you wait for a database to be ready before starting the app in Compose?](#170-how-do-you-wait-for-a-database-to-be-ready-before-starting-the-app-in-compose)
- [171: What conditions can you use in depends_on?](#171-what-conditions-can-you-use-in-depends_on)
- [172: How do you use several Compose files together?](#172-how-do-you-use-several-compose-files-together)
- [173: How are values merged when you combine Compose files?](#173-how-are-values-merged-when-you-combine-compose-files)
- [174: What is the include key in Compose?](#174-what-is-the-include-key-in-compose)
- [175: What does docker compose config do?](#175-what-does-docker-compose-config-do)
- [176: How does variable substitution work in Compose files?](#176-how-does-variable-substitution-work-in-compose-files)
- [177: What is the order of precedence for environment variables in Compose?](#177-what-is-the-order-of-precedence-for-environment-variables-in-compose)
- [178: What are profiles in Compose?](#178-what-are-profiles-in-compose)
- [179: What is Compose Watch?](#179-what-is-compose-watch)
- [180: When should you use Compose Watch instead of a bind mount?](#180-when-should-you-use-compose-watch-instead-of-a-bind-mount)
- [181: How do you scale a service in Compose?](#181-how-do-you-scale-a-service-in-compose)
- [182: How do you set resource limits in Compose?](#182-how-do-you-set-resource-limits-in-compose)
- [183: How do you use secrets in Compose?](#183-how-do-you-use-secrets-in-compose)
- [184: What are configs in Compose?](#184-what-are-configs-in-compose)
- [185: How do you define custom networks in Compose?](#185-how-do-you-define-custom-networks-in-compose)
- [186: How do you connect services from different Compose projects?](#186-how-do-you-connect-services-from-different-compose-projects)
- [187: What is the difference between ports and expose in Compose?](#187-what-is-the-difference-between-ports-and-expose-in-compose)
- [188: How do you override the command of a service in Compose?](#188-how-do-you-override-the-command-of-a-service-in-compose)
- [189: How do you extend a service from another file in Compose?](#189-how-do-you-extend-a-service-from-another-file-in-compose)
- [190: What are x- extension fields in Compose?](#190-what-are-x--extension-fields-in-compose)
- [191: How do you debug a container that exits right after starting?](#191-how-do-you-debug-a-container-that-exits-right-after-starting)
- [192: Why does a container stop right away when the main process runs in the background?](#192-why-does-a-container-stop-right-away-when-the-main-process-runs-in-the-background)
- [193: How do you write an entrypoint script?](#193-how-do-you-write-an-entrypoint-script)
- [194: Why does my entrypoint script fail with "no such file or directory" when the file exists?](#194-why-does-my-entrypoint-script-fail-with-no-such-file-or-directory-when-the-file-exists)
- [195: What is PID 1 in a container and why does it matter?](#195-what-is-pid-1-in-a-container-and-why-does-it-matter)
- [196: What does docker run --init do?](#196-what-does-docker-run---init-do)
- [197: How do you handle graceful shutdown in a containerized Node.js app?](#197-how-do-you-handle-graceful-shutdown-in-a-containerized-nodejs-app)
- [198: How do you see why a container was killed?](#198-how-do-you-see-why-a-container-was-killed)
- [199: How do you limit the size of container logs?](#199-how-do-you-limit-the-size-of-container-logs)
- [200: What logging drivers does Docker support?](#200-what-logging-drivers-does-docker-support)
- [201: How do user-defined bridge networks differ from the default bridge?](#201-how-do-user-defined-bridge-networks-differ-from-the-default-bridge)
- [202: How does DNS work between containers?](#202-how-does-dns-work-between-containers)
- [203: What is a network alias?](#203-what-is-a-network-alias)
- [204: How does a container reach a service running on the host?](#204-how-does-a-container-reach-a-service-running-on-the-host)
- [205: How does port publishing work under the hood on Linux?](#205-how-does-port-publishing-work-under-the-hood-on-linux)
- [206: Why can published Docker ports ignore UFW rules?](#206-why-can-published-docker-ports-ignore-ufw-rules)
- [207: What is the none network and when is it useful?](#207-what-is-the-none-network-and-when-is-it-useful)
- [208: What is the macvlan network driver?](#208-what-is-the-macvlan-network-driver)
- [209: How do you set a fixed IP for a container?](#209-how-do-you-set-a-fixed-ip-for-a-container)
- [210: How do you enable IPv6 for containers?](#210-how-do-you-enable-ipv6-for-containers)
- [211: How do you share a volume between containers?](#211-how-do-you-share-a-volume-between-containers)
- [212: How do you back up a volume?](#212-how-do-you-back-up-a-volume)
- [213: What is a volume driver?](#213-what-is-a-volume-driver)
- [214: How do file permissions work with bind mounts?](#214-how-do-file-permissions-work-with-bind-mounts)
- [215: What happens when you mount a volume over a folder that already has files in the image?](#215-what-happens-when-you-mount-a-volume-over-a-folder-that-already-has-files-in-the-image)
- [216: How do you keep node_modules from the image when you bind mount your source code?](#216-how-do-you-keep-node_modules-from-the-image-when-you-bind-mount-your-source-code)
- [217: How do you set up hot reload for development with Docker?](#217-how-do-you-set-up-hot-reload-for-development-with-docker)
- [218: How do you debug a Node.js app running in a container?](#218-how-do-you-debug-a-nodejs-app-running-in-a-container)
- [219: What is a dev container?](#219-what-is-a-dev-container)
- [220: How do you run tests in Docker?](#220-how-do-you-run-tests-in-docker)
- [221: What is Testcontainers?](#221-what-is-testcontainers)
- [222: How do you build and push an image in GitHub Actions?](#222-how-do-you-build-and-push-an-image-in-github-actions)
- [223: How do you speed up Docker builds in CI?](#223-how-do-you-speed-up-docker-builds-in-ci)
- [224: What cache backends does BuildKit support?](#224-what-cache-backends-does-buildkit-support)
- [225: How should you tag images in a CI pipeline?](#225-how-should-you-tag-images-in-a-ci-pipeline)
- [226: What is Docker Scout?](#226-what-is-docker-scout)
- [227: How do you scan an image for vulnerabilities?](#227-how-do-you-scan-an-image-for-vulnerabilities)
- [228: What is an SBOM and how do you create one for an image?](#228-what-is-an-sbom-and-how-do-you-create-one-for-an-image)
- [229: What is provenance in Docker builds?](#229-what-is-provenance-in-docker-builds)
- [230: How do you check what changed in a container's filesystem?](#230-how-do-you-check-what-changed-in-a-containers-filesystem)
- [231: How do you run a container with a read-only filesystem?](#231-how-do-you-run-a-container-with-a-read-only-filesystem)
- [232: How do you run a container as a non-root user without changing the image?](#232-how-do-you-run-a-container-as-a-non-root-user-without-changing-the-image)
- [233: What are Linux capabilities in Docker?](#233-what-are-linux-capabilities-in-docker)
- [234: What does --privileged do and why is it dangerous?](#234-what-does---privileged-do-and-why-is-it-dangerous)
- [235: How do you give a container access to a host device?](#235-how-do-you-give-a-container-access-to-a-host-device)
- [236: How do you use a GPU in a container?](#236-how-do-you-use-a-gpu-in-a-container)
- [237: How do you use the Docker CLI from inside a container?](#237-how-do-you-use-the-docker-cli-from-inside-a-container)
- [238: What is Docker-in-Docker?](#238-what-is-docker-in-docker)
- [239: How do you limit the number of processes in a container?](#239-how-do-you-limit-the-number-of-processes-in-a-container)
- [240: How do you set ulimits for a container?](#240-how-do-you-set-ulimits-for-a-container)
- [241: How do you set kernel parameters for a container?](#241-how-do-you-set-kernel-parameters-for-a-container)
- [242: How do you set the timezone in a container?](#242-how-do-you-set-the-timezone-in-a-container)
- [243: What is the difference between docker compose stop and docker compose down?](#243-what-is-the-difference-between-docker-compose-stop-and-docker-compose-down)
- [244: How do you recreate a single service in Compose?](#244-how-do-you-recreate-a-single-service-in-compose)
- [245: How do you stop Compose from removing containers that are no longer in the file?](#245-how-do-you-stop-compose-from-removing-containers-that-are-no-longer-in-the-file)
- [246: How do you see the logs of a container that keeps restarting?](#246-how-do-you-see-the-logs-of-a-container-that-keeps-restarting)
- [247: How do you clean up Docker on a build server?](#247-how-do-you-clean-up-docker-on-a-build-server)
- [248: How do you set default address pools for Docker networks?](#248-how-do-you-set-default-address-pools-for-docker-networks)
- [249: What is daemon.json?](#249-what-is-daemonjson)
- [250: What is live-restore?](#250-what-is-live-restore)
- [251: How do you use a registry mirror or pull-through cache?](#251-how-do-you-use-a-registry-mirror-or-pull-through-cache)
- [252: How do you run a private registry?](#252-how-do-you-run-a-private-registry)
- [253: What is an insecure registry?](#253-what-is-an-insecure-registry)
- [254: What are credential helpers?](#254-what-are-credential-helpers)
- [255: What are Docker Hub rate limits and how do you deal with them?](#255-what-are-docker-hub-rate-limits-and-how-do-you-deal-with-them)
- [256: How do you pin a base image to a digest and still get updates?](#256-how-do-you-pin-a-base-image-to-a-digest-and-still-get-updates)
- [257: How do you inspect an image in a registry without pulling it?](#257-how-do-you-inspect-an-image-in-a-registry-without-pulling-it)
- [258: What is docker buildx bake?](#258-what-is-docker-buildx-bake)
- [259: How do you create and use a separate Buildx builder?](#259-how-do-you-create-and-use-a-separate-buildx-builder)
- [260: What build outputs does Buildx support?](#260-what-build-outputs-does-buildx-support)
- [261: How do you get build artifacts out of a Docker build without running a container?](#261-how-do-you-get-build-artifacts-out-of-a-docker-build-without-running-a-container)
- [262: What are build checks?](#262-what-are-build-checks)
- [263: How do you use heredocs in a Dockerfile?](#263-how-do-you-use-heredocs-in-a-dockerfile)
- [264: What does COPY --link do?](#264-what-does-copy---link-do)
- [265: What does COPY --parents or --exclude do?](#265-what-does-copy---parents-or---exclude-do)
- [266: How do you use ONBUILD?](#266-how-do-you-use-onbuild)
- [267: How do you write a Dockerfile for a Go app?](#267-how-do-you-write-a-dockerfile-for-a-go-app)
- [268: How do you write a Dockerfile for a Java Spring Boot app?](#268-how-do-you-write-a-dockerfile-for-a-java-spring-boot-app)
- [269: How do you serve a single-page app from a container?](#269-how-do-you-serve-a-single-page-app-from-a-container)
- [270: How do you handle runtime config for a frontend app in a container?](#270-how-do-you-handle-runtime-config-for-a-frontend-app-in-a-container)
- [271: How do you put a reverse proxy in front of several containers?](#271-how-do-you-put-a-reverse-proxy-in-front-of-several-containers)
- [272: How do you run database migrations in a containerized setup?](#272-how-do-you-run-database-migrations-in-a-containerized-setup)
- [273: How do you deploy with Docker Compose to a single server?](#273-how-do-you-deploy-with-docker-compose-to-a-single-server)
- [274: How do you run Compose against a remote server?](#274-how-do-you-run-compose-against-a-remote-server)
- [275: How do you get a basic zero-downtime deploy with Compose?](#275-how-do-you-get-a-basic-zero-downtime-deploy-with-compose)
- [276: How do you see which image versions are running?](#276-how-do-you-see-which-image-versions-are-running)
- [277: How do you add a healthcheck to an image that has no curl?](#277-how-do-you-add-a-healthcheck-to-an-image-that-has-no-curl)
- [278: What are the healthcheck options?](#278-what-are-the-healthcheck-options)
- [279: Does Docker restart an unhealthy container?](#279-does-docker-restart-an-unhealthy-container)
- [280: How do you handle environment-specific config for the same image?](#280-how-do-you-handle-environment-specific-config-for-the-same-image)
- [281: What is the twelve-factor app and how does it relate to Docker?](#281-what-is-the-twelve-factor-app-and-how-does-it-relate-to-docker)
- [282: How do you collect logs from many containers?](#282-how-do-you-collect-logs-from-many-containers)
- [283: How do you monitor container metrics?](#283-how-do-you-monitor-container-metrics)
- [284: How do you give a container a custom hostname or extra hosts entries?](#284-how-do-you-give-a-container-a-custom-hostname-or-extra-hosts-entries)
- [285: How do you set custom DNS servers for containers?](#285-how-do-you-set-custom-dns-servers-for-containers)
- [286: What is the difference between docker compose run and docker compose up for one service?](#286-what-is-the-difference-between-docker-compose-run-and-docker-compose-up-for-one-service)
- [287: How do you share a Compose app with someone who does not have the source code?](#287-how-do-you-share-a-compose-app-with-someone-who-does-not-have-the-source-code)
- [288: How do you run a cron job with Docker?](#288-how-do-you-run-a-cron-job-with-docker)
- [289: How do you run more than one process in one container if you really must?](#289-how-do-you-run-more-than-one-process-in-one-container-if-you-really-must)
- [290: What is the difference between a Docker image ID and a digest?](#290-what-is-the-difference-between-a-docker-image-id-and-a-digest)
- [291: How do you find out why an image is so large?](#291-how-do-you-find-out-why-an-image-is-so-large)
- [292: Does deleting a file in a later layer make the image smaller?](#292-does-deleting-a-file-in-a-later-layer-make-the-image-smaller)
- [293: How do you build an image for a monorepo?](#293-how-do-you-build-an-image-for-a-monorepo)
- [294: What is a per-Dockerfile ignore file?](#294-what-is-a-per-dockerfile-ignore-file)
- [295: How do you use named build contexts?](#295-how-do-you-use-named-build-contexts)
- [296: How do you build from a Git repository directly?](#296-how-do-you-build-from-a-git-repository-directly)
- [297: How do you prevent secrets from leaking into images?](#297-how-do-you-prevent-secrets-from-leaking-into-images)
- [298: What is the difference between docker compose build and docker build?](#298-what-is-the-difference-between-docker-compose-build-and-docker-build)
- [299: How do you pass build arguments in Compose?](#299-how-do-you-pass-build-arguments-in-compose)
- [300: What are lifecycle hooks in Compose?](#300-what-are-lifecycle-hooks-in-compose)

### Advanced Questions (301-450)

- [301: What happens step by step when you run docker run nginx?](#301-what-happens-step-by-step-when-you-run-docker-run-nginx)
- [302: What are Linux namespaces and which ones do containers use?](#302-what-are-linux-namespaces-and-which-ones-do-containers-use)
- [303: What are cgroups and how does Docker use them?](#303-what-are-cgroups-and-how-does-docker-use-them)
- [304: What is the difference between namespaces and cgroups?](#304-what-is-the-difference-between-namespaces-and-cgroups)
- [305: What is the architecture of the Docker engine?](#305-what-is-the-architecture-of-the-docker-engine)
- [306: What is runc?](#306-what-is-runc)
- [307: What is containerd and how does it relate to Docker?](#307-what-is-containerd-and-how-does-it-relate-to-docker)
- [308: What is the containerd image store in Docker?](#308-what-is-the-containerd-image-store-in-docker)
- [309: What is a storage driver?](#309-what-is-a-storage-driver)
- [310: How does OverlayFS work for containers?](#310-how-does-overlayfs-work-for-containers)
- [311: What is copy-on-write and why does it matter for performance?](#311-what-is-copy-on-write-and-why-does-it-matter-for-performance)
- [312: How does Docker run containers on macOS in more detail?](#312-how-does-docker-run-containers-on-macos-in-more-detail)
- [313: How do you make bind mounts faster on macOS?](#313-how-do-you-make-bind-mounts-faster-on-macos)
- [314: What is rootless mode?](#314-what-is-rootless-mode)
- [315: What is user namespace remapping?](#315-what-is-user-namespace-remapping)
- [316: What is the difference between rootless mode and userns-remap?](#316-what-is-the-difference-between-rootless-mode-and-userns-remap)
- [317: What is seccomp and how does Docker use it?](#317-what-is-seccomp-and-how-does-docker-use-it)
- [318: What are AppArmor and SELinux in the context of Docker?](#318-what-are-apparmor-and-selinux-in-the-context-of-docker)
- [319: What does no-new-privileges do?](#319-what-does-no-new-privileges-do)
- [320: What is a container escape?](#320-what-is-a-container-escape)
- [321: How do you harden a container at run time?](#321-how-do-you-harden-a-container-at-run-time)
- [322: How do you harden a Docker image?](#322-how-do-you-harden-a-docker-image)
- [323: What are Docker Hardened Images?](#323-what-are-docker-hardened-images)
- [324: How do you sign images and verify signatures?](#324-how-do-you-sign-images-and-verify-signatures)
- [325: What was Docker Content Trust?](#325-what-was-docker-content-trust)
- [326: How does pulling an image work at the registry protocol level?](#326-how-does-pulling-an-image-work-at-the-registry-protocol-level)
- [327: What is an image manifest and an image index?](#327-what-is-an-image-manifest-and-an-image-index)
- [328: How are layers stored and shared?](#328-how-are-layers-stored-and-shared)
- [329: What is the difference between a layer digest and a diff ID?](#329-what-is-the-difference-between-a-layer-digest-and-a-diff-id)
- [330: What layer compression formats are supported?](#330-what-layer-compression-formats-are-supported)
- [331: What is lazy pulling?](#331-what-is-lazy-pulling)
- [332: How do you reduce container startup time?](#332-how-do-you-reduce-container-startup-time)
- [333: How does Docker networking work on Linux in detail?](#333-how-does-docker-networking-work-on-linux-in-detail)
- [334: What is docker-proxy and can you disable it?](#334-what-is-docker-proxy-and-can-you-disable-it)
- [335: Does Docker support nftables?](#335-does-docker-support-nftables)
- [336: How does the overlay network work?](#336-how-does-the-overlay-network-work)
- [337: How does service discovery and load balancing work in Swarm?](#337-how-does-service-discovery-and-load-balancing-work-in-swarm)
- [338: How do Swarm rolling updates and rollbacks work?](#338-how-do-swarm-rolling-updates-and-rollbacks-work)
- [339: How do Swarm secrets differ from Compose secrets?](#339-how-do-swarm-secrets-differ-from-compose-secrets)
- [340: When would you pick Swarm over Kubernetes?](#340-when-would-you-pick-swarm-over-kubernetes)
- [341: How does CPU limiting work under the hood?](#341-how-does-cpu-limiting-work-under-the-hood)
- [342: How does memory limiting work and what happens on OOM?](#342-how-does-memory-limiting-work-and-what-happens-on-oom)
- [343: Why does my app use more memory than expected in a container?](#343-why-does-my-app-use-more-memory-than-expected-in-a-container)
- [344: What happens to a container's disk I/O and how do you limit it?](#344-what-happens-to-a-containers-disk-io-and-how-do-you-limit-it)
- [345: What is the difference between --memory-swap and --memory?](#345-what-is-the-difference-between---memory-swap-and---memory)
- [346: Why can the Docker build cache be invalidated unexpectedly?](#346-why-can-the-docker-build-cache-be-invalidated-unexpectedly)
- [347: How does BuildKit execute a Dockerfile internally?](#347-how-does-buildkit-execute-a-dockerfile-internally)
- [348: What is the difference between mode=min and mode=max for cache export?](#348-what-is-the-difference-between-modemin-and-modemax-for-cache-export)
- [349: How does Docker Build Cloud work?](#349-how-does-docker-build-cloud-work)
- [350: How do you do multi-platform builds without slow emulation?](#350-how-do-you-do-multi-platform-builds-without-slow-emulation)
- [351: What automatic build arguments does BuildKit provide?](#351-what-automatic-build-arguments-does-buildkit-provide)
- [352: How does ARG scope work across stages?](#352-how-does-arg-scope-work-across-stages)
- [353: How would you design images for a team with many microservices?](#353-how-would-you-design-images-for-a-team-with-many-microservices)
- [354: How do you handle a critical CVE in a base image used by 50 services?](#354-how-do-you-handle-a-critical-cve-in-a-base-image-used-by-50-services)
- [355: What is VEX?](#355-what-is-vex)
- [356: How do you run untrusted code in containers safely?](#356-how-do-you-run-untrusted-code-in-containers-safely)
- [357: How do you use a different OCI runtime with Docker?](#357-how-do-you-use-a-different-oci-runtime-with-docker)
- [358: What is Enhanced Container Isolation?](#358-what-is-enhanced-container-isolation)
- [359: What is the security risk of mounting /var/run/docker.sock?](#359-what-is-the-security-risk-of-mounting-varrundockersock)
- [360: How do you expose the Docker API over the network safely?](#360-how-do-you-expose-the-docker-api-over-the-network-safely)
- [361: How would you audit a Docker host for security problems?](#361-how-would-you-audit-a-docker-host-for-security-problems)
- [362: How do secrets leak from containers and how do you prevent it?](#362-how-do-secrets-leak-from-containers-and-how-do-you-prevent-it)
- [363: How do you design a Dockerfile that builds fast in CI and runs small in production?](#363-how-do-you-design-a-dockerfile-that-builds-fast-in-ci-and-runs-small-in-production)
- [364: What are the trade-offs between Alpine, slim, distroless and scratch?](#364-what-are-the-trade-offs-between-alpine-slim-distroless-and-scratch)
- [365: What problems can musl libc cause?](#365-what-problems-can-musl-libc-cause)
- [366: How do you debug a distroless or scratch container that has no shell?](#366-how-do-you-debug-a-distroless-or-scratch-container-that-has-no-shell)
- [367: What does --pid container:x or --network container:x do?](#367-what-does---pid-containerx-or---network-containerx-do)
- [368: How do you trace system calls of a process in a container?](#368-how-do-you-trace-system-calls-of-a-process-in-a-container)
- [369: How do you enter a container's namespaces from the host?](#369-how-do-you-enter-a-containers-namespaces-from-the-host)
- [370: How do you capture network traffic of a container?](#370-how-do-you-capture-network-traffic-of-a-container)
- [371: A container cannot reach the internet. How do you troubleshoot it?](#371-a-container-cannot-reach-the-internet-how-do-you-troubleshoot-it)
- [372: How can an MTU mismatch break container networking?](#372-how-can-an-mtu-mismatch-break-container-networking)
- [373: Why are Docker subnets sometimes in conflict with a VPN?](#373-why-are-docker-subnets-sometimes-in-conflict-with-a-vpn)
- [374: How does a container's /etc/resolv.conf get generated?](#374-how-does-a-containers-etcresolvconf-get-generated)
- [375: What can cause slow DNS inside containers?](#375-what-can-cause-slow-dns-inside-containers)
- [376: How does Docker handle signals and stop timeouts in more detail?](#376-how-does-docker-handle-signals-and-stop-timeouts-in-more-detail)
- [377: What are zombie processes and why do they appear in containers?](#377-what-are-zombie-processes-and-why-do-they-appear-in-containers)
- [378: Why might logs from your app appear late or out of order in docker logs?](#378-why-might-logs-from-your-app-appear-late-or-out-of-order-in-docker-logs)
- [379: What happens when the json-file log driver fills the disk?](#379-what-happens-when-the-json-file-log-driver-fills-the-disk)
- [380: What is the blocking vs non-blocking log mode?](#380-what-is-the-blocking-vs-non-blocking-log-mode)
- [381: How do you size and tune Docker's data root on a server?](#381-how-do-you-size-and-tune-dockers-data-root-on-a-server)
- [382: How do you move Docker's data directory to another disk?](#382-how-do-you-move-dockers-data-directory-to-another-disk)
- [383: How do you upgrade Docker Engine on production hosts safely?](#383-how-do-you-upgrade-docker-engine-on-production-hosts-safely)
- [384: What is the Docker Engine API and how is it versioned?](#384-what-is-the-docker-engine-api-and-how-is-it-versioned)
- [385: How do you control Docker from code?](#385-how-do-you-control-docker-from-code)
- [386: What are Docker plugins?](#386-what-are-docker-plugins)
- [387: What are authorization plugins and their risks?](#387-what-are-authorization-plugins-and-their-risks)
- [388: How would you build a minimal image for a Python app with native dependencies?](#388-how-would-you-build-a-minimal-image-for-a-python-app-with-native-dependencies)
- [389: How do you make image builds reproducible?](#389-how-do-you-make-image-builds-reproducible)
- [390: How do you build an image without a Docker daemon?](#390-how-do-you-build-an-image-without-a-docker-daemon)
- [391: What are Cloud Native Buildpacks and when would you use them instead of a Dockerfile?](#391-what-are-cloud-native-buildpacks-and-when-would-you-use-them-instead-of-a-dockerfile)
- [392: How do you run a Compose app in production and what are its limits?](#392-how-do-you-run-a-compose-app-in-production-and-what-are-its-limits)
- [393: How would you migrate a Compose setup to Kubernetes?](#393-how-would-you-migrate-a-compose-setup-to-kubernetes)
- [394: How do Docker healthchecks map to Kubernetes probes?](#394-how-do-docker-healthchecks-map-to-kubernetes-probes)
- [395: How do image pull policies affect deployments?](#395-how-do-image-pull-policies-affect-deployments)
- [396: How do you choose a container platform for a new web app?](#396-how-do-you-choose-a-container-platform-for-a-new-web-app)
- [397: How do you keep images small for machine learning workloads?](#397-how-do-you-keep-images-small-for-machine-learning-workloads)
- [398: What is Docker Model Runner?](#398-what-is-docker-model-runner)
- [399: How do you store non-image artifacts in a container registry?](#399-how-do-you-store-non-image-artifacts-in-a-container-registry)
- [400: What is the referrers API?](#400-what-is-the-referrers-api)
- [401: Your image build takes 15 minutes in CI. How do you speed it up?](#401-your-image-build-takes-15-minutes-in-ci-how-do-you-speed-it-up)
- [402: A container works locally but crashes in production. How do you investigate?](#402-a-container-works-locally-but-crashes-in-production-how-do-you-investigate)
- [403: An image built on an Apple Silicon Mac fails with "exec format error" on the server. Why?](#403-an-image-built-on-an-apple-silicon-mac-fails-with-exec-format-error-on-the-server-why)
- [404: Your server's disk is full because of Docker. What do you do?](#404-your-servers-disk-is-full-because-of-docker-what-do-you-do)
- [405: Your app container takes 60 seconds to stop. Why and how do you fix it?](#405-your-app-container-takes-60-seconds-to-stop-why-and-how-do-you-fix-it)
- [406: How do you make a database container production-ready?](#406-how-do-you-make-a-database-container-production-ready)
- [407: Why should you be careful upgrading a Postgres container by changing the tag?](#407-why-should-you-be-careful-upgrading-a-postgres-container-by-changing-the-tag)
- [408: How do you share a cache between a CI build and local development?](#408-how-do-you-share-a-cache-between-a-ci-build-and-local-development)
- [409: How do you design container images for fast rollbacks?](#409-how-do-you-design-container-images-for-fast-rollbacks)
- [410: What is the expand and contract pattern for migrations, and why does it matter with containers?](#410-what-is-the-expand-and-contract-pattern-for-migrations-and-why-does-it-matter-with-containers)
- [411: How would you run Docker in a multi-tenant environment?](#411-how-would-you-run-docker-in-a-multi-tenant-environment)
- [412: How do resource limits interact with language runtimes?](#412-how-do-resource-limits-interact-with-language-runtimes)
- [413: What is CPU throttling and how do you detect it?](#413-what-is-cpu-throttling-and-how-do-you-detect-it)
- [414: How would you limit the network bandwidth of a container?](#414-how-would-you-limit-the-network-bandwidth-of-a-container)
- [415: What happens to running containers when the host reboots?](#415-what-happens-to-running-containers-when-the-host-reboots)
- [416: How do you run a container that needs to start before Docker networking is ready on boot?](#416-how-do-you-run-a-container-that-needs-to-start-before-docker-networking-is-ready-on-boot)
- [417: How do you handle time and clock issues in containers?](#417-how-do-you-handle-time-and-clock-issues-in-containers)
- [418: How does Docker handle IPv6 and dual-stack networks today?](#418-how-does-docker-handle-ipv6-and-dual-stack-networks-today)
- [419: What gateway modes can a bridge network use?](#419-what-gateway-modes-can-a-bridge-network-use)
- [420: How would you structure Compose files for local dev, CI and production?](#420-how-would-you-structure-compose-files-for-local-dev-ci-and-production)
- [421: How do you test a Dockerfile change safely?](#421-how-do-you-test-a-dockerfile-change-safely)
- [422: How do you write a test for an image's contents?](#422-how-do-you-write-a-test-for-an-images-contents)
- [423: How do you design a Dockerfile for a pnpm or Yarn workspace monorepo?](#423-how-do-you-design-a-dockerfile-for-a-pnpm-or-yarn-workspace-monorepo)
- [424: How do you run several versions of a service side by side on one host?](#424-how-do-you-run-several-versions-of-a-service-side-by-side-on-one-host)
- [425: How does Traefik discover containers?](#425-how-does-traefik-discover-containers)
- [426: What are the trade-offs of building images on the production server?](#426-what-are-the-trade-offs-of-building-images-on-the-production-server)
- [427: How do you use Docker to provide consistent tooling for a team without dev containers?](#427-how-do-you-use-docker-to-provide-consistent-tooling-for-a-team-without-dev-containers)
- [428: How do you handle file ownership problems with volumes written by containers?](#428-how-do-you-handle-file-ownership-problems-with-volumes-written-by-containers)
- [429: How do gosu and su-exec work in entrypoint scripts?](#429-how-do-gosu-and-su-exec-work-in-entrypoint-scripts)
- [430: Why should you use a fixed numeric UID in images?](#430-why-should-you-use-a-fixed-numeric-uid-in-images)
- [431: What happens when two containers write to the same bind-mounted file?](#431-what-happens-when-two-containers-write-to-the-same-bind-mounted-file)
- [432: How do you inspect what a running container is doing without stopping it?](#432-how-do-you-inspect-what-a-running-container-is-doing-without-stopping-it)
- [433: How do you profile a Python app running in a container?](#433-how-do-you-profile-a-python-app-running-in-a-container)
- [434: How do you handle very large build contexts?](#434-how-do-you-handle-very-large-build-contexts)
- [435: How do you avoid cache invalidation from COPY . . in an otherwise good Dockerfile?](#435-how-do-you-avoid-cache-invalidation-from-copy---in-an-otherwise-good-dockerfile)
- [436: What is a scenario where a multi-stage build makes the cache worse, and how do you fix it?](#436-what-is-a-scenario-where-a-multi-stage-build-makes-the-cache-worse-and-how-do-you-fix-it)
- [437: How would you build a minimal image for a Rust app?](#437-how-would-you-build-a-minimal-image-for-a-rust-app)
- [438: How does Docker Compose decide when to recreate a container?](#438-how-does-docker-compose-decide-when-to-recreate-a-container)
- [439: How do Compose and Docker labels help with automation?](#439-how-do-compose-and-docker-labels-help-with-automation)
- [440: How do you implement a sidecar pattern with Docker?](#440-how-do-you-implement-a-sidecar-pattern-with-docker)
- [441: How do you run Docker in CI on Kubernetes runners?](#441-how-do-you-run-docker-in-ci-on-kubernetes-runners)
- [442: How would you reduce cold start time for a containerized service on a serverless platform?](#442-how-would-you-reduce-cold-start-time-for-a-containerized-service-on-a-serverless-platform)
- [443: How do you check that a Dockerfile follows best practices automatically?](#443-how-do-you-check-that-a-dockerfile-follows-best-practices-automatically)
- [444: How do you enforce that only approved images run in your environment?](#444-how-do-you-enforce-that-only-approved-images-run-in-your-environment)
- [445: How would you design logging for 100 containers on a few hosts?](#445-how-would-you-design-logging-for-100-containers-on-a-few-hosts)
- [446: What are the costs and risks of running containers as root even with a non-root user inside?](#446-what-are-the-costs-and-risks-of-running-containers-as-root-even-with-a-non-root-user-inside)
- [447: How do you handle certificates and custom CAs in images?](#447-how-do-you-handle-certificates-and-custom-cas-in-images)
- [448: How do you use Docker behind a corporate proxy?](#448-how-do-you-use-docker-behind-a-corporate-proxy)
- [449: How would you explain the trade-off between one big image and many small images?](#449-how-would-you-explain-the-trade-off-between-one-big-image-and-many-small-images)
- [450: What changed in recent Docker versions that you should know about?](#450-what-changed-in-recent-docker-versions-that-you-should-know-about)

---

# Easy Questions (1-150)

## 1: What is Docker?

Docker is a tool for packaging an application together with everything it needs to run (runtime, libraries, system tools, config) into an image, and then running that image as a container. The container runs the same way on your laptop, on a CI server and in production.

Docker is made of a few parts:

- The Docker CLI (`docker`), which you type commands into
- The Docker daemon (`dockerd`), which builds images and runs containers
- Registries such as Docker Hub, where images are stored and shared
- Extra tools like Docker Compose, Buildx and Docker Desktop

## 2: What problem does Docker solve?

The classic problem is "it works on my machine". Different machines have different OS versions, library versions and config, so the same code behaves differently.

Docker fixes this by shipping the app with its environment. If the image runs on one machine, it will run the same way on any machine with a container runtime. It also makes setup faster: a new developer can run `docker compose up` instead of installing a database, a cache and a specific Node.js version by hand.

## 3: What is a container?

A container is a running process (or group of processes) that is isolated from the rest of the system. It has its own filesystem, its own network interfaces, its own process list and its own limits on CPU and memory.

It is not a virtual machine. A container shares the host's kernel and only isolates what the process can see and use. That is why containers start in milliseconds and use far less memory than VMs.

## 4: What is a Docker image?

An image is a read-only template used to create containers. It holds a filesystem (your app, its dependencies, a base OS userland) and metadata such as the default command, environment variables and exposed ports.

Images are built in layers. Each instruction in a Dockerfile that changes files adds a new layer. When you run an image, Docker adds a thin writable layer on top, and that becomes the container.

## 5: What is the difference between an image and a container?

An image is the blueprint. A container is a running (or stopped) instance of that blueprint.

You can compare it to a class and an object: one image can be used to start many containers, and each container has its own writable layer, its own state and its own lifecycle. Deleting a container does not delete the image.

```bash
docker run -d --name web1 nginx
docker run -d --name web2 nginx   # second container from the same image
```

## 6: What is the difference between a container and a virtual machine?

A virtual machine runs a full guest operating system on top of a hypervisor, with its own kernel. A container runs as a process on the host and shares the host kernel.

Practical differences:

- **Size:** VM images are usually gigabytes, container images are often tens of megabytes.
- **Startup:** VMs take tens of seconds or minutes, containers start in under a second.
- **Isolation:** VMs have stronger isolation because of the separate kernel. Containers rely on kernel features (namespaces, cgroups), so a kernel bug can affect all containers.
- **OS:** a Linux container needs a Linux kernel. On macOS and Windows, Docker Desktop runs a small Linux VM for this.

## 7: What is a Dockerfile?

A Dockerfile is a text file with instructions for building an image. Docker reads it from top to bottom and runs each instruction.

```dockerfile
FROM node:22-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

You build it with `docker build -t my-app .`.

## 8: What is Docker Hub?

Docker Hub is Docker's public registry. It hosts official images (like `node`, `postgres`, `nginx`), images from verified publishers, and images that anyone can push.

When you run `docker pull nginx` without a registry name, Docker pulls from Docker Hub by default. Free accounts have pull rate limits, so in CI it is a good idea to log in or use a mirror.

## 9: What is a container registry?

A registry is a server that stores images and serves them over HTTP. You push images to it and pull them from it.

Common registries:

- Docker Hub
- GitHub Container Registry (`ghcr.io`)
- Amazon ECR, Google Artifact Registry, Azure Container Registry
- Self-hosted ones like Harbor or the open source `registry` image

A registry holds repositories, and each repository holds tagged versions of an image.

## 10: How do you install Docker?

On macOS and Windows, the usual way is Docker Desktop. It installs the CLI, the engine (inside a small Linux VM), Compose, Buildx and a GUI.

On Linux servers, you install Docker Engine from Docker's apt or dnf repository. After that, add the Compose and Buildx plugins (they come as packages too). You can check that it works with:

```bash
docker version
docker run hello-world
```

## 11: What does docker run do?

`docker run` creates a new container from an image and starts it. If the image is not on your machine, Docker pulls it first.

```bash
docker run -d --name web -p 8080:80 nginx:1.27
```

This runs nginx in the background (`-d`), names the container `web`, and maps port 8080 on the host to port 80 in the container. It is basically `docker create` plus `docker start` in one step.

## 12: What are the most common options for docker run?

- `-d` runs the container in the background.
- `-it` gives you an interactive terminal (`-i` keeps stdin open, `-t` adds a TTY).
- `--name` sets a container name.
- `-p host:container` publishes a port.
- `-e KEY=value` sets an environment variable.
- `-v` or `--mount` attaches a volume or bind mount.
- `--rm` deletes the container when it stops.
- `--network` connects it to a network.
- `--restart` sets a restart policy.

```bash
docker run --rm -it -e NODE_ENV=development node:22 bash
```

## 13: How do you list running containers?

```bash
docker ps          # running containers
docker ps -a       # all containers, including stopped ones
docker ps -q       # only IDs
```

The newer form `docker container ls` does the same thing. The output shows the container ID, image, command, status, ports and name.

## 14: How do you stop and start a container?

```bash
docker stop web     # sends SIGTERM, then SIGKILL after 10 seconds
docker start web    # starts a stopped container again
docker restart web  # stop + start
```

`docker stop` gives the app time to shut down cleanly. You can change the wait time with `-t`, for example `docker stop -t 30 web`.

## 15: What is the difference between docker stop and docker kill?

`docker stop` sends `SIGTERM` (or the signal set by `STOPSIGNAL`) and waits for the process to exit. If it does not exit before the timeout (10 seconds by default), Docker sends `SIGKILL`.

`docker kill` sends `SIGKILL` right away, so the process has no chance to clean up. You can send a different signal with `docker kill -s SIGHUP web`, which is sometimes used to make a process reload its config.

## 16: How do you remove a container?

```bash
docker rm web         # remove a stopped container
docker rm -f web      # stop and remove a running container
docker container prune  # remove all stopped containers
```

If you start containers with `--rm`, Docker removes them automatically when they exit, so you do not collect old stopped containers.

## 17: How do you list and remove images?

```bash
docker images            # or: docker image ls
docker rmi nginx:1.27    # or: docker image rm nginx:1.27
docker image prune       # remove dangling images
docker image prune -a    # remove all images not used by a container
```

You cannot remove an image that a container (even a stopped one) still uses, unless you add `-f`.

## 18: What does docker pull do?

`docker pull` downloads an image from a registry to your machine.

```bash
docker pull postgres:17
docker pull ghcr.io/my-org/api:1.4.0
```

Docker only downloads the layers you do not already have. If you do not give a tag, it pulls `latest`.

## 19: What is an image tag?

A tag is a label that points to a specific version of an image, written after a colon: `node:22-alpine`, `my-api:1.4.0`.

Tags are mutable. The owner can push a new image under the same tag, so `node:22` today may not be the same image next month. If you need the exact same image every time, use a digest instead (see the question on digests).

## 20: What is the latest tag?

`latest` is just the default tag Docker uses when you do not give one. It does not mean "the newest version". It means "whatever was last pushed with the tag `latest`", or nothing at all if the publisher never used it.

In production, avoid `latest`. You cannot tell which version is running, rollbacks are harder, and a deploy can pick up a new version without anyone noticing. Use specific version tags.

## 21: How do you build an image?

```bash
docker build -t my-app:1.0 .
```

- `-t` gives the image a name and tag.
- `.` is the build context, the folder whose files are sent to the builder.
- Docker looks for a file called `Dockerfile` in the context. Use `-f` to point to another file.

Under the hood, `docker build` uses BuildKit (through Buildx), which is the default builder today.

## 22: What is the build context?

The build context is the set of files the builder can access during a build. When you run `docker build .`, the current folder is the context.

`COPY` and `ADD` can only read files from inside the context. You cannot do `COPY ../secret.txt .`. A big context (for example with `node_modules` or `.git` in it) makes builds slower, which is why you use a `.dockerignore` file.

## 23: What is a .dockerignore file?

It lists files and folders that should not be sent to the build context. It works like `.gitignore`.

```text
node_modules
.git
dist
*.log
.env
Dockerfile
```

This keeps builds fast, keeps images small and stops secrets like `.env` from ending up in an image by accident.

## 24: What does the FROM instruction do?

`FROM` sets the base image that the rest of the Dockerfile builds on. Almost every Dockerfile starts with it.

```dockerfile
FROM python:3.13-slim
```

You can use more than one `FROM` in a Dockerfile for multi-stage builds. `FROM scratch` starts from an empty image, which is useful for static binaries.

## 25: What does the RUN instruction do?

`RUN` runs a command at build time and saves the result as a new layer. It is used for installing packages, compiling code and similar setup.

```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
```

Commands are chained with `&&` so that installing and cleaning up happen in the same layer. If you cleaned up in a separate `RUN`, the files would still exist in the earlier layer and the image would not get smaller.

## 26: What does the CMD instruction do?

`CMD` sets the default command that runs when a container starts. Only the last `CMD` in a Dockerfile counts.

```dockerfile
CMD ["node", "server.js"]
```

You can override it from the command line: `docker run my-app node other.js` runs `node other.js` instead.

## 27: What does the ENTRYPOINT instruction do?

`ENTRYPOINT` sets the executable that always runs when the container starts. Arguments passed to `docker run` are added after it instead of replacing it.

```dockerfile
ENTRYPOINT ["curl"]
CMD ["--help"]
```

`docker run my-curl` runs `curl --help`. `docker run my-curl https://example.com` runs `curl https://example.com`. You can still replace the entrypoint with `docker run --entrypoint`.

## 28: What is the difference between CMD and ENTRYPOINT?

- `ENTRYPOINT` is the fixed program. It is not replaced by `docker run` arguments.
- `CMD` is the default command, or default arguments when an `ENTRYPOINT` exists. It is replaced by `docker run` arguments.

A common pattern: use `ENTRYPOINT` for the binary and `CMD` for default flags. If the image is a general app image, many teams use only `CMD` so it is easy to run other commands like `docker run my-app sh`.

## 29: What is the difference between the exec form and the shell form?

Exec form is a JSON array: `CMD ["node", "server.js"]`. Docker runs the program directly, so it becomes PID 1 and receives signals like `SIGTERM`.

Shell form is a plain string: `CMD node server.js`. Docker runs it as `/bin/sh -c "node server.js"`. The shell is PID 1, and it usually does not pass signals to your app, so `docker stop` waits for the timeout and then kills it.

Use exec form for `CMD` and `ENTRYPOINT`. Shell form is fine for `RUN`, where you often want shell features like `&&` and pipes.

## 30: What does COPY do?

`COPY` copies files or folders from the build context into the image.

```dockerfile
COPY package.json package-lock.json ./
COPY src/ ./src/
COPY --chown=node:node . .
```

`--chown` sets the owner of the copied files, and `--from=<stage>` copies from another build stage instead of the context.

## 31: What is the difference between COPY and ADD?

Both copy files into the image, but `ADD` does more:

- It can download a file from a URL.
- It automatically extracts local tar archives (`.tar`, `.tar.gz` and so on).
- It can also add a Git repository by URL.

Because of this extra behavior, the Docker docs recommend `COPY` for normal file copying. Use `ADD` only when you actually need extraction or a remote source, so it is clear what the line does.

## 32: What does WORKDIR do?

`WORKDIR` sets the working directory for the instructions that follow (`RUN`, `CMD`, `ENTRYPOINT`, `COPY`, `ADD`) and for the running container. If the folder does not exist, Docker creates it.

```dockerfile
WORKDIR /app
COPY . .
RUN npm ci
```

Use `WORKDIR` instead of `RUN cd /app && ...`, because `cd` in a `RUN` only lasts for that one command.

## 33: What does ENV do?

`ENV` sets an environment variable that is available in later build steps and in the running container.

```dockerfile
ENV NODE_ENV=production \
    PORT=3000
```

You can override it at run time with `docker run -e PORT=8080`. Do not put secrets in `ENV`, because they are stored in the image metadata and anyone with the image can read them.

## 34: What does ARG do?

`ARG` defines a variable that is only available during the build. You pass a value with `--build-arg`.

```dockerfile
ARG NODE_VERSION=22
FROM node:${NODE_VERSION}-alpine
ARG APP_VERSION
RUN echo "Building $APP_VERSION"
```

```bash
docker build --build-arg APP_VERSION=1.4.0 -t my-app .
```

`ARG` values are not set in the running container. They can still show up in the image history, so they are not safe for secrets either.

## 35: What is the difference between ARG and ENV?

- `ARG` exists only at build time. It is set with `--build-arg`.
- `ENV` exists at build time (after the line where it is defined) and at run time inside the container.

A common trick is to combine them so a build argument becomes a runtime variable:

```dockerfile
ARG APP_VERSION=dev
ENV APP_VERSION=$APP_VERSION
```

## 36: What does EXPOSE do?

`EXPOSE` documents which port the app inside the container listens on.

```dockerfile
EXPOSE 3000
```

It does not publish the port to the host. You still need `-p 3000:3000` when you run the container. `EXPOSE` is used by `docker run -P` (which publishes all exposed ports to random host ports) and is useful information for anyone reading the Dockerfile.

## 37: How do you publish a port?

Use `-p host_port:container_port` with `docker run`:

```bash
docker run -d -p 8080:80 nginx          # host 8080 -> container 80
docker run -d -p 127.0.0.1:8080:80 nginx  # only on localhost
docker run -d -p 5353:53/udp my-dns       # UDP port
```

Without `-p`, the container's ports are only reachable from other containers on the same Docker network, not from outside the host.

## 38: How do you see the logs of a container?

```bash
docker logs web
docker logs -f web            # follow, like tail -f
docker logs --tail 100 web    # last 100 lines
docker logs --since 10m web   # last 10 minutes
```

Docker captures whatever the main process writes to stdout and stderr. That is why apps in containers should log to stdout instead of writing to log files.

## 39: How do you run a command inside a running container?

Use `docker exec`:

```bash
docker exec -it web sh           # open a shell
docker exec web ls /usr/share/nginx/html
docker exec -u root -it web bash # run as root
```

`docker exec` starts an extra process inside an already running container. It does not work on stopped containers.

## 40: What is the difference between docker exec and docker attach?

`docker exec` starts a new process (for example a shell) inside the container. When you exit it, the container keeps running.

`docker attach` connects your terminal to the main process (PID 1) of the container. You see its output and your input goes to it. If you press Ctrl+C, you may stop the main process and the container with it. To detach without stopping, use Ctrl+P then Ctrl+Q (if the container was started with `-it`).

Most of the time you want `docker exec`.

## 41: How do you get detailed information about a container?

`docker inspect` returns JSON with everything Docker knows about a container: config, state, network settings, mounts, environment variables and more.

```bash
docker inspect web
docker inspect -f '{{.State.Status}}' web
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

It also works on images, volumes and networks.

## 42: What is a volume?

A volume is storage managed by Docker that lives outside the container's writable layer. Data in a volume survives when the container is removed, and the same volume can be used by several containers.

```bash
docker volume create pgdata
docker run -d -v pgdata:/var/lib/postgresql/data postgres:17
```

Volumes are the recommended way to keep data like database files.

## 43: What is a bind mount?

A bind mount maps a file or folder from the host into the container. Changes on either side are visible on the other side right away.

```bash
docker run -d -v "$(pwd)":/app -w /app node:22 npm run dev
```

Bind mounts are handy in development for live code reloading. In production, they tie the container to a specific host path, so volumes are usually a better fit.

## 44: What is the difference between a volume and a bind mount?

- **Volume:** Docker creates and manages it under its own storage folder. You refer to it by name. It works the same on every host and can use volume drivers (for example network storage).
- **Bind mount:** you choose an exact host path. It depends on the host's folder structure and file permissions.

Use volumes for app data you want to keep. Use bind mounts for development (source code) or for giving a container a specific config file from the host.

## 45: What is a tmpfs mount?

A tmpfs mount is stored in the host's memory only. It is never written to disk, and it disappears when the container stops.

```bash
docker run -d --tmpfs /tmp:size=64m my-app
```

It is useful for temporary files and for data you do not want on disk, such as short-lived secrets. tmpfs mounts are only available on Linux containers.

## 46: What happens to data inside a container when it is removed?

Anything written to the container's writable layer is deleted together with the container. Stopping a container keeps the data. Removing it (`docker rm`) deletes it.

That is why databases and uploads must be stored in a volume or bind mount. Treat the container itself as disposable.

## 47: What is the difference between -v and --mount?

Both attach volumes, bind mounts or tmpfs. `-v` uses a short colon-separated syntax. `--mount` uses explicit key=value pairs.

```bash
docker run -v pgdata:/var/lib/postgresql/data postgres:17
docker run --mount type=volume,source=pgdata,target=/var/lib/postgresql/data postgres:17
```

`--mount` is easier to read and has one important difference: with `-v`, if a bind-mount host path does not exist, Docker creates it as an empty folder. With `--mount`, Docker returns an error instead, which catches typos.

## 48: How do you list and remove volumes?

```bash
docker volume ls
docker volume inspect pgdata
docker volume rm pgdata
docker volume prune   # remove unused anonymous volumes
docker volume prune -a  # remove all unused volumes, including named ones
```

You cannot remove a volume that is used by a container. Be careful with prune commands, because deleted volumes cannot be recovered.

## 49: What is Docker Compose?

Docker Compose is a tool for defining and running multi-container apps. You describe your services, networks and volumes in a YAML file (`compose.yaml`) and start everything with one command.

```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
  db:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: example
```

```bash
docker compose up -d
```

## 50: What is the difference between docker-compose and docker compose?

`docker-compose` (with a hyphen) is the old Compose v1, a separate Python tool. It is no longer supported.

`docker compose` (with a space) is the current Compose, written in Go and installed as a plugin of the Docker CLI. It reads the same kind of files, so in most projects you just change the command. If you see `docker-compose` in old docs or scripts, it should be updated.

## 51: What is the compose.yaml file?

`compose.yaml` is the file Docker Compose reads to know what to run. The main top-level keys are:

- `services`: the containers you want to run
- `volumes`: named volumes
- `networks`: custom networks
- `configs` and `secrets`: files to give to services

Compose also accepts `compose.yml`, and the older names `docker-compose.yaml` and `docker-compose.yml`. `compose.yaml` is the preferred name today.

## 52: Do you still need the version field in a Compose file?

No. The top-level `version: "3.8"` field is obsolete. Current Compose follows the Compose Specification and ignores it, and it prints a warning if the field is there. You can remove it from old files.

## 53: What are the most common docker compose commands?

```bash
docker compose up -d        # create and start everything in the background
docker compose down         # stop and remove containers and networks
docker compose ps           # list services and their state
docker compose logs -f api  # follow logs of one service
docker compose exec api sh  # shell into a running service
docker compose build        # build images
docker compose pull         # pull newer images
docker compose restart api  # restart a service
```

## 54: What is the difference between docker compose up and docker compose start?

`docker compose up` creates the containers if needed (and builds or pulls images), creates networks and volumes, and starts everything. If the config changed, it recreates the affected containers.

`docker compose start` only starts containers that already exist and were stopped. It does not create anything and does not pick up config changes.

## 55: What does docker compose down do?

It stops and removes the containers and the networks Compose created for the project. By default it keeps named volumes and images.

```bash
docker compose down            # keep volumes
docker compose down -v         # also remove volumes (deletes data)
docker compose down --rmi local  # also remove images built by Compose
```

## 56: What is a service in Docker Compose?

A service is one part of your app, for example `api`, `web` or `db`. It describes how to run containers from one image: the image or build, ports, environment, volumes, networks and so on.

A service usually runs one container, but you can run several copies of it with `docker compose up --scale api=3` or `deploy.replicas`.

## 57: How do containers in the same Compose project talk to each other?

Compose creates a default network for the project and connects every service to it. Services can reach each other by service name, because Docker has a built-in DNS server.

```yaml
services:
  api:
    build: .
    environment:
      DATABASE_URL: postgres://postgres:example@db:5432/app
  db:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: example
```

Here `api` connects to the host name `db`. You do not need to publish the database port for this to work.

## 58: What is the official image of a technology on Docker Hub?

Official images are a curated set of images on Docker Hub, such as `node`, `python`, `postgres`, `redis` and `nginx`. They have no user prefix (it is `nginx`, not `someone/nginx`), they are maintained with Docker's review, they get security updates and they have documentation on their Hub page.

They are a good default base image. Docker also has Docker Hardened Images, which are minimal, low-CVE versions of popular images for teams that need stricter security.

## 59: What is a base image?

A base image is the image you start your Dockerfile from with `FROM`. It provides the OS userland and often a language runtime.

Examples:

- `debian:bookworm-slim`, `ubuntu:24.04`: general Linux distros
- `alpine:3.22`: very small distro using musl libc
- `node:22-slim`, `python:3.13-slim`: language runtimes
- `scratch`: empty, nothing in it

## 60: What is an Alpine image and why is it popular?

Alpine Linux is a very small distro (the base image is around 5 MB to 8 MB compressed). Images like `node:22-alpine` are much smaller than the Debian-based versions.

The catch is that Alpine uses musl libc instead of glibc. Some native modules and prebuilt binaries expect glibc and can fail or behave differently. If you hit problems, a `-slim` Debian image is a safe choice that is still fairly small.

## 61: What does slim mean in image tags like python:3.13-slim?

`slim` variants are based on Debian but with many packages removed (docs, compilers, extra tools). They are smaller than the full images and still use glibc, so they avoid most of the compatibility issues you may see with Alpine.

The full (non-slim) images include build tools, which helps if you need to compile native dependencies, but they are much bigger.

## 62: How do you tag an image?

```bash
docker tag my-app:latest my-app:1.4.0
docker tag my-app:1.4.0 ghcr.io/my-org/my-app:1.4.0
```

`docker tag` does not copy the image. It adds another name that points to the same image ID. You can also tag at build time with one or more `-t` flags.

## 63: How do you push an image to a registry?

1. Log in to the registry.
2. Tag the image with the registry and repository name.
3. Push it.

```bash
docker login ghcr.io
docker tag my-app:1.4.0 ghcr.io/my-org/my-app:1.4.0
docker push ghcr.io/my-org/my-app:1.4.0
```

For Docker Hub, the name is `username/repo:tag` and you log in with `docker login`.

## 64: What is the full name of an image?

The full format is:

```text
[registry[:port]/][namespace/]repository[:tag][@digest]
```

For example `ghcr.io/my-org/api:1.4.0`. If you leave parts out, Docker fills them in: `nginx` means `docker.io/library/nginx:latest`.

## 65: What is a dangling image?

A dangling image is an image that has no tag anymore. It shows up as `<none>:<none>` in `docker images`.

It usually happens when you rebuild an image with the same tag: the new image takes the tag and the old one is left without a name. You can clean them up with `docker image prune`.

## 66: How do you check how much disk space Docker uses?

```bash
docker system df
docker system df -v   # detailed per image, container and volume
```

It shows space used by images, containers, local volumes and the build cache, and how much of it can be reclaimed.

## 67: What does docker system prune do?

It removes things you are not using:

- stopped containers
- networks not used by any container
- dangling images
- unused build cache

```bash
docker system prune
docker system prune -a          # also all unused images
docker system prune --volumes   # also unused anonymous volumes
```

It asks for confirmation. Use it carefully on servers, especially with `--volumes`.

## 68: What is a restart policy?

A restart policy tells Docker what to do when a container exits.

- `no` (default): never restart.
- `on-failure[:max]`: restart only when the exit code is not 0, optionally with a retry limit.
- `always`: always restart. Also starts again when the Docker daemon restarts.
- `unless-stopped`: like `always`, but if you stopped it manually it stays stopped after a daemon restart.

```bash
docker run -d --restart unless-stopped my-app
```

## 69: What is the difference between restart always and unless-stopped?

Both restart the container whenever it exits. The difference is what happens after you run `docker stop` and then the daemon restarts (for example after a reboot):

- `always` starts the container again.
- `unless-stopped` keeps it stopped, because you stopped it on purpose.

## 70: How do you pass environment variables to a container?

```bash
docker run -e NODE_ENV=production -e PORT=3000 my-app
docker run --env-file .env my-app
```

In Compose:

```yaml
services:
  api:
    image: my-app
    environment:
      NODE_ENV: production
    env_file:
      - .env
```

## 71: What is the .env file in Docker Compose?

When you run `docker compose`, it automatically reads a file called `.env` in the project folder. Its values are used for variable substitution in `compose.yaml`.

```text
# .env
POSTGRES_VERSION=17
```

```yaml
services:
  db:
    image: postgres:${POSTGRES_VERSION}
```

Note the difference: this `.env` fills in values in the Compose file. It does not automatically pass the variables into containers. For that, use `env_file` or `environment`.

## 72: How do you rename a container?

```bash
docker rename old-name new-name
```

It works on running and stopped containers. Other containers that reach it by name on a user-defined network will see the new name.

## 73: What is a container ID?

Every container gets a unique 64-character hex ID. Docker shows the first 12 characters in most commands. You can use the full ID, the short ID or any unique prefix in commands, as well as the container name.

```bash
docker stop 3f2a9b
```

## 74: How do you copy files between a container and the host?

```bash
docker cp web:/etc/nginx/nginx.conf ./nginx.conf   # container -> host
docker cp ./index.html web:/usr/share/nginx/html/  # host -> container
```

`docker cp` works on running and stopped containers. It is good for quick debugging. For regular work, use volumes or bind mounts instead.

## 75: How do you see resource usage of containers?

```bash
docker stats
docker stats --no-stream   # print once and exit
```

It shows live CPU, memory, network I/O, block I/O and the number of processes for each running container. For the processes inside one container, use `docker top web`.

## 76: How do you limit the memory and CPU of a container?

```bash
docker run -d --memory 512m --cpus 1.5 my-app
```

- `--memory` (or `-m`) sets a hard memory limit. If the container goes over it, the kernel's OOM killer stops a process in it.
- `--cpus` limits how much CPU time it can use (1.5 means one and a half cores).

Without limits, a container can use all the resources of the host.

## 77: What does docker run -it do?

`-i` keeps stdin open and `-t` gives the container a terminal. Together they let you use the container interactively, like a normal shell.

```bash
docker run -it ubuntu:24.04 bash
```

Without `-t`, programs like `bash` do not show a prompt and things like colors and line editing do not work.

## 78: What does docker run --rm do?

It removes the container automatically when it exits. This is useful for one-off commands and tools:

```bash
docker run --rm -v "$(pwd)":/work -w /work node:22 npm test
```

Anonymous volumes created by the container are also removed. Named volumes are kept.

## 79: What is the default network for docker run?

If you do not pass `--network`, the container joins the default `bridge` network. On it, containers can reach each other by IP address but not by name.

For apps with several containers, create your own network (`docker network create`). User-defined bridge networks give you DNS-based name lookup and better isolation.

## 80: What network drivers does Docker have?

- `bridge`: the default. A private network on one host.
- `host`: the container uses the host's network directly, with no isolation.
- `none`: no networking at all, only loopback.
- `overlay`: a network across several Docker hosts (used with Swarm).
- `macvlan` and `ipvlan`: give containers addresses on the physical network.

Most apps use `bridge` networks.

## 81: How do you create a network and connect containers to it?

```bash
docker network create app-net
docker run -d --name db --network app-net -e POSTGRES_PASSWORD=example postgres:17
docker run -d --name api --network app-net my-api
```

Now `api` can reach the database at the host name `db`. You can connect an already running container with `docker network connect app-net some-container`.

## 82: What is the host network mode?

With `--network host`, the container does not get its own network namespace. It uses the host's interfaces and ports directly, so an app listening on port 3000 is reachable on the host's port 3000 without `-p`.

It removes the small overhead of NAT, but you lose network isolation and port conflicts become possible. On Docker Desktop, host networking is supported in newer versions but behaves differently than on a Linux host, because the "host" is the Docker VM.

## 83: What is the docker version command and how is it different from docker info?

`docker version` shows the version of the client and the server (engine), including API versions.

`docker info` shows system-wide details: number of containers and images, storage driver, logging driver, cgroup version, kernel version, registry mirrors, and so on. It is a good first command when something is not working.

## 84: What is Docker Desktop?

Docker Desktop is an app for macOS, Windows and Linux that bundles everything you need for local development: the Docker Engine (inside a lightweight VM), the CLI, Compose, Buildx, Kubernetes, Docker Scout and a GUI.

It is free for personal use, education, open source and small businesses. Larger companies need a paid subscription.

## 85: Why does Docker on macOS and Windows need a virtual machine?

Linux containers need a Linux kernel. macOS and Windows do not have one, so Docker Desktop runs a small Linux VM in the background and runs containers inside it. On Windows, this is usually done with WSL 2.

This is also why bind mounts can be slower on macOS: files have to be shared between the host and the VM.

## 86: What is a layer in a Docker image?

A layer is a set of filesystem changes. Each instruction that changes files (`RUN`, `COPY`, `ADD`) creates a new layer on top of the previous ones. Instructions like `ENV`, `CMD` and `EXPOSE` only change metadata.

Layers are read-only and shared. If two images use the same base image, its layers are stored once on disk and downloaded only once.

## 87: What is the build cache?

When you build an image, Docker saves the result of each step. On the next build, if an instruction and its inputs have not changed, Docker reuses the saved layer instead of running the step again.

Once a step changes, every step after it runs again. That is why you copy dependency files and install dependencies before copying the rest of the source code:

```dockerfile
COPY package*.json ./
RUN npm ci
COPY . .
```

Now changing your code does not reinstall all packages.

## 88: How do you build without using the cache?

```bash
docker build --no-cache -t my-app .
```

This is useful when a step like `apt-get update` would otherwise reuse old results, or when you suspect the cache is causing a problem. You can also use `--pull` to always check for a newer base image.

## 89: What does docker image history show?

It lists the layers of an image, the instruction that created each one and its size.

```bash
docker image history my-app:1.0
docker image history --no-trunc my-app:1.0
```

It is useful for finding which step makes an image big. It also shows why you should not pass secrets as build args: they can appear here.

## 90: What does docker commit do and should you use it?

`docker commit` creates a new image from the current state of a container.

```bash
docker commit web my-nginx:custom
```

It is fine for quick experiments, but not for real images. Nobody can see how the image was made, you cannot rebuild it reliably, and it often contains leftover junk. Use a Dockerfile instead.

## 91: How do you save an image to a file and load it back?

```bash
docker save -o my-app.tar my-app:1.0
docker load -i my-app.tar
```

This moves an image between machines without a registry, for example to an air-gapped server. The tar file contains all layers and metadata.

## 92: What is the difference between docker save and docker export?

- `docker save` works on images. It keeps all layers, tags and metadata (CMD, ENV and so on). You restore it with `docker load`.
- `docker export` works on containers. It produces a flat tar of the container filesystem with no layers and no metadata. You restore it with `docker import`, which creates a new single-layer image.

For moving images, use `save` and `load`.

## 93: What is a healthcheck?

A healthcheck is a command Docker runs inside the container at regular intervals to check whether the app is working, not just whether the process is alive.

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1
```

The container status then shows `healthy`, `unhealthy` or `starting`. Compose and Swarm can use this status, for example to wait for a database before starting the app.

## 94: What does the USER instruction do?

`USER` sets which user (and optionally group) runs the following `RUN` commands and the container's main process.

```dockerfile
RUN useradd --create-home appuser
USER appuser
CMD ["node", "server.js"]
```

By default, containers run as root. Running as a regular user limits the damage if someone breaks into the app. Many official images already include a user, like `node` in the Node.js images.

## 95: What does the LABEL instruction do?

`LABEL` adds metadata to an image as key-value pairs.

```dockerfile
LABEL org.opencontainers.image.source="https://github.com/my-org/api" \
      org.opencontainers.image.version="1.4.0"
```

Labels do not affect how the container runs. Tools use them to show the source repo, version, license or owner. The `org.opencontainers.image.*` keys are a standard set.

## 96: What does the VOLUME instruction do?

`VOLUME` marks a path in the image as a place for external data. If you run the container without mounting anything there, Docker creates an anonymous volume for that path.

```dockerfile
VOLUME /data
```

Be careful: any changes to that path in later Dockerfile steps are thrown away. Many teams prefer not to use `VOLUME` in their own images and just mount volumes at run time.

## 97: What is a multi-stage build?

A multi-stage build uses several `FROM` instructions in one Dockerfile. You build your app in one stage with all the tools, then copy only the result into a small final stage.

```dockerfile
FROM node:22 AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

The final image has nginx and the built files, but no Node.js, no source code and no `node_modules`.

## 98: Why should a container run only one main process?

A container is tied to its main process. Docker starts it, watches it, collects its logs and restarts it when it dies. If you put several services (for example app plus database) in one container, you lose that: one can crash while the container still looks healthy, logs get mixed, and you cannot scale or update them separately.

So the rule is one concern per container. A container can still have helper child processes, but one service should be in charge.

## 99: What is the difference between docker create and docker run?

`docker create` creates the container (writable layer, config) but does not start it. You start it later with `docker start`.

`docker run` does both in one step. `docker create` is useful when you want to set up a container first, for example to copy files into it with `docker cp` before it starts.

## 100: How do you see which ports a container publishes?

```bash
docker port web
docker ps   # PORTS column
```

Example output of `docker port web`:

```text
80/tcp -> 0.0.0.0:8080
```

## 101: What is the Docker daemon?

The Docker daemon (`dockerd`) is the background service that does the actual work: it builds images, pulls and pushes them, creates networks and volumes, and manages containers. It uses containerd and runc underneath to run the containers.

On Linux it runs as a system service. You can check it with `systemctl status docker`.

## 102: How does the Docker CLI talk to the daemon?

The CLI sends requests to the daemon's REST API. By default this goes through a Unix socket at `/var/run/docker.sock` on Linux (a named pipe on Windows).

You can point the CLI at another daemon with the `DOCKER_HOST` variable or with contexts:

```bash
DOCKER_HOST=ssh://user@server docker ps
```

## 103: What is a Docker context?

A context stores the connection settings for a Docker daemon, so you can switch between machines easily.

```bash
docker context create prod --docker "host=ssh://deploy@prod.example.com"
docker context use prod
docker ps            # now runs against the prod server
docker context use default
```

`docker context ls` shows all contexts and which one is active.

## 104: Why do you need sudo for docker commands on Linux?

The Docker socket is owned by root and the `docker` group. If your user is not in that group, you need `sudo`.

You can add yourself to the group with `sudo usermod -aG docker $USER` and log in again. Keep in mind that membership in the `docker` group is basically root access to the host, because you can start a container that mounts `/`. Rootless mode is an option if that is a concern.

## 105: What is the docker group?

It is a Linux group that has access to the Docker socket. Anyone in it can run Docker commands without `sudo`.

Since controlling Docker means you can mount any host path and run privileged containers, being in the `docker` group is effectively the same as having root. Only add trusted users.

## 106: What does docker run -d mean and how do you get back to the container?

`-d` (detached) runs the container in the background and prints its ID. Your terminal is free right away.

To see what it is doing, use `docker logs -f <name>`. To get a shell, use `docker exec -it <name> sh`. To connect to the main process, use `docker attach <name>`.

## 107: How do you pause and unpause a container?

```bash
docker pause web
docker unpause web
```

Pausing freezes all processes in the container using the cgroup freezer. They get no CPU time but stay in memory. This is different from `docker stop`, which ends the processes.

## 108: What container states exist?

- `created`: the container exists but was never started.
- `running`: the main process is running.
- `paused`: the processes are frozen.
- `restarting`: Docker is restarting it because of the restart policy.
- `exited`: the main process ended.
- `dead`: Docker failed to remove it properly.

You see the state in the `STATUS` column of `docker ps -a`.

## 109: What does the exit code of a container mean?

The container's exit code is the exit code of its main process. Some common ones:

- `0`: finished normally.
- `1`: general app error.
- `137`: killed with `SIGKILL` (128 + 9). Often caused by the OOM killer or by `docker stop` timing out.
- `143`: stopped with `SIGTERM` (128 + 15).
- `126` / `127`: command not executable or not found.

```bash
docker inspect -f '{{.State.ExitCode}} {{.State.OOMKilled}}' web
```

## 110: How do you run a one-off command with docker run?

Add the command after the image name. It replaces the image's `CMD`.

```bash
docker run --rm alpine:3.22 echo "hello"
docker run --rm python:3.13-slim python -c "print(2 + 2)"
```

This is a quick way to try tools or versions without installing anything on your machine.

## 111: How do you override the entrypoint of an image?

```bash
docker run --rm -it --entrypoint sh my-app
```

This is handy when an image has an `ENTRYPOINT` that starts the app and you want a shell to look around instead.

## 112: What is the scratch image?

`scratch` is a special, completely empty image. It has no shell, no libraries and no files. You use it as a base for statically compiled binaries, for example Go programs.

```dockerfile
FROM golang:1.25 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /app .

FROM scratch
COPY --from=build /app /app
ENTRYPOINT ["/app"]
```

The result is tiny, but there is no shell for debugging, and you may need to copy in CA certificates and timezone data yourself.

## 113: What is a distroless image?

Distroless images (from Google, for example `gcr.io/distroless/nodejs22-debian12`) contain only your app's runtime and its dependencies. They have no shell and no package manager.

They are smaller and have fewer packages that could have vulnerabilities. The trade-off is that debugging is harder, since you cannot just `exec` into a shell. Many have a `:debug` variant with a busybox shell.

## 114: How do you name a container and why does it matter?

Use `--name`:

```bash
docker run -d --name api my-api
```

Without it, Docker picks a random name like `focused_turing`. A fixed name makes it easier to run commands (`docker logs api`) and other containers on the same user-defined network can reach it by that name. Names must be unique on a host.

## 115: What happens if you run docker run twice with the same name?

The second command fails with an error saying the name is already in use, even if the first container is stopped. You need to remove the old one first (`docker rm api`) or pick another name.

## 116: How do you view the processes inside a container?

```bash
docker top web
```

It shows the processes running in the container, as seen from the host. If the image has `ps`, you can also run `docker exec web ps aux`.

## 117: What is the docker events command?

`docker events` streams real-time events from the daemon: containers being created, started, killed, dying, images being pulled, networks connecting and so on.

```bash
docker events --filter type=container --filter event=die
```

It is useful for debugging containers that keep restarting, or for simple automation.

## 118: How do you filter docker ps output?

```bash
docker ps --filter status=exited
docker ps --filter name=api
docker ps --filter label=env=prod
docker ps --format '{{.Names}}\t{{.Status}}'
```

`--filter` narrows the list and `--format` uses Go templates to choose which columns to print.

## 119: What does docker run --env-file do?

It reads environment variables from a file, one `KEY=value` per line, and passes them into the container.

```text
# app.env
NODE_ENV=production
LOG_LEVEL=info
```

```bash
docker run --env-file app.env my-app
```

Quotes in the file are not handled like in a shell, so values are taken mostly as written.

## 120: What is an anonymous volume?

An anonymous volume is a volume without a name you chose. Docker gives it a random ID. It is created when you use `-v /data` without a source, or when an image has a `VOLUME` instruction and you do not mount anything there.

Anonymous volumes are hard to find again and pile up over time. Use named volumes for data you care about.

## 121: Where does Docker store volumes on Linux?

By default, in `/var/lib/docker/volumes/<name>/_data`. You can see the exact path with:

```bash
docker volume inspect pgdata -f '{{.Mountpoint}}'
```

You should not change files there directly while containers are using them. On Docker Desktop, this path is inside the VM, not on your Mac or Windows filesystem.

## 122: How do you make a mount read-only?

Add `:ro` or `readonly`:

```bash
docker run -v ./nginx.conf:/etc/nginx/nginx.conf:ro nginx
docker run --mount type=bind,src=./config,dst=/config,readonly my-app
```

The container can read the files but cannot change them. This is a good default for config files.

## 123: How do you see the networks on a host?

```bash
docker network ls
docker network inspect app-net
```

By default you will see `bridge`, `host` and `none`, plus any networks you or Compose created. `inspect` shows the subnet, gateway and which containers are connected.

## 124: How do you remove a network?

```bash
docker network rm app-net
docker network prune   # remove all unused networks
```

You cannot remove a network while containers are connected to it. Disconnect them first with `docker network disconnect` or stop and remove them.

## 125: What is port mapping and why do you need it?

Containers have their own network namespace, so a port the app opens inside the container is not open on the host. Port mapping (`-p 8080:80`) tells Docker to forward traffic from a host port to a container port.

You only need it for traffic that comes from outside Docker (a browser, another machine). Containers on the same Docker network can talk directly using the container port.

## 126: What does 0.0.0.0 mean in port mappings?

`0.0.0.0:8080->80/tcp` means port 8080 is open on all network interfaces of the host, so other machines can reach it. If you only want local access, bind to localhost:

```bash
docker run -p 127.0.0.1:5432:5432 postgres:17
```

This is a good habit for databases on a dev machine or server.

## 127: How do you start a database for local development with Docker?

```bash
docker run -d --name pg \
  -e POSTGRES_PASSWORD=dev \
  -p 127.0.0.1:5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:17
```

You get a running Postgres in a few seconds without installing it. The volume keeps the data between restarts. Remove everything with `docker rm -f pg && docker volume rm pgdata`.

## 128: What is the depends_on option in Compose?

`depends_on` sets the start order of services.

```yaml
services:
  api:
    build: .
    depends_on:
      - db
  db:
    image: postgres:17
```

Compose starts `db` before `api`, and stops `api` before `db`. In this short form it only waits for the container to start, not for the database to be ready. For that, you use `condition: service_healthy` with a healthcheck.

## 129: How do you build images with Compose?

Use `build` instead of (or together with) `image`:

```yaml
services:
  api:
    build:
      context: ./api
      dockerfile: Dockerfile
    image: my-org/api:dev
```

`docker compose build` builds them, and `docker compose up --build` builds before starting. If you set both `build` and `image`, the built image gets that name.

## 130: How do you define volumes in Compose?

```yaml
services:
  db:
    image: postgres:17
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro

volumes:
  pgdata:
```

Named volumes must be listed under the top-level `volumes` key. Paths that start with `.` or `/` are bind mounts.

## 131: How do you define ports and environment variables in Compose?

```yaml
services:
  api:
    image: my-api:1.0
    ports:
      - "3000:3000"
      - "127.0.0.1:9229:9229"
    environment:
      NODE_ENV: production
      LOG_LEVEL: info
```

Quote port mappings. YAML can read some unquoted values like `22:22` as a base-60 number in older parsers, so quotes avoid surprises.

## 132: How do you see logs for all services in Compose?

```bash
docker compose logs
docker compose logs -f
docker compose logs -f api worker
docker compose logs --tail 50 api
```

Each line is prefixed with the service name, so you can follow several services at once.

## 133: What is a Compose project name?

Compose groups everything it creates under a project name. By default it is the name of the folder that contains `compose.yaml`. Container, network and volume names are prefixed with it, for example `shop-db-1` and `shop_default`.

You can change it with `-p`, the `COMPOSE_PROJECT_NAME` variable or the top-level `name:` key in the file. Different project names let you run two copies of the same stack.

## 134: How do you run a one-off command in a Compose service?

```bash
docker compose run --rm api npm run migrate
docker compose exec api npm run migrate
```

- `run` starts a new container for the service with the command you give.
- `exec` runs the command in the already running container.

Use `run --rm` for tasks like migrations or tests, so the container is cleaned up afterwards.

## 135: What is the image digest?

A digest is a SHA-256 hash of the image manifest, written like `sha256:3f2a...`. Unlike a tag, it never changes: the same digest always means the exact same image content.

```bash
docker pull nginx@sha256:<digest>
docker images --digests
```

Pinning by digest gives fully repeatable deploys.

## 136: How do you see the IP address of a container?

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}} {{end}}' web
```

You rarely need the IP, though. Container IPs can change on restart. Use container names or service names on a user-defined network instead.

## 137: What is the difference between docker image ls and docker images?

There is no difference. Docker added management commands grouped by object (`docker image ...`, `docker container ...`, `docker volume ...`) to make the CLI more consistent. The old short commands (`docker images`, `docker ps`, `docker rmi`) still work and are just aliases.

## 138: What is the hello-world image?

`hello-world` is a tiny image that prints a message and exits. You run it right after installing Docker to check that everything works: the client can reach the daemon, the daemon can pull from Docker Hub and can start a container.

```bash
docker run --rm hello-world
```

## 139: What is a Dockerfile comment and a parser directive?

Lines that start with `#` are comments. A special kind of comment at the very top of the file is a parser directive, for example the syntax directive:

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine
```

The `syntax` line tells BuildKit which Dockerfile frontend version to use, so you get the latest stable Dockerfile features no matter which Docker version is installed.

## 140: Can a Dockerfile have more than one CMD?

You can write several, but only the last `CMD` is used. The same is true for `ENTRYPOINT`. Docker's build checks warn about this, because it is usually a mistake.

## 141: What does the SHELL instruction do?

`SHELL` changes the shell used for shell-form commands. The default on Linux is `["/bin/sh", "-c"]`.

```dockerfile
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -fsSL https://example.com/install.sh | bash
```

Here `pipefail` makes the `RUN` fail if `curl` fails, instead of only looking at the exit code of the last command in the pipe.

## 142: What is the STOPSIGNAL instruction?

`STOPSIGNAL` sets which signal `docker stop` sends to the main process. The default is `SIGTERM`.

```dockerfile
STOPSIGNAL SIGQUIT
```

Some programs use a different signal for graceful shutdown. For example, nginx does a graceful shutdown on `SIGQUIT`, which is why the official nginx image sets it.

## 143: How do you update an image to a newer version?

Images do not update themselves. You pull or build the new version and recreate the container:

```bash
docker pull nginx:1.27
docker rm -f web
docker run -d --name web -p 8080:80 nginx:1.27
```

With Compose:

```bash
docker compose pull
docker compose up -d
```

Compose only recreates containers whose image or config changed.

## 144: What is Docker Swarm?

Swarm mode is Docker's built-in orchestrator. It joins several Docker hosts into a cluster and lets you run services with replicas, rolling updates, overlay networks and secrets.

```bash
docker swarm init
docker service create --name web --replicas 3 -p 80:80 nginx
```

It is simpler than Kubernetes but much less popular. Most teams that need orchestration today use Kubernetes or a managed container service.

## 145: What is the relationship between Docker and Kubernetes?

Docker is used to build images and run containers on one machine. Kubernetes is an orchestrator that runs containers across many machines, handles scaling, self-healing, service discovery and rolling updates.

Images built with Docker follow the OCI standard, so Kubernetes can run them. Kubernetes does not use the Docker daemon directly anymore (dockershim was removed in v1.24). It uses containerd or CRI-O, which run the same images.

## 146: What is OCI?

The Open Container Initiative (OCI) is a Linux Foundation project that defines open standards for containers:

- **Image spec:** how an image and its layers are stored.
- **Runtime spec:** how a container is started from a filesystem bundle.
- **Distribution spec:** how registries serve images.

Because of these standards, an image built with Docker can be run by Podman, containerd or Kubernetes, and pushed to any compliant registry.

## 147: What are some alternatives to Docker?

- **Podman:** daemonless, rootless by default, mostly the same CLI (`alias docker=podman`).
- **containerd with nerdctl:** the runtime Docker itself uses, with a Docker-like CLI.
- **Buildah / kaniko:** build images without a Docker daemon (common in CI).
- **Rancher Desktop, OrbStack, Colima:** Docker Desktop alternatives on macOS and Windows.

All of them work with OCI images, so you can mix them.

## 148: How do you log in to a registry?

```bash
docker login                     # Docker Hub
docker login ghcr.io -u my-user  # GitHub Container Registry
echo "$TOKEN" | docker login ghcr.io -u my-user --password-stdin
```

Use `--password-stdin` in scripts so the password does not end up in your shell history. Credentials are saved in `~/.docker/config.json` or, better, in a credential helper.

## 149: How do you check the Docker Compose version?

```bash
docker compose version
```

It prints the Compose plugin version. Compose v2 and later are all part of the same `docker compose` plugin. Current releases are in the v5 line.

## 150: What is docker init?

`docker init` asks a few questions about your project (language, version, port, start command) and creates a `Dockerfile`, `compose.yaml`, `.dockerignore` and a README with sensible defaults.

```bash
cd my-project
docker init
```

It supports common stacks such as Node.js, Python, Go, Rust, Java, PHP and .NET. It is a good starting point, and you can adjust the files afterwards.

---

# Moderate Questions (151-300)

## 151: How do you write a good Dockerfile for a Node.js app?

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-slim AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --omit=dev

FROM node:22-slim
ENV NODE_ENV=production
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY --chown=node:node . .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

Main points: pin the base image version, install dependencies before copying source code so the cache works, use `npm ci` for repeatable installs, use a cache mount for the npm cache, run as the non-root `node` user, and use the exec form of `CMD`.

## 152: How do you order Dockerfile instructions to get the most out of the cache?

Put things that change rarely at the top and things that change often at the bottom:

1. `FROM` and system packages
2. Dependency manifests (`package.json`, `requirements.txt`, `go.mod`)
3. Dependency install
4. Source code
5. Build step

When you change one line of code, only steps 4 and 5 run again. If you copy all source code before installing dependencies, every code change reinstalls everything.

## 153: How does Docker decide whether a cached layer can be reused?

For most instructions, Docker compares the instruction text with the cached one. For `COPY` and `ADD`, it also compares checksums of the files being copied (content and metadata, not modification time).

If anything differs, that layer and every layer after it are rebuilt. `RUN` commands are not re-run just because the outside world changed: `RUN apt-get update` stays cached even if new packages are out. Use `--no-cache` or change the instruction to force it.

## 154: Why should you combine apt-get update and apt-get install in one RUN?

```dockerfile
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*
```

If `apt-get update` is in its own `RUN`, it gets cached. Later, when you add a package to the install line, Docker reuses the old package index, and the install can fail or install old versions. Putting them together means the index is always refreshed when the package list changes. Removing `/var/lib/apt/lists` in the same step keeps the layer small.

## 155: How do you make images smaller?

- Use a small base image (`-slim`, Alpine, distroless or `scratch`).
- Use multi-stage builds so build tools stay out of the final image.
- Install only production dependencies.
- Clean package caches in the same `RUN` that created them.
- Use `--no-install-recommends` with apt.
- Use a `.dockerignore` so you do not copy tests, docs or `.git`.
- Check what takes space with `docker image history` or a tool like `dive`.

## 156: What is BuildKit?

BuildKit is the build engine behind `docker build`. It has been the default since Docker 23. Compared to the old builder, it:

- Runs independent stages in parallel and skips stages the target does not need
- Has better caching, including cache export and import
- Supports cache mounts, secret mounts and SSH mounts in `RUN`
- Can build for several platforms
- Gives clearer progress output

## 157: What is Buildx?

Buildx is the Docker CLI plugin that talks to BuildKit. `docker build` is actually an alias for `docker buildx build` now.

Buildx adds features on top: creating separate builders (`docker buildx create`), building multi-platform images, exporting results to different outputs, and running several builds from one file with `docker buildx bake`.

## 158: How do you build an image for a different CPU architecture?

Use `--platform`:

```bash
docker buildx build --platform linux/amd64 -t my-app:amd64 .
docker buildx build --platform linux/amd64,linux/arm64 -t my-org/app:1.0 --push .
```

On a Mac with Apple Silicon, images are `linux/arm64` by default. If your servers are `amd64`, you need to build for that platform or build a multi-platform image. Cross builds use QEMU emulation (slow) unless you use cross-compilation in the Dockerfile or native builders.

## 159: What is a multi-platform image?

A multi-platform image is one tag that points to an image index (manifest list) with a separate image for each platform, for example `linux/amd64` and `linux/arm64`. When you pull it, Docker automatically picks the version for your machine.

Official images like `node` and `postgres` are multi-platform. You can check with:

```bash
docker buildx imagetools inspect node:22
```

## 160: How do you pass secrets to a build safely?

Use a secret mount. The secret is available only during that `RUN` and is never saved in a layer.

```dockerfile
# syntax=docker/dockerfile:1
RUN --mount=type=secret,id=npm_token,env=NPM_TOKEN \
    npm ci
```

```bash
docker build --secret id=npm_token,env=NPM_TOKEN -t my-app .
```

Do not use `ARG` or `ENV` for secrets, and do not `COPY` a secret file and then delete it. The file would still exist in an earlier layer.

## 161: What is a cache mount?

A cache mount gives a `RUN` step a folder that is kept between builds but is not part of the image. It is used for package manager caches.

```dockerfile
RUN --mount=type=cache,target=/root/.npm npm ci
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    apt-get update && apt-get install -y gcc
```

Even when the layer cache is invalid (for example `package.json` changed), the package manager can reuse already downloaded packages, so the step runs much faster.

## 162: What is an SSH mount in a build?

An SSH mount forwards your local SSH agent into a `RUN` step, so the build can clone private Git repos without copying your private key into the image.

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine:3.22
RUN apk add --no-cache git openssh-client
RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN --mount=type=ssh git clone git@github.com:my-org/private-lib.git
```

```bash
docker build --ssh default .
```

## 163: What is a bind mount in a RUN instruction?

`RUN --mount=type=bind` makes files from the build context (or another stage) available during one `RUN` without copying them into a layer.

```dockerfile
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev
```

This is the pattern `docker init` uses. The lock files are used for the install but do not add a separate layer.

## 164: How do you build only one stage of a multi-stage Dockerfile?

Use `--target`:

```dockerfile
FROM node:22 AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM base AS test
COPY . .
RUN npm test

FROM base AS prod
COPY . .
CMD ["node", "server.js"]
```

```bash
docker build --target test .
docker build --target prod -t my-app .
```

BuildKit only builds the stages the target depends on, so building `prod` skips `test`.

## 165: How do you use a named stage as a base for another stage?

You give a stage a name with `AS` and then use that name in a later `FROM` or `COPY --from`:

```dockerfile
FROM python:3.13-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS dev
RUN pip install --no-cache-dir debugpy
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "app.py"]

FROM base AS prod
COPY . .
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
```

## 166: How can you copy files from another image in a Dockerfile?

`COPY --from` accepts a full image name, not only a stage name:

```dockerfile
FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
```

This is a common way to add a single binary without installing it with a package manager. Pin the image version (or digest) in real projects.

## 167: What is the difference between docker build --pull and a normal build?

Normally, if you already have the base image locally (say `node:22`), BuildKit uses that local copy. With `--pull`, it checks the registry for a newer version of the base image first.

In CI it is a good idea to use `--pull` so you get security fixes in base images instead of building on an old cached copy.

## 168: How do you write a Python Dockerfile?

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
COPY . .
RUN useradd --no-create-home appuser
USER appuser
EXPOSE 8000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
```

`PYTHONUNBUFFERED=1` makes logs show up right away in `docker logs`. Binding to `0.0.0.0` (not `127.0.0.1`) is needed so the app is reachable from outside the container.

## 169: Why does my app work inside the container but not from the host?

The most common reason is that the app listens on `127.0.0.1` (localhost) inside the container. That address only accepts connections from inside the same container. Port forwarding from the host arrives on the container's network interface, not on its loopback.

Make the app listen on `0.0.0.0`. Other things to check: the port is published (`-p`), the container port in `-p` matches the port the app uses, and the container is actually running.

## 170: How do you wait for a database to be ready before starting the app in Compose?

Add a healthcheck to the database and use `condition: service_healthy`:

```yaml
services:
  db:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: example
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 3s
      retries: 10

  api:
    build: .
    depends_on:
      db:
        condition: service_healthy
```

Your app should still retry connections, because the database can restart later too.

## 171: What conditions can you use in depends_on?

- `service_started`: the default. Wait until the container has started.
- `service_healthy`: wait until its healthcheck reports healthy.
- `service_completed_successfully`: wait until it exits with code 0. Good for one-off tasks like migrations.

```yaml
services:
  migrate:
    build: .
    command: npm run migrate
  api:
    build: .
    depends_on:
      migrate:
        condition: service_completed_successfully
```

You can also add `restart: true` so the dependent service restarts when the dependency is restarted by Compose.

## 172: How do you use several Compose files together?

You can pass several files with `-f`. Later files override or extend earlier ones.

```bash
docker compose -f compose.yaml -f compose.prod.yaml up -d
```

If you have `compose.override.yaml` next to `compose.yaml`, Compose loads it automatically. A common setup is to keep shared config in `compose.yaml` and dev-only settings (bind mounts, debug ports) in `compose.override.yaml`.

## 173: How are values merged when you combine Compose files?

- Single values like `image`, `command` or `restart` are replaced by the later file.
- Maps like `environment` and `labels` are merged key by key.
- Lists like `ports`, `expose` and `dns` are combined.
- `volumes` and `devices` are merged by mount path in the container.

You can see the final result with `docker compose config`.

## 174: What is the include key in Compose?

`include` lets one Compose file pull in other Compose files as separate parts of the app. Each included file keeps its own folder for relative paths.

```yaml
include:
  - ./infra/compose.db.yaml
  - ./infra/compose.cache.yaml

services:
  api:
    build: .
    depends_on:
      - db
```

This is different from `-f` merging. `include` is for splitting a big app into pieces, often owned by different teams.

## 175: What does docker compose config do?

It reads all Compose files, applies overrides, fills in variables and prints the final config. If there is a mistake, it shows an error.

```bash
docker compose config
docker compose config --services
docker compose -f compose.yaml -f compose.prod.yaml config
```

It is a quick way to check what Compose will actually run.

## 176: How does variable substitution work in Compose files?

Compose replaces `${VAR}` with values from your shell environment or the `.env` file.

```yaml
services:
  api:
    image: my-api:${TAG:-latest}
    environment:
      DB_PASSWORD: ${DB_PASSWORD:?DB_PASSWORD is required}
```

- `${VAR:-default}`: use `default` if `VAR` is unset or empty.
- `${VAR-default}`: use `default` only if unset.
- `${VAR:?message}`: fail with a message if unset or empty.
- `$$` writes a literal `$`.

## 177: What is the order of precedence for environment variables in Compose?

From highest to lowest, for variables set inside the container:

1. `docker compose run -e` on the command line
2. `environment` in the Compose file (its values can come from the shell or `.env` through substitution)
3. `env_file` in the Compose file
4. `ENV` in the Dockerfile

When a variable is set in more than one place, the higher one wins. If you are confused about the result, check `docker compose config` and `docker compose exec api env`.

## 178: What are profiles in Compose?

Profiles let you mark services that should only start when asked for.

```yaml
services:
  api:
    build: .
  db:
    image: postgres:17
  adminer:
    image: adminer
    profiles: ["tools"]
```

`docker compose up` starts `api` and `db`. `docker compose --profile tools up` also starts `adminer`. This is useful for debug tools, test runners or optional services.

## 179: What is Compose Watch?

Compose Watch syncs your code into running containers or rebuilds them when files change. You configure it in the `develop` section:

```yaml
services:
  web:
    build: .
    develop:
      watch:
        - action: sync
          path: ./src
          target: /app/src
        - action: rebuild
          path: package.json
```

```bash
docker compose watch
# or
docker compose up --watch
```

`sync` copies changed files into the container, `rebuild` builds a new image and recreates the container, and `sync+restart` copies files and then restarts the container.

## 180: When should you use Compose Watch instead of a bind mount?

Bind mounts share the whole folder, including things like `node_modules` from the host, which can break native modules built for another OS. On macOS and Windows they can also be slow.

Compose Watch only copies the files you choose and can ignore paths. It also handles changes that need a rebuild (like `package.json`). Bind mounts are still simpler for small projects and work without extra config.

## 181: How do you scale a service in Compose?

```bash
docker compose up -d --scale worker=3
```

Or in the file:

```yaml
services:
  worker:
    build: .
    deploy:
      replicas: 3
```

You cannot publish a fixed host port (like `"3000:3000"`) on a scaled service, because only one container can bind that port. Either publish only the container port (`"3000"`, Docker picks random host ports) or put a load balancer in front.

## 182: How do you set resource limits in Compose?

```yaml
services:
  api:
    image: my-api:1.0
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512M
        reservations:
          memory: 256M
```

Current Compose applies `deploy.resources` when running locally too. You can also use the shorter `mem_limit` and `cpus` keys.

## 183: How do you use secrets in Compose?

```yaml
services:
  api:
    image: my-api:1.0
    secrets:
      - db_password
    environment:
      DB_PASSWORD_FILE: /run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

The secret is mounted as a file at `/run/secrets/db_password`. Many official images (like `postgres` and `mysql`) support `_FILE` variables for this. Files are less likely to leak than environment variables, which show up in `docker inspect` and in crash dumps.

## 184: What are configs in Compose?

Configs are like secrets but for non-sensitive files, for example an nginx config. They are mounted into the container as files.

```yaml
services:
  web:
    image: nginx:1.27
    configs:
      - source: nginx_conf
        target: /etc/nginx/conf.d/default.conf

configs:
  nginx_conf:
    file: ./nginx/default.conf
```

You can also define the content inline with `content:` in newer Compose versions.

## 185: How do you define custom networks in Compose?

```yaml
services:
  web:
    image: nginx:1.27
    networks: [frontend]
  api:
    build: .
    networks: [frontend, backend]
  db:
    image: postgres:17
    networks: [backend]

networks:
  frontend:
  backend:
```

Now `web` can reach `api`, and `api` can reach `db`, but `web` cannot reach `db`. Splitting networks like this limits what each service can talk to.

## 186: How do you connect services from different Compose projects?

Create a network outside Compose and mark it as `external` in both projects:

```bash
docker network create shared-net
```

```yaml
services:
  api:
    build: .
    networks: [shared-net]

networks:
  shared-net:
    external: true
```

Compose will not create or delete an external network. It just attaches services to it. You can also reach another project's services with `include` if they are part of one app.

## 187: What is the difference between ports and expose in Compose?

- `ports` publishes ports to the host, so they are reachable from outside Docker.
- `expose` only documents ports for other services on the same network. It does not publish anything.

Containers on the same network can reach all ports of each other anyway, so `expose` is mostly informational.

## 188: How do you override the command of a service in Compose?

```yaml
services:
  worker:
    build: .
    command: ["node", "worker.js"]
    entrypoint: ["/app/docker-entrypoint.sh"]
```

`command` replaces the image's `CMD`, and `entrypoint` replaces its `ENTRYPOINT`. A common use is running a web server and a background worker from the same image with different commands.

## 189: How do you extend a service from another file in Compose?

With `extends`:

```yaml
# common.yaml
services:
  base:
    image: my-api:1.0
    environment:
      LOG_LEVEL: info
```

```yaml
# compose.yaml
services:
  api:
    extends:
      file: common.yaml
      service: base
    ports:
      - "3000:3000"
```

YAML anchors (`&default` and `<<: *default`) inside one file are another way to share settings. Compose ignores top-level keys that start with `x-`, so you can put shared blocks there.

## 190: What are x- extension fields in Compose?

Top-level (and service-level) keys that start with `x-` are ignored by Compose. You can use them with YAML anchors to avoid repeating config.

```yaml
x-common-env: &common-env
  LOG_LEVEL: info
  TZ: UTC

services:
  api:
    image: my-api:1.0
    environment:
      <<: *common-env
      PORT: "3000"
  worker:
    image: my-api:1.0
    environment: *common-env
```

## 191: How do you debug a container that exits right after starting?

1. Check the exit code and error: `docker ps -a` and `docker logs <name>`.
2. Check for OOM: `docker inspect -f '{{.State.OOMKilled}}' <name>`.
3. Start it with a shell instead of the normal command: `docker run -it --entrypoint sh my-app`, then run the command by hand.
4. Check that `CMD` runs a foreground process. If it starts a daemon that forks into the background, the main process ends and the container stops.
5. Check that files and paths exist in the image (`docker run --rm my-app ls -la /app`).

## 192: Why does a container stop right away when the main process runs in the background?

A container lives as long as its main process (PID 1). If your `CMD` starts a service that goes to the background (like `service nginx start` or `nginx` without `daemon off`), the starting process exits, and Docker sees the container as finished.

Run the program in the foreground:

```dockerfile
CMD ["nginx", "-g", "daemon off;"]
```

Do not use tricks like `tail -f /dev/null` to keep a container alive in production.

## 193: How do you write an entrypoint script?

```bash
#!/bin/sh
set -e

if [ -n "$RUN_MIGRATIONS" ]; then
  node migrate.js
fi

exec "$@"
```

```dockerfile
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["node", "server.js"]
```

`exec "$@"` replaces the shell with the `CMD` process, so your app becomes PID 1 and gets signals directly. Without `exec`, the shell stays PID 1 and `SIGTERM` may never reach your app.

## 194: Why does my entrypoint script fail with "no such file or directory" when the file exists?

The usual cause is Windows line endings (CRLF). The first line becomes `#!/bin/sh\r`, and the kernel looks for an interpreter called `sh\r`, which does not exist.

Other causes: the shebang points to `bash` but the image (for example Alpine) only has `sh`, or the binary was built for glibc and the image uses musl. Fix line endings with a `.gitattributes` rule (`*.sh text eol=lf`) or `dos2unix`.

## 195: What is PID 1 in a container and why does it matter?

The first process in a container gets PID 1 in its PID namespace. PID 1 is special in Linux:

- It does not get default signal handlers. If your app does not handle `SIGTERM` itself, the signal is ignored, and `docker stop` has to wait for the timeout and send `SIGKILL`.
- It must reap zombie child processes. Many apps do not do this.

To fix both, handle signals in your app and either run a small init process or use `docker run --init`.

## 196: What does docker run --init do?

It starts a tiny init process (`tini`, bundled with Docker) as PID 1, which then starts your command. The init process forwards signals to your app and reaps zombie processes.

```bash
docker run --init my-app
```

```yaml
services:
  api:
    image: my-app
    init: true
```

It is a cheap fix for apps that spawn child processes or do not handle signals as PID 1.

## 197: How do you handle graceful shutdown in a containerized Node.js app?

Listen for `SIGTERM`, stop accepting new work, finish what is in progress and then exit:

```js
const server = app.listen(3000);

process.on("SIGTERM", () => {
  console.log("SIGTERM received, closing server");
  server.close(() => {
    // close DB pools, flush queues, etc.
    process.exit(0);
  });
  setTimeout(() => process.exit(1), 10000).unref();
});
```

Run `node` directly (exec form `CMD ["node", "server.js"]`) instead of `npm start`. npm is not always reliable about passing signals to the child process.

## 198: How do you see why a container was killed?

```bash
docker inspect web --format '{{json .State}}'
```

Look at `ExitCode`, `OOMKilled`, `Error` and `FinishedAt`. Exit code 137 with `OOMKilled: true` means it hit its memory limit. Exit code 137 without OOM usually means it was killed by `docker stop` after the timeout or by someone running `docker kill`.

`docker events --filter container=web` and the host's kernel log (`dmesg`) can give more detail.

## 199: How do you limit the size of container logs?

The default `json-file` logging driver keeps logs forever unless you set limits. Set them per container or for the whole daemon:

```bash
docker run --log-opt max-size=10m --log-opt max-file=3 my-app
```

```json
{
  "log-driver": "local",
  "log-opts": { "max-size": "10m", "max-file": "3" }
}
```

The daemon config goes in `/etc/docker/daemon.json`. The `local` driver rotates by default and is more compact than `json-file`.

## 200: What logging drivers does Docker support?

- `json-file`: the default, stores JSON lines on disk.
- `local`: compressed, rotated files. Recommended for most single hosts.
- `journald`, `syslog`: send logs to the system log.
- `fluentd`, `gelf`, `awslogs`, `gcplogs`, `splunk`: send logs to external systems.
- `none`: no logs.

`docker logs` works with `json-file`, `local` and `journald`. For other drivers, Docker's "dual logging" keeps a local cache so `docker logs` still works.

## 201: How do user-defined bridge networks differ from the default bridge?

- **DNS:** on a user-defined network, containers can reach each other by name. On the default `bridge`, only by IP (the old `--link` flag is legacy).
- **Isolation:** only containers you attach can talk to each other. Everything without `--network` lands on the default bridge together.
- **Attach and detach on the fly:** you can connect and disconnect running containers.
- **Config per network:** you can set the subnet, MTU and other options per network.

Always use user-defined networks for apps. Compose does this for you.

## 202: How does DNS work between containers?

Docker runs an embedded DNS server at `127.0.0.11` inside every container on a user-defined network. When a container looks up a name, this server answers with the IP of the container (or service) with that name or network alias. Names it does not know are forwarded to the host's DNS servers.

You can add extra names with `--network-alias` or `aliases` in Compose.

## 203: What is a network alias?

An alias is an extra DNS name for a container on a specific network.

```bash
docker run -d --network app-net --network-alias search elasticsearch:8.15.0
```

```yaml
services:
  es:
    image: elasticsearch:8.15.0
    networks:
      app-net:
        aliases: [search]
```

Several containers can share an alias. Docker's DNS then returns all their IPs, which gives very basic round-robin load balancing.

## 204: How does a container reach a service running on the host?

On Docker Desktop, use the special name `host.docker.internal`. On Linux, it does not exist by default, but you can add it:

```bash
docker run --add-host=host.docker.internal:host-gateway my-app
```

```yaml
services:
  api:
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

`host-gateway` is replaced with the host's IP on the bridge. The service on the host must also listen on an interface the container can reach, not only `127.0.0.1`.

## 205: How does port publishing work under the hood on Linux?

When you publish a port, Docker adds NAT rules to the host firewall (iptables, or nftables with newer Docker versions) that forward traffic from the host port to the container's IP and port. It may also start a small `docker-proxy` process for cases like traffic from localhost.

This is also why published ports can bypass rules you set with `ufw`: Docker's rules are in a different chain that runs first. Bind to `127.0.0.1` or use the `DOCKER-USER` chain if you need to restrict access.

## 206: Why can published Docker ports ignore UFW rules?

UFW manages the `INPUT` chain. Traffic to published container ports is NATed and goes through the `FORWARD` chain, where Docker adds its own rules before UFW sees the packet. So a container published on `0.0.0.0:5432` can be reachable from the internet even if UFW blocks 5432.

Fixes:

- Publish only on `127.0.0.1` or a private interface.
- Add filtering rules to the `DOCKER-USER` chain, which Docker leaves for you.
- Do not publish ports that only other containers need.

## 207: What is the none network and when is it useful?

`--network none` gives the container only a loopback interface. It cannot reach anything and nothing can reach it.

It is useful for jobs that should have no network access at all, for example processing untrusted files, or running code you do not trust. It is a simple way to reduce what a compromised process can do.

## 208: What is the macvlan network driver?

`macvlan` gives each container its own MAC address and an IP on your physical network, so the container looks like a separate machine on the LAN.

```bash
docker network create -d macvlan \
  --subnet=192.168.1.0/24 --gateway=192.168.1.1 \
  -o parent=eth0 lan-net
```

It is used for legacy apps that expect to be directly on the network, or for network appliances. By default the host itself cannot talk to its macvlan containers, and some cloud networks do not allow multiple MAC addresses on one interface.

## 209: How do you set a fixed IP for a container?

Create a network with a subnet and pass `--ip`:

```bash
docker network create --subnet 172.30.0.0/24 fixed-net
docker run -d --network fixed-net --ip 172.30.0.10 nginx
```

This only works on user-defined networks. Most of the time you should use names instead of fixed IPs, but sometimes old software or firewall rules need them.

## 210: How do you enable IPv6 for containers?

Create a network with IPv6 turned on:

```bash
docker network create --ipv6 app-v6
```

Docker can assign an IPv6 subnet automatically from its default pools, or you can pass one with `--subnet`. In Compose, set `enable_ipv6: true` on the network. Your host also needs working IPv6 connectivity for containers to reach the outside.

## 211: How do you share a volume between containers?

Mount the same named volume in both:

```bash
docker volume create shared
docker run -d --name writer -v shared:/data alpine sh -c 'while true; do date >> /data/log; sleep 1; done'
docker run --rm -v shared:/data alpine tail /data/log
```

Docker does not lock the files, so the apps have to deal with concurrent writes themselves. Many apps (like databases) must never share their data folder with another instance.

## 212: How do you back up a volume?

Run a temporary container that mounts the volume and a host folder, and create an archive:

```bash
docker run --rm \
  -v pgdata:/data:ro \
  -v "$(pwd)":/backup \
  alpine tar czf /backup/pgdata.tar.gz -C /data .
```

Restore it the same way, with `tar xzf` into an empty volume. For databases, it is safer to use the database's own tools (`pg_dump`, `mysqldump`) because copying files of a running database can give an inconsistent backup.

## 213: What is a volume driver?

A volume driver decides where volume data is actually stored. The default `local` driver stores data on the host's disk. Plugins can store volumes on NFS, cloud block storage or distributed filesystems.

The `local` driver can also mount NFS shares:

```bash
docker volume create --driver local \
  --opt type=nfs --opt o=addr=10.0.0.5,rw \
  --opt device=:/exports/data nfs-data
```

## 214: How do file permissions work with bind mounts?

Linux checks permissions by numeric user ID (UID), not by name. If the container runs as UID 1000 and the host folder belongs to UID 1001, the container may not be able to write.

Common fixes:

- Run the container with your host UID: `docker run -u "$(id -u):$(id -g)" ...`.
- Make the image's user have the same UID as your host user.
- Change ownership of the host folder.

On Docker Desktop, file sharing usually maps permissions for you, so this mostly shows up on Linux hosts.

## 215: What happens when you mount a volume over a folder that already has files in the image?

- **Empty named volume:** Docker copies the image's files at that path into the volume the first time. This is how a new `postgres` volume gets the right structure.
- **Volume that already has data:** the existing volume content is shown, the image files are hidden.
- **Bind mount:** the host folder always hides the image files. Nothing is copied.

This is why a bind mount over `/app` can hide `node_modules` that you installed in the image.

## 216: How do you keep node_modules from the image when you bind mount your source code?

Add an extra anonymous or named volume for `node_modules`, so that path is not covered by the bind mount:

```yaml
services:
  web:
    build: .
    volumes:
      - .:/app
      - /app/node_modules
```

The bind mount shares your code, while `/app/node_modules` keeps the packages installed in the image (built for Linux). Compose Watch is a cleaner alternative that avoids this trick.

## 217: How do you set up hot reload for development with Docker?

Mount the source code into the container and run the dev server in watch mode, or use Compose Watch:

```yaml
services:
  web:
    build:
      context: .
      target: dev
    command: npm run dev
    ports:
      - "5173:5173"
    develop:
      watch:
        - action: sync
          path: ./src
          target: /app/src
        - action: rebuild
          path: package.json
```

If file change events do not reach the container (this can happen with some bind mount setups), enable polling in your dev tool, for example `CHOKIDAR_USEPOLLING=true` or the polling option of Vite or webpack.

## 218: How do you debug a Node.js app running in a container?

Start Node.js with the inspector listening on all interfaces and publish the port, only on localhost:

```yaml
services:
  api:
    build: .
    command: ["node", "--inspect=0.0.0.0:9229", "server.js"]
    ports:
      - "3000:3000"
      - "127.0.0.1:9229:9229"
```

Then attach VS Code or Chrome DevTools to `localhost:9229`. Never expose the inspector port publicly, because it allows running any code in the process.

## 219: What is a dev container?

A dev container is a container set up as your full development environment, defined in `.devcontainer/devcontainer.json`. Editors like VS Code and tools like GitHub Codespaces open the project inside that container, with the right runtime, tools and extensions.

```json
{
  "name": "api",
  "image": "mcr.microsoft.com/devcontainers/typescript-node:22",
  "forwardPorts": [3000],
  "postCreateCommand": "npm ci"
}
```

The whole team gets the same setup without installing tools locally.

## 220: How do you run tests in Docker?

A simple way is a test stage in your Dockerfile:

```dockerfile
FROM node:22-slim AS test
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm test
```

```bash
docker build --target test .
```

For integration tests that need a database, use Compose and run the tests in a one-off container:

```bash
docker compose run --rm api npm run test:integration
docker compose down -v
```

## 221: What is Testcontainers?

Testcontainers is a library (for Java, Node.js, Go, Python, .NET and others) that starts real Docker containers from your test code, for example a Postgres or Kafka, and removes them after the test.

```js
import { PostgreSqlContainer } from "@testcontainers/postgresql";

const pg = await new PostgreSqlContainer("postgres:17").start();
const url = pg.getConnectionUri();
// run tests against url
await pg.stop();
```

You test against the real database instead of mocks or in-memory replacements, and each test run gets a clean instance.

## 222: How do you build and push an image in GitHub Actions?

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v5
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v6
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

The `gha` cache keeps BuildKit layers between workflow runs, which makes builds much faster. Check the action docs for the current major versions.

## 223: How do you speed up Docker builds in CI?

- Use BuildKit's cache export: registry cache (`type=registry`) or the GitHub Actions cache (`type=gha`).
- Order the Dockerfile so dependency installs are cached.
- Use cache mounts for package managers.
- Use a `.dockerignore` to keep the context small.
- Split work into stages so they can run in parallel.
- Use a remote builder that keeps its cache, such as Docker Build Cloud or a self-hosted BuildKit.

## 224: What cache backends does BuildKit support?

- `inline`: cache metadata stored in the image itself. Simple but only supports `mode=min`.
- `registry`: cache stored as a separate image in a registry.
- `local`: cache stored in a local folder.
- `gha`: GitHub Actions cache.
- `s3` and `azblob`: cloud storage.

```bash
docker buildx build \
  --cache-from type=registry,ref=ghcr.io/my-org/api:cache \
  --cache-to type=registry,ref=ghcr.io/my-org/api:cache,mode=max \
  -t ghcr.io/my-org/api:1.0 --push .
```

`mode=max` caches layers of all stages, not only the final one.

## 225: How should you tag images in a CI pipeline?

Use tags that tell you what is inside:

- The Git commit SHA (`api:3f2a9b1`) for every build. It is unique and easy to trace.
- A version number for releases (`api:1.4.0`, and maybe `api:1.4` and `api:1`).
- Optionally a branch tag (`api:main`) for the latest build of a branch.

Deploy by version or SHA, not by `latest` or a branch name, so you always know what runs and can roll back. The `docker/metadata-action` in GitHub Actions can create these tags for you.

## 226: What is Docker Scout?

Docker Scout analyzes images for known vulnerabilities (CVEs) and outdated base images, and suggests fixes.

```bash
docker scout quickview my-app:1.0
docker scout cves my-app:1.0
docker scout recommendations my-app:1.0
```

It builds a list of packages in the image (an SBOM) and matches it against vulnerability databases. It is built into Docker Desktop and Docker Hub, and can run in CI.

## 227: How do you scan an image for vulnerabilities?

Common tools:

- `docker scout cves my-app:1.0`
- Trivy: `trivy image my-app:1.0`
- Grype: `grype my-app:1.0`
- Registry scanning in ECR, GHCR, Artifact Registry and others

Run scans in CI and fail the build on serious issues that have a fix. Rebuild images regularly, because new CVEs appear even when your code does not change.

## 228: What is an SBOM and how do you create one for an image?

An SBOM (software bill of materials) lists every package and version inside the image. It helps with vulnerability scanning and license checks.

```bash
docker buildx build --sbom=true -t my-org/api:1.0 --push .
docker scout sbom my-org/api:1.0
```

With `--sbom=true`, BuildKit attaches the SBOM to the image as an attestation, so it is stored in the registry with the image.

## 229: What is provenance in Docker builds?

Provenance is metadata that says how an image was built: the source repo, the commit, the Dockerfile, build args and the builder used. BuildKit can attach it as an attestation (based on the SLSA format).

```bash
docker buildx build --provenance=mode=max -t my-org/api:1.0 --push .
```

It lets others check that an image really came from your CI and your source code. Buildx adds minimal provenance by default when pushing to a registry.

## 230: How do you check what changed in a container's filesystem?

```bash
docker diff web
```

It lists files that were added (`A`), changed (`C`) or deleted (`D`) compared to the image. It is useful to find out what an app writes at run time, for example to decide what needs a volume or whether you can run with a read-only filesystem.

## 231: How do you run a container with a read-only filesystem?

```bash
docker run -d --read-only --tmpfs /tmp --tmpfs /run my-app
```

```yaml
services:
  api:
    image: my-app
    read_only: true
    tmpfs:
      - /tmp
```

The app cannot change its own files, which makes some attacks much harder. Give it writable places only where it really needs them, with tmpfs or volumes.

## 232: How do you run a container as a non-root user without changing the image?

```bash
docker run -u 1000:1000 my-app
docker run -u nobody my-app
```

In Compose, use `user: "1000:1000"`. The user does not have to exist in `/etc/passwd`, but the files the app needs must be readable (and writable where needed) by that UID.

## 233: What are Linux capabilities in Docker?

Linux splits root's powers into separate capabilities, like `NET_BIND_SERVICE` (bind ports below 1024), `CHOWN` or `SYS_ADMIN`. Docker gives containers a reduced default set, even when running as root.

You can remove more or add specific ones:

```bash
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE my-app
```

A good practice is to drop all capabilities and add back only what the app needs.

## 234: What does --privileged do and why is it dangerous?

`--privileged` gives the container all capabilities, access to all host devices, and turns off seccomp and AppArmor or SELinux restrictions. A process in a privileged container can easily take over the host.

It is sometimes used for Docker-in-Docker or hardware access. Avoid it. If you need one specific power, add that capability or device (`--device`, `--cap-add`) instead.

## 235: How do you give a container access to a host device?

```bash
docker run --device /dev/ttyUSB0 my-serial-app
docker run --device /dev/snd my-audio-app
```

This exposes only that device to the container, which is much safer than `--privileged`. For GPUs, you use `--gpus` with the NVIDIA Container Toolkit.

## 236: How do you use a GPU in a container?

On Linux with NVIDIA GPUs, install the NVIDIA driver and the NVIDIA Container Toolkit, then:

```bash
docker run --rm --gpus all nvidia/cuda:12.6.3-base-ubuntu24.04 nvidia-smi
```

In Compose:

```yaml
services:
  ml:
    image: my-ml-app
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

## 237: How do you use the Docker CLI from inside a container?

Mount the host's Docker socket:

```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock docker:cli docker ps
```

The container then controls the host's Docker daemon. This is used by CI agents, Traefik, Portainer and similar tools. Keep in mind this gives the container full control over the host. Mounting the socket with `:ro` does not help, because the API still accepts write requests. If a tool only needs to read, put a socket proxy in front that allows only some API calls.

## 238: What is Docker-in-Docker?

Docker-in-Docker (DinD) runs a full Docker daemon inside a container, usually with the `docker:dind` image and `--privileged`. It gives you an isolated Docker daemon, which some CI systems use for builds.

The downsides are the privileged mode, storage driver issues and no shared cache with the host. Alternatives: mount the host socket, use a remote BuildKit, or use daemonless tools like Buildah or kaniko.

## 239: How do you limit the number of processes in a container?

```bash
docker run --pids-limit 200 my-app
```

In Compose, use `pids_limit: 200`. This protects the host from fork bombs or apps that spawn too many processes by mistake. When the limit is hit, new `fork` calls fail inside the container.

## 240: How do you set ulimits for a container?

```bash
docker run --ulimit nofile=65535:65535 my-app
```

```yaml
services:
  api:
    image: my-app
    ulimits:
      nofile:
        soft: 65535
        hard: 65535
```

`nofile` (open files) is the most common one to raise, for example for servers with many connections or for Elasticsearch.

## 241: How do you set kernel parameters for a container?

Use `--sysctl` for namespaced kernel settings:

```bash
docker run --sysctl net.core.somaxconn=1024 my-app
```

In Compose, use the `sysctls` key. Only sysctls that belong to the container's namespaces (mostly `net.*` and some `kernel.*` IPC settings) can be set per container. Global ones like `vm.max_map_count` must be set on the host.

## 242: How do you set the timezone in a container?

Set the `TZ` variable. The image needs the timezone database (`tzdata`) installed:

```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends tzdata \
    && rm -rf /var/lib/apt/lists/*
ENV TZ=Europe/Berlin
```

Many teams keep containers in UTC and convert times in the app, which avoids surprises with daylight saving time.

## 243: What is the difference between docker compose stop and docker compose down?

- `stop` stops the containers but keeps them, along with networks and volumes. `docker compose start` brings them back as they were.
- `down` stops and removes containers and networks. Named volumes stay unless you add `-v`.

## 244: How do you recreate a single service in Compose?

```bash
docker compose up -d --force-recreate api
docker compose up -d --no-deps api   # do not touch its dependencies
docker compose up -d --build api     # rebuild then recreate
```

By default, `docker compose up -d` only recreates services whose config or image changed.

## 245: How do you stop Compose from removing containers that are no longer in the file?

When you remove a service from `compose.yaml`, its old container is not removed automatically. Compose warns about "orphan containers". Use:

```bash
docker compose up -d --remove-orphans
docker compose down --remove-orphans
```

## 246: How do you see the logs of a container that keeps restarting?

```bash
docker logs --tail 50 web
docker logs -f web
```

Docker keeps the logs of a container across restarts (the container stays the same), so `docker logs` shows output from earlier runs too. Combine it with `docker inspect -f '{{.RestartCount}}' web` and `docker events` to see how often and why it restarts.

## 247: How do you clean up Docker on a build server?

```bash
docker builder prune --filter until=72h -f
docker image prune -a --filter until=168h -f
docker container prune -f
```

Run cleanup on a schedule (cron or a CI job). `docker builder prune` removes build cache, which is often the biggest item. You can also set a garbage collection limit for BuildKit in `daemon.json` so the cache stays under a size.

## 248: How do you set default address pools for Docker networks?

Docker picks subnets for new networks from default pools (like `172.17.0.0/16` and up). If they clash with your company or VPN networks, set your own in `/etc/docker/daemon.json`:

```json
{
  "default-address-pools": [{ "base": "10.200.0.0/16", "size": 24 }]
}
```

Restart the daemon after changing it. You can also set `bip` to change the default bridge subnet.

## 249: What is daemon.json?

`/etc/docker/daemon.json` (on Linux) is the config file for the Docker daemon. Common settings:

```json
{
  "log-driver": "local",
  "log-opts": { "max-size": "10m" },
  "registry-mirrors": ["https://mirror.example.com"],
  "live-restore": true,
  "default-address-pools": [{ "base": "10.200.0.0/16", "size": 24 }]
}
```

After changing it, restart Docker with `sudo systemctl restart docker`. On Docker Desktop, you edit it in the settings under "Docker Engine".

## 250: What is live-restore?

With `"live-restore": true` in `daemon.json`, containers keep running when the Docker daemon stops or restarts, for example during an engine upgrade. When the daemon comes back, it reconnects to them.

It reduces downtime on single hosts. It does not work with Swarm mode.

## 251: How do you use a registry mirror or pull-through cache?

A pull-through cache is a registry that sits between your hosts and Docker Hub. The first pull downloads the image from Hub, and later pulls come from the cache. This saves bandwidth and helps with Docker Hub rate limits.

```json
{
  "registry-mirrors": ["https://mirror.example.com"]
}
```

The `registry-mirrors` setting only applies to Docker Hub images. For other registries, you point image names at your proxy directly (for example Harbor or Artifactory proxy projects).

## 252: How do you run a private registry?

The simplest way is the open source `registry` image (the CNCF Distribution project):

```bash
docker run -d -p 5000:5000 --name registry \
  -v registry-data:/var/lib/registry registry:3
docker tag my-app localhost:5000/my-app:1.0
docker push localhost:5000/my-app:1.0
```

For real use, put TLS and authentication in front of it. Harbor is a fuller option with a UI, user management, scanning and replication.

## 253: What is an insecure registry?

By default, Docker only talks to registries over HTTPS with a trusted certificate (localhost is an exception). If you have a registry on plain HTTP or with a self-signed certificate, you must list it in `daemon.json`:

```json
{
  "insecure-registries": ["registry.internal:5000"]
}
```

Only do this on trusted internal networks. A better fix for self-signed certs is to add your CA certificate to `/etc/docker/certs.d/<registry>/ca.crt`.

## 254: What are credential helpers?

By default, `docker login` stores credentials in `~/.docker/config.json`, base64-encoded but not encrypted. Credential helpers store them in a secure place instead: macOS Keychain, Windows Credential Manager, `pass` on Linux, or they fetch short-lived tokens from a cloud provider.

```json
{
  "credsStore": "osxkeychain",
  "credHelpers": {
    "123456789012.dkr.ecr.eu-west-1.amazonaws.com": "ecr-login"
  }
}
```

## 255: What are Docker Hub rate limits and how do you deal with them?

Docker Hub limits how many images you can pull in a time window. Anonymous users have the lowest limit (counted per IP), and logged-in and paid users get more. Shared CI runners often hit the anonymous limit because many jobs share one IP.

Ways to deal with it:

- Log in to Docker Hub in CI.
- Use a pull-through cache or mirror.
- Copy the base images you use into your own registry.
- Use a cloud provider's mirror of Docker Hub where available.

## 256: How do you pin a base image to a digest and still get updates?

Write the tag and the digest together:

```dockerfile
FROM node:22-slim@sha256:<digest>
```

Docker uses the digest and ignores the tag, but the tag tells readers what version it is. To still get security fixes, use a bot like Renovate or Dependabot, which opens pull requests when a new digest is published for that tag.

## 257: How do you inspect an image in a registry without pulling it?

```bash
docker buildx imagetools inspect nginx:1.27
docker manifest inspect nginx:1.27
```

`imagetools inspect` shows the manifest list, the platforms and digests. It is useful to check whether an image supports `arm64` or to get the digest for pinning.

## 258: What is docker buildx bake?

Bake builds several images from one config file (HCL, JSON or a Compose file), in parallel.

```hcl
group "default" {
  targets = ["api", "worker"]
}

target "api" {
  context = "./api"
  tags = ["my-org/api:latest"]
  platforms = ["linux/amd64", "linux/arm64"]
}

target "worker" {
  context = "./worker"
  tags = ["my-org/worker:latest"]
}
```

```bash
docker buildx bake
docker buildx bake --push api
```

It replaces long shell scripts full of `docker build` commands. Current Compose versions use Bake under the hood for `docker compose build`.

## 259: How do you create and use a separate Buildx builder?

```bash
docker buildx create --name multi --driver docker-container --use
docker buildx inspect --bootstrap
docker buildx build --platform linux/amd64,linux/arm64 -t my-org/app:1.0 --push .
```

The `docker-container` driver runs BuildKit in its own container. It supports features the default builder may not, like exporting cache to a registry and building multi-platform images on systems that do not use the containerd image store.

## 260: What build outputs does Buildx support?

With `--output` (or `-o`) you choose where the result goes:

```bash
docker buildx build -o type=docker .                # load into local image store
docker buildx build -o type=registry -t repo/app .  # push (same as --push)
docker buildx build -o type=local,dest=./out .      # write files to a folder
docker buildx build -o type=tar,dest=out.tar .      # tar of the filesystem
docker buildx build -o type=oci,dest=app.tar .      # OCI image tarball
```

`type=local` is handy for using Docker only as a build tool, for example to compile a binary and copy it out.

## 261: How do you get build artifacts out of a Docker build without running a container?

Make a final stage that only contains the artifact, and export it with a local output:

```dockerfile
FROM golang:1.25 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /out/app .

FROM scratch AS artifact
COPY --from=build /out/app /
```

```bash
docker build --target artifact -o ./bin .
```

The binary ends up in `./bin/app` on your machine.

## 262: What are build checks?

Build checks are lint rules that BuildKit runs on your Dockerfile. For example, they warn when `FROM` and `AS` use different casing, when you use the legacy `ENV key value` format, when `CMD` uses the shell form instead of JSON, when a variable is used but never defined, or when an `ARG` or `ENV` name looks like a secret.

```bash
docker build --check .
```

Warnings are shown during normal builds too. You can make a build fail on warnings with a `# check=error=true` directive at the top of the Dockerfile.

## 263: How do you use heredocs in a Dockerfile?

With the Dockerfile 1.4+ syntax, you can write multi-line scripts and files with heredocs:

```dockerfile
# syntax=docker/dockerfile:1
RUN <<EOF
set -e
apt-get update
apt-get install -y --no-install-recommends curl
rm -rf /var/lib/apt/lists/*
EOF

COPY <<EOF /app/config.json
{ "port": 3000 }
EOF
```

This is easier to read than long lines joined with `&& \`.

## 264: What does COPY --link do?

`COPY --link` copies files into a separate, independent layer that does not depend on the layers below it.

```dockerfile
FROM nginx:1.27-alpine
COPY --link ./dist /usr/share/nginx/html
```

When the base image changes, BuildKit can reuse this layer without re-running the copy, and when pushing it can avoid re-uploading it. It works best for copying files into a final image, but you cannot rely on files or symlinks from earlier layers at the destination.

## 265: What does COPY --parents or --exclude do?

Newer Dockerfile syntax adds more `COPY` options:

- `--parents` keeps the folder structure of matched files: `COPY --parents ./packages/*/package.json ./` copies each `package.json` into its matching folder. This is useful for monorepos.
- `--exclude` skips matching files: `COPY --exclude=*.test.js ./src ./src`.

They need a recent `# syntax=docker/dockerfile:1` frontend. Check the Dockerfile reference before using them, since some options came out as labs features first.

## 266: How do you use ONBUILD?

`ONBUILD` adds an instruction that runs later, when someone else uses your image as a base.

```dockerfile
FROM node:22-slim
WORKDIR /app
ONBUILD COPY package*.json ./
ONBUILD RUN npm ci
ONBUILD COPY . .
```

It was popular for "builder" base images. It is hidden from the person writing the child Dockerfile, which makes builds hard to understand, so most teams avoid it today.

## 267: How do you write a Dockerfile for a Go app?

```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.25 AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg/mod go mod download
COPY . .
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    CGO_ENABLED=0 go build -ldflags="-s -w" -o /out/server ./cmd/server

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/server /server
USER nonroot:nonroot
ENTRYPOINT ["/server"]
```

The final image is just the binary plus CA certs and timezone data from distroless, and it runs as non-root.

## 268: How do you write a Dockerfile for a Java Spring Boot app?

```dockerfile
FROM eclipse-temurin:21-jdk AS build
WORKDIR /app
COPY . .
RUN ./mvnw -q package -DskipTests

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
RUN useradd --system appuser
USER appuser
EXPOSE 8080
ENTRYPOINT ["java", "-XX:MaxRAMPercentage=75", "-jar", "app.jar"]
```

`-XX:MaxRAMPercentage` makes the JVM size its heap based on the container memory limit. Spring Boot can also split the jar into layers (dependencies, app code) for better caching.

## 269: How do you serve a single-page app from a container?

Build it in a Node.js stage and serve the static files with nginx:

```dockerfile
FROM node:22-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
```

```nginx
server {
  listen 80;
  root /usr/share/nginx/html;
  location / {
    try_files $uri /index.html;
  }
}
```

The `try_files` line sends unknown paths to `index.html` so client-side routing works on refresh.

## 270: How do you handle runtime config for a frontend app in a container?

Frontend builds bake environment variables into the JavaScript at build time. If you want one image for all environments, you need runtime config:

- Generate a small `config.js` (or `config.json`) when the container starts, from environment variables, in an entrypoint script.
- Load it in `index.html` before the app bundle.

```sh
#!/bin/sh
cat > /usr/share/nginx/html/config.js <<EOF
window.APP_CONFIG = { apiUrl: "${API_URL}" };
EOF
exec nginx -g 'daemon off;'
```

Never put secrets there, since everything sent to the browser is public.

## 271: How do you put a reverse proxy in front of several containers?

Run nginx, Traefik or Caddy as a container on the same network and proxy to services by name:

```yaml
services:
  proxy:
    image: caddy:2
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy_data:/data
  api:
    build: ./api
  web:
    build: ./web

volumes:
  caddy_data:
```

```text
example.com {
  reverse_proxy /api/* api:3000
  reverse_proxy web:80
}
```

Only the proxy publishes ports. Caddy also gets TLS certificates automatically.

## 272: How do you run database migrations in a containerized setup?

Common options:

- A separate one-off service in Compose that runs migrations and exits, with other services depending on it using `service_completed_successfully`.
- A step in the deploy pipeline: `docker compose run --rm api npm run migrate` before switching traffic.
- A Kubernetes Job or init container.

Avoid running migrations at the start of every app container when you have several replicas. They can run at the same time and conflict, unless your migration tool uses a lock.

## 273: How do you deploy with Docker Compose to a single server?

A simple, common setup:

1. CI builds the image and pushes it to a registry with a version tag.
2. On the server, `compose.yaml` refers to `image: ghcr.io/my-org/api:${TAG}`.
3. Deploy runs:

```bash
export TAG=1.4.0
docker compose pull
docker compose up -d --remove-orphans
docker image prune -f
```

Add `restart: unless-stopped`, healthchecks, log limits and resource limits. This works well for small apps, but there is a short downtime while containers are recreated unless you put a proxy in front and run two copies.

## 274: How do you run Compose against a remote server?

Use a Docker context or `DOCKER_HOST` over SSH:

```bash
docker context create prod --docker "host=ssh://deploy@prod.example.com"
docker --context prod compose up -d
```

Compose reads the files locally and sends commands to the remote daemon. Bind mounts with relative paths then refer to the remote machine's filesystem, which can be confusing, so prefer images with everything baked in.

## 275: How do you get a basic zero-downtime deploy with Compose?

Compose recreates a container by stopping the old one and starting the new one, which causes a short gap. To avoid it:

- Run the new version next to the old one (for example scale to two replicas, or blue/green projects), wait for it to be healthy, then remove the old one.
- Put a reverse proxy (Traefik, Caddy, nginx) in front that sends traffic only to healthy containers.
- Make the app handle `SIGTERM` gracefully so in-flight requests finish.

Tools like Kamal or an orchestrator handle this for you. Compose alone was not designed for rolling deploys.

## 276: How do you see which image versions are running?

```bash
docker ps --format '{{.Names}}\t{{.Image}}'
docker inspect -f '{{.Config.Image}} {{.Image}}' api
docker compose images
```

`.Config.Image` is the name you used to start it, and `.Image` is the image ID. If you used a tag like `latest`, the image ID is the only reliable way to know which build is running.

## 277: How do you add a healthcheck to an image that has no curl?

Use a tool that exists in the image, or a tiny check written in the app's own language:

```dockerfile
HEALTHCHECK CMD ["node", "-e", "fetch('http://localhost:3000/health').then(r => process.exit(r.ok ? 0 : 1)).catch(() => process.exit(1))"]
```

Busybox images can use `wget -q -O- http://localhost/health`. For distroless images, you can ship a small health check binary or let the orchestrator do HTTP checks instead.

## 278: What are the healthcheck options?

- `--interval`: time between checks (default 30s).
- `--timeout`: how long one check may take (default 30s).
- `--retries`: failures in a row before it is `unhealthy` (default 3).
- `--start-period`: grace period during startup where failures do not count (default 0s).
- `--start-interval`: check interval during the start period (default 5s).

```dockerfile
HEALTHCHECK --interval=15s --timeout=3s --start-period=30s --retries=3 \
  CMD wget -q -O /dev/null http://localhost:8080/health || exit 1
```

## 279: Does Docker restart an unhealthy container?

No. Plain Docker only marks it as `unhealthy`. The restart policy reacts to the container exiting, not to the health status.

Swarm does replace unhealthy tasks, and Compose uses health status for `depends_on`. For single hosts, people sometimes use a small helper like `autoheal` that restarts unhealthy containers, or make the app exit when it is broken so the restart policy kicks in.

## 280: How do you handle environment-specific config for the same image?

Build one image and pass the environment-specific parts at run time:

- Environment variables for simple settings.
- Mounted config files (bind mount, Compose `configs`, Kubernetes ConfigMaps).
- Secrets as files.

Do not build a separate image per environment. Then the image you tested in staging is exactly the one that runs in production.

## 281: What is the twelve-factor app and how does it relate to Docker?

The twelve-factor app is a set of guidelines for building web apps. Several of them match how containers work:

- Store config in the environment.
- Treat logs as event streams (write to stdout).
- Processes are stateless; state goes in backing services.
- Fast startup and graceful shutdown.
- Same build runs in every environment.

Following them makes an app much easier to run in Docker and orchestrators.

## 282: How do you collect logs from many containers?

Write logs to stdout as structured JSON, and ship them with a log collector:

- A logging driver (`fluentd`, `gelf`, `awslogs`) that sends logs directly.
- An agent such as Fluent Bit, Vector or Promtail that reads the container log files on the host and forwards them to Loki, Elasticsearch or a cloud service.

The agent approach is more common, because if the log backend is down, the containers are not affected.

## 283: How do you monitor container metrics?

- `docker stats` for a quick look.
- cAdvisor exposes per-container CPU, memory, network and disk metrics for Prometheus.
- The Docker daemon can expose its own Prometheus metrics with `"metrics-addr": "127.0.0.1:9323"` in `daemon.json`.
- Node exporter for host metrics.

A typical stack is Prometheus plus Grafana, with alerts on memory near the limit, restart counts and unhealthy containers.

## 284: How do you give a container a custom hostname or extra hosts entries?

```bash
docker run --hostname api-1 --add-host db.local:10.0.0.5 my-app
```

```yaml
services:
  api:
    hostname: api-1
    extra_hosts:
      - "db.local:10.0.0.5"
```

`--add-host` writes an entry into the container's `/etc/hosts`. Docker manages that file, so do not edit it by hand inside the container.

## 285: How do you set custom DNS servers for containers?

```bash
docker run --dns 1.1.1.1 --dns-search corp.local my-app
```

Or for all containers in `daemon.json`:

```json
{ "dns": ["10.0.0.2", "1.1.1.1"] }
```

On user-defined networks, the container still uses Docker's embedded DNS (`127.0.0.11`), which forwards unknown names to the servers you set.

## 286: What is the difference between docker compose run and docker compose up for one service?

- `docker compose up api` starts the service as defined, with its ports, and also starts its dependencies.
- `docker compose run api <cmd>` starts a new one-off container with a different command. It does not publish the service's ports unless you add `--service-ports`, and it creates a container with a different name.

`run` is for tasks (tests, migrations, shells). `up` is for running the app.

## 287: How do you share a Compose app with someone who does not have the source code?

Push the images to a registry and share a `compose.yaml` that uses `image:` instead of `build:`. They only need the Compose file and access to the registry.

You can also publish the Compose file itself as an OCI artifact:

```bash
docker compose publish my-org/my-stack:1.0
docker compose -f oci://docker.io/my-org/my-stack:1.0 up -d
```

## 288: How do you run a cron job with Docker?

Options, from simplest:

- Use the host's cron to run `docker run --rm my-app node job.js` or `docker compose run --rm job`.
- Run a container with a small scheduler like `supercronic`, made for containers (logs to stdout, handles signals).
- In Kubernetes, use a CronJob.

Avoid running the standard `cron` daemon as a second process inside your app container. It does not pass environment variables to jobs by default and logs go to the wrong place.

## 289: How do you run more than one process in one container if you really must?

Use a small process manager as PID 1 that starts and watches the processes, for example `supervisord` or `s6-overlay`:

```dockerfile
RUN apt-get update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*
COPY supervisord.conf /etc/supervisor/conf.d/app.conf
CMD ["supervisord", "-n"]
```

It is sometimes acceptable (for example nginx plus PHP-FPM in one image), but you lose per-process restarts, separate scaling and separate logs. Separate containers are usually better.

## 290: What is the difference between a Docker image ID and a digest?

- The **image ID** is a hash of the image config. It identifies the image on your local machine.
- The **digest** (repo digest) is a hash of the manifest as stored in a registry. It is what you use to pull exactly that image.

With the classic storage, the same image can have a different local ID than its registry digest. With the containerd image store, local images are identified by their manifest or index digest, so the values usually match. When you pin images, use the repo digest.

## 291: How do you find out why an image is so large?

```bash
docker image history --no-trunc my-app:1.0
dive my-app:1.0
```

`dive` is a third-party tool that shows each layer's files and the wasted space. Common causes: build tools in the final image, package caches not cleaned, `node_modules` with dev dependencies, copying the whole repo including `.git`, or deleting files in a later layer (they still exist in the earlier one).

## 292: Does deleting a file in a later layer make the image smaller?

No. Layers are stacked. If one layer adds a 200 MB file and a later layer deletes it, the later layer just hides it with a "whiteout" marker. The 200 MB is still in the image and still downloaded.

To keep it out of the image, create and delete it in the same `RUN`, or use a multi-stage build and copy only what you need.

## 293: How do you build an image for a monorepo?

- Set the build context to the repo root so shared packages are available, and use `-f` to pick the app's Dockerfile.
- Use `.dockerignore` (or a per-Dockerfile `Dockerfile.dockerignore`) to skip the parts you do not need.
- Copy only the manifests first and install dependencies, then copy source code.
- Tools like `turbo prune` or `pnpm deploy` can produce a pruned copy of the workspace for one app.

```bash
docker build -f apps/api/Dockerfile -t api .
```

## 294: What is a per-Dockerfile ignore file?

BuildKit looks for an ignore file next to the Dockerfile named `<Dockerfile name>.dockerignore`. For example, if you build with `-f apps/api/Dockerfile`, it uses `apps/api/Dockerfile.dockerignore` instead of the root `.dockerignore`.

This lets different images in one repo use the same context with different ignore rules.

## 295: How do you use named build contexts?

You can give a build extra contexts besides the main one, and use them in `FROM` or `COPY --from`:

```bash
docker buildx build --build-context shared=../shared-lib -t api .
```

```dockerfile
COPY --from=shared . /app/shared
```

A named context can be a local folder, a Git URL or an image (`docker-image://alpine:3.22`). It is useful when files live outside the main context or when you want to replace a base image in tests.

## 296: How do you build from a Git repository directly?

```bash
docker build https://github.com/my-org/api.git#main
docker build https://github.com/my-org/api.git#v1.4.0:services/api
```

The part after `#` is the branch, tag or commit, and after `:` a subfolder to use as context. BuildKit clones the repo for you, so you do not need a local checkout.

## 297: How do you prevent secrets from leaking into images?

- Add `.env`, keys and credentials to `.dockerignore`.
- Never pass secrets as `ARG` or `ENV`.
- Use `RUN --mount=type=secret` for build-time secrets.
- Use runtime secrets (mounted files, a secrets manager) instead of baking them in.
- Scan images for secrets (Docker Scout, Trivy and others can detect some).
- If a secret ever ended up in a pushed image, rotate it. Deleting the tag is not enough.

## 298: What is the difference between docker compose build and docker build?

`docker build` builds one image from one Dockerfile with the options you type.

`docker compose build` builds every service that has a `build` section, with the context, Dockerfile, args, target and tags from the Compose file. Current Compose versions send this work to Buildx Bake, so services can build in parallel and share cache.

## 299: How do you pass build arguments in Compose?

```yaml
services:
  api:
    build:
      context: .
      args:
        NODE_VERSION: "22"
        APP_VERSION: ${APP_VERSION:-dev}
      target: prod
```

```bash
docker compose build --build-arg APP_VERSION=1.4.0
```

The Dockerfile must declare each one with `ARG`, or it is ignored.

## 300: What are lifecycle hooks in Compose?

Compose lets you run commands inside a service container right after it starts and right before it stops, with `post_start` and `pre_stop`:

```yaml
services:
  api:
    image: my-api:1.0
    post_start:
      - command: ["sh", "-c", "chown -R app:app /data"]
        user: root
    pre_stop:
      - command: ["./scripts/drain.sh"]
```

They are handy for small setup or cleanup tasks, like fixing volume permissions as root while the app itself runs as a normal user. Hooks were added in Compose 2.30, so older versions do not support them.

---

# Advanced Questions (301-450)

## 301: What happens step by step when you run docker run nginx?

1. The CLI sends a create request to the daemon's API.
2. The daemon checks for the image locally. If it is missing, it resolves the tag to a digest in the registry, pulls the manifest for your platform and downloads the missing layers.
3. The daemon prepares the container's root filesystem by stacking the image layers and adding a writable layer (through the snapshotter or storage driver).
4. It sets up networking: creates a network namespace, a veth pair connected to the bridge, assigns an IP and adds NAT rules for published ports.
5. It hands the container config to containerd, which starts a shim process and calls runc.
6. runc creates the namespaces and cgroups, applies seccomp, capabilities and AppArmor or SELinux, switches to the new root filesystem and runs the entrypoint.
7. runc exits. The shim stays as the parent of the container process and keeps stdout and stderr connected.

## 302: What are Linux namespaces and which ones do containers use?

Namespaces limit what a process can see. Each container gets its own:

- **PID:** its own process tree, where the app is PID 1.
- **NET:** its own network interfaces, IPs, routes and ports.
- **MNT:** its own mount table and root filesystem.
- **UTS:** its own hostname.
- **IPC:** its own shared memory and semaphores.
- **USER:** optional, maps container UIDs to different host UIDs.
- **CGROUP:** its own view of the cgroup tree.

You can share some of them on purpose, for example `--pid host` or `--network container:other`.

## 303: What are cgroups and how does Docker use them?

Control groups (cgroups) limit and measure how much of the host's resources a group of processes can use: CPU, memory, block I/O, number of processes and so on. Docker puts each container in its own cgroup and writes your `--memory`, `--cpus`, `--pids-limit` values into it.

Modern distros use cgroup v2, which has one unified tree and better memory accounting. Docker supports both v1 and v2, and `docker info` shows which one is in use.

## 304: What is the difference between namespaces and cgroups?

Namespaces control what a process can **see** (other processes, network, filesystem). Cgroups control how much a process can **use** (CPU, memory, I/O).

A container needs both: namespaces for isolation and cgroups for resource limits. Neither of them is a security boundary like a VM. Seccomp, capabilities and LSMs (AppArmor, SELinux) add the extra protection.

## 305: What is the architecture of the Docker engine?

- **Docker CLI:** sends API requests.
- **dockerd:** the API server. It handles images, builds (through BuildKit), networks, volumes and higher-level container management.
- **containerd:** manages the container lifecycle, image storage and snapshots. It is a CNCF project and is also used by Kubernetes.
- **containerd-shim:** one per container. It keeps the container running independently of containerd and dockerd, and holds its stdio.
- **runc:** the low-level OCI runtime that actually creates the container and then exits.

Because of the shim, you can restart dockerd or containerd (with live-restore) without killing containers.

## 306: What is runc?

runc is the reference implementation of the OCI runtime spec. It takes a bundle (a root filesystem plus a `config.json`) and creates a container: sets up namespaces, cgroups, mounts, capabilities and seccomp, and then starts the process.

It is a short-lived tool. After the container starts, runc exits. Alternatives that implement the same spec include `crun` (written in C, faster and lighter), gVisor's `runsc` and Kata Containers.

## 307: What is containerd and how does it relate to Docker?

containerd is a container runtime daemon that Docker split out of its engine and donated to the CNCF. It pulls images, stores them, manages snapshots (filesystems), and starts and supervises containers through shims and runc.

Docker uses containerd under the hood. Kubernetes can use it directly through its CRI plugin, without Docker. You can talk to it with `ctr` (low-level) or `nerdctl` (Docker-like). Docker keeps its containers in containerd's `moby` namespace.

## 308: What is the containerd image store in Docker?

Historically, Docker stored images using its own graph drivers (like overlay2). The containerd image store makes Docker use containerd's image storage and snapshotters instead.

It became the default for new installs in Docker Desktop and then Docker Engine 29. Benefits: it can store multi-platform images and attestations (SBOMs, provenance) locally, it supports image formats like lazy pulling, and `docker build` can produce multi-platform images without a separate builder. Existing installs that upgrade keep the old store until you switch.

## 309: What is a storage driver?

A storage driver (or snapshotter, with the containerd image store) builds the container's filesystem from image layers and handles writes to the container layer.

`overlay2` is the default and recommended one on Linux. Others include `btrfs`, `zfs`, `fuse-overlayfs` (used in some rootless setups) and `vfs` (no copy-on-write, slow, only for testing). Check yours with `docker info`.

## 310: How does OverlayFS work for containers?

OverlayFS merges several folders into one view:

- **lowerdir:** the read-only image layers.
- **upperdir:** the container's writable layer.
- **merged:** what the container sees.

Reads come from the top-most layer that has the file. When a container changes a file from a lower layer, OverlayFS first copies the whole file into the upper layer (copy-up) and then changes it there. Deleted files get a whiteout entry in the upper layer that hides the lower file.

## 311: What is copy-on-write and why does it matter for performance?

Copy-on-write means image layers are shared and only copied when a container changes them. This lets hundreds of containers share one image on disk and start quickly.

The cost is on the first write to an existing file: OverlayFS copies the whole file up, even for a one-byte change. For a large file (like a database file shipped in the image) this is slow. Also, deep layer stacks make lookups a bit slower. That is why write-heavy data should be on volumes, which bypass the overlay filesystem.

## 312: How does Docker run containers on macOS in more detail?

Docker Desktop runs a Linux VM using Apple's Virtualization framework. The Docker daemon, containerd and all containers run inside that VM. The CLI on macOS talks to the daemon through a socket that is forwarded from the VM.

File sharing for bind mounts goes through VirtioFS (the default today), and published ports are forwarded from the VM to macOS by Docker's networking layer. This explains several differences from Linux: bind mount performance, `host.docker.internal`, and why "host network" really means the VM's network.

## 313: How do you make bind mounts faster on macOS?

- Use VirtioFS file sharing (the default in current Docker Desktop).
- Turn on synchronized file shares in Docker Desktop (a paid feature), which syncs files into the VM.
- Keep heavy folders like `node_modules` or build output inside the container (a named volume) instead of on the bind mount.
- Use Compose Watch to sync only source files.
- Mount only the folders you need, not your whole home directory.

## 314: What is rootless mode?

Rootless mode runs the Docker daemon and containers as a normal (non-root) user, using user namespaces. If someone breaks out of a container, they only get that user's permissions on the host, not root.

```bash
dockerd-rootless-setuptool.sh install
export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/docker.sock
```

Limits: binding to ports below 1024 needs extra config, some storage drivers and network features are restricted, networking goes through a user-mode network stack which can be slower, and cgroup limits need cgroup v2 with delegation.

## 315: What is user namespace remapping?

With `userns-remap` in `daemon.json`, the daemon still runs as root, but root inside containers is mapped to an unprivileged UID range on the host (from `/etc/subuid` and `/etc/subgid`).

```json
{ "userns-remap": "default" }
```

So a process that is UID 0 in the container is, for example, UID 100000 on the host. This limits damage from container escapes. The trade-offs: volume and bind-mount permissions need care, and some features (like `--privileged` and host namespaces) do not work with it.

## 316: What is the difference between rootless mode and userns-remap?

- **userns-remap:** the daemon runs as root, containers are remapped to unprivileged UIDs. A bug in the daemon itself can still give root.
- **Rootless:** both the daemon and the containers run as a normal user. Even a daemon compromise only gives that user's rights.

Rootless is the stronger option, but has more limitations around networking and storage. Podman follows a similar rootless model by default.

## 317: What is seccomp and how does Docker use it?

Seccomp filters which system calls a process can make. Docker applies a default seccomp profile to every container that blocks around 40 to 50 dangerous or rarely needed syscalls out of 300+, such as `reboot`, `mount` (without the right capability), `kexec_load` and some keyring calls.

You can provide a stricter custom profile:

```bash
docker run --security-opt seccomp=./profile.json my-app
```

Avoid `seccomp=unconfined` unless you understand why a specific syscall is needed.

## 318: What are AppArmor and SELinux in the context of Docker?

They are Linux Security Modules (LSMs) that restrict what files, capabilities and resources a process can access, even if it runs as root.

- On Ubuntu and Debian, Docker loads the `docker-default` AppArmor profile for containers.
- On RHEL, Fedora and CentOS, SELinux labels each container's processes and files so containers cannot access each other's files or host files.

For SELinux, bind mounts need a label: `-v ./data:/data:Z` (private to this container) or `:z` (shared between containers).

## 319: What does no-new-privileges do?

```bash
docker run --security-opt no-new-privileges my-app
```

It sets the `no_new_privs` flag on the container's processes. After that, a process cannot gain more privileges through setuid or setgid binaries (like `sudo` or `su`) or file capabilities. If an attacker gets a shell as a normal user in the container, they cannot use a setuid binary to become root.

It is a cheap hardening option that rarely breaks apps.

## 320: What is a container escape?

A container escape is when a process inside a container gets access to the host or to other containers. Common causes:

- Running with `--privileged` or with dangerous capabilities (`SYS_ADMIN`).
- Mounting the Docker socket or sensitive host paths (`/`, `/proc`, `/sys`) into the container.
- Kernel vulnerabilities, since all containers share the host kernel.
- Bugs in the runtime itself (for example CVE-2019-5736 in runc, or the "Leaky Vessels" runc and BuildKit bugs in 2024).

Defense: keep the kernel and Docker updated, run as non-root, drop capabilities, use seccomp and LSMs, and consider rootless mode or sandboxed runtimes for untrusted code.

## 321: How do you harden a container at run time?

```bash
docker run -d \
  --user 10001:10001 \
  --read-only --tmpfs /tmp \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --memory 512m --cpus 1 --pids-limit 200 \
  --network app-net \
  my-app:1.4.0
```

This runs as non-root, with a read-only root filesystem, no extra capabilities, no privilege escalation, resource limits and a private network. Add a custom seccomp profile for extra protection.

## 322: How do you harden a Docker image?

- Start from a minimal, maintained base (distroless, slim, or hardened images).
- Use multi-stage builds so compilers and package managers are not in the final image.
- Run as a non-root user with a fixed numeric UID.
- Pin base images by version and digest, and update them with a bot.
- Do not include secrets, `.git` or test files.
- Remove setuid binaries you do not need.
- Scan for CVEs and generate an SBOM in CI.
- Sign images and check signatures before deploying.

## 323: What are Docker Hardened Images?

Docker Hardened Images (DHI) are minimal versions of popular images (Node.js, Python, nginx and many others) maintained by Docker. They aim for close to zero known CVEs, ship without shells and package managers in the runtime variants, run as non-root by default and come with SBOMs, provenance and signatures.

Docker made the catalog freely available in late 2025, with paid tiers for extended support and compliance needs. They are an alternative to distroless or Chainguard images.

## 324: How do you sign images and verify signatures?

The most common tool today is Sigstore's `cosign`:

```bash
cosign sign --key cosign.key ghcr.io/my-org/api@sha256:<digest>
cosign verify --key cosign.pub ghcr.io/my-org/api@sha256:<digest>
```

You can also use keyless signing in CI with OIDC identities (for example GitHub Actions), where the signature is tied to the workflow that built the image. Always sign the digest, not the tag. Enforce verification at deploy time, for example with a Kubernetes admission controller like Kyverno or the Sigstore policy controller.

## 325: What was Docker Content Trust?

Docker Content Trust (DCT) was Docker's older image signing system based on Notary v1. You enabled it with `DOCKER_CONTENT_TRUST=1`, and Docker would only pull signed tags.

It is legacy now. Docker has announced its retirement for Docker Hub official images, and most of the ecosystem moved to Sigstore (cosign) and Notary Project (Notation) signatures stored as OCI artifacts. You may still see `DOCKER_CONTENT_TRUST` in old CI scripts.

## 326: How does pulling an image work at the registry protocol level?

1. The client asks the registry for the manifest: `GET /v2/<name>/manifests/<tag>`, with headers saying which manifest formats it accepts.
2. If it gets an image index (multi-platform), it picks the manifest for its platform and requests that by digest.
3. The manifest lists the config blob and the layer blobs by digest.
4. The client downloads each blob it does not have: `GET /v2/<name>/blobs/<digest>`, often redirected to object storage.
5. It checks each blob's SHA-256 against its digest, then unpacks the layers.

Authentication usually uses a bearer token from the registry's auth server.

## 327: What is an image manifest and an image index?

- **Image manifest:** a JSON document for one platform. It lists the config blob (environment, entrypoint, history) and the ordered layer blobs, each with a media type, size and digest.
- **Image index** (manifest list): a JSON document that lists several manifests, one per platform (`linux/amd64`, `linux/arm64`), plus attestation manifests.

A multi-platform tag points to an index. Docker picks the right manifest for your platform when you pull.

## 328: How are layers stored and shared?

Each layer is a compressed tar file (a blob) identified by the SHA-256 digest of its content. Registries and hosts store each blob once, no matter how many images use it.

So if 20 images use the same `node:22-slim` base, a host downloads and stores those base layers once. That is a good reason to standardize base images across a company.

## 329: What is the difference between a layer digest and a diff ID?

- The **layer digest** (in the manifest) is the hash of the compressed layer blob as stored in the registry.
- The **diff ID** (in the image config) is the hash of the uncompressed tar.

The image config lists diff IDs, and the image ID is derived from the config. Because the same content compressed differently gives different digests, two registries can show different layer digests for an image with the same diff IDs.

## 330: What layer compression formats are supported?

The default is gzip. BuildKit can also produce `zstd` layers, which decompress much faster and are often smaller:

```bash
docker buildx build \
  --output type=image,name=my-org/api:1.0,push=true,compression=zstd,force-compression=true .
```

Older clients and some registries may not support zstd, so check your target platforms first. `estargz` is another format that allows lazy pulling.

## 331: What is lazy pulling?

Normally a container cannot start until all layers are downloaded and unpacked. With lazy pulling, the container starts right away and files are fetched from the registry on demand as they are read.

Formats and snapshotters that support it include eStargz (stargz-snapshotter), SOCI (by AWS) and Nydus. It can cut startup time a lot for big images (like ML images) where only a small part of the files are used at startup. It needs containerd snapshotter support on the host.

## 332: How do you reduce container startup time?

- Make images smaller so pulls are faster, and keep large data out of images.
- Pre-pull images on nodes before you need them.
- Use a registry close to the hosts (same region) or a pull-through cache.
- Use lazy pulling for very large images.
- Reduce what the app does at boot (warm-up, migrations, downloads).
- For JVM apps, look at class data sharing or native images.
- Use `zstd` compression for faster decompression.

## 333: How does Docker networking work on Linux in detail?

For a bridge network, Docker:

1. Creates a Linux bridge (like `docker0` or `br-<id>`) on the host, with the network's gateway IP.
2. For each container, creates a veth pair: one end goes into the container's network namespace as `eth0`, the other end is attached to the bridge.
3. Assigns an IP to the container from the network's subnet.
4. Adds firewall rules (iptables or nftables): masquerade (SNAT) for outgoing traffic, DNAT for published ports, and isolation rules between different bridge networks.

Containers on the same bridge talk at layer 2 through the bridge. Traffic to the outside is NATed through the host's IP.

## 334: What is docker-proxy and can you disable it?

`docker-proxy` is a small userland process Docker starts for each published port. It handles cases that the NAT rules do not, like connections from the host to its own published port on some setups, or hairpin traffic.

You can disable it with `"userland-proxy": false` in `daemon.json`, and Docker will rely on iptables rules (including hairpin NAT) instead. This saves a process per port, which matters if you publish many ports. Test it first, because some localhost and IPv6 cases behave differently.

## 335: Does Docker support nftables?

Historically Docker only wrote iptables rules (which on many modern distros go through the `iptables-nft` compatibility layer). Newer Docker Engine versions (from 29) added a native nftables firewall backend you can turn on in `daemon.json`:

```json
{ "firewall-backend": "nftables" }
```

It is still marked experimental. With it, Docker creates its own nftables tables instead of iptables chains, which makes rules easier to read and avoids some conflicts with host firewall tools.

## 336: How does the overlay network work?

The overlay driver creates a virtual network that spans several Docker hosts (in Swarm mode). Containers on different hosts get IPs in the same subnet and talk as if they were on one switch.

Under the hood, each host has a network namespace with a bridge and a VXLAN interface. Traffic between hosts is wrapped in VXLAN (UDP port 4789). The control plane (which container is on which host) is shared through Swarm's gossip protocol. You can turn on encryption of the data plane with `--opt encrypted` (IPsec).

## 337: How does service discovery and load balancing work in Swarm?

Each Swarm service gets a virtual IP (VIP) on its overlay networks. Docker's DNS returns that VIP for the service name, and IPVS in the kernel spreads connections across the healthy tasks.

For published ports, the routing mesh opens the port on every node in the swarm. Any node accepts the connection and forwards it to a task, even on another node. You can use `endpoint_mode: dnsrr` to return task IPs directly instead of a VIP, for example to use your own load balancer.

## 338: How do Swarm rolling updates and rollbacks work?

```bash
docker service update \
  --image my-org/api:1.5.0 \
  --update-parallelism 1 \
  --update-delay 10s \
  --update-failure-action rollback \
  --update-order start-first \
  api
```

Swarm replaces tasks in batches. `start-first` starts the new task before stopping the old one, which avoids losing capacity. If tasks fail (or become unhealthy) during the update, Swarm can pause or roll back automatically. `docker service rollback api` goes back to the previous spec by hand.

## 339: How do Swarm secrets differ from Compose secrets?

In Swarm, secrets are stored encrypted in the Raft log of the managers. They are only sent over TLS to nodes that run a task using them and mounted in memory (tmpfs) at `/run/secrets/<name>`. They are never written to disk on worker nodes.

```bash
printf 'S3cret' | docker secret create db_password -
docker service create --secret db_password my-app
```

Compose secrets without Swarm are basically bind-mounted files from the host. They avoid environment variables but are not encrypted at rest.

## 340: When would you pick Swarm over Kubernetes?

Swarm can make sense when:

- You have a small team and a few hosts, and want something simpler than Kubernetes.
- You already use Compose files and want multi-host with little extra learning.
- You do not need the Kubernetes ecosystem (operators, Helm charts, service meshes).

Kubernetes is the better choice when you need autoscaling, a large ecosystem, managed offerings from all cloud providers, or more complex workloads. For a single server, plain Compose is often enough.

## 341: How does CPU limiting work under the hood?

- `--cpus` uses the CFS quota: the container gets that much CPU time per period (default 100ms). `--cpus 0.5` means 50ms per 100ms. If it uses its quota early, it is throttled until the next period.
- `--cpu-shares` (cgroup v2: `cpu.weight`) sets a relative weight. It only matters when CPUs are busy.
- `--cpuset-cpus 0,1` pins the container to specific CPU cores.

Throttling can cause latency spikes for apps with bursty work (for example GC or many threads), even when average usage looks low. Check `nr_throttled` in the cgroup's `cpu.stat`.

## 342: How does memory limiting work and what happens on OOM?

`--memory` sets the cgroup's hard memory limit (`memory.max` in cgroup v2). The container's memory includes the app's RSS plus page cache it uses (for example file reads). When usage hits the limit, the kernel first tries to reclaim cache. If it cannot, the OOM killer kills a process in that cgroup, usually the biggest one.

If that process is PID 1, the container exits with code 137 and `OOMKilled` is true. `--memory-reservation` sets a soft limit, and `--memory-swap` controls swap use (set it equal to `--memory` to disable swap).

## 343: Why does my app use more memory than expected in a container?

- Page cache from file I/O is counted against the cgroup.
- Runtimes may size themselves from the host, not the container limit. Old JVMs, or Node.js with a manual `--max-old-space-size`, can try to use more than the limit.
- Native memory (thread stacks, buffers, glibc malloc arenas) is not visible in heap metrics.
- Memory leaks show up as a slow climb until OOM.

Check `docker stats`, the cgroup's `memory.stat` (anon vs file), and the runtime's own metrics. Newer JVMs and Node.js read cgroup limits, but setting heap size explicitly (like `-XX:MaxRAMPercentage` or `--max-old-space-size`) gives more predictable behavior.

## 344: What happens to a container's disk I/O and how do you limit it?

Writes to the container layer go through the overlay filesystem. Volumes write directly to the host filesystem. You can limit I/O with block I/O controls:

```bash
docker run --device-write-bps /dev/sda:10mb --device-read-iops /dev/sda:1000 my-app
docker run --blkio-weight 300 my-app
```

On cgroup v2, these map to `io.max` and `io.weight`. Limits on buffered writes only work properly with cgroup v2, which accounts writeback to the right cgroup.

## 345: What is the difference between --memory-swap and --memory?

- `--memory 512m` alone: the container can use 512 MB of RAM and the same amount of swap again (total 1 GB), if the host has swap.
- `--memory 512m --memory-swap 1g`: 512 MB RAM plus 512 MB swap.
- `--memory 512m --memory-swap 512m`: no swap at all.
- `--memory-swap -1`: unlimited swap.

For latency-sensitive services, many teams disable swap so problems show up as OOM kills instead of slow responses.

## 346: Why can the Docker build cache be invalidated unexpectedly?

- A file in the context changed that you did not expect to matter, because you `COPY . .` too early. Even editor files or `.git` changes can do it if not ignored.
- A different build arg value. `ARG` values used in a step invalidate it.
- The base image tag points to a new image after `--pull`.
- File permissions or ownership changed (for example after a fresh Git clone on CI, file modes can differ).
- A different builder: the cache is stored per builder, so a new CI runner starts empty unless you import cache.

Use `--progress=plain` to see which step was `CACHED` and which was not.

## 347: How does BuildKit execute a Dockerfile internally?

The Dockerfile frontend converts the Dockerfile into LLB (low-level build), a graph of operations (images, file copies, command executions) with their inputs. BuildKit's solver then:

- Computes a cache key for each node from its definition and the content of its inputs.
- Skips nodes whose cache key is already in the cache.
- Runs independent nodes in parallel.
- Only builds what the requested target needs.

Because the frontend is pluggable (`# syntax=`), other formats (like Buildpacks or Earthly-style files) can compile to the same LLB.

## 348: What is the difference between mode=min and mode=max for cache export?

- `mode=min` (the default) exports cache only for layers that end up in the final image.
- `mode=max` exports cache for every step of every stage, including intermediate build stages.

With multi-stage builds, `mode=min` misses most of the useful cache (dependency install and compile steps in the build stage), so CI builds stay slow. `mode=max` produces a larger cache but much better hit rates.

## 349: How does Docker Build Cloud work?

Docker Build Cloud runs your builds on remote BuildKit builders hosted by Docker, with native `amd64` and `arm64` machines and a shared cache that the whole team and CI use.

```bash
docker buildx create --driver cloud my-org/default
docker buildx build --builder cloud-my-org-default -t my-org/api:1.0 --push .
```

The benefits are faster builds from the shared cache, no QEMU emulation for multi-platform builds, and less load on laptops and CI runners. It is a paid service with included build minutes in some subscriptions.

## 350: How do you do multi-platform builds without slow emulation?

- **Cross-compilation:** run the build stage on the builder's native platform and compile for the target. Use the automatic `BUILDPLATFORM` and `TARGETOS` / `TARGETARCH` args:

```dockerfile
FROM --platform=$BUILDPLATFORM golang:1.25 AS build
ARG TARGETOS TARGETARCH
WORKDIR /src
COPY . .
RUN GOOS=$TARGETOS GOARCH=$TARGETARCH CGO_ENABLED=0 go build -o /app .

FROM gcr.io/distroless/static-debian12
COPY --from=build /app /app
ENTRYPOINT ["/app"]
```

- **Native builders:** add an `arm64` and an `amd64` node to one Buildx builder (`docker buildx create --append`), or use Docker Build Cloud.

Emulation with QEMU still works but can be 5 to 20 times slower for compile-heavy steps.

## 351: What automatic build arguments does BuildKit provide?

BuildKit sets these platform args for you. You only need to declare them with `ARG` to use them:

- `BUILDPLATFORM`, `BUILDOS`, `BUILDARCH`, `BUILDVARIANT`: the platform of the machine running the build.
- `TARGETPLATFORM`, `TARGETOS`, `TARGETARCH`, `TARGETVARIANT`: the platform you are building for.

```dockerfile
FROM alpine:3.22
ARG TARGETARCH
RUN echo "Building for $TARGETARCH"
```

There are also proxy args (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`) that are passed through without being saved in the image history.

## 352: How does ARG scope work across stages?

An `ARG` declared before the first `FROM` is global, but it can only be used in `FROM` lines. To use it inside a stage, you must declare it again (without a value) in that stage:

```dockerfile
ARG NODE_VERSION=22
FROM node:${NODE_VERSION}-slim
ARG NODE_VERSION
RUN echo "Node $NODE_VERSION"
```

An `ARG` declared inside a stage only exists in that stage. This trips up a lot of people because the variable just comes out empty, with no error. Build checks warn about some of these cases.

## 353: How would you design images for a team with many microservices?

- Create a small set of approved base images (for example one per language) maintained by a platform team, rebuilt weekly with security fixes.
- Give every service the same Dockerfile structure: multi-stage, non-root, healthcheck, labels with source and version.
- Build in CI with shared remote cache, tag with the commit SHA, push SBOM and provenance, sign the digest.
- Scan in CI and block deploys on critical CVEs that have fixes.
- Use Renovate or Dependabot to bump base image digests automatically.

This keeps images consistent, small and easy to patch at scale.

## 354: How do you handle a critical CVE in a base image used by 50 services?

1. Check if a fixed base image is available (or if the CVE actually affects you, using the scanner's details and VEX data).
2. Update the shared base image, or bump the digest in each service via automated pull requests.
3. Rebuild all images. Because you have a shared CI pipeline, this can be triggered for all repos.
4. Use the SBOMs to find every image that contains the vulnerable package, including ones not built from the shared base.
5. Deploy and confirm through registry or runtime scanning that no running image still has the vulnerable version.

The setup work (shared bases, SBOMs, automatic bumps) is what makes this hours instead of weeks.

## 355: What is VEX?

VEX (Vulnerability Exploitability eXchange) is a format for saying whether a known CVE actually affects a product, for example "not affected, vulnerable code is not used". Scanners like Docker Scout and Trivy can read VEX documents and hide CVEs marked as not affecting you.

It reduces noise from scanners. Docker Hardened Images and some vendors ship VEX statements with their images.

## 356: How do you run untrusted code in containers safely?

Standard containers share the host kernel, so they are not enough for truly hostile code. Options:

- **gVisor (`runsc`):** a user-space kernel that intercepts syscalls. Strong isolation, some performance cost.
- **Kata Containers or Firecracker microVMs:** each container runs in a lightweight VM with its own kernel.
- **Docker Desktop's Enhanced Container Isolation** for developer machines.

Add the usual hardening too: no network or a restricted one, read-only filesystem, no capabilities, strict resource limits and short lifetimes.

```bash
docker run --runtime=runsc --network none --read-only --cap-drop ALL sandbox-image
```

## 357: How do you use a different OCI runtime with Docker?

Register it in `daemon.json` and pick it per container:

```json
{
  "runtimes": {
    "runsc": { "path": "/usr/local/bin/runsc" },
    "crun": { "path": "/usr/bin/crun" }
  }
}
```

```bash
docker run --runtime=runsc my-app
```

You can set `"default-runtime"` to change it for all containers.

## 358: What is Enhanced Container Isolation?

Enhanced Container Isolation (ECI) is a Docker Desktop feature for business subscriptions. It runs containers inside the Docker Desktop VM using a user-namespace-based runtime (Sysbox), so root in a container is not root in the VM. It also blocks containers from mounting the Docker socket or changing the Docker Desktop VM's settings, even with `--privileged`.

It protects developer machines and company settings from malicious or misconfigured containers.

## 359: What is the security risk of mounting /var/run/docker.sock?

Access to the Docker socket means full control of the daemon. A process with it can:

```bash
docker run --rm -it --privileged -v /:/host alpine chroot /host
```

and get a root shell on the host. So any container with the socket mounted is as powerful as root on the host, and a bug in that container is a host compromise.

Mitigations: avoid it if possible, use a socket proxy that only allows specific API endpoints, use rootless Docker, or switch to tools that do not need the socket (Kaniko or Buildah for builds).

## 360: How do you expose the Docker API over the network safely?

Never expose it on TCP without TLS. Anyone who can reach it controls the host.

Safer options:

- Use SSH: `DOCKER_HOST=ssh://user@host`, which reuses SSH keys and needs no open Docker port.
- If you need TCP, use mutual TLS: `dockerd --tlsverify --tlscacert=ca.pem --tlscert=server-cert.pem --tlskey=server-key.pem -H tcp://0.0.0.0:2376`, and give clients their own certs.
- Restrict access with firewall rules or a VPN.

Port 2375 (no TLS) open to the internet is one of the most common ways servers get crypto miners installed.

## 361: How would you audit a Docker host for security problems?

- Run Docker Bench for Security, which checks the host against the CIS Docker Benchmark.
- Check `docker info` for rootless, userns, live-restore, logging and storage settings.
- List containers with dangerous settings:

```bash
docker ps -q | xargs docker inspect -f \
  '{{.Name}} privileged={{.HostConfig.Privileged}} caps={{.HostConfig.CapAdd}} user={{.Config.User}} binds={{.HostConfig.Binds}}'
```

- Check for published ports on `0.0.0.0` and the Docker socket being mounted.
- Check who is in the `docker` group.
- Make sure Docker, containerd, runc and the kernel are patched.

## 362: How do secrets leak from containers and how do you prevent it?

Common leaks:

- Environment variables, visible in `docker inspect`, `/proc/<pid>/environ`, crash reports and child processes.
- Build args or `ENV`, stored in image metadata.
- Files copied into layers and deleted later.
- Logs that print config at startup.
- `.env` files pushed to Git or included in images.

Prevention: mount secrets as files (tmpfs), read them at startup, use a secrets manager (Vault, AWS Secrets Manager) with short-lived credentials, use build secret mounts, and scan images and repos for secrets.

## 363: How do you design a Dockerfile that builds fast in CI and runs small in production?

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-slim AS base
WORKDIR /app

FROM base AS deps
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci

FROM deps AS build
COPY . .
RUN npm run build && npm prune --omit=dev

FROM base AS prod
ENV NODE_ENV=production
COPY --from=build --chown=node:node /app/node_modules ./node_modules
COPY --from=build --chown=node:node /app/dist ./dist
COPY --chown=node:node package.json ./
USER node
CMD ["node", "dist/server.js"]
```

Combine this with `mode=max` remote cache in CI. Dependency install is cached unless the lock file changes, and the final image only has production files.

## 364: What are the trade-offs between Alpine, slim, distroless and scratch?

| Base        | Size       | Shell | libc  | Notes                                                 |
| ----------- | ---------- | ----- | ----- | ----------------------------------------------------- |
| Alpine      | very small | yes   | musl  | Native module issues, different DNS resolver behavior |
| Debian slim | small      | yes   | glibc | Most compatible, easy to debug                        |
| Distroless  | small      | no    | glibc | Fewer CVEs, harder to debug                           |
| scratch     | tiny       | no    | none  | Only for static binaries                              |

For most apps, `-slim` or distroless are good defaults. Pick Alpine when size matters a lot and you have tested your dependencies with musl.

## 365: What problems can musl libc cause?

- Native Node.js modules or Python wheels built for glibc fail to load, or must be compiled from source (slow builds, extra build tools).
- Performance differences, for example in memory allocation for heavily multi-threaded apps.
- DNS resolution differences: older musl versions did not fall back to TCP for large DNS responses, and the resolver handles `search` and `ndots` differently from glibc, which has caused issues in Kubernetes.
- Locale and timezone support is more limited.

If you see strange crashes or DNS problems only in Alpine images, try a Debian-based image to compare.

## 366: How do you debug a distroless or scratch container that has no shell?

- `docker debug <container>` (part of Docker Desktop) attaches a toolbox shell with common tools to any container, even without a shell in the image.
- Start a debug container that shares the target's namespaces:

```bash
docker run --rm -it \
  --pid container:api \
  --network container:api \
  nicolaka/netshoot
```

From there you can see its processes (`ps`), use network tools and read its filesystem through `/proc/1/root`.

- Use the `:debug` variant of the distroless image in a staging environment.

## 367: What does --pid container:x or --network container:x do?

They make a new container join the namespace of an existing container instead of getting its own:

- `--network container:api`: the new container shares `api`'s network stack. Both see the same interfaces, and `localhost` in one is `localhost` in the other.
- `--pid container:api`: it shares the process list, so you can see and trace `api`'s processes.

This is the same idea as a Kubernetes pod, where containers share a network namespace. It is very useful for debugging and for sidecar patterns.

## 368: How do you trace system calls of a process in a container?

From a debug container that shares the PID namespace and has the right capability:

```bash
docker run --rm -it --pid container:api --cap-add SYS_PTRACE \
  alpine sh -c "apk add --no-cache strace && strace -f -p 1"
```

Or from the host, find the host PID with `docker inspect -f '{{.State.Pid}}' api` and run `strace -p <pid>`. For production, eBPF tools (`bpftrace`, Inspektor Gadget, Falco) can trace with less overhead.

## 369: How do you enter a container's namespaces from the host?

Use `nsenter` with the container's host PID:

```bash
PID=$(docker inspect -f '{{.State.Pid}}' api)
sudo nsenter -t "$PID" -n ip addr      # network namespace only
sudo nsenter -t "$PID" -n -p -m sh     # network, PID, mount
```

With `-n` only, you can use the host's tools (like `tcpdump`) inside the container's network, even if the image has no tools at all.

## 370: How do you capture network traffic of a container?

```bash
docker run --rm -it --network container:api nicolaka/netshoot \
  tcpdump -i eth0 -w - port 5432 > capture.pcap
```

Or with `nsenter -t <pid> -n tcpdump -i eth0` from the host. Open the file in Wireshark. This lets you debug database or HTTP traffic without changing the app image.

## 371: A container cannot reach the internet. How do you troubleshoot it?

1. Check DNS: `docker run --rm busybox nslookup example.com`. If it fails, check the host's `/etc/resolv.conf` (a `127.0.0.53` systemd-resolved address is not reachable from containers, Docker handles this but custom setups can break it) or set `dns` in `daemon.json`.
2. Check IP connectivity: `docker run --rm busybox ping -c1 1.1.1.1`.
3. Check that IP forwarding is on: `sysctl net.ipv4.ip_forward`.
4. Check firewall rules. Something may have flushed Docker's iptables rules or a host firewall drops forwarded traffic. Restarting Docker recreates its rules.
5. Check for subnet conflicts with a VPN or company network.
6. Check MTU. On VPNs or some cloud networks, a smaller MTU is needed, or large packets will hang.

## 372: How can an MTU mismatch break container networking?

Docker bridges use MTU 1500 by default. If the host's real path has a smaller MTU (VPNs, some cloud overlays, VXLAN), large packets get dropped. Small requests like DNS or a TCP handshake work, but TLS handshakes or big responses hang, which looks very confusing.

Fix it by setting a matching MTU:

```json
{ "mtu": 1400 }
```

For user-defined networks, use `docker network create -o com.docker.network.driver.mtu=1400 net`, or `driver_opts` in Compose.

## 373: Why are Docker subnets sometimes in conflict with a VPN?

Docker picks private subnets like `172.17.0.0/16`, `172.18.0.0/16` and so on for new networks. Many companies use the same ranges internally. When a Docker network uses a range that the VPN routes, traffic to those company hosts goes to the Docker bridge instead and the hosts become unreachable.

Fix it with `default-address-pools` and `bip` in `daemon.json`, choosing ranges nobody uses, and remove existing networks so they are recreated.

## 374: How does a container's /etc/resolv.conf get generated?

On the default bridge, Docker copies the host's `/etc/resolv.conf` and removes localhost entries (which would point to the container itself), falling back to public DNS if nothing is left.

On user-defined networks, the container's `resolv.conf` points to `127.0.0.11`, Docker's embedded DNS. That server answers container names and forwards everything else to the upstream servers from the host config or `--dns`. If the host uses `systemd-resolved`, Docker reads the real upstream file instead of the stub.

## 375: What can cause slow DNS inside containers?

- Search domains plus `ndots` settings cause several failed lookups before the right one (very common in Kubernetes with `ndots:5`).
- IPv6 AAAA lookups that time out before IPv4 answers come back.
- An upstream DNS server that is slow or unreachable from the container network.
- Apps that do not cache DNS and resolve on every request.

Use fully qualified names (with a trailing dot) for external hosts, tune `ndots`, check the upstream servers, and add DNS caching in the app or a local cache.

## 376: How does Docker handle signals and stop timeouts in more detail?

On `docker stop`, the daemon sends the stop signal (`SIGTERM` or `STOPSIGNAL`) to PID 1 in the container. It then waits for the stop timeout (default 10 seconds, changeable with `--stop-timeout`, `-t` on stop, or `stop_grace_period` in Compose). If the process is still running, it sends `SIGKILL` to the container's cgroup.

PID 1 in a namespace ignores signals it has no handler for. A shell-form `CMD` or a script without `exec` makes the shell PID 1, which usually does not forward signals. The result is always waiting the full timeout and a hard kill. Use exec form, `exec` in scripts and `--init` if needed.

## 377: What are zombie processes and why do they appear in containers?

A zombie is a process that has finished but whose parent has not called `wait()` to collect its exit status. Normally, orphaned processes are adopted by PID 1 (init), which reaps them.

In a container, your app is PID 1. If it starts child processes (for example shelling out to tools, or a headless browser) and does not reap orphans, zombies pile up and can eventually hit the PID limit. Running `tini` (`--init`) or another minimal init as PID 1 fixes it.

## 378: Why might logs from your app appear late or out of order in docker logs?

The app is not writing to a terminal, so many languages switch stdout to full buffering. Output only appears when the buffer fills or the process exits. Python and some C programs are common examples.

Fixes:

- Python: `PYTHONUNBUFFERED=1` or `python -u`.
- Flush logs explicitly or use a logging library that writes line by line.
- Running with `-t` makes stdout line-buffered, but it merges stdout and stderr, so it is not recommended for production.

stdout and stderr are also captured as separate streams, which can make lines from both look out of order.

## 379: What happens when the json-file log driver fills the disk?

Without `max-size`, the json-file driver keeps appending to `/var/lib/docker/containers/<id>/<id>-json.log` forever. A chatty container can fill the disk, which then breaks Docker itself (no new layers, failed writes, crashed databases).

Prevent it with default log options in `daemon.json` (they only apply to new containers), the `local` driver, or shipping logs off the host. Truncating a live log file by hand works in an emergency, but recreating the container with limits is the real fix.

## 380: What is the blocking vs non-blocking log mode?

By default, log delivery is blocking: if the logging driver cannot keep up (for example a slow remote endpoint), the app's writes to stdout block, and the app slows down or hangs.

```bash
docker run --log-opt mode=non-blocking --log-opt max-buffer-size=4m my-app
```

In non-blocking mode, logs go into an in-memory buffer. If the buffer is full, new log lines are dropped, but the app keeps running. You choose between losing logs and slowing the app.

## 381: How do you size and tune Docker's data root on a server?

- Put `/var/lib/docker` (or `data-root` in `daemon.json`) on a fast, separate disk with enough space, so image pulls and logs cannot fill the root filesystem.
- Use a filesystem that supports overlay2 properly (ext4 or xfs with `ftype=1`).
- Set BuildKit garbage collection limits on build servers.
- Clean up images and build cache on a schedule.
- Monitor disk usage and inode usage. Many small files in images can run out of inodes before space.

## 382: How do you move Docker's data directory to another disk?

1. Stop Docker: `sudo systemctl stop docker docker.socket`.
2. Copy the data, keeping permissions: `sudo rsync -aHAX /var/lib/docker/ /mnt/docker/`.
3. Set it in `/etc/docker/daemon.json`:

```json
{ "data-root": "/mnt/docker" }
```

4. Start Docker and check `docker info | grep "Docker Root Dir"` and that images and volumes are there.
5. Remove the old folder when everything works.

If you use the containerd image store, containerd's own root (`/var/lib/containerd`) holds the images, so it may need to be moved too.

## 383: How do you upgrade Docker Engine on production hosts safely?

- Read the release notes for breaking changes (API version bumps, removed options, default changes like the image store or firewall backend).
- Test the new version on a staging host with your real workloads.
- Turn on `live-restore` so containers keep running during the daemon restart, or drain the host first if it is in a cluster.
- Upgrade hosts one at a time and keep the old package available for rollback.
- After upgrading, check `docker info`, container health and logs.

## 384: What is the Docker Engine API and how is it versioned?

The Engine API is the REST API that the CLI and other tools use. Each Engine release supports a range of API versions, and clients can request a specific version in the URL (`/v1.47/containers/json`).

```bash
curl --unix-socket /var/run/docker.sock http://localhost/v1.47/containers/json
docker version --format '{{.Server.APIVersion}} {{.Server.MinAPIVersion}}'
```

Newer engines raise the minimum supported API version over time, so very old clients or libraries (for example an old Docker SDK in a CI tool) can stop working after an upgrade.

## 385: How do you control Docker from code?

Use an official or community SDK that wraps the Engine API:

- Go: `github.com/docker/docker/client` (the official one; newer versions move to `github.com/moby/moby/client`).
- Python: `docker` package (`docker-py`).
- Node.js: `dockerode`.

```python
import docker

client = docker.from_env()
container = client.containers.run("nginx:1.27", detach=True, ports={"80/tcp": 8080})
print(container.status)
```

Treat code with Docker access like code with root access.

## 386: What are Docker plugins?

Plugins extend the Docker daemon with extra drivers:

- Volume plugins (network or cloud storage)
- Network plugins
- Logging plugins
- Authorization plugins (to allow or deny API calls)

```bash
docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
```

They run as special containers managed by the daemon. Do not confuse them with CLI plugins like Compose and Buildx, which are just extra CLI commands in `~/.docker/cli-plugins`.

## 387: What are authorization plugins and their risks?

An authorization (AuthZ) plugin sees every API request and can allow or deny it, for example to block `--privileged` or socket mounts.

They are hard to get right. The daemon must pass the full request body to the plugin, and there have been bugs where specially crafted requests bypassed the check (CVE-2024-41110 is a well-known one). They also add latency and are a single point of failure. Rootless mode, ECI, or a restrictive socket proxy are often simpler controls.

## 388: How would you build a minimal image for a Python app with native dependencies?

Build wheels in a full image, then install them in a slim one:

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.13 AS build
WORKDIR /build
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip wheel --wheel-dir /wheels -r requirements.txt

FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN --mount=type=bind,from=build,source=/wheels,target=/wheels \
    pip install --no-cache-dir --no-index --find-links=/wheels /wheels/*.whl
COPY . .
RUN useradd --system app
USER app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
```

Compilers and headers stay in the build stage. Any system libraries the compiled wheels need at run time (like `libpq5`) must be installed in the final stage.

## 389: How do you make image builds reproducible?

- Pin base images by digest.
- Pin package versions (lock files, `apt-get install pkg=version`, or a snapshot repository like `snapshot.debian.org`).
- Avoid downloading "latest" anything at build time.
- Set `SOURCE_DATE_EPOCH` so file timestamps and image creation time are fixed:

```bash
docker buildx build --build-arg SOURCE_DATE_EPOCH=$(git log -1 --format=%ct) \
  --output type=image,name=my-app,rewrite-timestamp=true .
```

With all inputs fixed, the same source produces the same digest, which makes it possible to verify builds independently.

## 390: How do you build an image without a Docker daemon?

- **BuildKit standalone** (`buildkitd` plus `buildctl`), including rootless mode.
- **Buildah**, which can build from Dockerfiles without a daemon and without root.
- **Kaniko**, made for building inside Kubernetes pods without privileges. Note that the original Google project was archived in 2025, so check for a maintained fork before choosing it.
- **ko** (Go) and **Jib** (Java), which build images directly from source without a Dockerfile.
- **Cloud Native Buildpacks** (`pack`), which detect the language and build an image.

This is common in Kubernetes-based CI, where mounting a Docker socket is not allowed.

## 391: What are Cloud Native Buildpacks and when would you use them instead of a Dockerfile?

Buildpacks inspect your source code, detect the language and build an OCI image with a standard runtime layout, without a Dockerfile.

```bash
pack build my-app --builder paketobuildpacks/builder-jammy-base
```

They are useful when a platform team wants every app built the same way, and they support "rebasing": swapping the OS base layers for a patched version without rebuilding the app layers. The downside is less control over the image than with a Dockerfile.

## 392: How do you run a Compose app in production and what are its limits?

Compose works well for single-host production if you add:

- `restart: unless-stopped` and healthchecks
- Resource limits and log rotation
- Images from a registry (not builds on the server)
- Secrets as files, not in the Compose file
- A reverse proxy with TLS
- Backups for volumes
- Monitoring and alerting

Its limits: one host only (no failover), no rolling updates out of the box, no autoscaling. When you need those, move to Swarm, Kubernetes, ECS, Cloud Run or similar.

## 393: How would you migrate a Compose setup to Kubernetes?

1. Make sure images are in a registry and config comes from env and files, not from bind mounts of source code.
2. Turn each service into a Deployment and a Service. Ports become Service ports, `environment` becomes ConfigMaps and Secrets, named volumes become PersistentVolumeClaims.
3. `depends_on` has no direct equivalent: use readiness probes, retries in the app and init containers.
4. Healthchecks become liveness, readiness and startup probes.
5. The reverse proxy becomes an Ingress or Gateway.

Tools like Kompose can generate a first draft from `compose.yaml`, but the result usually needs manual cleanup.

## 394: How do Docker healthchecks map to Kubernetes probes?

Kubernetes ignores the `HEALTHCHECK` in an image. It has its own probes:

- **Liveness:** if it fails, the container is restarted. Closest to "unhealthy means broken".
- **Readiness:** if it fails, the pod is removed from Service endpoints but not restarted.
- **Startup:** delays other probes until the app has started. Similar to `--start-period`.

Probes are usually HTTP or TCP checks done by the kubelet, so you do not need `curl` in the image.

## 395: How do image pull policies affect deployments?

In Kubernetes, `imagePullPolicy` decides when the node pulls an image:

- `IfNotPresent` uses the cached image if the tag exists on the node.
- `Always` checks the registry on every pod start (cheap if layers are cached, since only the manifest is checked).
- `Never` only uses local images.

With mutable tags and `IfNotPresent`, different nodes can run different images under the same tag. That is why immutable tags or digests are recommended. The same issue exists in Compose with `pull_policy`.

## 396: How do you choose a container platform for a new web app?

- **One server, small team:** Docker Compose, maybe with a tool like Kamal for deploys.
- **No servers to manage, simple HTTP services:** a serverless container platform such as AWS App Runner, Google Cloud Run or Azure Container Apps.
- **AWS with moderate needs:** ECS with Fargate.
- **Many services, need control and portability:** Kubernetes (EKS, GKE, AKS).

All of them run the same OCI images, so starting simple and moving later is realistic if you follow twelve-factor practices.

## 397: How do you keep images small for machine learning workloads?

- Use runtime base images (`-runtime` CUDA images) instead of `-devel` ones in the final stage.
- Install only the CUDA and library versions you need, and avoid shipping several frameworks in one image.
- Do not bake model weights into the image. Download them at startup into a volume or cache, or mount them from shared storage.
- Use lazy pulling or pre-pulled images on GPU nodes.
- Use multi-stage builds to keep compilers out.

ML images often reach 10 GB or more, which makes cold starts and autoscaling slow.

## 398: What is Docker Model Runner?

Docker Model Runner lets you pull and run AI models (LLMs) locally through Docker, using inference engines such as llama.cpp. Models are distributed as OCI artifacts on Docker Hub and other registries.

```bash
docker model pull ai/smollm2
docker model run ai/smollm2 "Explain Docker volumes in one sentence"
```

It serves an OpenAI-compatible API, so apps in containers can call it. Compose files can declare models with the top-level `models` key so a service gets the model's endpoint injected. It runs in Docker Desktop and as a plugin on Docker Engine.

## 399: How do you store non-image artifacts in a container registry?

OCI registries can store any artifact, not only images: Helm charts, SBOMs, signatures, Compose files, WASM modules, AI models. Tools like ORAS push and pull them:

```bash
oras push ghcr.io/my-org/configs:1.0 config.yaml:application/yaml
oras pull ghcr.io/my-org/configs:1.0
```

The OCI 1.1 spec added the `subject` field and the referrers API, so you can attach artifacts (like signatures or SBOMs) to an image and look them up later.

## 400: What is the referrers API?

The referrers API (OCI distribution spec 1.1) lets a client ask a registry: "which artifacts point to this image digest?" Artifacts like signatures, SBOMs and attestations set the `subject` field to the image they describe.

```text
GET /v2/<name>/referrers/<digest>
```

Before this, tools used tag naming tricks (like `sha256-<digest>.sig`) to find signatures. With the referrers API, supply chain data stays linked to the image without extra tags.

## 401: Your image build takes 15 minutes in CI. How do you speed it up?

1. Look at the build output (`--progress=plain`) to see which steps take the time and whether they are cached.
2. Fix layer order so dependency installs are cached, and add a `.dockerignore`.
3. Export and import cache (`type=registry` or `type=gha`) with `mode=max`, because CI runners start empty.
4. Add cache mounts for package managers and compiler caches.
5. Split the Dockerfile into stages that can run in parallel (for example frontend and backend builds).
6. Avoid QEMU for multi-platform builds: cross-compile or use native builders.
7. Consider a persistent remote builder (Docker Build Cloud or self-hosted BuildKit) so cache is always warm.

## 402: A container works locally but crashes in production. How do you investigate?

1. Compare the image: same digest? Same platform (`arm64` locally vs `amd64` in prod is a classic)?
2. Compare config: environment variables, mounted secrets, command, user.
3. Check resource limits: production may have a memory limit that local runs do not, so look for OOM kills.
4. Check the exit code and logs right after the crash.
5. Check permissions: production may run with a different UID, read-only filesystem or dropped capabilities.
6. Check network access: DNS names, firewall rules, TLS certificates (missing CA certificates in minimal images).

Reproduce locally with the same limits and flags to confirm.

## 403: An image built on an Apple Silicon Mac fails with "exec format error" on the server. Why?

The image was built for `linux/arm64` (the Mac's native platform), and the server is `linux/amd64`. The binaries in it cannot run on that CPU.

Fix it by building for the server's platform or a multi-platform image:

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t my-org/app:1.0 --push .
```

Also set `platform` in Compose or pin `--platform` in CI so it is not left to whatever machine builds it. The same error can also come from a script with a missing or wrong shebang.

## 404: Your server's disk is full because of Docker. What do you do?

1. See what uses the space: `docker system df -v` and `du -sh /var/lib/docker/*`.
2. Quick wins: `docker builder prune`, `docker image prune -a`, `docker container prune`.
3. Look for huge container log files in `/var/lib/docker/containers/*/*-json.log` and set log limits.
4. Look for unused volumes (`docker volume ls -f dangling=true`), but check what they hold before removing.
5. Look for containers writing a lot to their writable layer (`docker ps -s`) and move that data to volumes.
6. Prevent it: log rotation in `daemon.json`, scheduled cleanup, monitoring, a separate disk for Docker data.

## 405: Your app container takes 60 seconds to stop. Why and how do you fix it?

60 seconds suggests a custom stop timeout, but the cause is usually the same as with the default 10 seconds: the app never receives `SIGTERM`, or ignores it, so Docker waits for the timeout and then kills it.

Check:

- Is `CMD` or `ENTRYPOINT` in shell form, or is a script running without `exec`? Then a shell is PID 1 and swallows the signal.
- Is the app started through `npm start` or another wrapper?
- Does the app have a `SIGTERM` handler, and does it actually close servers and connections?
- Is it waiting for long-running requests or jobs without a deadline?

Fix with exec form, `exec "$@"`, `--init`, and a proper shutdown handler with its own deadline.

## 406: How do you make a database container production-ready?

- Use a named volume (or dedicated disk) for data, with a fast filesystem.
- Pin the exact major version. Major upgrades of databases like Postgres need a dump and restore or `pg_upgrade`, not just a new tag.
- Set memory limits and tune the database for them (shared buffers, cache sizes).
- Use secrets as files for passwords.
- Do not publish its port publicly. Put it on a private network.
- Set up backups with the database's own tools, and test restores.
- Add a healthcheck.

For many teams, a managed database service is simpler and safer than running it in a container.

## 407: Why should you be careful upgrading a Postgres container by changing the tag?

Postgres stores data in a format specific to the major version. If you change `postgres:16` to `postgres:17` and start it on the old volume, it refuses to start with an error about incompatible data files.

You need to:

1. Dump the data with `pg_dumpall` from the old version and restore into a new volume with the new version, or
2. Run `pg_upgrade` (there are community images built for this).

Minor version updates (17.1 to 17.2) are safe to do by just changing the tag. Always back up first.

## 408: How do you share a cache between a CI build and local development?

Push the build cache to a registry from CI, and import it locally:

```bash
# CI
docker buildx build \
  --cache-to type=registry,ref=ghcr.io/my-org/api:buildcache,mode=max \
  --cache-from type=registry,ref=ghcr.io/my-org/api:buildcache \
  -t ghcr.io/my-org/api:${GIT_SHA} --push .

# local
docker buildx build \
  --cache-from type=registry,ref=ghcr.io/my-org/api:buildcache \
  -t api:dev .
```

Developers then get CI's cached layers for unchanged steps. Docker Build Cloud does this automatically with a shared builder.

## 409: How do you design container images for fast rollbacks?

- Tag every build with an immutable tag (commit SHA or version) and never overwrite tags.
- Keep old images in the registry for a while (lifecycle rules that keep the last N releases).
- Deploy by digest or immutable tag, so rollback is "deploy the previous tag".
- Keep database migrations backwards compatible (expand and contract), so the old version still works with the new schema.
- Keep images pre-pulled on hosts if rollback speed matters.

## 410: What is the expand and contract pattern for migrations, and why does it matter with containers?

During a rolling deploy, old and new containers run at the same time against the same database. A migration that renames or drops a column breaks the old version.

Expand and contract splits it:

1. **Expand:** add the new column or table, keep the old one. Deploy code that writes both and reads the new one.
2. **Migrate data** in the background.
3. **Contract:** after all old containers are gone, remove the old column.

This makes deploys and rollbacks safe without downtime.

## 411: How would you run Docker in a multi-tenant environment?

Plain Docker on one host is not a strong multi-tenant boundary, because all tenants share the kernel and anyone with API access is root.

Options:

- Give each tenant its own VM or microVM (Firecracker, Kata) and run containers inside it.
- Use sandboxed runtimes like gVisor.
- Never give tenants direct access to the Docker API. Put an API of your own in front that only allows safe options.
- Use separate networks per tenant, strict resource limits and per-tenant storage.

Managed platforms like Cloud Run or Fargate use microVM-style isolation for this reason.

## 412: How do resource limits interact with language runtimes?

Many runtimes read the host's CPU count and memory, not the container's limits, unless they are cgroup-aware:

- **JVM:** recent versions read cgroup limits. Use `-XX:MaxRAMPercentage` to control heap size.
- **Node.js:** recent versions are cgroup-aware for the default heap size. Set `--max-old-space-size` if you want an exact value.
- **Go:** `GOMAXPROCS` used to default to the host CPU count. Go 1.25 made it respect cgroup CPU limits. Use `GOMEMLIMIT` for memory.
- **Python:** worker counts like `gunicorn -w` based on `os.cpu_count()` return host CPUs, so set them explicitly.

Wrong sizing causes CPU throttling, too many threads or OOM kills.

## 413: What is CPU throttling and how do you detect it?

When a container uses its full CFS quota before the period ends, the kernel pauses it until the next period. This is throttling. An app with a 1-CPU limit and 8 busy threads can use the quota in 12.5 ms and then sit idle for the rest of the 100 ms period, adding latency.

Detect it:

```bash
cat /sys/fs/cgroup/cpu.stat   # inside the container on cgroup v2
# nr_periods, nr_throttled, throttled_usec
```

cAdvisor exposes `container_cpu_cfs_throttled_periods_total`. Fix it by raising the limit, reducing thread counts to match the limit, or removing CPU limits and relying on CPU shares.

## 414: How would you limit the network bandwidth of a container?

Docker has no built-in bandwidth option. Options:

- Use Linux traffic control (`tc`) on the container's veth interface on the host, or inside the container's network namespace with `nsenter`.
- Use a tool built on `tc` for Docker.
- In Kubernetes, use the CNI bandwidth plugin annotations.

```bash
PID=$(docker inspect -f '{{.State.Pid}}' api)
sudo nsenter -t "$PID" -n tc qdisc add dev eth0 root tbf rate 10mbit burst 32kbit latency 400ms
```

## 415: What happens to running containers when the host reboots?

The containers stop. When the Docker daemon starts again, it starts containers that have `restart: always` or `unless-stopped` (if they were not stopped manually before). Containers with `no` or `on-failure` stay stopped.

The container's writable layer and volumes are kept, so state on disk survives. Anything in tmpfs or memory is lost. Make sure the Docker service itself is enabled at boot (`systemctl enable docker`).

## 416: How do you run a container that needs to start before Docker networking is ready on boot?

You usually do not. Instead, let Docker start containers with a restart policy, and make the app retry its connections. If you need ordering with other host services, create a systemd unit that runs the container:

```ini
[Unit]
After=docker.service network-online.target
Requires=docker.service

[Service]
ExecStart=/usr/bin/docker run --rm --name agent my-agent:1.0
ExecStop=/usr/bin/docker stop agent
Restart=always

[Install]
WantedBy=multi-user.target
```

Podman has Quadlet for this kind of systemd integration.

## 417: How do you handle time and clock issues in containers?

Containers use the host's kernel clock. You cannot set the time per container (no time namespace in Docker by default), and you should not try. Keep the host synced with NTP (chrony or systemd-timesyncd).

Time zone is just a user-space setting (`TZ` and `tzdata`). Clock drift on the host shows up as TLS errors, expired tokens or wrong log times in every container, so check the host first.

## 418: How does Docker handle IPv6 and dual-stack networks today?

You can create dual-stack networks where containers get both IPv4 and IPv6 addresses. Newer Docker versions can also create IPv6-only networks (`--ipv4=false`). Published ports listen on both stacks by default when the host supports it.

Things to watch for: Docker NATs IPv6 traffic by default on bridge networks (it uses `ip6tables`), you need a routable prefix for direct routing without NAT, and some apps only bind IPv4 (`0.0.0.0`) and are not reachable over IPv6 unless they bind `::`.

## 419: What gateway modes can a bridge network use?

The bridge driver supports options like `com.docker.network.bridge.gateway_mode_ipv4` (and `_ipv6`):

- `nat` (default): containers are masqueraded behind the host's IP.
- `routed`: no NAT. Containers are directly reachable with their own IPs if the network routes to them.
- `nat-unprotected` and `isolated`: variants for special cases, such as no external connectivity at all.

`routed` mode is useful with IPv6, where every container can have a global address.

## 420: How would you structure Compose files for local dev, CI and production?

```text
compose.yaml           # shared: services, networks, volumes
compose.override.yaml  # dev: build, bind mounts, debug ports (loaded automatically)
compose.ci.yaml        # CI: test runners, no published ports
compose.prod.yaml      # prod: images from registry, restart, limits, logging
```

```bash
docker compose up                                        # dev
docker compose -f compose.yaml -f compose.ci.yaml run --rm tests
docker compose -f compose.yaml -f compose.prod.yaml up -d
```

You can also set `COMPOSE_FILE` in a `.env` file per environment so people do not have to type the `-f` flags.

## 421: How do you test a Dockerfile change safely?

- Run `docker build --check` for lint warnings.
- Build and run the image locally with production-like flags (non-root, read-only, limits).
- Use container structure tests (Google's `container-structure-test`) or simple scripts to check files, users, ports and that commands run.
- Scan the image and compare size and CVE count with the current one.
- Run the integration test suite against the new image in CI before merging.

## 422: How do you write a test for an image's contents?

With `container-structure-test`:

```yaml
schemaVersion: 2.0.0
commandTests:
  - name: "node version"
    command: "node"
    args: ["--version"]
    expectedOutput: ["v22\\..*"]
fileExistenceTests:
  - name: "app exists"
    path: "/app/dist/server.js"
    shouldExist: true
metadataTest:
  user: "node"
  exposedPorts: ["3000"]
```

```bash
container-structure-test test --image my-app:1.0 --config tests.yaml
```

It catches problems like running as root or missing files before deployment.

## 423: How do you design a Dockerfile for a pnpm or Yarn workspace monorepo?

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-slim AS base
RUN corepack enable
WORKDIR /repo

FROM base AS build
COPY . .
RUN --mount=type=cache,id=pnpm,target=/root/.local/share/pnpm/store \
    pnpm install --frozen-lockfile
RUN pnpm --filter api build
RUN pnpm --filter api deploy --prod /out

FROM node:22-slim
WORKDIR /app
COPY --from=build /out .
USER node
CMD ["node", "dist/server.js"]
```

`pnpm deploy` copies one package with only its production dependencies into `/out`, so the final image has no other workspace packages. For better caching, copy only the lock file and `pnpm fetch` first. Check the corepack status for your Node.js version, since newer Node.js releases stopped bundling it.

## 424: How do you run several versions of a service side by side on one host?

Use separate Compose project names or separate container names, and avoid fixed host ports:

```bash
TAG=1.4.0 docker compose -p api-blue up -d
TAG=1.5.0 docker compose -p api-green up -d
```

Put a reverse proxy in front that routes by host name or path, or by labels (Traefik reads Docker labels). Then you can switch traffic between them and remove the old project.

## 425: How does Traefik discover containers?

Traefik connects to the Docker API (through the socket or a socket proxy) and watches for containers with labels:

```yaml
services:
  api:
    image: my-api:1.0
    labels:
      - traefik.enable=true
      - traefik.http.routers.api.rule=Host(`api.example.com`)
      - traefik.http.services.api.loadbalancer.server.port=3000
```

When a container starts or stops, Traefik updates its routes automatically. It also only sends traffic to healthy containers if healthchecks are set.

## 426: What are the trade-offs of building images on the production server?

Building on the server (`build:` in production Compose files) is simple, but:

- Every server may produce a slightly different image.
- Build tools and source code must be on the server.
- Builds use CPU and memory that the running app needs.
- You cannot scan, sign or test the exact image before it runs.
- Rollback means rebuilding an older commit.

Building once in CI and pushing to a registry avoids all of these.

## 427: How do you use Docker to provide consistent tooling for a team without dev containers?

Wrap tools in containers and call them through scripts or a Makefile:

```makefile
TF = docker run --rm -it -v $(PWD):/work -w /work hashicorp/terraform:1.13

plan:
	$(TF) plan

fmt:
	$(TF) fmt -recursive
```

Everyone uses the same tool version without installing it. Pin the image versions and mount only what the tool needs.

## 428: How do you handle file ownership problems with volumes written by containers?

Files created by a container belong to the UID the process runs as. If that is root, files on a bind mount end up owned by root on the host, and your user cannot edit or delete them.

Options:

- Run the container as your UID: `-u "$(id -u):$(id -g)"`.
- Build the image with a user whose UID matches the typical host UID (often 1000), passed as a build arg.
- Use an entrypoint that adjusts the user's UID at start (common in dev images, needs root at start then drops privileges with `gosu` or `su-exec`).
- Use user namespaces or rootless Docker, where container root maps to your user.

## 429: How do gosu and su-exec work in entrypoint scripts?

They switch to another user and then `exec` the command, so the target process replaces them as PID 1 with no extra process left behind. Unlike `sudo` or `su`, they do not keep a parent process around, so signals reach the app directly.

```bash
#!/bin/sh
set -e
chown -R app:app /data
exec su-exec app "$@"
```

The official Postgres and Redis images use this pattern: start as root to fix permissions on the data folder, then drop to a normal user.

## 430: Why should you use a fixed numeric UID in images?

```dockerfile
RUN groupadd --gid 10001 app && useradd --uid 10001 --gid app --no-create-home app
USER 10001:10001
```

- Kubernetes `runAsNonRoot` can only verify a numeric user. With `USER app`, it cannot tell if `app` is root without looking at `/etc/passwd`.
- File ownership on volumes is predictable across images and hosts.
- A high UID (above typical host users) avoids accidentally matching a real host user.

## 431: What happens when two containers write to the same bind-mounted file?

Docker does nothing special. Both processes write to the same host file, and the result depends on the app. Without file locking, writes can interleave or overwrite each other. Some locking mechanisms do not work across certain bind mount setups (for example network filesystems, or Docker Desktop's file sharing).

SQLite and similar file databases are especially risky to share. Use a single writer, a proper database server, or a queue.

## 432: How do you inspect what a running container is doing without stopping it?

- `docker stats` and `docker top` for resource and process info.
- `docker logs -f` for output.
- `docker exec` to run tools inside, if available.
- A debug container that joins its namespaces (`--pid container:x --network container:x`) with tools like `ps`, `ss`, `tcpdump`, `strace`.
- `docker diff` to see what files it changed.
- For runtimes, built-in profilers (Node.js inspector, `py-spy`, Java Flight Recorder) attached through the shared PID namespace.

## 433: How do you profile a Python app running in a container?

Use `py-spy` from a debug container that shares the PID namespace:

```bash
docker run --rm -it --pid container:api --cap-add SYS_PTRACE \
  python:3.13-slim sh -c "pip install py-spy && py-spy top --pid 1"
```

`py-spy dump --pid 1` prints the current stack of every thread, which helps with hangs. It does not require changes to the app or a restart.

## 434: How do you handle very large build contexts?

- Write a strict `.dockerignore`, or invert it: ignore everything with `*` and allow only what you need with `!src`, `!package.json`.
- Use a smaller folder as the context and add others with named build contexts.
- Build from a Git URL so only tracked files are used.
- Check what is sent: BuildKit prints "transferring context" with the size. If it is hundreds of MB, something is not ignored.

BuildKit only transfers files that the Dockerfile uses and caches them between builds, but a messy context still slows down the first build and can invalidate cache.

## 435: How do you avoid cache invalidation from COPY . . in an otherwise good Dockerfile?

- Copy only what is needed: `COPY src ./src` and `COPY tsconfig.json ./` instead of everything.
- Ignore files that change often but do not affect the build: `.git`, logs, test reports, editor folders, local `.env`.
- Generate files like version info at the end, in their own step, or pass them as build args only to the final stage.
- Keep CI from changing files before the build (for example writing a build number into a tracked file early).

## 436: What is a scenario where a multi-stage build makes the cache worse, and how do you fix it?

If the final stage starts with `COPY --from=build /app .` and the build stage copies all source code before installing dependencies, every code change invalidates the dependency install in the build stage. If you copy `node_modules` and the built output in one step, any change re-copies a huge folder.

Fix it by keeping a separate deps stage that only depends on lock files, and copy `node_modules` and the build output in separate `COPY` steps, putting the one that changes less first. In CI, export the cache with `mode=max`, so intermediate stages are cached too.

## 437: How would you build a minimal image for a Rust app?

```dockerfile
# syntax=docker/dockerfile:1
FROM rust:1.90 AS build
WORKDIR /src
COPY . .
RUN --mount=type=cache,target=/usr/local/cargo/registry \
    --mount=type=cache,target=/src/target \
    cargo build --release && cp target/release/my-app /my-app

FROM gcr.io/distroless/cc-debian12:nonroot
COPY --from=build /my-app /my-app
ENTRYPOINT ["/my-app"]
```

The target folder is a cache mount, so the binary must be copied out of it in the same `RUN`. The `cc` distroless variant includes glibc and libgcc, which most Rust binaries need. For `scratch`, build a fully static binary with the `musl` target.

## 438: How does Docker Compose decide when to recreate a container?

When you run `docker compose up`, Compose computes a hash of each service's config and stores it as a label on the container. On the next `up`, it compares:

- If the config hash changed (image, environment, ports, volumes, command and so on), it recreates the container.
- If the image tag now points to a different image ID (for example after `pull` or `build`), it recreates it.
- Otherwise, it leaves the container running.

`--force-recreate` and `--no-recreate` override this. Changes in a mounted file's content do not trigger a recreate, since the config itself did not change.

## 439: How do Compose and Docker labels help with automation?

Compose adds labels to everything it creates, like `com.docker.compose.project`, `com.docker.compose.service` and `com.docker.compose.config-hash`. You can use them in filters:

```bash
docker ps --filter label=com.docker.compose.project=shop
docker ps --filter label=com.docker.compose.service=api -q | xargs docker restart
```

Your own labels (owner, team, backup schedule) let tools like Traefik, backup scripts and monitoring find containers without hard-coded names.

## 440: How do you implement a sidecar pattern with Docker?

Run the helper container in the main container's network namespace, so it can talk to the app on `localhost`:

```yaml
services:
  app:
    image: my-app:1.0
  metrics-exporter:
    image: my-exporter:1.0
    network_mode: "service:app"
    depends_on: [app]
```

`network_mode: "service:app"` makes the exporter share `app`'s network. Common sidecars are log shippers, proxies (like Envoy) and metrics exporters. In Kubernetes, this is how containers in a pod work by default.

## 441: How do you run Docker in CI on Kubernetes runners?

Options, from most to least common:

- Use a remote builder (Docker Build Cloud, a BuildKit deployment in the cluster) and only run the CLI in the CI pod.
- Use rootless BuildKit or Buildah in the pod.
- Use Docker-in-Docker as a privileged sidecar, if your cluster allows privileged pods.
- Mount the node's container runtime socket (risky, and nodes usually do not run Docker anymore).

For tests that need containers (like Testcontainers), use a remote Docker endpoint or Testcontainers Cloud, since you cannot easily start containers inside a normal pod.

## 442: How would you reduce cold start time for a containerized service on a serverless platform?

- Make the image small and use a base image that the platform caches well.
- Keep startup work small: lazy-load modules, avoid big downloads or migrations at boot.
- Use languages and runtimes that start fast, or features like JVM CRaC, GraalVM native images or snapshot-based startup where supported.
- Set a minimum number of instances to keep warm.
- Make readiness depend on what is really needed to serve requests.

Many platforms also support image streaming (lazy pulling) for large images.

## 443: How do you check that a Dockerfile follows best practices automatically?

- `docker build --check` runs BuildKit's built-in checks.
- Hadolint lints Dockerfiles (and runs ShellCheck on `RUN` lines).
- Policy tools like Conftest (OPA) or Checkov can enforce company rules, for example "base image must come from our registry" or "USER must be set".
- Scanners (Scout, Trivy) report CVEs and some misconfigurations in the built image.

Run them in CI and as a pre-commit hook.

## 444: How do you enforce that only approved images run in your environment?

- Only allow pulls from your own registry (network rules, or registry allow lists in Docker Desktop settings for developer machines).
- Mirror approved public images into that registry after scanning.
- Sign images in CI and verify signatures at deploy time (Kyverno, Sigstore policy controller, or a deploy script that runs `cosign verify`).
- Use Docker Desktop's Image Access Management or Registry Access Management for laptops.
- Block `latest` and require digests in policies.

## 445: How would you design logging for 100 containers on a few hosts?

- Apps write structured JSON logs to stdout with a request ID or trace ID.
- Each host runs one log agent container (Fluent Bit, Vector or Grafana Alloy) that reads `/var/lib/docker/containers/*/*.log`, adds container metadata (name, image, Compose labels) and ships to a central store (Loki, Elasticsearch, a cloud service).
- Local logs use the `local` or `json-file` driver with rotation, so hosts never fill up.
- Alerts on error rates and on missing logs from a service.

This keeps apps simple and avoids losing logs when the central store is slow.

## 446: What are the costs and risks of running containers as root even with a non-root user inside?

If the daemon runs as root and there is no user namespace remapping, UID 0 inside the container is UID 0 on the host. A non-root user in the container helps because:

- A compromised app cannot install packages or change system files in the container.
- If there is a container escape bug, the attacker lands on the host as a normal UID instead of root.
- Writable host mounts are not written as root.

But the setup is only as strong as its weakest part: one container with `--privileged`, a mounted socket or dangerous capabilities can still give root access to the host.

## 447: How do you handle certificates and custom CAs in images?

Minimal images may not have CA certificates at all, which breaks HTTPS calls. Install them, and add company CAs if needed:

```dockerfile
FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/*
COPY company-root-ca.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates
```

Some runtimes use their own trust store: Node.js can use `NODE_EXTRA_CA_CERTS`, Java uses its own keystore, and Python `requests` uses `certifi` unless you set `REQUESTS_CA_BUNDLE`. Build-time downloads behind a TLS-inspecting proxy also need the CA inside the builder.

## 448: How do you use Docker behind a corporate proxy?

There are three separate places to configure:

- **The daemon** (for pulls): set `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` in a systemd drop-in for `docker.service`, or in `daemon.json` under `"proxies"`.
- **Builds:** pass them as build args. BuildKit treats the proxy args as special and does not store them in the image.
- **Containers at run time:** set them in `~/.docker/config.json` under `"proxies"`, and the CLI injects them into new containers and builds automatically.

```json
{
  "proxies": {
    "default": {
      "httpProxy": "http://proxy.corp:3128",
      "httpsProxy": "http://proxy.corp:3128",
      "noProxy": "localhost,127.0.0.1,.corp"
    }
  }
}
```

## 449: How would you explain the trade-off between one big image and many small images?

One big image with all tools:

- Simple to manage, one build.
- Larger attack surface, slower pulls and every service gets every dependency.
- A change in one component rebuilds and redeploys everything.

Many small, focused images:

- Each service only has what it needs, smaller CVE surface, independent releases.
- More pipelines and more images to keep updated.

The usual middle ground is shared base images with small per-service layers on top, so common layers are pulled once and updates to the base roll out to all services.

## 450: What changed in recent Docker versions that you should know about?

Some notable changes in the last couple of years:

- Compose v1 (`docker-compose`) is gone. Compose v2 and later are a CLI plugin, the `version` key is obsolete, and current releases (v5) build through Bake.
- BuildKit is the default builder, with build checks, cache and secret mounts, SBOM and provenance attestations.
- Docker Engine 29 uses the containerd image store by default on new installs, raised the minimum API version, and added an experimental nftables firewall backend.
- `docker init`, Compose Watch, `docker debug` and Docker Scout became part of everyday workflows.
- Docker Hardened Images became freely available, and Docker Content Trust is being retired in favor of Sigstore and Notation.
- Docker Model Runner and the `models` key in Compose added local AI model support.

Check the release notes of the Engine, Compose and Desktop before upgrading, because defaults change between major versions.
