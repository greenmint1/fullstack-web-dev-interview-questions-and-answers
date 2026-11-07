# Kubernetes Interview Questions and Answers

_Last updated: October 28, 2026_

450 Kubernetes interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target current Kubernetes (1.37, released in August 2026) and the tools around it, like kubectl, Helm, Kustomize and the Gateway API. Older things like Ingress, ingress-nginx, PodSecurityPolicy and the IPVS proxy mode are mentioned where they still matter, since you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Kubernetes?](#1-what-is-kubernetes)
- [2: What problems does Kubernetes solve?](#2-what-problems-does-kubernetes-solve)
- [3: What does the name K8s mean?](#3-what-does-the-name-k8s-mean)
- [4: What is a cluster?](#4-what-is-a-cluster)
- [5: What is a node?](#5-what-is-a-node)
- [6: What is a Pod?](#6-what-is-a-pod)
- [7: Why does Kubernetes use Pods instead of running containers directly?](#7-why-does-kubernetes-use-pods-instead-of-running-containers-directly)
- [8: What is the control plane?](#8-what-is-the-control-plane)
- [9: What is the kube-apiserver?](#9-what-is-the-kube-apiserver)
- [10: What is etcd?](#10-what-is-etcd)
- [11: What does the kube-scheduler do?](#11-what-does-the-kube-scheduler-do)
- [12: What does the kube-controller-manager do?](#12-what-does-the-kube-controller-manager-do)
- [13: What is the kubelet?](#13-what-is-the-kubelet)
- [14: What is kube-proxy?](#14-what-is-kube-proxy)
- [15: What is a container runtime?](#15-what-is-a-container-runtime)
- [16: What is kubectl?](#16-what-is-kubectl)
- [17: What is a kubeconfig file?](#17-what-is-a-kubeconfig-file)
- [18: What is a context in kubectl?](#18-what-is-a-context-in-kubectl)
- [19: What is a manifest?](#19-what-is-a-manifest)
- [20: What is the difference between spec and status?](#20-what-is-the-difference-between-spec-and-status)
- [21: What is declarative configuration?](#21-what-is-declarative-configuration)
- [22: What is the difference between kubectl create and kubectl apply?](#22-what-is-the-difference-between-kubectl-create-and-kubectl-apply)
- [23: What is a Namespace?](#23-what-is-a-namespace)
- [24: What namespaces exist by default?](#24-what-namespaces-exist-by-default)
- [25: Are all objects namespaced?](#25-are-all-objects-namespaced)
- [26: What are labels?](#26-what-are-labels)
- [27: What is a label selector?](#27-what-is-a-label-selector)
- [28: What are annotations and how are they different from labels?](#28-what-are-annotations-and-how-are-they-different-from-labels)
- [29: What is a Deployment?](#29-what-is-a-deployment)
- [30: What is a ReplicaSet?](#30-what-is-a-replicaset)
- [31: What is the difference between a Deployment and a ReplicaSet?](#31-what-is-the-difference-between-a-deployment-and-a-replicaset)
- [32: What is a ReplicationController?](#32-what-is-a-replicationcontroller)
- [33: How do you scale a Deployment?](#33-how-do-you-scale-a-deployment)
- [34: What is a Service?](#34-what-is-a-service)
- [35: What types of Services are there?](#35-what-types-of-services-are-there)
- [36: What is a ClusterIP Service?](#36-what-is-a-clusterip-service)
- [37: What is a NodePort Service?](#37-what-is-a-nodeport-service)
- [38: What is a LoadBalancer Service?](#38-what-is-a-loadbalancer-service)
- [39: What is an ExternalName Service?](#39-what-is-an-externalname-service)
- [40: What is the difference between port, targetPort and nodePort?](#40-what-is-the-difference-between-port-targetport-and-nodeport)
- [41: How does service discovery work in Kubernetes?](#41-how-does-service-discovery-work-in-kubernetes)
- [42: What is CoreDNS?](#42-what-is-coredns)
- [43: What is an Ingress?](#43-what-is-an-ingress)
- [44: What is an Ingress controller?](#44-what-is-an-ingress-controller)
- [45: What is the Gateway API?](#45-what-is-the-gateway-api)
- [46: What is a ConfigMap?](#46-what-is-a-configmap)
- [47: What is a Secret?](#47-what-is-a-secret)
- [48: Is base64 encryption?](#48-is-base64-encryption)
- [49: How do you use a ConfigMap as environment variables?](#49-how-do-you-use-a-configmap-as-environment-variables)
- [50: How do you mount a ConfigMap as files?](#50-how-do-you-mount-a-configmap-as-files)
- [51: What is a volume in Kubernetes?](#51-what-is-a-volume-in-kubernetes)
- [52: What is an emptyDir volume?](#52-what-is-an-emptydir-volume)
- [53: What is a hostPath volume?](#53-what-is-a-hostpath-volume)
- [54: What is a PersistentVolume?](#54-what-is-a-persistentvolume)
- [55: What is a PersistentVolumeClaim?](#55-what-is-a-persistentvolumeclaim)
- [56: What is the difference between a PV and a PVC?](#56-what-is-the-difference-between-a-pv-and-a-pvc)
- [57: What is a StorageClass?](#57-what-is-a-storageclass)
- [58: What are the access modes of a PersistentVolume?](#58-what-are-the-access-modes-of-a-persistentvolume)
- [59: What is a DaemonSet?](#59-what-is-a-daemonset)
- [60: What is a StatefulSet?](#60-what-is-a-statefulset)
- [61: What is the difference between a Deployment and a StatefulSet?](#61-what-is-the-difference-between-a-deployment-and-a-statefulset)
- [62: What is a Job?](#62-what-is-a-job)
- [63: What is a CronJob?](#63-what-is-a-cronjob)
- [64: What is the restartPolicy of a Pod?](#64-what-is-the-restartpolicy-of-a-pod)
- [65: What are the phases of a Pod?](#65-what-are-the-phases-of-a-pod)
- [66: What does CrashLoopBackOff mean?](#66-what-does-crashloopbackoff-mean)
- [67: What does ImagePullBackOff mean?](#67-what-does-imagepullbackoff-mean)
- [68: How do you see the logs of a Pod?](#68-how-do-you-see-the-logs-of-a-pod)
- [69: How do you open a shell in a running container?](#69-how-do-you-open-a-shell-in-a-running-container)
- [70: What does kubectl describe show?](#70-what-does-kubectl-describe-show)
- [71: What are events in Kubernetes?](#71-what-are-events-in-kubernetes)
- [72: How do you see the YAML of an existing object?](#72-how-do-you-see-the-yaml-of-an-existing-object)
- [73: What output formats does kubectl get support?](#73-what-output-formats-does-kubectl-get-support)
- [74: How do you delete objects?](#74-how-do-you-delete-objects)
- [75: How do you get quick help on a resource's fields?](#75-how-do-you-get-quick-help-on-a-resources-fields)
- [76: What is port forwarding in kubectl?](#76-what-is-port-forwarding-in-kubectl)
- [77: What is a resource request?](#77-what-is-a-resource-request)
- [78: What is a resource limit?](#78-what-is-a-resource-limit)
- [79: What do units like 500m and 512Mi mean?](#79-what-do-units-like-500m-and-512mi-mean)
- [80: What does OOMKilled mean?](#80-what-does-oomkilled-mean)
- [81: What is a liveness probe?](#81-what-is-a-liveness-probe)
- [82: What is a readiness probe?](#82-what-is-a-readiness-probe)
- [83: What is a startup probe?](#83-what-is-a-startup-probe)
- [84: What kinds of probe checks are there?](#84-what-kinds-of-probe-checks-are-there)
- [85: What is the difference between liveness and readiness probes?](#85-what-is-the-difference-between-liveness-and-readiness-probes)
- [86: What are init containers?](#86-what-are-init-containers)
- [87: What is a sidecar container?](#87-what-is-a-sidecar-container)
- [88: What is a multi-container Pod?](#88-what-is-a-multi-container-pod)
- [89: What is the difference between a container image tag and a digest?](#89-what-is-the-difference-between-a-container-image-tag-and-a-digest)
- [90: What is imagePullPolicy?](#90-what-is-imagepullpolicy)
- [91: Why should you avoid the latest tag in Kubernetes?](#91-why-should-you-avoid-the-latest-tag-in-kubernetes)
- [92: How do you pull images from a private registry?](#92-how-do-you-pull-images-from-a-private-registry)
- [93: What is a ServiceAccount?](#93-what-is-a-serviceaccount)
- [94: What is the difference between a user account and a ServiceAccount?](#94-what-is-the-difference-between-a-user-account-and-a-serviceaccount)
- [95: What is RBAC?](#95-what-is-rbac)
- [96: How do you give a ServiceAccount read access to Pods in one namespace?](#96-how-do-you-give-a-serviceaccount-read-access-to-pods-in-one-namespace)
- [97: How do you check if you have permission to do something?](#97-how-do-you-check-if-you-have-permission-to-do-something)
- [98: What is a rolling update?](#98-what-is-a-rolling-update)
- [99: How do you update the image of a Deployment?](#99-how-do-you-update-the-image-of-a-deployment)
- [100: How do you roll back a Deployment?](#100-how-do-you-roll-back-a-deployment)
- [101: What is the Recreate deployment strategy?](#101-what-is-the-recreate-deployment-strategy)
- [102: How do you check the status of a rollout?](#102-how-do-you-check-the-status-of-a-rollout)
- [103: How do you restart all Pods of a Deployment?](#103-how-do-you-restart-all-pods-of-a-deployment)
- [104: What is a HorizontalPodAutoscaler?](#104-what-is-a-horizontalpodautoscaler)
- [105: What is the Metrics Server?](#105-what-is-the-metrics-server)
- [106: What is the difference between horizontal and vertical scaling?](#106-what-is-the-difference-between-horizontal-and-vertical-scaling)
- [107: What is the Cluster Autoscaler?](#107-what-is-the-cluster-autoscaler)
- [108: What are taints and tolerations?](#108-what-are-taints-and-tolerations)
- [109: What taint effects exist?](#109-what-taint-effects-exist)
- [110: What is a nodeSelector?](#110-what-is-a-nodeselector)
- [111: What is node affinity?](#111-what-is-node-affinity)
- [112: What is Pod affinity and anti-affinity?](#112-what-is-pod-affinity-and-anti-affinity)
- [113: What is a Pod's QoS class?](#113-what-is-a-pods-qos-class)
- [114: What is Minikube?](#114-what-is-minikube)
- [115: What is kind?](#115-what-is-kind)
- [116: What are some other ways to run Kubernetes locally?](#116-what-are-some-other-ways-to-run-kubernetes-locally)
- [117: What are managed Kubernetes services?](#117-what-are-managed-kubernetes-services)
- [118: What is k3s?](#118-what-is-k3s)
- [119: How do you create a Deployment quickly without writing YAML?](#119-how-do-you-create-a-deployment-quickly-without-writing-yaml)
- [120: What does kubectl run do?](#120-what-does-kubectl-run-do)
- [121: Why should you not create bare Pods for applications?](#121-why-should-you-not-create-bare-pods-for-applications)
- [122: What is a multi-document YAML file?](#122-what-is-a-multi-document-yaml-file)
- [123: How do you apply all manifests in a folder?](#123-how-do-you-apply-all-manifests-in-a-folder)
- [124: What is Helm?](#124-what-is-helm)
- [125: What is Kustomize?](#125-what-is-kustomize)
- [126: What is the Kubernetes Dashboard?](#126-what-is-the-kubernetes-dashboard)
- [127: What is k9s?](#127-what-is-k9s)
- [128: What is the API group of common resources?](#128-what-is-the-api-group-of-common-resources)
- [129: What are API versions like v1alpha1, v1beta1 and v1?](#129-what-are-api-versions-like-v1alpha1-v1beta1-and-v1)
- [130: What is a NetworkPolicy?](#130-what-is-a-networkpolicy)
- [131: What is a CNI plugin?](#131-what-is-a-cni-plugin)
- [132: What are the basic rules of the Kubernetes network model?](#132-what-are-the-basic-rules-of-the-kubernetes-network-model)
- [133: How do containers in the same Pod talk to each other?](#133-how-do-containers-in-the-same-pod-talk-to-each-other)
- [134: What is a headless Service?](#134-what-is-a-headless-service)
- [135: What are EndpointSlices?](#135-what-are-endpointslices)
- [136: What is the Downward API?](#136-what-is-the-downward-api)
- [137: How do you set environment variables in a container?](#137-how-do-you-set-environment-variables-in-a-container)
- [138: What is the difference between command and args in a container?](#138-what-is-the-difference-between-command-and-args-in-a-container)
- [139: What is a ResourceQuota?](#139-what-is-a-resourcequota)
- [140: What is a LimitRange?](#140-what-is-a-limitrange)
- [141: What does kubectl cordon do?](#141-what-does-kubectl-cordon-do)
- [142: What does kubectl drain do?](#142-what-does-kubectl-drain-do)
- [143: What is a PodDisruptionBudget?](#143-what-is-a-poddisruptionbudget)
- [144: What is the difference between a voluntary and an involuntary disruption?](#144-what-is-the-difference-between-a-voluntary-and-an-involuntary-disruption)
- [145: What is a static Pod?](#145-what-is-a-static-pod)
- [146: What is kubeadm?](#146-what-is-kubeadm)
- [147: What is the difference between Docker and Kubernetes?](#147-what-is-the-difference-between-docker-and-kubernetes)
- [148: What are finalizers?](#148-what-are-finalizers)
- [149: What is the kubectl diff command?](#149-what-is-the-kubectl-diff-command)
- [150: What is the release cycle of Kubernetes?](#150-what-is-the-release-cycle-of-kubernetes)

### Moderate Questions (151-300)

- [151: What does a production-ready Deployment manifest look like?](#151-what-does-a-production-ready-deployment-manifest-look-like)
- [152: How do you choose good requests and limits?](#152-how-do-you-choose-good-requests-and-limits)
- [153: Should you set CPU limits?](#153-should-you-set-cpu-limits)
- [154: How do you pick maxSurge and maxUnavailable?](#154-how-do-you-pick-maxsurge-and-maxunavailable)
- [155: What do minReadySeconds and progressDeadlineSeconds do?](#155-what-do-minreadyseconds-and-progressdeadlineseconds-do)
- [156: How does Pod termination work?](#156-how-does-pod-termination-work)
- [157: Why do some requests fail during a rolling update even with readiness probes?](#157-why-do-some-requests-fail-during-a-rolling-update-even-with-readiness-probes)
- [158: What is a postStart hook?](#158-what-is-a-poststart-hook)
- [159: How do you do a blue-green deployment in Kubernetes?](#159-how-do-you-do-a-blue-green-deployment-in-kubernetes)
- [160: How do you do a canary deployment?](#160-how-do-you-do-a-canary-deployment)
- [161: What are Argo Rollouts and Flagger?](#161-what-are-argo-rollouts-and-flagger)
- [162: How do you make Pods pick up a changed ConfigMap?](#162-how-do-you-make-pods-pick-up-a-changed-configmap)
- [163: What is the problem with subPath mounts?](#163-what-is-the-problem-with-subpath-mounts)
- [164: What are immutable ConfigMaps and Secrets?](#164-what-are-immutable-configmaps-and-secrets)
- [165: What is a projected volume?](#165-what-is-a-projected-volume)
- [166: How do you manage secrets without storing them in Git as plain text?](#166-how-do-you-manage-secrets-without-storing-them-in-git-as-plain-text)
- [167: How do you enable encryption at rest for Secrets?](#167-how-do-you-enable-encryption-at-rest-for-secrets)
- [168: Which probe settings can you tune?](#168-which-probe-settings-can-you-tune)
- [169: A Pod is stuck in Pending. How do you debug it?](#169-a-pod-is-stuck-in-pending-how-do-you-debug-it)
- [170: A Service is not reachable. How do you troubleshoot it?](#170-a-service-is-not-reachable-how-do-you-troubleshoot-it)
- [171: What is kubectl debug and ephemeral containers?](#171-what-is-kubectl-debug-and-ephemeral-containers)
- [172: How do you debug a node with kubectl?](#172-how-do-you-debug-a-node-with-kubectl)
- [173: How do you debug DNS problems in a cluster?](#173-how-do-you-debug-dns-problems-in-a-cluster)
- [174: What is ndots and why does it matter for DNS performance?](#174-what-is-ndots-and-why-does-it-matter-for-dns-performance)
- [175: What are the Pod dnsPolicy options?](#175-what-are-the-pod-dnspolicy-options)
- [176: How do you get HTTPS certificates for Ingress automatically?](#176-how-do-you-get-https-certificates-for-ingress-automatically)
- [177: What are the Ingress path types?](#177-what-are-the-ingress-path-types)
- [178: What is an IngressClass?](#178-what-is-an-ingressclass)
- [179: How do you route HTTP traffic with the Gateway API?](#179-how-do-you-route-http-traffic-with-the-gateway-api)
- [180: How do you split traffic between two versions with the Gateway API?](#180-how-do-you-split-traffic-between-two-versions-with-the-gateway-api)
- [181: What is a ReferenceGrant?](#181-what-is-a-referencegrant)
- [182: How would you migrate off the retired ingress-nginx controller?](#182-how-would-you-migrate-off-the-retired-ingress-nginx-controller)
- [183: What is externalTrafficPolicy?](#183-what-is-externaltrafficpolicy)
- [184: What is sessionAffinity on a Service?](#184-what-is-sessionaffinity-on-a-service)
- [185: How can you keep Service traffic inside the same zone?](#185-how-can-you-keep-service-traffic-inside-the-same-zone)
- [186: What are topology spread constraints?](#186-what-are-topology-spread-constraints)
- [187: What is a PriorityClass?](#187-what-is-a-priorityclass)
- [188: How do you block all traffic by default with NetworkPolicy?](#188-how-do-you-block-all-traffic-by-default-with-networkpolicy)
- [189: Why do Pods lose DNS after a default-deny egress policy, and how do you fix it?](#189-why-do-pods-lose-dns-after-a-default-deny-egress-policy-and-how-do-you-fix-it)
- [190: How do you allow traffic from another namespace in a NetworkPolicy?](#190-how-do-you-allow-traffic-from-another-namespace-in-a-networkpolicy)
- [191: What are the Pod Security Standards?](#191-what-are-the-pod-security-standards)
- [192: How do you enforce Pod Security Standards?](#192-how-do-you-enforce-pod-security-standards)
- [193: What securityContext settings should most containers have?](#193-what-securitycontext-settings-should-most-containers-have)
- [194: Why use readOnlyRootFilesystem?](#194-why-use-readonlyrootfilesystem)
- [195: What are Linux capabilities in a Pod spec?](#195-what-are-linux-capabilities-in-a-pod-spec)
- [196: What does seccompProfile RuntimeDefault do?](#196-what-does-seccompprofile-runtimedefault-do)
- [197: Why disable automountServiceAccountToken?](#197-why-disable-automountserviceaccounttoken)
- [198: How are ServiceAccount tokens issued today?](#198-how-are-serviceaccount-tokens-issued-today)
- [199: How do Pods get access to cloud services without static keys?](#199-how-do-pods-get-access-to-cloud-services-without-static-keys)
- [200: What are the default user-facing ClusterRoles?](#200-what-are-the-default-user-facing-clusterroles)
- [201: What does a Helm chart look like?](#201-what-does-a-helm-chart-look-like)
- [202: How does templating work in Helm?](#202-how-does-templating-work-in-helm)
- [203: What are Helm hooks?](#203-what-are-helm-hooks)
- [204: How do you check a Helm chart before installing it?](#204-how-do-you-check-a-helm-chart-before-installing-it)
- [205: When would you pick Helm over Kustomize?](#205-when-would-you-pick-helm-over-kustomize)
- [206: What does configMapGenerator do in Kustomize?](#206-what-does-configmapgenerator-do-in-kustomize)
- [207: What is GitOps?](#207-what-is-gitops)
- [208: What is Argo CD?](#208-what-is-argo-cd)
- [209: What is Flux?](#209-what-is-flux)
- [210: How do you manage several environments like dev, staging and prod?](#210-how-do-you-manage-several-environments-like-dev-staging-and-prod)
- [211: What does a typical CI/CD pipeline for Kubernetes look like?](#211-what-does-a-typical-cicd-pipeline-for-kubernetes-look-like)
- [212: How do volumeClaimTemplates work in a StatefulSet?](#212-how-do-volumeclaimtemplates-work-in-a-statefulset)
- [213: How do StatefulSet updates work?](#213-how-do-statefulset-updates-work)
- [214: What is podManagementPolicy in a StatefulSet?](#214-what-is-podmanagementpolicy-in-a-statefulset)
- [215: Should you run databases on Kubernetes?](#215-should-you-run-databases-on-kubernetes)
- [216: What is an Operator?](#216-what-is-an-operator)
- [217: What is a CustomResourceDefinition?](#217-what-is-a-customresourcedefinition)
- [218: How do you make a PersistentVolumeClaim bigger?](#218-how-do-you-make-a-persistentvolumeclaim-bigger)
- [219: What are VolumeSnapshots?](#219-what-are-volumesnapshots)
- [220: What is volumeBindingMode WaitForFirstConsumer?](#220-what-is-volumebindingmode-waitforfirstconsumer)
- [221: What are PV reclaim policies?](#221-what-are-pv-reclaim-policies)
- [222: A PVC is stuck in Pending. What do you check?](#222-a-pvc-is-stuck-in-pending-what-do-you-check)
- [223: How do parallelism and completions work in a Job?](#223-how-do-parallelism-and-completions-work-in-a-job)
- [224: How do you clean up finished Jobs and stop Jobs that run too long?](#224-how-do-you-clean-up-finished-jobs-and-stop-jobs-that-run-too-long)
- [225: What is a Pod failure policy in a Job?](#225-what-is-a-pod-failure-policy-in-a-job)
- [226: Which CronJob settings matter in practice?](#226-which-cronjob-settings-matter-in-practice)
- [227: How do you pause a Job or CronJob?](#227-how-do-you-pause-a-job-or-cronjob)
- [228: How do you stop an HPA from scaling up and down too often?](#228-how-do-you-stop-an-hpa-from-scaling-up-and-down-too-often)
- [229: How do you scale on custom metrics like requests per second?](#229-how-do-you-scale-on-custom-metrics-like-requests-per-second)
- [230: What is KEDA?](#230-what-is-keda)
- [231: What is the VerticalPodAutoscaler?](#231-what-is-the-verticalpodautoscaler)
- [232: What is in-place Pod resize?](#232-what-is-in-place-pod-resize)
- [233: Can you use HPA and VPA on the same workload?](#233-can-you-use-hpa-and-vpa-on-the-same-workload)
- [234: What is the difference between Cluster Autoscaler and Karpenter?](#234-what-is-the-difference-between-cluster-autoscaler-and-karpenter)
- [235: How do you monitor a Kubernetes cluster?](#235-how-do-you-monitor-a-kubernetes-cluster)
- [236: What is a ServiceMonitor?](#236-what-is-a-servicemonitor)
- [237: How does logging work in Kubernetes?](#237-how-does-logging-work-in-kubernetes)
- [238: What is the difference between metrics-server and kube-state-metrics?](#238-what-is-the-difference-between-metrics-server-and-kube-state-metrics)
- [239: How do you add distributed tracing to apps on Kubernetes?](#239-how-do-you-add-distributed-tracing-to-apps-on-kubernetes)
- [240: Which alerts should every cluster have?](#240-which-alerts-should-every-cluster-have)
- [241: What is node-pressure eviction?](#241-what-is-node-pressure-eviction)
- [242: What is node allocatable?](#242-what-is-node-allocatable)
- [243: What is ephemeral storage and why should you set it?](#243-what-is-ephemeral-storage-and-why-should-you-set-it)
- [244: What are the recommended labels for Kubernetes objects?](#244-what-are-the-recommended-labels-for-kubernetes-objects)
- [245: What are field selectors?](#245-what-are-field-selectors)
- [246: What are the kinds of kubectl patch?](#246-what-are-the-kinds-of-kubectl-patch)
- [247: What is server-side apply?](#247-what-is-server-side-apply)
- [248: How do you wait for something in a script?](#248-how-do-you-wait-for-something-in-a-script)
- [249: How do you find the Pods using the most memory or restarting the most?](#249-how-do-you-find-the-pods-using-the-most-memory-or-restarting-the-most)
- [250: What are kubectl plugins and krew?](#250-what-are-kubectl-plugins-and-krew)
- [251: What is the .kuberc file?](#251-what-is-the-kuberc-file)
- [252: How do you work with many clusters from one machine?](#252-how-do-you-work-with-many-clusters-from-one-machine)
- [253: How would you organize namespaces for several teams?](#253-how-would-you-organize-namespaces-for-several-teams)
- [254: What is multi-tenancy in Kubernetes and what are its limits?](#254-what-is-multi-tenancy-in-kubernetes-and-what-are-its-limits)
- [255: How do you reduce the cost of a Kubernetes cluster?](#255-how-do-you-reduce-the-cost-of-a-kubernetes-cluster)
- [256: How do you run workloads on spot instances safely?](#256-how-do-you-run-workloads-on-spot-instances-safely)
- [257: What are node pools and why use several?](#257-what-are-node-pools-and-why-use-several)
- [258: How do Pods use GPUs?](#258-how-do-pods-use-gpus)
- [259: Can Kubernetes run Windows containers?](#259-can-kubernetes-run-windows-containers)
- [260: What is a service mesh?](#260-what-is-a-service-mesh)
- [261: What is the difference between sidecar mode and ambient mode in Istio?](#261-what-is-the-difference-between-sidecar-mode-and-ambient-mode-in-istio)
- [262: How do you get mutual TLS between services?](#262-how-do-you-get-mutual-tls-between-services)
- [263: How should an app design its health endpoints for Kubernetes?](#263-how-should-an-app-design-its-health-endpoints-for-kubernetes)
- [264: How does the twelve-factor app approach fit Kubernetes?](#264-how-does-the-twelve-factor-app-approach-fit-kubernetes)
- [265: How do you run database migrations when deploying to Kubernetes?](#265-how-do-you-run-database-migrations-when-deploying-to-kubernetes)
- [266: What tools help with local development on Kubernetes?](#266-what-tools-help-with-local-development-on-kubernetes)
- [267: How do you validate manifests in CI?](#267-how-do-you-validate-manifests-in-ci)
- [268: What are Kyverno and OPA Gatekeeper?](#268-what-are-kyverno-and-opa-gatekeeper)
- [269: What are ValidatingAdmissionPolicy and MutatingAdmissionPolicy?](#269-what-are-validatingadmissionpolicy-and-mutatingadmissionpolicy)
- [270: How does garbage collection with owner references work?](#270-how-does-garbage-collection-with-owner-references-work)
- [271: A Pod is stuck in Terminating. What do you do?](#271-a-pod-is-stuck-in-terminating-what-do-you-do)
- [272: A namespace is stuck in Terminating. Why?](#272-a-namespace-is-stuck-in-terminating-why)
- [273: What do common container exit codes mean?](#273-what-do-common-container-exit-codes-mean)
- [274: What happens to evicted Pods and how do you clean them up?](#274-what-happens-to-evicted-pods-and-how-do-you-clean-them-up)
- [275: What is an image volume?](#275-what-is-an-image-volume)
- [276: What are Pod readiness gates?](#276-what-are-pod-readiness-gates)
- [277: What are hostNetwork and hostPort, and when should you use them?](#277-what-are-hostnetwork-and-hostport-and-when-should-you-use-them)
- [278: Should you pass secrets as environment variables or files?](#278-should-you-pass-secrets-as-environment-variables-or-files)
- [279: How do you handle user uploads in an app with many replicas?](#279-how-do-you-handle-user-uploads-in-an-app-with-many-replicas)
- [280: How do you back up a Kubernetes cluster?](#280-how-do-you-back-up-a-kubernetes-cluster)
- [281: How do you upgrade a Kubernetes cluster?](#281-how-do-you-upgrade-a-kubernetes-cluster)
- [282: How do you find manifests that use deprecated or removed APIs?](#282-how-do-you-find-manifests-that-use-deprecated-or-removed-apis)
- [283: How do DaemonSet updates work?](#283-how-do-daemonset-updates-work)
- [284: How can your own app do leader election on Kubernetes?](#284-how-can-your-own-app-do-leader-election-on-kubernetes)
- [285: How do you find node-level problems like a broken disk or kernel issue?](#285-how-do-you-find-node-level-problems-like-a-broken-disk-or-kernel-issue)
- [286: How do you expose a non-HTTP service like a database or MQTT broker?](#286-how-do-you-expose-a-non-http-service-like-a-database-or-mqtt-broker)
- [287: How do hostname and subdomain work for Pods?](#287-how-do-hostname-and-subdomain-work-for-pods)
- [288: In what order do init containers, sidecars and app containers start and stop?](#288-in-what-order-do-init-containers-sidecars-and-app-containers-start-and-stop)
- [289: How do you size memory for a JVM or Node.js app in a container?](#289-how-do-you-size-memory-for-a-jvm-or-nodejs-app-in-a-container)
- [290: How do you give an outside service a name inside the cluster?](#290-how-do-you-give-an-outside-service-a-name-inside-the-cluster)
- [291: What is the difference between client and server dry run?](#291-what-is-the-difference-between-client-and-server-dry-run)
- [292: How do you delete objects that you removed from your manifests?](#292-how-do-you-delete-objects-that-you-removed-from-your-manifests)
- [293: What is the difference between mutating and validating admission webhooks?](#293-what-is-the-difference-between-mutating-and-validating-admission-webhooks)
- [294: How do you allow only images from trusted registries?](#294-how-do-you-allow-only-images-from-trusted-registries)
- [295: How do you run batch Jobs on separate nodes from your web apps?](#295-how-do-you-run-batch-jobs-on-separate-nodes-from-your-web-apps)
- [296: When do you need more than one cluster?](#296-when-do-you-need-more-than-one-cluster)
- [297: How do you find out who changed or deleted something in the cluster?](#297-how-do-you-find-out-who-changed-or-deleted-something-in-the-cluster)
- [298: What is the Kubernetes API deprecation policy?](#298-what-is-the-kubernetes-api-deprecation-policy)
- [299: How do you control outgoing traffic from Pods to the internet?](#299-how-do-you-control-outgoing-traffic-from-pods-to-the-internet)
- [300: How are certificates handled inside a cluster and how do you rotate them?](#300-how-are-certificates-handled-inside-a-cluster-and-how-do-you-rotate-them)

### Advanced Questions (301-450)

- [301: What happens step by step when you run kubectl apply on a new Deployment?](#301-what-happens-step-by-step-when-you-run-kubectl-apply-on-a-new-deployment)
- [302: What does it mean that Kubernetes controllers are level-triggered?](#302-what-does-it-mean-that-kubernetes-controllers-are-level-triggered)
- [303: What are informers and why do controllers use them?](#303-what-are-informers-and-why-do-controllers-use-them)
- [304: What is resourceVersion and how does Kubernetes handle concurrent updates?](#304-what-is-resourceversion-and-how-does-kubernetes-handle-concurrent-updates)
- [305: How does the API server serve reads and watches efficiently?](#305-how-does-the-api-server-serve-reads-and-watches-efficiently)
- [306: How does the API server handle a request?](#306-how-does-the-api-server-handle-a-request)
- [307: How do users authenticate to Kubernetes?](#307-how-do-users-authenticate-to-kubernetes)
- [308: What authorization modes does Kubernetes have?](#308-what-authorization-modes-does-kubernetes-have)
- [309: What are the Node authorizer and NodeRestriction admission plugin?](#309-what-are-the-node-authorizer-and-noderestriction-admission-plugin)
- [310: How does etcd stay consistent?](#310-how-does-etcd-stay-consistent)
- [311: What affects etcd performance?](#311-what-affects-etcd-performance)
- [312: How do you back up and restore etcd?](#312-how-do-you-back-up-and-restore-etcd)
- [313: How do you design a highly available control plane?](#313-how-do-you-design-a-highly-available-control-plane)
- [314: How does the scheduler framework work?](#314-how-does-the-scheduler-framework-work)
- [315: How do you change how the scheduler places Pods?](#315-how-do-you-change-how-the-scheduler-places-pods)
- [316: How does preemption work in detail?](#316-how-does-preemption-work-in-detail)
- [317: What is gang scheduling and how does Kubernetes support it?](#317-what-is-gang-scheduling-and-how-does-kubernetes-support-it)
- [318: What is Dynamic Resource Allocation?](#318-what-is-dynamic-resource-allocation)
- [319: How does the kubelet manage Pods internally?](#319-how-does-the-kubelet-manage-pods-internally)
- [320: How do the kubelet, containerd and runc fit together?](#320-how-do-the-kubelet-containerd-and-runc-fit-together)
- [321: How do requests and limits map to cgroups v2?](#321-how-do-requests-and-limits-map-to-cgroups-v2)
- [322: What is the status of cgroup v1 in Kubernetes?](#322-what-is-the-status-of-cgroup-v1-in-kubernetes)
- [323: What are the CPU manager and Topology manager?](#323-what-are-the-cpu-manager-and-topology-manager)
- [324: What are PSI metrics and why are they useful?](#324-what-are-psi-metrics-and-why-are-they-useful)
- [325: Does Kubernetes support swap?](#325-does-kubernetes-support-swap)
- [326: What are user namespaces in Pods?](#326-what-are-user-namespaces-in-pods)
- [327: What kube-proxy modes are there today?](#327-what-kube-proxy-modes-are-there-today)
- [328: How does a packet to a ClusterIP Service reach a Pod?](#328-how-does-a-packet-to-a-clusterip-service-reach-a-pod)
- [329: How does an eBPF dataplane like Cilium replace kube-proxy?](#329-how-does-an-ebpf-dataplane-like-cilium-replace-kube-proxy)
- [330: What is the difference between overlay and routed Pod networking?](#330-what-is-the-difference-between-overlay-and-routed-pod-networking)
- [331: What conntrack problems can you hit in Kubernetes?](#331-what-conntrack-problems-can-you-hit-in-kubernetes)
- [332: What is NodeLocal DNSCache?](#332-what-is-nodelocal-dnscache)
- [333: How does dual-stack networking work in Kubernetes?](#333-how-does-dual-stack-networking-work-in-kubernetes)
- [334: How can you grow the Service IP range of a running cluster?](#334-how-can-you-grow-the-service-ip-range-of-a-running-cluster)
- [335: Why is Service externalIPs being deprecated?](#335-why-is-service-externalips-being-deprecated)
- [336: Which RBAC permissions are dangerous even if they look harmless?](#336-which-rbac-permissions-are-dangerous-even-if-they-look-harmless)
- [337: How do you protect the kubelet API?](#337-how-do-you-protect-the-kubelet-api)
- [338: Why is the cloud metadata endpoint a risk and how do you protect it?](#338-why-is-the-cloud-metadata-endpoint-a-risk-and-how-do-you-protect-it)
- [339: How do you secure the software supply chain for Kubernetes workloads?](#339-how-do-you-secure-the-software-supply-chain-for-kubernetes-workloads)
- [340: How do you detect attacks at runtime in a cluster?](#340-how-do-you-detect-attacks-at-runtime-in-a-cluster)
- [341: What is a RuntimeClass and when do you use a sandboxed runtime?](#341-what-is-a-runtimeclass-and-when-do-you-use-a-sandboxed-runtime)
- [342: How does KMS v2 encryption work for Secrets?](#342-how-does-kms-v2-encryption-work-for-secrets)
- [343: What are Pod Certificates and ClusterTrustBundles?](#343-what-are-pod-certificates-and-clustertrustbundles)
- [344: What is external signing of ServiceAccount tokens?](#344-what-is-external-signing-of-serviceaccount-tokens)
- [345: How do you check a cluster against security best practices?](#345-how-do-you-check-a-cluster-against-security-best-practices)
- [346: Should the API server be reachable from the internet?](#346-should-the-api-server-be-reachable-from-the-internet)
- [347: What are the limits of standard NetworkPolicy?](#347-what-are-the-limits-of-standard-networkpolicy)
- [348: How does a well-written controller's reconcile loop look?](#348-how-does-a-well-written-controllers-reconcile-loop-look)
- [349: Why do controllers use finalizers?](#349-why-do-controllers-use-finalizers)
- [350: How should a custom resource report its status?](#350-how-should-a-custom-resource-report-its-status)
- [351: How do you version a CRD and change its schema over time?](#351-how-do-you-version-a-crd-and-change-its-schema-over-time)
- [352: How do you validate custom resources with CEL?](#352-how-do-you-validate-custom-resources-with-cel)
- [353: What is storage version migration?](#353-what-is-storage-version-migration)
- [354: When would you use an aggregated API server instead of a CRD?](#354-when-would-you-use-an-aggregated-api-server-instead-of-a-crd)
- [355: What is API Priority and Fairness?](#355-what-is-api-priority-and-fairness)
- [356: What are the scalability limits of a single Kubernetes cluster?](#356-what-are-the-scalability-limits-of-a-single-kubernetes-cluster)
- [357: Why are large LIST requests a problem and how do clients avoid them?](#357-why-are-large-list-requests-a-problem-and-how-do-clients-avoid-them)
- [358: How can you make Pods start faster?](#358-how-can-you-make-pods-start-faster)
- [359: How do you make autoscaling react faster when new nodes take minutes to start?](#359-how-do-you-make-autoscaling-react-faster-when-new-nodes-take-minutes-to-start)
- [360: How does the HPA calculate the number of replicas?](#360-how-does-the-hpa-calculate-the-number-of-replicas)
- [361: Can the HPA scale a workload to zero?](#361-can-the-hpa-scale-a-workload-to-zero)
- [362: How do you detect and fix CPU throttling?](#362-how-do-you-detect-and-fix-cpu-throttling)
- [363: How do you deal with noisy neighbors on shared nodes?](#363-how-do-you-deal-with-noisy-neighbors-on-shared-nodes)
- [364: How do you design an app on Kubernetes to survive the loss of a zone?](#364-how-do-you-design-an-app-on-kubernetes-to-survive-the-loss-of-a-zone)
- [365: How would you set up disaster recovery across regions?](#365-how-would-you-set-up-disaster-recovery-across-regions)
- [366: How do you run a stateful clustered system like Kafka or etcd safely on Kubernetes?](#366-how-do-you-run-a-stateful-clustered-system-like-kafka-or-etcd-safely-on-kubernetes)
- [367: A StatefulSet rollout is stuck after a bad update. Why, and how do you fix it?](#367-a-statefulset-rollout-is-stuck-after-a-bad-update-why-and-how-do-you-fix-it)
- [368: What happens to Pods when a node shuts down or dies?](#368-what-happens-to-pods-when-a-node-shuts-down-or-dies)
- [369: How does CSI work?](#369-how-does-csi-work)
- [370: What does a Multi-Attach error mean?](#370-what-does-a-multi-attach-error-mean)
- [371: When would you use local persistent volumes?](#371-when-would-you-use-local-persistent-volumes)
- [372: Your API has latency spikes every few minutes. What might cause it in Kubernetes?](#372-your-api-has-latency-spikes-every-few-minutes-what-might-cause-it-in-kubernetes)
- [373: Users get 502 errors during every deployment. How do you fix it?](#373-users-get-502-errors-during-every-deployment-how-do-you-fix-it)
- [374: A node shows NotReady. How do you investigate?](#374-a-node-shows-notready-how-do-you-investigate)
- [375: A container is OOMKilled but its memory graph never reached the limit. Why?](#375-a-container-is-oomkilled-but-its-memory-graph-never-reached-the-limit-why)
- [376: Pods are stuck in ContainerCreating. What do you check?](#376-pods-are-stuck-in-containercreating-what-do-you-check)
- [377: kubectl commands are slow and the API server is under heavy load. What do you do?](#377-kubectl-commands-are-slow-and-the-api-server-is-under-heavy-load-what-do-you-do)
- [378: Your EKS cluster ran out of Pod IP addresses. What are your options?](#378-your-eks-cluster-ran-out-of-pod-ip-addresses-what-are-your-options)
- [379: etcd reports "mvcc: database space exceeded". What happened and how do you fix it?](#379-etcd-reports-mvcc-database-space-exceeded-what-happened-and-how-do-you-fix-it)
- [380: A broken admission webhook blocked deployments across the cluster. How do you prevent this?](#380-a-broken-admission-webhook-blocked-deployments-across-the-cluster-how-do-you-prevent-this)
- [381: A Secret was committed to a public Git repository. What do you do?](#381-a-secret-was-committed-to-a-public-git-repository-what-do-you-do)
- [382: A Deployment rollout is stuck halfway. How do you debug it?](#382-a-deployment-rollout-is-stuck-halfway-how-do-you-debug-it)
- [383: Load is uneven across Pods even though the Service balances it. Why?](#383-load-is-uneven-across-pods-even-though-the-service-balances-it-why)
- [384: How do you load balance gRPC traffic in Kubernetes?](#384-how-do-you-load-balance-grpc-traffic-in-kubernetes)
- [385: How do you handle WebSockets and other long-lived connections during deploys?](#385-how-do-you-handle-websockets-and-other-long-lived-connections-during-deploys)
- [386: What is your checklist for zero-downtime deployments on Kubernetes?](#386-what-is-your-checklist-for-zero-downtime-deployments-on-kubernetes)
- [387: How would you build an internal developer platform on top of Kubernetes?](#387-how-would-you-build-an-internal-developer-platform-on-top-of-kubernetes)
- [388: How would you design a cluster setup for 200 microservices and 20 teams?](#388-how-would-you-design-a-cluster-setup-for-200-microservices-and-20-teams)
- [389: What is Cluster API?](#389-what-is-cluster-api)
- [390: How do you manage clusters as code?](#390-how-do-you-manage-clusters-as-code)
- [391: What is Crossplane?](#391-what-is-crossplane)
- [392: How do you enforce governance in large clusters without slowing teams down?](#392-how-do-you-enforce-governance-in-large-clusters-without-slowing-teams-down)
- [393: How do you split cluster costs between teams?](#393-how-do-you-split-cluster-costs-between-teams)
- [394: How do you run LLM inference workloads on Kubernetes?](#394-how-do-you-run-llm-inference-workloads-on-kubernetes)
- [395: How do you run batch and HPC workloads on Kubernetes?](#395-how-do-you-run-batch-and-hpc-workloads-on-kubernetes)
- [396: How do you run Kubernetes at the edge?](#396-how-do-you-run-kubernetes-at-the-edge)
- [397: How do you upgrade many clusters safely?](#397-how-do-you-upgrade-many-clusters-safely)
- [398: What is the Kubernetes version skew policy?](#398-what-is-the-kubernetes-version-skew-policy)
- [399: What are feature gates?](#399-what-are-feature-gates)
- [400: What is the mixed version proxy?](#400-what-is-the-mixed-version-proxy)
- [401: What is KYAML?](#401-what-is-kyaml)
- [402: Which control plane metrics would you watch?](#402-which-control-plane-metrics-would-you-watch)
- [403: How would you define SLOs for a Kubernetes platform?](#403-how-would-you-define-slos-for-a-kubernetes-platform)
- [404: How do you test that your setup really survives failures?](#404-how-do-you-test-that-your-setup-really-survives-failures)
- [405: What are Pod-level resources?](#405-what-are-pod-level-resources)
- [406: Why did sidecars used to break Jobs, and how do native sidecars fix it?](#406-why-did-sidecars-used-to-break-jobs-and-how-do-native-sidecars-fix-it)
- [407: What are the security risks of ephemeral debug containers?](#407-what-are-the-security-risks-of-ephemeral-debug-containers)
- [408: How do nodes get credentials for private registries without imagePullSecrets?](#408-how-do-nodes-get-credentials-for-private-registries-without-imagepullsecrets)
- [409: What are Pod scheduling gates?](#409-what-are-pod-scheduling-gates)
- [410: What is the descheduler?](#410-what-is-the-descheduler)
- [411: How do you use huge pages in Kubernetes?](#411-how-do-you-use-huge-pages-in-kubernetes)
- [412: How can you change how quickly Pods are evicted from a failed node?](#412-how-can-you-change-how-quickly-pods-are-evicted-from-a-failed-node)
- [413: Why does a Pod with a large volume take minutes to start, and how do you fix it?](#413-why-does-a-pod-with-a-large-volume-take-minutes-to-start-and-how-do-you-fix-it)
- [414: How does Kubernetes avoid slow SELinux relabeling of volumes?](#414-how-does-kubernetes-avoid-slow-selinux-relabeling-of-volumes)
- [415: How do Secrets get from the API server to a container?](#415-how-do-secrets-get-from-the-api-server-to-a-container)
- [416: How can a PodDisruptionBudget block node drains, and how do you avoid it?](#416-how-can-a-poddisruptionbudget-block-node-drains-and-how-do-you-avoid-it)
- [417: How do you roll out config changes as safely as code changes?](#417-how-do-you-roll-out-config-changes-as-safely-as-code-changes)
- [418: How do you protect services from traffic spikes at the edge?](#418-how-do-you-protect-services-from-traffic-spikes-at-the-edge)
- [419: How do you protect long-running jobs from node drains and scale-downs?](#419-how-do-you-protect-long-running-jobs-from-node-drains-and-scale-downs)
- [420: Why does the HPA keep fighting with your GitOps tool over replicas?](#420-why-does-the-hpa-keep-fighting-with-your-gitops-tool-over-replicas)
- [421: Why does Argo CD show resources as out of sync even right after a sync?](#421-why-does-argo-cd-show-resources-as-out-of-sync-even-right-after-a-sync)
- [422: What are the limits of Helm at scale?](#422-what-are-the-limits-of-helm-at-scale)
- [423: How do you rotate a database password with no downtime?](#423-how-do-you-rotate-a-database-password-with-no-downtime)
- [424: What happens to the database when you scale an app to 100 Pods?](#424-what-happens-to-the-database-when-you-scale-an-app-to-100-pods)
- [425: What are SPIFFE and SPIRE?](#425-what-are-spiffe-and-spire)
- [426: How do you meet compliance rules like PCI DSS on Kubernetes?](#426-how-do-you-meet-compliance-rules-like-pci-dss-on-kubernetes)
- [427: How do you test that a cluster works correctly after changes?](#427-how-do-you-test-that-a-cluster-works-correctly-after-changes)
- [428: When is Kubernetes the wrong choice?](#428-when-is-kubernetes-the-wrong-choice)
- [429: How do you move an app from VMs to Kubernetes?](#429-how-do-you-move-an-app-from-vms-to-kubernetes)
- [430: How do you move workloads to a new cluster with no downtime?](#430-how-do-you-move-workloads-to-a-new-cluster-with-no-downtime)
- [431: How do you fail over traffic between clusters?](#431-how-do-you-fail-over-traffic-between-clusters)
- [432: How would you prepare a Kubernetes app for a big planned traffic event?](#432-how-would-you-prepare-a-kubernetes-app-for-a-big-planned-traffic-event)
- [433: How do you choose a CNI plugin?](#433-how-do-you-choose-a-cni-plugin)
- [434: What are the trade-offs of fully managed node options like GKE Autopilot or EKS Auto Mode?](#434-what-are-the-trade-offs-of-fully-managed-node-options-like-gke-autopilot-or-eks-auto-mode)
- [435: What is the pause container?](#435-what-is-the-pause-container)
- [436: How does the kubelet clean up images and containers?](#436-how-does-the-kubelet-clean-up-images-and-containers)
- [437: How are container logs rotated, and what happens with very chatty apps?](#437-how-are-container-logs-rotated-and-what-happens-with-very-chatty-apps)
- [438: Can a node have more requested resources than it has?](#438-can-a-node-have-more-requested-resources-than-it-has)
- [439: How do you test a Kubernetes controller?](#439-how-do-you-test-a-kubernetes-controller)
- [440: How does a program talk to the Kubernetes API from inside a Pod?](#440-how-does-a-program-talk-to-the-kubernetes-api-from-inside-a-pod)
- [441: When are Kubernetes Secrets not enough?](#441-when-are-kubernetes-secrets-not-enough)
- [442: How does the kubelet decide which process the OOM killer kills?](#442-how-does-the-kubelet-decide-which-process-the-oom-killer-kills)
- [443: How do you keep Kubernetes events longer than an hour?](#443-how-do-you-keep-kubernetes-events-longer-than-an-hour)
- [444: How do you find out which NetworkPolicy is dropping traffic?](#444-how-do-you-find-out-which-networkpolicy-is-dropping-traffic)
- [445: How do you profile an app running in a Kubernetes Pod?](#445-how-do-you-profile-an-app-running-in-a-kubernetes-pod)
- [446: How do you manage the versions of cluster add-ons?](#446-how-do-you-manage-the-versions-of-cluster-add-ons)
- [447: When would you run an agent as a sidecar and when as a DaemonSet?](#447-when-would-you-run-an-agent-as-a-sidecar-and-when-as-a-daemonset)
- [448: How should a CI system get access to deploy to a cluster?](#448-how-should-a-ci-system-get-access-to-deploy-to-a-cluster)
- [449: Walk through deploying a new service to production on Kubernetes.](#449-walk-through-deploying-a-new-service-to-production-on-kubernetes)
- [450: What changed in Kubernetes recently that you should know about?](#450-what-changed-in-kubernetes-recently-that-you-should-know-about)

---

# Easy Questions (1-150)

## 1: What is Kubernetes?

Kubernetes (often written K8s) is an open source system for running containers on a group of machines. You tell it what you want to run, for example "three copies of this image, reachable on port 80", and it starts the containers, places them on machines, restarts them when they crash and spreads traffic between them.

It was started at Google, based on their internal system Borg, and is now maintained by the Cloud Native Computing Foundation (CNCF).

## 2: What problems does Kubernetes solve?

Running one container on one server is easy. Running hundreds of containers on dozens of servers is not. Kubernetes handles the hard parts for you:

- Deciding which server each container runs on
- Restarting containers that crash and moving them off dead servers
- Giving containers stable network names and load balancing between them
- Rolling out new versions without downtime and rolling back when something breaks
- Scaling up and down based on load
- Handing config and secrets to containers

## 3: What does the name K8s mean?

It is a short form of "Kubernetes". The 8 stands for the eight letters between the K and the s. The word Kubernetes comes from Greek and means helmsman or pilot, which is why the logo is a ship's wheel.

## 4: What is a cluster?

A cluster is a set of machines that run Kubernetes together. It has two parts:

- The control plane, which stores the state of the cluster and makes decisions
- Worker nodes, which actually run your containers

When you use `kubectl`, you talk to the control plane, and it makes the nodes do the work.

## 5: What is a node?

A node is one machine in the cluster, either a virtual machine or a physical server. Each worker node runs a few things:

- The kubelet, which starts and watches containers on that node
- A container runtime such as containerd or CRI-O
- kube-proxy (or a replacement from the network plugin) for Service networking

```bash
kubectl get nodes
kubectl describe node worker-1
```

## 6: What is a Pod?

A Pod is the smallest thing you can deploy in Kubernetes. It is a wrapper around one or more containers that share the same network (one IP address, one set of ports) and can share volumes.

Most Pods have just one main container. You add more containers to the same Pod only when they really need to live together, like a log shipper next to the app.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web
spec:
  containers:
    - name: nginx
      image: nginx:1.29
      ports:
        - containerPort: 80
```

## 7: Why does Kubernetes use Pods instead of running containers directly?

A Pod gives Kubernetes a unit that can hold several tightly coupled containers. They share an IP address, can talk over `localhost`, share volumes and are always scheduled on the same node together.

It also gives a stable place to attach things like the network namespace, volumes and security settings, no matter how many containers are inside or how often they restart.

## 8: What is the control plane?

The control plane is the brain of the cluster. Its main parts are:

- kube-apiserver: the front door, every request goes through it
- etcd: the database that stores all cluster data
- kube-scheduler: picks a node for each new Pod
- kube-controller-manager: runs the control loops that keep the cluster in the wanted state
- cloud-controller-manager: talks to the cloud provider (load balancers, nodes, routes), only on cloud clusters

In managed services like EKS, GKE and AKS, the cloud provider runs the control plane for you.

## 9: What is the kube-apiserver?

It is the only component that talks to etcd directly, and every other component, plus `kubectl`, talks to the API server. It exposes a REST API, checks who you are (authentication), checks what you are allowed to do (authorization), runs admission checks and then saves the object.

You can run several API server instances behind a load balancer for high availability, because the server itself keeps no state.

## 10: What is etcd?

etcd is a distributed key-value store. Kubernetes keeps all of its objects in it: Pods, Deployments, Secrets, ConfigMaps and so on. If you lose etcd and have no backup, you lose the cluster state.

Production clusters usually run three or five etcd members so they can survive the loss of one or two of them.

## 11: What does the kube-scheduler do?

When a new Pod is created, it has no node yet. The scheduler looks at all nodes, filters out the ones that cannot run the Pod (not enough CPU or memory, taints, node selectors and so on), scores the remaining ones and writes the best node name into the Pod. The kubelet on that node then starts the Pod.

The scheduler only decides where a Pod goes. It does not start anything itself.

## 12: What does the kube-controller-manager do?

It runs many controllers in one process. Each controller watches some kind of object and works to make the real state match the wanted state. Examples:

- The Deployment controller creates and updates ReplicaSets
- The ReplicaSet controller creates and deletes Pods to match the replica count
- The Node controller notices nodes that stopped responding
- The Job controller runs Pods until a Job is complete

## 13: What is the kubelet?

The kubelet is an agent that runs on every node. It watches the API server for Pods assigned to its node, asks the container runtime to start the containers, runs health checks and reports Pod and node status back to the API server.

The kubelet does not manage containers that were not created through Kubernetes.

## 14: What is kube-proxy?

kube-proxy runs on each node and makes Services work. When you send traffic to a Service IP, kube-proxy's rules (iptables or nftables) send it to one of the Pods behind that Service.

Some network plugins, like Cilium, can replace kube-proxy completely and do the same job with eBPF.

## 15: What is a container runtime?

It is the software that actually pulls images and runs containers. Kubernetes talks to it through the Container Runtime Interface (CRI). The common runtimes are containerd and CRI-O.

Docker Engine is no longer used directly. The built-in Docker support (dockershim) was removed in Kubernetes 1.24, but images built with Docker still work fine because they are standard OCI images.

## 16: What is kubectl?

`kubectl` is the command line tool for talking to a Kubernetes cluster. You use it to create, read, update and delete objects, look at logs, open a shell in a container and more.

```bash
kubectl get pods
kubectl apply -f deployment.yaml
kubectl logs my-pod
kubectl exec -it my-pod -- sh
```

## 17: What is a kubeconfig file?

It is the file that tells `kubectl` which clusters exist, which user credentials to use and which combination (context) is active. By default it lives at `~/.kube/config`. You can point to another file with the `KUBECONFIG` environment variable or the `--kubeconfig` flag.

```bash
kubectl config view
kubectl config current-context
```

## 18: What is a context in kubectl?

A context is a named combination of a cluster, a user and an optional default namespace. Switching contexts is how you move between clusters, for example from staging to production.

```bash
kubectl config get-contexts
kubectl config use-context prod
kubectl config set-context --current --namespace=payments
```

## 19: What is a manifest?

A manifest is a YAML (or JSON) file that describes a Kubernetes object. Almost every manifest has four top-level fields:

- `apiVersion`: which API group and version, like `apps/v1`
- `kind`: the type of object, like `Deployment`
- `metadata`: name, namespace, labels, annotations
- `spec`: what you want

Kubernetes adds a fifth field, `status`, which shows what actually exists.

## 20: What is the difference between spec and status?

`spec` is what you want. You write it. `status` is what Kubernetes sees right now. Controllers write it.

For example, a Deployment's `spec.replicas` might be 3, while `status.readyReplicas` is 2 because one Pod is still starting. Controllers keep working until status matches spec.

## 21: What is declarative configuration?

You describe the end state you want in files and let Kubernetes figure out how to get there. You run `kubectl apply -f` with the files, and Kubernetes creates, updates or leaves things alone as needed.

The other style is imperative: you run commands like `kubectl create` or `kubectl scale` that say exactly what to do. Imperative is fine for quick tests, declarative is what you use for real systems because the files can live in Git.

## 22: What is the difference between kubectl create and kubectl apply?

`kubectl create` makes a new object and fails if it already exists. `kubectl apply` creates the object if it is missing and updates it if it exists, based on the difference between your file and what is in the cluster.

```bash
kubectl create -f pod.yaml   # fails the second time
kubectl apply -f pod.yaml    # safe to run again and again
```

For files kept in Git, use `apply`.

## 23: What is a Namespace?

A Namespace is a way to split one cluster into separate groups of objects. Names must be unique inside a namespace, but two namespaces can each have a Pod called `web`. Namespaces are also the unit you usually attach permissions, quotas and network rules to.

```bash
kubectl create namespace staging
kubectl get pods -n staging
kubectl get pods -A   # all namespaces
```

## 24: What namespaces exist by default?

- `default`: where objects go if you do not set a namespace
- `kube-system`: system components like CoreDNS and kube-proxy
- `kube-public`: readable by everyone, rarely used
- `kube-node-lease`: holds Lease objects that nodes use as heartbeats

## 25: Are all objects namespaced?

No. Most objects that apps use (Pods, Deployments, Services, ConfigMaps, Secrets) are namespaced. Some objects belong to the whole cluster: Nodes, PersistentVolumes, Namespaces themselves, StorageClasses, ClusterRoles and CustomResourceDefinitions.

```bash
kubectl api-resources --namespaced=true
kubectl api-resources --namespaced=false
```

## 26: What are labels?

Labels are key-value pairs you attach to objects. They are used to group and select objects. A Service finds its Pods by label, a Deployment finds the Pods it owns by label, and you can filter with labels in `kubectl`.

```yaml
metadata:
  labels:
    app: web
    tier: frontend
    env: prod
```

```bash
kubectl get pods -l app=web,env=prod
```

## 27: What is a label selector?

A selector is a query over labels. There are two kinds:

- Equality based: `app=web`, `env!=dev`
- Set based: `env in (prod, staging)`, `tier notin (cache)`, `!canary`

```yaml
selector:
  matchLabels:
    app: web
  matchExpressions:
    - key: env
      operator: In
      values: [prod, staging]
```

## 28: What are annotations and how are they different from labels?

Annotations are also key-value pairs on objects, but they are not used for selecting. They hold extra information for tools and people, such as a build commit, a description or config for an ingress controller. Annotation values can be long and free-form, while label values are short and limited to certain characters.

```yaml
metadata:
  annotations:
    git-commit: "a1b2c3d"
    owner: "team-payments@example.com"
```

## 29: What is a Deployment?

A Deployment runs a set of identical Pods and keeps that number running. It is the standard way to run stateless apps. It also handles rolling updates: when you change the image, it slowly replaces old Pods with new ones.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: nginx:1.29
          ports:
            - containerPort: 80
```

## 30: What is a ReplicaSet?

A ReplicaSet makes sure a set number of Pods with a certain label is running. If one dies, it creates a new one. If there are too many, it deletes some.

You almost never create ReplicaSets yourself. A Deployment creates them, one per version of the Pod template, and switches between them during updates.

## 31: What is the difference between a Deployment and a ReplicaSet?

A ReplicaSet only keeps a number of Pods running. A Deployment manages ReplicaSets on top of that, which gives you rolling updates, rollbacks, rollout history and pausing. When you update a Deployment, it creates a new ReplicaSet and scales the old one down step by step.

## 32: What is a ReplicationController?

It is the older version of a ReplicaSet. It only supports equality-based selectors. It still exists in the API but you should use a Deployment instead. You will mostly see it in very old tutorials.

## 33: How do you scale a Deployment?

Change `replicas` in the manifest and apply it, or use `kubectl scale` for a quick change.

```bash
kubectl scale deployment web --replicas=5
```

If a HorizontalPodAutoscaler manages the Deployment, it will overwrite manual changes, so change the HPA's min and max instead.

## 34: What is a Service?

Pods come and go and their IP addresses change. A Service gives a group of Pods one stable name and IP address and load balances traffic between them. It finds its Pods with a label selector.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 8080
```

Other Pods can now reach the app at `http://web` (same namespace) or `http://web.<namespace>.svc.cluster.local`.

## 35: What types of Services are there?

- `ClusterIP` (default): a virtual IP reachable only inside the cluster
- `NodePort`: opens the same port on every node and sends traffic to the Service
- `LoadBalancer`: asks the cloud provider for an external load balancer
- `ExternalName`: a DNS alias (CNAME) to a name outside the cluster

There is also the headless Service (`clusterIP: None`), which has no virtual IP and returns Pod IPs directly in DNS.

## 36: What is a ClusterIP Service?

It is the default Service type. It gets a virtual IP from the cluster's service range that only works inside the cluster. It is what you use for internal traffic between your services, such as an API talking to a database or a cache.

## 37: What is a NodePort Service?

A NodePort Service opens a port (by default between 30000 and 32767) on every node. Traffic to `<any-node-ip>:<nodePort>` goes to the Service and then to a Pod.

```yaml
spec:
  type: NodePort
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080
```

It is simple but not great for production: odd port numbers, and clients have to know node IPs.

## 38: What is a LoadBalancer Service?

On a cloud cluster, a `LoadBalancer` Service makes the cloud provider create an external load balancer (for example an AWS NLB) that sends traffic to your Pods. The external IP or hostname appears in the Service status.

```bash
kubectl get svc web
# NAME  TYPE           CLUSTER-IP   EXTERNAL-IP     PORT(S)
# web   LoadBalancer   10.96.1.20   203.0.113.10    80:31234/TCP
```

On bare metal you need something like MetalLB to get this behavior.

## 39: What is an ExternalName Service?

It maps a Service name to an outside DNS name. No proxying happens, the cluster DNS just returns a CNAME record.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db
spec:
  type: ExternalName
  externalName: mydb.abc123.eu-west-1.rds.amazonaws.com
```

Your app can then connect to `db` and you can later move the database into the cluster without changing app config.

## 40: What is the difference between port, targetPort and nodePort?

- `port`: the port the Service listens on
- `targetPort`: the port on the Pod that traffic is sent to
- `nodePort`: the port opened on every node (only for NodePort and LoadBalancer types)

If `targetPort` is not set, it defaults to the same value as `port`. `targetPort` can also be the name of a container port, like `http`, which makes it easier to change port numbers later.

## 41: How does service discovery work in Kubernetes?

Mainly through DNS. CoreDNS runs in the cluster and creates a record for every Service: `<service>.<namespace>.svc.cluster.local`. Pods have their DNS set up so they can use the short name `web` inside the same namespace, or `web.other-namespace` across namespaces.

Kubernetes also injects environment variables like `WEB_SERVICE_HOST` for Services that existed when the Pod started, but DNS is the method you should use.

## 42: What is CoreDNS?

CoreDNS is the DNS server that runs inside most Kubernetes clusters. It answers DNS queries for Services and Pods and forwards other queries to upstream DNS servers. It runs as a Deployment in `kube-system`, usually behind a Service called `kube-dns` (the name is kept for compatibility).

The older kube-dns project is deprecated, so new clusters should use CoreDNS.

## 43: What is an Ingress?

An Ingress is a set of HTTP routing rules: send `shop.example.com/api` to the `api` Service, send `/` to the `frontend` Service, use this TLS certificate, and so on. It lets many Services share one external load balancer.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: shop
spec:
  ingressClassName: nginx
  rules:
    - host: shop.example.com
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api
                port:
                  number: 80
```

The Ingress API is stable but frozen. New features go into the Gateway API.

## 44: What is an Ingress controller?

An Ingress object is just rules. Nothing happens until an Ingress controller reads those rules and configures a real proxy. Kubernetes does not ship one, you install it yourself. Examples are Traefik, HAProxy, Contour, and cloud-specific ones like the AWS Load Balancer Controller.

The community ingress-nginx controller was retired in March 2026 and no longer gets security fixes, so new setups should pick another controller or move to the Gateway API.

## 45: What is the Gateway API?

The Gateway API is the newer, more powerful replacement for Ingress. It splits the setup into roles:

- `GatewayClass`: which controller implementation to use (set by the platform team)
- `Gateway`: the actual listener, ports and TLS (set by cluster operators)
- `HTTPRoute`, `GRPCRoute` and others: routing rules (set by app teams)

It supports things that needed custom annotations in Ingress, like header matching, traffic splitting and cross-namespace routing.

## 46: What is a ConfigMap?

A ConfigMap stores non-secret config as key-value pairs. Pods can read it as environment variables or as files in a volume. This keeps config out of the image so the same image can run in dev and prod.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: info
  config.json: |
    { "featureX": true }
```

## 47: What is a Secret?

A Secret holds sensitive data like passwords, tokens and keys. It works much like a ConfigMap: you can mount it as files or expose it as environment variables.

```bash
kubectl create secret generic db-creds \
  --from-literal=username=app \
  --from-literal=password='s3cr3t'
```

By default Secret values are only base64 encoded, not encrypted. You need to turn on encryption at rest and limit who can read Secrets with RBAC.

## 48: Is base64 encryption?

No. base64 is just an encoding. Anyone who can read the Secret can decode it in one command:

```bash
kubectl get secret db-creds -o jsonpath='{.data.password}' | base64 -d
```

The encoding exists only so binary data can be stored in YAML. Protection comes from RBAC, encryption at rest in etcd and keeping secrets out of Git.

## 49: How do you use a ConfigMap as environment variables?

You can load single keys with `valueFrom` or all keys at once with `envFrom`.

```yaml
containers:
  - name: app
    image: my-app:1.0
    env:
      - name: LOG_LEVEL
        valueFrom:
          configMapKeyRef:
            name: app-config
            key: LOG_LEVEL
    envFrom:
      - configMapRef:
          name: app-config
```

Environment variables are read only once, when the container starts. Changing the ConfigMap does not change them in running Pods.

## 50: How do you mount a ConfigMap as files?

Add a `configMap` volume and mount it. Each key becomes a file.

```yaml
spec:
  containers:
    - name: app
      image: my-app:1.0
      volumeMounts:
        - name: config
          mountPath: /etc/app
  volumes:
    - name: config
      configMap:
        name: app-config
```

The app sees `/etc/app/LOG_LEVEL` and `/etc/app/config.json`. Files mounted this way get updated in place after the ConfigMap changes (with a short delay), unless you mount them with `subPath`.

## 51: What is a volume in Kubernetes?

A volume is a directory that containers in a Pod can mount. Files written in a container's own filesystem are lost when the container restarts. A volume lives as long as the Pod (or longer, for persistent volumes), so data can survive container restarts and be shared between containers in the Pod.

There are many volume types: `emptyDir`, `configMap`, `secret`, `persistentVolumeClaim`, `hostPath`, `projected`, `image` and more.

## 52: What is an emptyDir volume?

An `emptyDir` is an empty directory created when the Pod starts on a node. All containers in the Pod can read and write it. When the Pod is removed from the node, the data is deleted.

```yaml
volumes:
  - name: cache
    emptyDir:
      sizeLimit: 1Gi
```

It is good for scratch space, caches and sharing files between containers. With `medium: Memory` it is backed by RAM (tmpfs), and the data counts against the container's memory limit.

## 53: What is a hostPath volume?

A `hostPath` volume mounts a file or folder from the node's filesystem into the Pod. It is mostly used by system tools like log collectors or monitoring agents that need to read node files.

You should avoid it for normal apps. The data is tied to one node, and it can be a security hole because a Pod could read or change sensitive files on the host.

## 54: What is a PersistentVolume?

A PersistentVolume (PV) is a piece of storage in the cluster, like an AWS EBS disk or an NFS share, represented as a Kubernetes object. It exists apart from any Pod, so the data stays when Pods are deleted.

PVs are usually created automatically through a StorageClass, but an admin can also create them by hand.

## 55: What is a PersistentVolumeClaim?

A PersistentVolumeClaim (PVC) is a request for storage made by a user: "I need 10Gi, read-write, from the `fast-ssd` class." Kubernetes binds the claim to a matching PV, creating one if needed. Pods then use the PVC as a volume.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data
spec:
  accessModes: [ReadWriteOnce]
  storageClassName: fast-ssd
  resources:
    requests:
      storage: 10Gi
```

```yaml
volumes:
  - name: data
    persistentVolumeClaim:
      claimName: data
```

## 56: What is the difference between a PV and a PVC?

The PV is the actual storage. The PVC is the request for storage. App developers write PVCs and do not need to know what kind of disk is behind them. Admins (or the StorageClass) take care of PVs. One PV binds to exactly one PVC.

## 57: What is a StorageClass?

A StorageClass describes a type of storage and how to create it. It names a provisioner (usually a CSI driver) and its parameters, like disk type or IOPS. When a PVC asks for that class, a new PV is created automatically. This is called dynamic provisioning.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

## 58: What are the access modes of a PersistentVolume?

- `ReadWriteOnce` (RWO): read-write by Pods on one node
- `ReadOnlyMany` (ROX): read-only by many nodes
- `ReadWriteMany` (RWX): read-write by many nodes
- `ReadWriteOncePod` (RWOP): read-write by only one Pod in the whole cluster

Block storage like EBS supports RWO and RWOP. For RWX you need a shared filesystem like NFS, EFS or CephFS.

## 59: What is a DaemonSet?

A DaemonSet runs one copy of a Pod on every node (or on every node that matches a selector). When a new node joins, the Pod is added there automatically.

It is used for node-level agents: log collectors (Fluent Bit), monitoring agents (node-exporter), network plugins and storage drivers.

## 60: What is a StatefulSet?

A StatefulSet runs Pods that need a stable identity. Each Pod gets a fixed name (`db-0`, `db-1`, `db-2`), its own PersistentVolumeClaim that follows it, and a stable DNS name. Pods are created and deleted in order by default.

It is used for databases, message brokers and other clustered apps where each member has to be told apart from the others.

## 61: What is the difference between a Deployment and a StatefulSet?

- Deployment Pods are interchangeable, get random names and usually share no per-Pod storage.
- StatefulSet Pods have stable names and ordinal numbers, each has its own volume, and they start and stop in order.

If a replica of your app can be thrown away and replaced by any other, use a Deployment. If each replica has its own data or role, use a StatefulSet.

## 62: What is a Job?

A Job runs Pods until a task finishes successfully, then stops. If a Pod fails, the Job retries up to `backoffLimit` times.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: migrate
spec:
  backoffLimit: 3
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: my-app:1.4
          command: ["npm", "run", "migrate"]
```

## 63: What is a CronJob?

A CronJob creates Jobs on a schedule written in cron format.

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: nightly-report
spec:
  schedule: "0 2 * * *"
  timeZone: "Europe/Berlin"
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: report
              image: report:2.1
```

## 64: What is the restartPolicy of a Pod?

It tells the kubelet what to do when a container exits:

- `Always` (default): always restart it. Required for Deployments, StatefulSets and DaemonSets.
- `OnFailure`: restart only if it exited with a non-zero code.
- `Never`: never restart it.

Jobs must use `OnFailure` or `Never`.

## 65: What are the phases of a Pod?

- `Pending`: accepted, but containers are not running yet (scheduling or image pull)
- `Running`: bound to a node and at least one container is running
- `Succeeded`: all containers exited with success and will not restart
- `Failed`: all containers have stopped and at least one failed
- `Unknown`: the node cannot be reached

Things like `CrashLoopBackOff` or `ImagePullBackOff` are not phases. They are container states that `kubectl get pods` shows in the STATUS column.

## 66: What does CrashLoopBackOff mean?

The container keeps starting and crashing, and the kubelet is waiting longer and longer between restarts (up to five minutes). The cause is in the app or its config: a missing env variable, a bad command, a failed connection at startup, or a liveness probe that kills it.

```bash
kubectl logs my-pod --previous
kubectl describe pod my-pod
```

`--previous` shows logs from the crashed container, which is usually where the error is.

## 67: What does ImagePullBackOff mean?

The kubelet could not pull the image and is waiting before it tries again. Common causes are a typo in the image name or tag, a tag that does not exist, a private registry without `imagePullSecrets`, or a registry rate limit. `kubectl describe pod` shows the exact error in the Events section.

## 68: How do you see the logs of a Pod?

```bash
kubectl logs my-pod
kubectl logs my-pod -c sidecar        # a specific container
kubectl logs my-pod -f                # follow
kubectl logs my-pod --previous        # crashed container
kubectl logs deploy/web               # one Pod of a Deployment
kubectl logs -l app=web --all-containers --prefix
```

Logs come from what the container writes to stdout and stderr.

## 69: How do you open a shell in a running container?

```bash
kubectl exec -it my-pod -- sh
kubectl exec -it my-pod -c app -- bash
```

`-i` keeps stdin open and `-t` gives you a terminal. Everything after `--` is the command to run. If the image has no shell (distroless), use `kubectl debug` instead.

## 70: What does kubectl describe show?

It shows a readable summary of an object plus its recent events. For a Pod you see the node, IP, container states, restart counts, probes, volumes and events like scheduling failures or image pull errors. It is the first command to run when a Pod is not working.

```bash
kubectl describe pod my-pod
kubectl describe node worker-1
```

## 71: What are events in Kubernetes?

Events are short records of what happened to objects: "Scheduled", "Pulling image", "Back-off restarting failed container", "FailedScheduling". They are kept for about an hour by default.

```bash
kubectl get events --sort-by=.lastTimestamp
kubectl events --for pod/my-pod
```

## 72: How do you see the YAML of an existing object?

```bash
kubectl get deployment web -o yaml
kubectl get pod my-pod -o json
```

The output includes the `status` and fields Kubernetes added, like `uid`, `resourceVersion` and `managedFields`. Strip those before reusing it as a manifest.

## 73: What output formats does kubectl get support?

- `-o wide`: more columns, like node and IP
- `-o yaml` and `-o json`: the full object
- `-o name`: just `kind/name`
- `-o jsonpath='{...}'`: pick fields
- `-o custom-columns=...`: build your own table
- `-o kyaml`: a stricter YAML style that avoids common YAML gotchas

```bash
kubectl get pods -o jsonpath='{.items[*].metadata.name}'
kubectl get pods -o custom-columns=NAME:.metadata.name,NODE:.spec.nodeName
```

## 74: How do you delete objects?

```bash
kubectl delete pod my-pod
kubectl delete -f deployment.yaml
kubectl delete pods -l app=web
kubectl delete namespace staging   # deletes everything inside it
```

Deleting a Pod that belongs to a Deployment just makes the Deployment create a new one. To remove it for good, delete or scale down the Deployment.

## 75: How do you get quick help on a resource's fields?

Use `kubectl explain`. It reads the schema from the API server, so it matches your cluster version.

```bash
kubectl explain deployment.spec.strategy
kubectl explain pod.spec.containers.resources --recursive
```

## 76: What is port forwarding in kubectl?

`kubectl port-forward` opens a tunnel from your machine to a Pod or Service in the cluster. It is great for debugging without exposing anything publicly.

```bash
kubectl port-forward svc/web 8080:80
kubectl port-forward pod/db-0 5432:5432
```

Now `localhost:8080` reaches the Service. It goes through the API server, so it is not meant for real traffic.

## 77: What is a resource request?

A request is the amount of CPU and memory a container says it needs. The scheduler uses requests to pick a node that has enough free capacity. The container is guaranteed at least that much.

```yaml
resources:
  requests:
    cpu: 250m
    memory: 256Mi
```

## 78: What is a resource limit?

A limit is the most a container may use.

- If it goes over the memory limit, the kernel kills it (OOMKilled).
- If it hits the CPU limit, it is throttled (slowed down), not killed.

```yaml
resources:
  requests:
    cpu: 250m
    memory: 256Mi
  limits:
    memory: 512Mi
```

Many teams set memory limits but leave out CPU limits, to avoid needless throttling.

## 79: What do units like 500m and 512Mi mean?

- CPU is measured in cores. `1` is one full core and `500m` (500 millicores) is half a core.
- Memory is in bytes. `Mi` and `Gi` are powers of 1024 (mebibytes, gibibytes). `M` and `G` are powers of 1000.

Watch out for `512m` in memory, which means 0.512 bytes and is almost always a typo for `512Mi`.

## 80: What does OOMKilled mean?

The container used more memory than its limit (or the node ran out of memory) and the Linux kernel killed it. `kubectl describe pod` shows `Last State: Terminated, Reason: OOMKilled` and exit code 137.

The fix is to raise the limit, fix a memory leak, or make the app aware of its limit (for example tune the JVM heap or Node.js `--max-old-space-size`).

## 81: What is a liveness probe?

A liveness probe checks whether the container is still working. If it fails a set number of times in a row, the kubelet restarts the container. It is for cases where the app is stuck, like a deadlock, and cannot recover on its own.

```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  periodSeconds: 10
  failureThreshold: 3
```

## 82: What is a readiness probe?

A readiness probe checks whether the container is ready to get traffic. If it fails, the Pod is removed from the Service's endpoints but is not restarted. When it passes again, traffic comes back.

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
```

Use it for warm-up time, or when a dependency is down and the Pod should stop taking requests for a while.

## 83: What is a startup probe?

A startup probe is for slow-starting apps. While it runs, liveness and readiness probes are paused. Once it passes, the others take over. This stops a slow app from being killed by its liveness probe before it has even finished starting.

```yaml
startupProbe:
  httpGet:
    path: /healthz
    port: 8080
  periodSeconds: 5
  failureThreshold: 30 # up to 150 seconds to start
```

## 84: What kinds of probe checks are there?

- `httpGet`: success if the HTTP status is 200-399
- `tcpSocket`: success if a TCP connection opens
- `exec`: runs a command in the container, success if exit code is 0
- `grpc`: uses the standard gRPC health check protocol

```yaml
livenessProbe:
  grpc:
    port: 9090
```

## 85: What is the difference between liveness and readiness probes?

A failed liveness probe restarts the container. A failed readiness probe only takes the Pod out of load balancing. A common mistake is to check a database in the liveness probe: if the database goes down, every Pod gets restarted over and over, which helps nobody. Liveness should only check the process itself.

## 86: What are init containers?

Init containers run before the main containers start, one after another. Each must finish successfully before the next one runs. They are used for setup work: waiting for a dependency, running migrations, downloading files or fixing permissions.

```yaml
spec:
  initContainers:
    - name: wait-for-db
      image: busybox:1.37
      command: ["sh", "-c", "until nc -z db 5432; do sleep 2; done"]
  containers:
    - name: app
      image: my-app:1.0
```

## 87: What is a sidecar container?

A sidecar is a helper container that runs next to the main container in the same Pod for the whole Pod's life, for example a log shipper, a proxy or a config reloader.

Since Kubernetes 1.33 there is native support (stable): you define the sidecar as an init container with `restartPolicy: Always`. It starts before the main containers, keeps running, and is stopped after them.

```yaml
initContainers:
  - name: log-shipper
    image: fluent-bit:4.0
    restartPolicy: Always
```

## 88: What is a multi-container Pod?

A Pod with more than one container. The containers share the network (they can reach each other on `localhost`) and can share volumes. Common patterns are sidecar (helper next to the app), ambassador (proxy for outbound connections) and adapter (changes output format, for example metrics).

Only put containers together if they must scale and be scheduled together.

## 89: What is the difference between a container image tag and a digest?

A tag like `my-app:1.4` is a name that can be moved to point to a different image. A digest like `my-app@sha256:abc...` is the hash of the image content and never changes. Using digests in production means you always run exactly the image you tested.

## 90: What is imagePullPolicy?

It tells the kubelet when to pull an image:

- `IfNotPresent`: pull only if the image is not already on the node
- `Always`: check the registry every time a container starts (only downloads if the digest changed)
- `Never`: never pull, the image must already be on the node

If you do not set it, it is `Always` for the `:latest` tag or no tag, and `IfNotPresent` for everything else.

## 91: Why should you avoid the latest tag in Kubernetes?

`latest` does not tell you which version is running, so rollbacks are unclear, and different nodes can end up with different images under the same tag. Also, changing what `latest` points to does not trigger a rollout, because the Pod template did not change. Use a version tag or a digest.

## 92: How do you pull images from a private registry?

Create a docker-registry Secret and reference it in the Pod spec, or attach it to the ServiceAccount.

```bash
kubectl create secret docker-registry regcred \
  --docker-server=ghcr.io \
  --docker-username=me \
  --docker-password="$TOKEN"
```

```yaml
spec:
  imagePullSecrets:
    - name: regcred
```

On managed clusters you can often use the node's cloud identity instead, for example EKS nodes pulling from ECR through their IAM role.

## 93: What is a ServiceAccount?

A ServiceAccount is an identity for processes running in Pods. Every namespace has a `default` ServiceAccount. Pods get a short-lived token for their ServiceAccount, which they use to call the Kubernetes API. You give it permissions with RBAC.

```yaml
spec:
  serviceAccountName: report-reader
```

## 94: What is the difference between a user account and a ServiceAccount?

User accounts are for people. Kubernetes has no User object, users come from outside (certificates, OIDC from your identity provider, cloud IAM). ServiceAccounts are Kubernetes objects, belong to a namespace and are meant for apps and automation running in or against the cluster.

## 95: What is RBAC?

Role-Based Access Control decides who can do what in the cluster. It has four object types:

- `Role`: a set of permissions in one namespace
- `ClusterRole`: a set of permissions cluster-wide (or reusable in many namespaces)
- `RoleBinding`: gives a Role or ClusterRole to users, groups or ServiceAccounts in one namespace
- `ClusterRoleBinding`: gives a ClusterRole across the whole cluster

## 96: How do you give a ServiceAccount read access to Pods in one namespace?

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: dev
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
  namespace: dev
subjects:
  - kind: ServiceAccount
    name: report-reader
    namespace: dev
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

## 97: How do you check if you have permission to do something?

```bash
kubectl auth can-i create deployments -n dev
kubectl auth can-i list secrets --as=system:serviceaccount:dev:report-reader -n dev
kubectl auth can-i --list -n dev
```

`--as` lets an admin test permissions for another user or ServiceAccount.

## 98: What is a rolling update?

It is the default way a Deployment updates Pods. It creates new Pods a few at a time and removes old ones as the new ones become ready, so the app stays available. You control the speed with `maxSurge` (extra Pods allowed) and `maxUnavailable` (Pods allowed to be down).

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 25%
    maxUnavailable: 0
```

## 99: How do you update the image of a Deployment?

Change the image in the YAML and apply it. For quick changes:

```bash
kubectl set image deployment/web web=my-app:1.5
kubectl rollout status deployment/web
```

Any change to the Pod template (image, env, labels in the template) triggers a new rollout.

## 100: How do you roll back a Deployment?

```bash
kubectl rollout history deployment/web
kubectl rollout undo deployment/web
kubectl rollout undo deployment/web --to-revision=3
```

Kubernetes keeps old ReplicaSets (10 by default, set by `revisionHistoryLimit`) so it can switch back quickly. If you use GitOps, revert the commit instead, or the tool will undo your rollback.

## 101: What is the Recreate deployment strategy?

With `type: Recreate`, Kubernetes deletes all old Pods first and then creates the new ones. There is downtime between the two steps.

You use it when two versions cannot run at the same time, for example when the app holds an exclusive lock on a volume or a database migration is not backward compatible.

## 102: How do you check the status of a rollout?

```bash
kubectl rollout status deployment/web
kubectl get deployment web
kubectl get rs -l app=web
```

`rollout status` waits until the rollout is done or fails, which makes it handy in CI scripts. You can also pause and resume rollouts with `kubectl rollout pause` and `kubectl rollout resume`.

## 103: How do you restart all Pods of a Deployment?

```bash
kubectl rollout restart deployment/web
```

It adds a timestamp annotation to the Pod template, which starts a normal rolling update. It is a common way to pick up a changed ConfigMap or Secret that is used as environment variables.

## 104: What is a HorizontalPodAutoscaler?

An HPA changes the number of replicas of a Deployment or StatefulSet based on metrics, usually CPU or memory use, or custom metrics like requests per second.

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

CPU utilization is measured against the container's CPU request, so requests must be set.

## 105: What is the Metrics Server?

Metrics Server collects CPU and memory usage from the kubelets and serves it through the `metrics.k8s.io` API. The HPA and `kubectl top` use it. It keeps only current values, not history, so it is not a monitoring system.

```bash
kubectl top nodes
kubectl top pods -n dev
```

## 106: What is the difference between horizontal and vertical scaling?

Horizontal scaling adds or removes Pods (HPA). Vertical scaling changes the CPU and memory of each Pod (VerticalPodAutoscaler, or in-place resize). Stateless web apps usually scale horizontally. Apps that cannot easily run in many copies, like some databases, often scale vertically.

## 107: What is the Cluster Autoscaler?

The Cluster Autoscaler adds nodes when Pods cannot be scheduled because there is not enough capacity, and removes nodes that are mostly empty for a while. It works with cloud node groups like AWS Auto Scaling groups. Karpenter is a popular alternative that picks instance types on the fly.

## 108: What are taints and tolerations?

A taint on a node pushes Pods away. Only Pods with a matching toleration can be scheduled there.

```bash
kubectl taint nodes gpu-1 gpu=true:NoSchedule
```

```yaml
tolerations:
  - key: gpu
    operator: Equal
    value: "true"
    effect: NoSchedule
```

A toleration lets a Pod go on a tainted node, it does not force it there. To force placement you also need a node selector or node affinity.

## 109: What taint effects exist?

- `NoSchedule`: new Pods without a toleration are not scheduled on the node
- `PreferNoSchedule`: the scheduler tries to avoid the node but may still use it
- `NoExecute`: new Pods are not scheduled, and running Pods without a toleration are evicted

## 110: What is a nodeSelector?

The simplest way to make a Pod run only on certain nodes. The Pod is scheduled only on nodes that have all the given labels.

```yaml
spec:
  nodeSelector:
    disktype: ssd
```

```bash
kubectl label nodes worker-3 disktype=ssd
```

## 111: What is node affinity?

Node affinity is a more flexible version of `nodeSelector`. It supports operators like `In`, `NotIn` and `Exists`, and has two kinds:

- `requiredDuringSchedulingIgnoredDuringExecution`: a hard rule
- `preferredDuringSchedulingIgnoredDuringExecution`: a soft preference with a weight

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: topology.kubernetes.io/zone
              operator: In
              values: [eu-west-1a, eu-west-1b]
```

## 112: What is Pod affinity and anti-affinity?

Pod affinity places a Pod near other Pods (same node or same zone). Pod anti-affinity keeps it away from them. A common use is spreading replicas so they do not all land on one node.

```yaml
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          topologyKey: kubernetes.io/hostname
          labelSelector:
            matchLabels:
              app: web
```

## 113: What is a Pod's QoS class?

Kubernetes puts every Pod into one of three Quality of Service classes based on its requests and limits:

- `Guaranteed`: every container has CPU and memory requests equal to limits
- `Burstable`: at least one container has a request or limit, but it is not Guaranteed
- `BestEffort`: no requests or limits at all

When a node runs low on memory, BestEffort Pods are evicted first and Guaranteed Pods last.

## 114: What is Minikube?

Minikube runs a small Kubernetes cluster on your own machine, inside a VM or a container. It is used for learning and local development and has add-ons for things like an ingress controller and metrics server.

```bash
minikube start
minikube dashboard
```

## 115: What is kind?

kind stands for "Kubernetes in Docker". It runs each Kubernetes node as a Docker container. It starts fast and is very popular for testing in CI, including testing Kubernetes itself. It can run multi-node clusters on one machine.

```bash
kind create cluster --name dev
kind load docker-image my-app:dev --name dev
```

## 116: What are some other ways to run Kubernetes locally?

- Docker Desktop and Rancher Desktop have a built-in Kubernetes option
- k3d runs k3s (a light Kubernetes distribution) in Docker
- MicroK8s from Canonical
- Minikube and kind

They all give you a real API server, so manifests that work there also work on a real cluster, apart from cloud features like load balancers and storage classes.

## 117: What are managed Kubernetes services?

Cloud providers run the control plane for you, handle upgrades and integrate with their load balancers, storage and IAM. The main ones are Amazon EKS, Google GKE and Azure AKS. You usually still manage the worker nodes, unless you use options like GKE Autopilot or EKS Auto Mode, which manage nodes too.

## 118: What is k3s?

k3s is a lightweight, certified Kubernetes distribution packed into a single binary. It uses less memory and fits edge devices, IoT, small servers and CI. It ships with things like a default storage provisioner and Traefik as the ingress controller.

## 119: How do you create a Deployment quickly without writing YAML?

```bash
kubectl create deployment web --image=nginx:1.29 --replicas=2
kubectl expose deployment web --port=80 --target-port=80
```

To get a YAML file you can edit and keep, add `--dry-run=client -o yaml`:

```bash
kubectl create deployment web --image=nginx:1.29 --dry-run=client -o yaml > web.yaml
```

## 120: What does kubectl run do?

`kubectl run` creates a single Pod. It is handy for quick tests and debug Pods.

```bash
kubectl run tmp --rm -it --image=busybox:1.37 -- sh
kubectl run curl --rm -it --image=curlimages/curl -- curl http://web
```

`--rm` deletes the Pod when you exit. For apps, use a Deployment instead of a bare Pod.

## 121: Why should you not create bare Pods for applications?

A bare Pod is not managed by any controller. If its node dies, or the Pod gets evicted, nothing creates a replacement. A Deployment, StatefulSet or Job watches its Pods and recreates them. Bare Pods are fine only for one-off tests.

## 122: What is a multi-document YAML file?

You can put several objects in one file, separated by `---`. `kubectl apply -f` applies all of them.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  MODE: prod
---
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
    - port: 80
```

## 123: How do you apply all manifests in a folder?

```bash
kubectl apply -f k8s/
kubectl apply -f k8s/ --recursive
kubectl apply -k overlays/prod   # Kustomize
```

## 124: What is Helm?

Helm is a package manager for Kubernetes. A package is called a chart. It contains templated manifests plus a `values.yaml` file with defaults. You install a chart as a release and override values per environment.

```bash
helm repo add jetstack https://charts.jetstack.io
helm install cert-manager jetstack/cert-manager -n cert-manager --create-namespace --set crds.enabled=true
helm upgrade cert-manager jetstack/cert-manager -n cert-manager -f values-prod.yaml
helm rollback cert-manager 1 -n cert-manager
```

## 125: What is Kustomize?

Kustomize customizes plain YAML without templates. You keep a base set of manifests and add overlays per environment that patch them (change replicas, image tags, add labels). It is built into kubectl.

```yaml
# overlays/prod/kustomization.yaml
resources:
  - ../../base
images:
  - name: my-app
    newTag: "1.5.0"
patches:
  - path: replicas.yaml
```

```bash
kubectl apply -k overlays/prod
```

## 126: What is the Kubernetes Dashboard?

It is a web UI for looking at and managing cluster objects. It is not installed by default. Because it can be a big security risk if exposed, many teams skip it and use tools like k9s, Headlamp or Lens on their own machines instead.

## 127: What is k9s?

k9s is a terminal UI for Kubernetes. You can browse resources, view logs, exec into Pods, port-forward and delete objects with a few keys. It uses your kubeconfig, so it has the same permissions as `kubectl`.

## 128: What is the API group of common resources?

- Core group (written as `v1`, empty string in RBAC): Pod, Service, ConfigMap, Secret, Namespace, PersistentVolumeClaim, ServiceAccount
- `apps/v1`: Deployment, ReplicaSet, StatefulSet, DaemonSet
- `batch/v1`: Job, CronJob
- `networking.k8s.io/v1`: Ingress, NetworkPolicy, IngressClass
- `autoscaling/v2`: HorizontalPodAutoscaler
- `rbac.authorization.k8s.io/v1`: Role, ClusterRole and bindings
- `storage.k8s.io/v1`: StorageClass

```bash
kubectl api-resources
```

## 129: What are API versions like v1alpha1, v1beta1 and v1?

- Alpha: experimental, off by default, can change or disappear
- Beta: well tested, new beta APIs are off by default since 1.24, may still change
- Stable (v1, v2): supported for a long time, safe for production

When an API version is removed, you must move manifests to the newer version before upgrading the cluster.

## 130: What is a NetworkPolicy?

By default, every Pod can talk to every other Pod in the cluster. A NetworkPolicy limits that. It selects Pods by label and lists which traffic is allowed in (ingress) and out (egress).

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-allow-api
spec:
  podSelector:
    matchLabels:
      app: db
  policyTypes: [Ingress]
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: api
      ports:
        - port: 5432
```

NetworkPolicies only work if the network plugin supports them (Calico, Cilium and others do).

## 131: What is a CNI plugin?

CNI (Container Network Interface) is the standard Kubernetes uses to set up Pod networking. A CNI plugin gives each Pod an IP address and makes Pods reachable across nodes. Popular ones are Calico, Cilium and Flannel, and clouds have their own, like the AWS VPC CNI.

Kubernetes does not ship a network plugin. A cluster does not work until you install one.

## 132: What are the basic rules of the Kubernetes network model?

- Every Pod gets its own IP address
- Pods can talk to all other Pods on any node without NAT
- Agents on a node (like the kubelet) can talk to all Pods on that node
- Containers in the same Pod share the IP and talk over localhost

How these rules are met is up to the CNI plugin.

## 133: How do containers in the same Pod talk to each other?

Over `localhost`, because they share one network namespace. If the app listens on 8080 and a sidecar on 9090, they reach each other at `localhost:8080` and `localhost:9090`. That also means two containers in one Pod cannot listen on the same port. They can also share files through a shared volume.

## 134: What is a headless Service?

A Service with `clusterIP: None`. It has no virtual IP. A DNS lookup returns the IPs of all ready Pods instead. With a StatefulSet, each Pod also gets its own DNS name like `db-0.db.default.svc.cluster.local`.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db
spec:
  clusterIP: None
  selector:
    app: db
  ports:
    - port: 5432
```

## 135: What are EndpointSlices?

EndpointSlices list the Pod IPs and ports behind a Service. The control plane updates them as Pods become ready or go away, and kube-proxy reads them to build routing rules. They split large lists into chunks (100 endpoints per slice by default), which scales much better than the old Endpoints object.

```bash
kubectl get endpointslices -l kubernetes.io/service-name=web
```

## 136: What is the Downward API?

It lets a container learn facts about itself, like its Pod name, namespace, node name, IP, labels or resource limits, through env variables or files.

```yaml
env:
  - name: POD_NAME
    valueFrom:
      fieldRef:
        fieldPath: metadata.name
  - name: NODE_NAME
    valueFrom:
      fieldRef:
        fieldPath: spec.nodeName
  - name: MEMORY_LIMIT
    valueFrom:
      resourceFieldRef:
        resource: limits.memory
```

## 137: How do you set environment variables in a container?

```yaml
containers:
  - name: app
    image: my-app:1.0
    env:
      - name: NODE_ENV
        value: production
      - name: DB_PASSWORD
        valueFrom:
          secretKeyRef:
            name: db-creds
            key: password
    envFrom:
      - configMapRef:
          name: app-config
```

If the same name appears in `env` and `envFrom`, `env` wins.

## 138: What is the difference between command and args in a container?

- `command` overrides the image's `ENTRYPOINT`
- `args` overrides the image's `CMD`

```yaml
containers:
  - name: worker
    image: my-app:1.0
    command: ["node"]
    args: ["dist/worker.js", "--concurrency=4"]
```

If you set only `args`, the image's entrypoint runs with your args.

## 139: What is a ResourceQuota?

A ResourceQuota caps the total resources a namespace can use, like total CPU requests, total memory, or the number of Pods, Services or PVCs.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-a
  namespace: team-a
spec:
  hard:
    requests.cpu: "10"
    requests.memory: 20Gi
    limits.memory: 40Gi
    pods: "50"
```

When a CPU or memory quota is set, every new Pod in that namespace must set those requests or limits, or it is rejected.

## 140: What is a LimitRange?

A LimitRange sets default requests and limits for containers in a namespace, and min and max values. It helps when developers forget to set resources.

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: defaults
  namespace: team-a
spec:
  limits:
    - type: Container
      defaultRequest:
        cpu: 100m
        memory: 128Mi
      default:
        memory: 256Mi
      max:
        memory: 2Gi
```

## 141: What does kubectl cordon do?

It marks a node as unschedulable. New Pods will not go there, but Pods already running stay. You use it before maintenance.

```bash
kubectl cordon worker-2
kubectl uncordon worker-2
```

## 142: What does kubectl drain do?

It cordons the node and then evicts its Pods so they get recreated elsewhere. It respects PodDisruptionBudgets.

```bash
kubectl drain worker-2 --ignore-daemonsets --delete-emptydir-data
```

`--ignore-daemonsets` is needed because DaemonSet Pods would just come back. `--delete-emptydir-data` confirms you are OK losing `emptyDir` data.

## 143: What is a PodDisruptionBudget?

A PDB limits how many Pods of an app can be down at the same time because of voluntary disruptions like node drains and cluster upgrades.

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: web
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: web
```

It does not protect against node crashes, only against planned evictions.

## 144: What is the difference between a voluntary and an involuntary disruption?

Voluntary disruptions are planned: draining a node, a cluster upgrade, the Cluster Autoscaler removing a node, or deleting a Pod. Involuntary disruptions are failures: hardware crashes, kernel panics, a node losing network, or a Pod getting evicted because the node ran out of memory. PDBs only apply to voluntary disruptions that use the Eviction API.

## 145: What is a static Pod?

A static Pod is defined by a manifest file in a folder on a node (usually `/etc/kubernetes/manifests`). The kubelet runs it directly, without the API server or scheduler. kubeadm uses static Pods to run the control plane itself: the API server, etcd, scheduler and controller manager.

The API server shows a read-only "mirror Pod" for each static Pod. Static Pods cannot use ConfigMaps or Secrets from the API.

## 146: What is kubeadm?

kubeadm is the official tool for setting up a cluster on your own machines. `kubeadm init` creates the control plane and `kubeadm join` adds nodes. It also handles certificate renewal and cluster upgrades. It does not install a network plugin or provision machines.

## 147: What is the difference between Docker and Kubernetes?

Docker builds images and runs containers on one machine. Kubernetes runs containers across many machines and takes care of scheduling, healing, scaling, networking and rollouts. They are often used together: you build images with Docker and run them on Kubernetes (through containerd or CRI-O).

## 148: What are finalizers?

A finalizer is a key in `metadata.finalizers` that blocks an object from being deleted until a controller does some cleanup and removes the key. For example, PVCs have `kubernetes.io/pvc-protection`, so a PVC is not deleted while a Pod still uses it.

If an object is stuck in `Terminating`, a finalizer is often the reason.

## 149: What is the kubectl diff command?

It shows what would change if you applied a file, without changing anything. It is useful in code review and CI.

```bash
kubectl diff -f deployment.yaml
```

The output is a normal diff between the live object and what it would be after applying.

## 150: What is the release cycle of Kubernetes?

Kubernetes releases a new minor version about every four months, around three per year. Each minor version gets patch releases for about 14 months. That means you need to upgrade at least once a year to stay supported. Managed services have their own support windows, often with paid extended support.

# Moderate Questions (151-300)

## 151: What does a production-ready Deployment manifest look like?

It sets resources, probes, a security context, a sensible rollout strategy and labels. Something like this:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
  labels:
    app.kubernetes.io/name: api
spec:
  replicas: 3
  revisionHistoryLimit: 5
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app.kubernetes.io/name: api
  template:
    metadata:
      labels:
        app.kubernetes.io/name: api
    spec:
      serviceAccountName: api
      automountServiceAccountToken: false
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      terminationGracePeriodSeconds: 30
      containers:
        - name: api
          image: registry.example.com/api:1.8.2
          ports:
            - name: http
              containerPort: 8080
          resources:
            requests:
              cpu: 200m
              memory: 256Mi
            limits:
              memory: 512Mi
          readinessProbe:
            httpGet:
              path: /ready
              port: http
          livenessProbe:
            httpGet:
              path: /healthz
              port: http
            periodSeconds: 10
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
```

Add a PodDisruptionBudget, an HPA and topology spread constraints on top of it.

## 152: How do you choose good requests and limits?

Start from real data, not guesses. Run the app under normal load, look at CPU and memory usage in Prometheus or `kubectl top`, and set:

- Memory request close to normal usage, memory limit with headroom for peaks (often equal to the request for steady apps)
- CPU request close to the average usage under normal load
- CPU limit often left out, or set high

The VerticalPodAutoscaler in recommendation mode (`updateMode: "Off"`) can suggest values. Review them after big releases, because usage changes.

## 153: Should you set CPU limits?

It is debated. CPU limits are enforced with CFS quotas, which can throttle a container even when the node has idle CPU. That adds latency, especially for multi-threaded apps that burn their quota early in each 100ms period.

Many teams set CPU requests (for fair scheduling and fair sharing under contention) and skip CPU limits. You may still want limits for noisy batch jobs, in multi-tenant clusters, or when you need Guaranteed QoS. Memory limits are different, you should almost always set them.

## 154: How do you pick maxSurge and maxUnavailable?

- `maxUnavailable: 0` with `maxSurge: 1` (or 25%) means capacity never drops during a rollout. It is the safe choice for user-facing apps but needs spare cluster capacity.
- A higher `maxUnavailable` makes rollouts faster but reduces capacity while they run.
- A higher `maxSurge` makes rollouts faster but needs more room on the nodes.

Both can be numbers or percentages. They cannot both be 0.

## 155: What do minReadySeconds and progressDeadlineSeconds do?

- `minReadySeconds`: a new Pod must stay ready this long before it counts as available. It catches apps that pass the readiness probe and crash a few seconds later.
- `progressDeadlineSeconds` (default 600): if the rollout makes no progress for this long, the Deployment gets a `Progressing=False` condition with reason `ProgressDeadlineExceeded`. Kubernetes does not roll back by itself, but `kubectl rollout status` exits with an error, which your pipeline can act on.

## 156: How does Pod termination work?

When a Pod is deleted:

1. The Pod is marked as terminating and gets removed from Service endpoints.
2. If there is a `preStop` hook, it runs.
3. The container's main process gets SIGTERM.
4. Kubernetes waits up to `terminationGracePeriodSeconds` (default 30) in total.
5. Anything still running gets SIGKILL.

Your app should catch SIGTERM, stop taking new work, finish requests in progress, close connections and exit.

## 157: Why do some requests fail during a rolling update even with readiness probes?

Removing a Pod from endpoints and sending SIGTERM happen at the same time, not one after the other. kube-proxy, ingress controllers and cloud load balancers need a moment to see that the Pod is gone. If the app exits right away, requests still routed to it fail.

The usual fix is a short `preStop` sleep so the Pod keeps serving while the rest of the system catches up:

```yaml
lifecycle:
  preStop:
    sleep:
      seconds: 10
```

The built-in `sleep` action works even in images with no shell. Make sure `terminationGracePeriodSeconds` is longer than the sleep plus your app's shutdown time.

## 158: What is a postStart hook?

It runs right after a container is created. It runs at the same time as the container's entrypoint, so there is no guarantee it runs before the app starts. If it fails, the container is killed. The container is not marked as running until the hook finishes.

```yaml
lifecycle:
  postStart:
    exec:
      command: ["sh", "-c", "echo started > /tmp/started"]
```

It is rarely needed. Init containers or the app's own startup code are usually a better fit.

## 159: How do you do a blue-green deployment in Kubernetes?

Run two Deployments, `web-blue` (current) and `web-green` (new), with a `version` label. The Service selects one of them. After testing green, switch the Service selector.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
    version: green # was blue
  ports:
    - port: 80
      targetPort: 8080
```

Switching back is just changing the selector again. The downside is that you run double capacity during the switch.

## 160: How do you do a canary deployment?

Send a small share of traffic to the new version, watch metrics, then increase it. Ways to do it:

- Basic: two Deployments behind one Service. The traffic split follows the replica ratio (1 canary Pod and 9 stable Pods is about 10%). Rough but needs no extra tools.
- Gateway API `HTTPRoute` with weights on backends
- A service mesh like Istio or Linkerd
- Argo Rollouts or Flagger, which automate the steps and roll back on bad metrics

## 161: What are Argo Rollouts and Flagger?

Both are controllers that add progressive delivery to Kubernetes. Argo Rollouts gives you a `Rollout` resource, used in place of a Deployment, with canary and blue-green steps, traffic shifting through ingress controllers, Gateway API or meshes, and automatic analysis using Prometheus queries. Flagger works with your normal Deployment and creates the canary objects for you. It is often used with Flux.

## 162: How do you make Pods pick up a changed ConfigMap?

Env variables never update in a running container. Mounted files update after a short delay, but the app must reread them. Common approaches:

- Put a hash of the config in a Pod template annotation, so a config change triggers a rollout. Helm charts often do this with `checksum/config`.
- Use Kustomize `configMapGenerator`, which adds a hash suffix to the name and updates references.
- Run `kubectl rollout restart` after changing the ConfigMap.
- Use a tool like Stakater Reloader that restarts workloads when their config changes.

```yaml
template:
  metadata:
    annotations:
      checksum/config:
        {
          {
            include (print $.Template.BasePath "/configmap.yaml") . | sha256sum,
          },
        }
```

## 163: What is the problem with subPath mounts?

A `subPath` mount places a single file or folder from a volume at a path. It is useful for dropping one file into a folder that already has other files. But files mounted with `subPath` from a ConfigMap or Secret are never updated when the source changes. The Pod has to be restarted to see new values.

```yaml
volumeMounts:
  - name: config
    mountPath: /etc/nginx/conf.d/default.conf
    subPath: default.conf
```

## 164: What are immutable ConfigMaps and Secrets?

Setting `immutable: true` stops anyone from changing the data. To change config you create a new object with a new name and point the workload to it. The kubelet also stops watching immutable objects, which takes load off the API server in big clusters.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config-v7
immutable: true
data:
  MODE: prod
```

## 165: What is a projected volume?

A projected volume puts several sources into one folder: Secrets, ConfigMaps, Downward API fields, ServiceAccount tokens and ClusterTrustBundles.

```yaml
volumes:
  - name: app-files
    projected:
      sources:
        - secret:
            name: db-creds
        - configMap:
            name: app-config
        - serviceAccountToken:
            path: vault-token
            audience: vault
            expirationSeconds: 3600
```

## 166: How do you manage secrets without storing them in Git as plain text?

Common options:

- External Secrets Operator: syncs secrets from AWS Secrets Manager, Vault, GCP Secret Manager and others into Kubernetes Secrets.
- Secrets Store CSI Driver: mounts secrets from an external store as files, optionally syncing to a Secret.
- Sealed Secrets: you encrypt a Secret with the cluster's public key and commit the encrypted version. Only the controller in the cluster can decrypt it.
- SOPS: encrypts values in YAML files, used with Flux, Argo CD plugins or Helm plugins.

## 167: How do you enable encryption at rest for Secrets?

You give the API server an `EncryptionConfiguration` file with `--encryption-provider-config`. The best option is a KMS provider (KMS v2), where a cloud KMS or Vault holds the key encryption key.

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources: ["secrets"]
    providers:
      - kms:
          apiVersion: v2
          name: my-kms
          endpoint: unix:///var/run/kms-plugin/socket.sock
      - identity: {}
```

Existing Secrets are only encrypted when they are written again, so rewrite them after enabling it. Managed clusters usually have a checkbox or encrypt by default.

## 168: Which probe settings can you tune?

- `initialDelaySeconds`: wait before the first check (prefer a startup probe for slow apps)
- `periodSeconds`: how often to check (default 10)
- `timeoutSeconds`: how long to wait for an answer (default 1)
- `failureThreshold`: failures in a row before acting (default 3)
- `successThreshold`: successes in a row to count as healthy again (must be 1 for liveness and startup)
- `terminationGracePeriodSeconds`: a shorter grace period used only when a liveness probe kills the container

The default 1 second timeout is a common cause of random restarts under load.

## 169: A Pod is stuck in Pending. How do you debug it?

Run `kubectl describe pod` and read the Events. Usual causes:

- `Insufficient cpu` or `Insufficient memory`: requests too big or the cluster is full
- `didn't match Pod's node affinity/selector`: no node has the needed labels
- `had untolerated taint`: all fitting nodes are tainted
- `pod has unbound immediate PersistentVolumeClaims`: the PVC cannot be bound
- Quota exceeded: the Pod is not even created, look at the ReplicaSet events instead

If the Cluster Autoscaler is running, its events tell you whether it tried to add a node.

## 170: A Service is not reachable. How do you troubleshoot it?

Work from the Pods outward:

```bash
kubectl get pods -l app=web -o wide                      # are Pods running and ready?
kubectl get endpointslices -l kubernetes.io/service-name=web   # does the Service have endpoints?
kubectl get svc web -o yaml                              # selector and ports correct?
kubectl run tmp --rm -it --image=busybox:1.37 -- wget -qO- http://web
```

No endpoints usually means the selector does not match the Pod labels, or the Pods are not ready. Endpoints but no answer usually means a wrong `targetPort`, the app listening on 127.0.0.1 instead of 0.0.0.0, or a NetworkPolicy blocking traffic.

## 171: What is kubectl debug and ephemeral containers?

`kubectl debug` adds a temporary debug container to a running Pod. It is how you debug distroless images that have no shell. With `--target`, the debug container shares the process namespace of the app container, so you can see its processes.

```bash
kubectl debug -it my-pod --image=busybox:1.37 --target=app
```

You can also make a copy of the Pod with a changed image or command:

```bash
kubectl debug my-pod -it --copy-to=my-pod-debug --container=app -- sh
```

## 172: How do you debug a node with kubectl?

`kubectl debug node/<name>` starts a Pod on that node with the host filesystem mounted at `/host`. You can then read logs and config without SSH.

```bash
kubectl debug node/worker-1 -it --image=ubuntu:24.04 --profile=sysadmin
chroot /host
journalctl -u kubelet
```

Delete the debug Pod when you are done.

## 173: How do you debug DNS problems in a cluster?

```bash
kubectl run dnstest --rm -it --image=busybox:1.37 -- nslookup web.default.svc.cluster.local
kubectl -n kube-system get pods -l k8s-app=kube-dns
kubectl -n kube-system logs -l k8s-app=kube-dns
```

Check that CoreDNS Pods are running, that `/etc/resolv.conf` in the Pod points to the cluster DNS IP, and that NetworkPolicies allow UDP and TCP port 53 to CoreDNS. Adding `log` to the Corefile temporarily shows every query.

## 174: What is ndots and why does it matter for DNS performance?

Pods get `options ndots:5` in `/etc/resolv.conf`. Any name with fewer than 5 dots is first tried with each search domain added (`namespace.svc.cluster.local`, `svc.cluster.local`, `cluster.local` and so on) before trying it as-is. A lookup of `api.stripe.com` can therefore cause several failed queries first, which adds latency and load on CoreDNS.

Fixes: use a trailing dot (`api.stripe.com.`), lower ndots per Pod, or run NodeLocal DNSCache.

```yaml
spec:
  dnsConfig:
    options:
      - name: ndots
        value: "2"
```

## 175: What are the Pod dnsPolicy options?

- `ClusterFirst` (default): use cluster DNS, forward unknown names upstream
- `ClusterFirstWithHostNet`: the same, for Pods using `hostNetwork: true`
- `Default`: use the node's DNS settings, so no cluster names
- `None`: ignore everything, use only what is in `dnsConfig`

## 176: How do you get HTTPS certificates for Ingress automatically?

Install cert-manager, create an `Issuer` or `ClusterIssuer` for Let's Encrypt, and add an annotation and a `tls` section to your Ingress. cert-manager gets the certificate, stores it in a Secret and renews it.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: traefik
  tls:
    - hosts: [shop.example.com]
      secretName: shop-tls
  rules:
    - host: shop.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web
                port:
                  number: 80
```

cert-manager also works with the Gateway API.

## 177: What are the Ingress path types?

- `Exact`: matches the path exactly, `/foo` does not match `/foo/`
- `Prefix`: matches by path segments, `/foo` matches `/foo`, `/foo/` and `/foo/bar` but not `/foobar`
- `ImplementationSpecific`: up to the controller, for example regex support

When several paths match, the longest one wins.

## 178: What is an IngressClass?

An IngressClass says which controller should handle an Ingress. You set `spec.ingressClassName` on the Ingress. One class can be marked as default with an annotation, and Ingresses without a class go to it.

```yaml
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: traefik
  annotations:
    ingressclass.kubernetes.io/is-default-class: "true"
spec:
  controller: traefik.io/ingress-controller
```

The old `kubernetes.io/ingress.class` annotation is deprecated.

## 179: How do you route HTTP traffic with the Gateway API?

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: public
  namespace: infra
spec:
  gatewayClassName: envoy
  listeners:
    - name: https
      protocol: HTTPS
      port: 443
      hostname: "*.example.com"
      tls:
        certificateRefs:
          - name: wildcard-tls
      allowedRoutes:
        namespaces:
          from: All
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: shop
  namespace: shop
spec:
  parentRefs:
    - name: public
      namespace: infra
  hostnames: ["shop.example.com"]
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: api
          port: 80
```

The platform team owns the Gateway, and app teams attach their routes to it.

## 180: How do you split traffic between two versions with the Gateway API?

Give each backend a weight in the `HTTPRoute`:

```yaml
rules:
  - backendRefs:
      - name: api-v1
        port: 80
        weight: 90
      - name: api-v2
        port: 80
        weight: 10
```

You can also route by header, for example send requests with `x-canary: true` to v2 for internal testers.

```yaml
- matches:
    - headers:
        - name: x-canary
          value: "true"
  backendRefs:
    - name: api-v2
      port: 80
```

## 181: What is a ReferenceGrant?

In the Gateway API, a route in one namespace cannot point to a Service or Secret in another namespace unless the other namespace allows it. A `ReferenceGrant` in the target namespace gives that permission. This stops one team from routing traffic to another team's Services without their consent.

```yaml
apiVersion: gateway.networking.k8s.io/v1beta1
kind: ReferenceGrant
metadata:
  name: allow-shop-routes
  namespace: payments
spec:
  from:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      namespace: shop
  to:
    - group: ""
      kind: Service
```

## 182: How would you migrate off the retired ingress-nginx controller?

1. List every Ingress and every `nginx.ingress.kubernetes.io/*` annotation you use. Those annotations are the hard part, since other controllers do not understand them.
2. Pick a target: another Ingress controller (Traefik, HAProxy, a cloud controller) or a Gateway API implementation (Envoy Gateway, Istio, Cilium, NGINX Gateway Fabric and others).
3. Use the `ingress2gateway` tool to convert Ingress objects to Gateway API resources as a starting point.
4. Run the new controller next to the old one with a separate IP, test each host, then move DNS over host by host.
5. Remove the old controller once traffic is gone.

Existing ingress-nginx installs keep working, but they get no more security fixes.

## 183: What is externalTrafficPolicy?

It controls how a NodePort or LoadBalancer Service handles outside traffic:

- `Cluster` (default): any node can accept traffic and forward it to a Pod on another node. Load is spread evenly, but the client IP is replaced by the node IP (SNAT).
- `Local`: a node only sends traffic to Pods on itself. The client source IP is kept and there is no extra hop, but nodes without Pods fail the load balancer health check, and spreading can be uneven.

Use `Local` when your app needs the real client IP.

## 184: What is sessionAffinity on a Service?

`sessionAffinity: ClientIP` sends all requests from the same client IP to the same Pod for a while (default 3 hours). It is a simple form of sticky sessions.

```yaml
spec:
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 600
```

It breaks down behind proxies or NAT, where many users share one IP. Storing sessions in Redis or using cookie-based affinity in the ingress is usually better.

## 185: How can you keep Service traffic inside the same zone?

Set `trafficDistribution: PreferClose` on the Service. kube-proxy will prefer endpoints in the same zone as the client when there are healthy ones, which lowers latency and cuts cross-zone data costs.

```yaml
spec:
  trafficDistribution: PreferClose
```

There is also `internalTrafficPolicy: Local`, which only sends traffic to Pods on the same node. It is useful for node-local agents, but traffic is dropped if there is no local Pod.

## 186: What are topology spread constraints?

They spread Pods evenly across zones, nodes or other topology domains, which is more precise than Pod anti-affinity.

```yaml
topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: topology.kubernetes.io/zone
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        app: web
  - maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: ScheduleAnyway
    labelSelector:
      matchLabels:
        app: web
```

`maxSkew: 1` means the number of matching Pods in any two domains can differ by at most one. Spreading is only checked when Pods are scheduled, so the balance can drift later.

## 187: What is a PriorityClass?

A PriorityClass gives Pods a priority number. When the cluster is full, the scheduler can evict (preempt) lower-priority Pods to make room for higher-priority ones. Under node pressure, the kubelet also uses priority when choosing which Pods to evict.

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: critical-api
value: 100000
preemptionPolicy: PreemptLowerPriority
description: "User-facing APIs"
```

```yaml
spec:
  priorityClassName: critical-api
```

Built-in classes `system-cluster-critical` and `system-node-critical` are for cluster components.

## 188: How do you block all traffic by default with NetworkPolicy?

Create a policy that selects all Pods in the namespace and allows nothing. Then add policies that allow only what is needed.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
  namespace: shop
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

Policies are additive. A Pod is allowed a connection if any policy that selects it allows it.

## 189: Why do Pods lose DNS after a default-deny egress policy, and how do you fix it?

Denying all egress also blocks DNS queries to CoreDNS, so every hostname lookup fails. You must allow port 53 to the DNS Pods:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
  namespace: shop
spec:
  podSelector: {}
  policyTypes: [Egress]
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: kube-system
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
        - protocol: TCP
          port: 53
```

## 190: How do you allow traffic from another namespace in a NetworkPolicy?

Use a `namespaceSelector`. Every namespace has the label `kubernetes.io/metadata.name` set automatically.

```yaml
ingress:
  - from:
      - namespaceSelector:
          matchLabels:
            kubernetes.io/metadata.name: monitoring
        podSelector:
          matchLabels:
            app: prometheus
```

Watch the YAML: when `namespaceSelector` and `podSelector` are in the same list item, both must match. If they are two separate items (each with its own `-`), either one is enough. This difference is a common source of policies that allow too much.

## 191: What are the Pod Security Standards?

They are three predefined security levels for Pods:

- `privileged`: no restrictions
- `baseline`: blocks known privilege escalations like host namespaces, privileged containers and hostPath
- `restricted`: follows hardening best practices: must run as non-root, drop all capabilities, use a seccomp profile, no privilege escalation

They replaced PodSecurityPolicy, which was removed in 1.25.

## 192: How do you enforce Pod Security Standards?

The built-in Pod Security Admission controller reads labels on namespaces. Each level can be applied in three modes: `enforce` (reject), `audit` (log) and `warn` (show a warning to the user).

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: shop
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/warn: restricted
```

A good way to roll it out is to start with `warn` and `audit`, fix the workloads, then turn on `enforce`.

## 193: What securityContext settings should most containers have?

```yaml
securityContext: # Pod level
  runAsNonRoot: true
  runAsUser: 10001
  runAsGroup: 10001
  fsGroup: 10001
  seccompProfile:
    type: RuntimeDefault
containers:
  - name: app
    image: my-app:1.0
    securityContext: # container level
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
```

This meets the `restricted` Pod Security Standard. If the app needs to write files, mount an `emptyDir` at that path.

## 194: Why use readOnlyRootFilesystem?

If an attacker gets code running in your container, they cannot change binaries or drop tools on the filesystem. It also forces you to know exactly where your app writes, such as `/tmp` or a cache folder, which you then back with `emptyDir` volumes.

```yaml
volumeMounts:
  - name: tmp
    mountPath: /tmp
volumes:
  - name: tmp
    emptyDir: {}
```

## 195: What are Linux capabilities in a Pod spec?

Capabilities split root's powers into small pieces, like `NET_BIND_SERVICE` (bind ports below 1024) or `SYS_ADMIN` (a lot of things). The best practice is to drop all of them and add back only what the app needs.

```yaml
securityContext:
  capabilities:
    drop: ["ALL"]
    add: ["NET_BIND_SERVICE"]
```

The `restricted` standard only allows adding `NET_BIND_SERVICE`.

## 196: What does seccompProfile RuntimeDefault do?

Seccomp filters which Linux system calls a process may make. `RuntimeDefault` uses the container runtime's default profile, which blocks dangerous and rarely used syscalls such as those for loading kernel modules. Without it, Pods run `Unconfined` unless the kubelet is set to use `RuntimeDefault` by default. Almost all apps work fine with it.

## 197: Why disable automountServiceAccountToken?

By default, every Pod gets a token for its ServiceAccount mounted at `/var/run/secrets/kubernetes.io/serviceaccount/`. Most apps never call the Kubernetes API, so the token is only useful to an attacker who breaks into the container.

```yaml
spec:
  automountServiceAccountToken: false
```

You can set it on the ServiceAccount or the Pod. The Pod setting wins.

## 198: How are ServiceAccount tokens issued today?

Pods get bound tokens through the TokenRequest API. They are short-lived (about an hour by default), tied to the Pod (invalid once the Pod is deleted) and have a set audience. The kubelet refreshes them automatically.

The old style, long-lived tokens stored in Secrets, is no longer created automatically since 1.24. Create one yourself only if you really need a token that never expires, and prefer `kubectl create token` for short-lived ones:

```bash
kubectl create token ci-deployer --duration=1h -n ci
```

## 199: How do Pods get access to cloud services without static keys?

With workload identity. The cloud trusts the cluster's ServiceAccount tokens (OIDC) and maps a ServiceAccount to a cloud identity:

- AWS: IAM Roles for Service Accounts (IRSA) or EKS Pod Identity
- GCP: Workload Identity Federation for GKE
- Azure: Microsoft Entra Workload ID

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: uploader
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/s3-uploader
```

The cloud SDK in the Pod picks up the credentials automatically. Nothing secret is stored in the cluster.

## 200: What are the default user-facing ClusterRoles?

- `cluster-admin`: full access to everything
- `admin`: full access within a namespace, including RBAC there, when bound with a RoleBinding
- `edit`: read and write most objects in a namespace, but not roles or bindings
- `view`: read-only access to most objects, but not Secrets

`admin`, `edit` and `view` are aggregated roles. If you add a ClusterRole with a label like `rbac.authorization.k8s.io/aggregate-to-edit: "true"`, its rules are merged into `edit`, which is how CRD permissions reach normal users.

## 201: What does a Helm chart look like?

```
mychart/
  Chart.yaml          # name, version, appVersion, dependencies
  values.yaml         # default values
  values.schema.json  # optional JSON schema to validate values
  templates/
    deployment.yaml
    service.yaml
    _helpers.tpl      # reusable template snippets
    NOTES.txt         # printed after install
  charts/             # dependency charts
```

`version` in `Chart.yaml` is the chart's version, `appVersion` is the version of the app it deploys.

## 202: How does templating work in Helm?

Templates use Go templates with extra functions from the Sprig library. You read values with `.Values`, release info with `.Release`, and chart info with `.Chart`.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "mychart.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: app
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          {{- with .Values.resources }}
          resources:
            {{- toYaml . | nindent 12 }}
          {{- end }}
```

`{{-` trims whitespace, and `nindent` fixes indentation, which is where most Helm bugs come from.

## 203: What are Helm hooks?

Hooks let you run resources at certain points in a release: `pre-install`, `post-install`, `pre-upgrade`, `post-upgrade`, `pre-delete` and so on. A typical use is a Job that runs database migrations before the upgrade.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: migrate
  annotations:
    "helm.sh/hook": pre-upgrade,pre-install
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
```

Hook resources are not managed as part of the release, so Helm does not delete them on uninstall unless a delete policy says so.

## 204: How do you check a Helm chart before installing it?

```bash
helm lint ./mychart
helm template my-release ./mychart -f values-prod.yaml   # render locally
helm install my-release ./mychart --dry-run=server        # validate against the cluster
helm diff upgrade my-release ./mychart -f values-prod.yaml  # needs the helm-diff plugin
```

`helm template` piped into a schema checker like kubeconform is a common CI step.

## 205: When would you pick Helm over Kustomize?

Helm is better when you package something for many users with many options, need versioned releases, or install third-party software (most projects ship a Helm chart). Kustomize is better for your own apps when you want plain YAML and a few differences per environment, with no template language to learn.

Many teams use both: Helm for third-party charts and Kustomize for their own services. Kustomize can even render Helm charts with `helmCharts`.

## 206: What does configMapGenerator do in Kustomize?

It builds a ConfigMap from files or literals and adds a hash of the content to the name, like `app-config-7f9c2kd8bh`. Kustomize updates all references to it. When the content changes, the name changes, the Pod template changes, and a rollout happens automatically.

```yaml
configMapGenerator:
  - name: app-config
    files:
      - config.json
    literals:
      - LOG_LEVEL=info
```

`secretGenerator` does the same for Secrets.

## 207: What is GitOps?

GitOps means Git is the source of truth for what runs in the cluster. An agent running in the cluster watches a Git repo and keeps applying it, fixing any drift. You deploy by merging a pull request, and you roll back by reverting a commit.

Benefits: a full history of changes, code review for deployments, and no CI system needing admin credentials to the cluster.

## 208: What is Argo CD?

Argo CD is a GitOps tool for Kubernetes. You define `Application` objects that point to a Git path (plain YAML, Kustomize or Helm) and a target cluster and namespace. Argo CD shows sync status and drift in a web UI, can sync automatically, prune deleted resources and self-heal manual changes.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: shop
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/acme/deploy
    path: shop/overlays/prod
    targetRevision: main
  destination:
    server: https://kubernetes.default.svc
    namespace: shop
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

`ApplicationSet` generates many Applications, for example one per cluster or per folder.

## 209: What is Flux?

Flux is another CNCF GitOps tool. It is a set of controllers driven by CRDs: `GitRepository` or `OCIRepository` for sources, `Kustomization` for applying manifests and `HelmRelease` for Helm charts. It has no built-in web UI and is managed fully through Git and the `flux` CLI. It also has image automation controllers that can commit new image tags back to Git.

## 210: How do you manage several environments like dev, staging and prod?

A common layout:

- Separate clusters for prod and non-prod (or at least separate namespaces with strict RBAC)
- One base set of manifests or one Helm chart
- Per-environment overlays or values files holding only what differs: replicas, resources, hostnames, image tags
- Promotion by changing the image tag in the next environment's folder, through a pull request

Avoid long-lived branches per environment, they drift apart and merges get painful.

## 211: What does a typical CI/CD pipeline for Kubernetes look like?

1. CI builds and tests the code, builds the image and pushes it with an immutable tag (the Git SHA).
2. CI scans the image and maybe signs it.
3. The new tag is written to the deployment repo, either by CI or by an image updater.
4. Argo CD or Flux applies the change to the cluster.
5. The rollout is watched, and a failed rollout or bad metrics lead to a rollback.

In push-style pipelines, CI runs `kubectl apply` or `helm upgrade` itself, which is simpler but means CI needs cluster credentials.

## 212: How do volumeClaimTemplates work in a StatefulSet?

Each StatefulSet Pod gets its own PVC made from the template, named `<template>-<statefulset>-<ordinal>`, for example `data-db-0`. If `db-0` is rescheduled to another node, it gets the same PVC back.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db
spec:
  serviceName: db
  replicas: 3
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
        - name: postgres
          image: postgres:18
          volumeMounts:
            - name: data
              mountPath: /var/lib/postgresql
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: [ReadWriteOnce]
        resources:
          requests:
            storage: 20Gi
```

By default, PVCs are kept when you scale down or delete the StatefulSet. `persistentVolumeClaimRetentionPolicy` lets you change that.

## 213: How do StatefulSet updates work?

With the default `RollingUpdate` strategy, Pods are updated one at a time in reverse order, from the highest ordinal to the lowest. Each must be ready before the next one is updated.

The `partition` setting lets you update only Pods with an ordinal at or above a number, which is a simple canary:

```yaml
updateStrategy:
  type: RollingUpdate
  rollingUpdate:
    partition: 2 # only db-2 gets the new version
```

The `OnDelete` strategy only updates a Pod when you delete it by hand.

## 214: What is podManagementPolicy in a StatefulSet?

- `OrderedReady` (default): Pods are created one by one in order, each waits for the previous one to be ready. Deletion is in reverse order.
- `Parallel`: Pods are created and deleted all at once.

`Parallel` is useful when members do not depend on start order, for example some Kafka or Elasticsearch setups, and makes scaling much faster. It only affects scaling, not updates.

## 215: Should you run databases on Kubernetes?

It can work well, but it is more work than a managed database. You need a good storage class, backups, monitoring, upgrade procedures and people who understand both the database and Kubernetes.

Reasons to do it: no managed option in your environment, cost at scale, or wanting one platform everywhere. Use a mature operator such as CloudNativePG for PostgreSQL. For small teams, a managed database like RDS or Cloud SQL is usually the better choice.

## 216: What is an Operator?

An Operator is a custom controller plus custom resources that encode how to run a specific piece of software. Instead of writing a StatefulSet, Services and backup CronJobs for Postgres yourself, you create a `Cluster` object and the operator handles setup, failover, backups and upgrades.

Examples: CloudNativePG, Strimzi (Kafka), Prometheus Operator, cert-manager. You can write your own with Kubebuilder or Operator SDK.

## 217: What is a CustomResourceDefinition?

A CRD adds a new resource type to the Kubernetes API. After you apply it, you can create, list and watch objects of that type with kubectl just like built-in ones. The CRD includes an OpenAPI schema for validation.

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: backups.example.com
spec:
  group: example.com
  scope: Namespaced
  names:
    kind: Backup
    plural: backups
    singular: backup
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                schedule:
                  type: string
```

A CRD on its own only stores data. A controller has to act on it.

## 218: How do you make a PersistentVolumeClaim bigger?

If the StorageClass has `allowVolumeExpansion: true`, edit the PVC and raise `spec.resources.requests.storage`. The CSI driver grows the disk and the filesystem, usually while the Pod keeps running.

```bash
kubectl patch pvc data -p '{"spec":{"resources":{"requests":{"storage":"50Gi"}}}}'
```

Shrinking a volume is not supported. For StatefulSets, you have to patch each PVC, because changing `volumeClaimTemplates` has no effect on existing PVCs.

## 219: What are VolumeSnapshots?

They are a standard API for taking point-in-time snapshots of PVCs through the CSI driver. You can create a new PVC from a snapshot. `VolumeGroupSnapshot` (stable since 1.36) snapshots several volumes at the same moment, which matters for apps that spread data over several disks.

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: data-snap
spec:
  volumeSnapshotClassName: csi-snapclass
  source:
    persistentVolumeClaimName: data
```

The snapshot CRDs and controller must be installed, which managed clusters often do for you.

## 220: What is volumeBindingMode WaitForFirstConsumer?

With `Immediate`, the volume is created as soon as the PVC exists, maybe in a zone where the Pod cannot run. With `WaitForFirstConsumer`, the volume is created only when a Pod using it is scheduled, in that Pod's zone. For zonal storage like EBS or Persistent Disk, `WaitForFirstConsumer` avoids Pods stuck because their disk is in another zone.

## 221: What are PV reclaim policies?

When a PVC is deleted, the reclaim policy decides what happens to the PV and the disk:

- `Delete`: the PV and the real disk are deleted. Default for dynamically created volumes.
- `Retain`: the PV stays in `Released` state and the data is kept. An admin must clean it up or reuse it by hand.

Use `Retain` for important data, so a mistaken `kubectl delete` does not wipe it.

## 222: A PVC is stuck in Pending. What do you check?

```bash
kubectl describe pvc data
kubectl get storageclass
```

Common causes:

- No default StorageClass, and the PVC does not name one
- The StorageClass uses `WaitForFirstConsumer`, so the PVC stays Pending until a Pod uses it (this is normal)
- The CSI driver is not installed or its Pods are failing
- Asking for an access mode the driver does not support, like RWX on block storage
- Cloud quota or permission errors, which show up in the events or the CSI controller logs

## 223: How do parallelism and completions work in a Job?

- `completions`: how many Pods must finish successfully
- `parallelism`: how many Pods may run at the same time

```yaml
spec:
  completions: 10
  parallelism: 3
  completionMode: Indexed
```

With `completionMode: Indexed`, each Pod gets a number from 0 to 9 in the `JOB_COMPLETION_INDEX` env variable, so it knows which slice of work to do.

## 224: How do you clean up finished Jobs and stop Jobs that run too long?

- `ttlSecondsAfterFinished`: delete the Job and its Pods this many seconds after it finishes
- `activeDeadlineSeconds`: fail the Job if it runs longer than this, killing its Pods

```yaml
spec:
  ttlSecondsAfterFinished: 3600
  activeDeadlineSeconds: 1800
  backoffLimit: 4
```

## 225: What is a Pod failure policy in a Job?

It lets a Job treat failures differently based on the exit code or Pod condition. For example, fail the whole Job right away on a known bug exit code, but do not count Pods that were evicted because of node maintenance.

```yaml
spec:
  backoffLimit: 6
  podFailurePolicy:
    rules:
      - action: FailJob
        onExitCodes:
          containerName: main
          operator: In
          values: [42]
      - action: Ignore
        onPodConditions:
          - type: DisruptionTarget
```

For Indexed Jobs, `backoffLimitPerIndex` gives each index its own retry budget.

## 226: Which CronJob settings matter in practice?

- `concurrencyPolicy`: `Allow` (default), `Forbid` (skip a run if the last one is still going) or `Replace` (kill the old run)
- `startingDeadlineSeconds`: skip a run if it could not start within this time, for example after the controller was down
- `successfulJobsHistoryLimit` and `failedJobsHistoryLimit`: how many old Jobs to keep
- `timeZone`: run the schedule in a named time zone instead of the controller's local time
- `suspend: true`: pause the schedule

CronJobs can occasionally run twice or skip a run, so make the work idempotent.

## 227: How do you pause a Job or CronJob?

Set `spec.suspend: true`. For a CronJob, no new Jobs are created. For a Job, running Pods are terminated, and they are created again when you set it back to false.

```bash
kubectl patch cronjob nightly-report -p '{"spec":{"suspend":true}}'
```

Queue systems like Kueue use Job suspension to hold Jobs until there is capacity.

## 228: How do you stop an HPA from scaling up and down too often?

Use the `behavior` section to set stabilization windows and rate limits.

```yaml
spec:
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 50
          periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Pods
          value: 4
          periodSeconds: 30
```

The default scale-down window is 300 seconds. Recent versions also let you set a `tolerance` per direction, so small metric changes are ignored.

## 229: How do you scale on custom metrics like requests per second?

The HPA reads custom metrics through the `custom.metrics.k8s.io` or `external.metrics.k8s.io` APIs. Something has to serve those APIs, usually Prometheus Adapter or KEDA.

```yaml
metrics:
  - type: Pods
    pods:
      metric:
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: "100"
```

Request-based metrics often react better than CPU for web apps, because CPU can be low while requests queue up.

## 230: What is KEDA?

KEDA (Kubernetes Event-Driven Autoscaling) scales workloads based on events from many sources: queue length in RabbitMQ, SQS or Kafka lag, Prometheus queries, cron schedules and more. It creates and feeds an HPA behind the scenes and can scale to zero when there is no work.

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: worker
spec:
  scaleTargetRef:
    name: worker
  minReplicaCount: 0
  maxReplicaCount: 50
  triggers:
    - type: rabbitmq
      metadata:
        queueName: jobs
        mode: QueueLength
        value: "20"
      authenticationRef:
        name: rabbitmq-auth
```

## 231: What is the VerticalPodAutoscaler?

The VPA watches resource usage and recommends or sets CPU and memory requests. It is a separate project you install. Its update modes include:

- `Off`: only recommends, you read the values and apply them yourself
- `Initial`: sets requests only when Pods are created
- `Recreate`: evicts Pods to apply new values
- `InPlaceOrRecreate`: tries to resize running Pods in place, and evicts only when that is not possible

Many teams run it in `Off` mode just to right-size their requests.

## 232: What is in-place Pod resize?

Since Kubernetes 1.35 (stable), you can change the CPU and memory of a running Pod's containers without recreating the Pod. You update the Pod through the `resize` subresource.

```bash
kubectl patch pod api-7d9f --subresource resize --patch \
  '{"spec":{"containers":[{"name":"api","resources":{"requests":{"cpu":"800m"},"limits":{"cpu":"1"}}}]}}'
```

`resizePolicy` on a container says whether a change needs a container restart. CPU changes usually do not. Memory changes may, depending on the app. If the node has no room, the resize stays pending and Kubernetes retries it.

## 233: Can you use HPA and VPA on the same workload?

Not on the same metric. If the HPA scales on CPU utilization and the VPA changes CPU requests, they fight each other, because utilization is measured against the request. It is fine if the HPA scales on a custom metric like requests per second while the VPA manages CPU and memory, or if the VPA only gives recommendations.

## 234: What is the difference between Cluster Autoscaler and Karpenter?

The Cluster Autoscaler scales existing node groups up or down. You define the groups and their instance types in advance. Karpenter looks at pending Pods and launches the best-fitting instances directly, with no fixed groups. It can mix instance types, use spot instances, and consolidate workloads onto fewer or cheaper nodes. Karpenter started on AWS and now has providers for other clouds, including Azure.

## 235: How do you monitor a Kubernetes cluster?

The common stack is Prometheus for metrics, Grafana for dashboards and Alertmanager for alerts. The kube-prometheus-stack Helm chart installs them together with:

- node-exporter for node metrics
- kube-state-metrics for object state (Deployments, Pods, Jobs)
- kubelet and cAdvisor metrics for containers
- ready-made dashboards and alert rules

Managed options include Amazon Managed Prometheus, Google Managed Prometheus and Grafana Cloud.

## 236: What is a ServiceMonitor?

It is a custom resource from the Prometheus Operator that tells Prometheus which Services to scrape and how. You do not edit the Prometheus config file by hand.

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: api
  labels:
    release: kube-prometheus-stack
spec:
  selector:
    matchLabels:
      app: api
  endpoints:
    - port: metrics
      interval: 30s
```

`PodMonitor` does the same for Pods without a Service. The label must match what the Prometheus instance selects, which is a common reason a ServiceMonitor gets ignored.

## 237: How does logging work in Kubernetes?

Containers write to stdout and stderr. The container runtime saves that to files on the node under `/var/log/pods`, and the kubelet rotates them. `kubectl logs` reads those files.

Kubernetes does not keep logs long term. You run a log agent as a DaemonSet (Fluent Bit, Vector, the OpenTelemetry Collector, Grafana Alloy) that reads the files, adds Pod labels and ships them to a backend like Loki, Elasticsearch or a cloud logging service. Logs as JSON make searching much easier.

## 238: What is the difference between metrics-server and kube-state-metrics?

- metrics-server reports current CPU and memory usage of Pods and nodes, for autoscaling and `kubectl top`.
- kube-state-metrics turns object state into Prometheus metrics: desired versus available replicas, Pod phases, restart counts, Job results, resource requests.

You usually want both: one for autoscaling and one for monitoring and alerts.

## 239: How do you add distributed tracing to apps on Kubernetes?

Instrument the apps with OpenTelemetry SDKs (or auto-instrumentation), send spans to an OpenTelemetry Collector running in the cluster, and export them to a backend like Jaeger, Tempo or a vendor. The OpenTelemetry Operator can inject auto-instrumentation into Pods through an annotation:

```yaml
metadata:
  annotations:
    instrumentation.opentelemetry.io/inject-nodejs: "true"
```

The Collector can also add Kubernetes metadata such as Pod, namespace and node to every span.

## 240: Which alerts should every cluster have?

- Pods in CrashLoopBackOff or restarting often
- Deployments with fewer available replicas than wanted for a while
- Nodes not ready, or under memory, disk or PID pressure
- PVCs almost full
- Jobs failing, CronJobs not running when they should
- High CPU throttling or OOM kills
- Certificates close to expiry
- API server errors and latency, etcd health

Alert on symptoms users feel (error rate, latency) first, and use the rest to find causes.

## 241: What is node-pressure eviction?

When a node runs low on memory, disk or PIDs, the kubelet evicts Pods to protect the node. It picks Pods based on whether their usage is above their requests, then on priority, then on how much over they are. So BestEffort and Burstable Pods using more than they asked for go first.

Thresholds are set in the kubelet config, such as `memory.available<100Mi` for hard eviction. Evicted Pods show status `Evicted` and their controller creates replacements.

## 242: What is node allocatable?

Not all of a node's capacity is available to Pods. The kubelet subtracts resources for the OS (`systemReserved`), for Kubernetes daemons (`kubeReserved`) and the eviction threshold. What is left is the allocatable amount the scheduler uses.

```bash
kubectl describe node worker-1 | grep -A 6 Allocatable
```

Without reservations, Pods can starve the kubelet and the container runtime, and the whole node can become unstable.

## 243: What is ephemeral storage and why should you set it?

Ephemeral storage is node disk used by containers: writable layers, logs and `emptyDir` volumes (not memory-backed ones). If a Pod fills the disk, the whole node gets disk pressure. You can request and limit it like CPU and memory:

```yaml
resources:
  requests:
    ephemeral-storage: 1Gi
  limits:
    ephemeral-storage: 4Gi
```

A Pod that goes over its limit is evicted.

## 244: What are the recommended labels for Kubernetes objects?

The `app.kubernetes.io` labels are a common standard that tools understand:

```yaml
metadata:
  labels:
    app.kubernetes.io/name: api
    app.kubernetes.io/instance: api-prod
    app.kubernetes.io/version: "1.8.2"
    app.kubernetes.io/component: backend
    app.kubernetes.io/part-of: shop
    app.kubernetes.io/managed-by: helm
```

Keep labels that change often, like `version`, out of Deployment selectors, because selectors cannot be changed after creation.

## 245: What are field selectors?

Field selectors filter by fields of the object instead of labels. Only some fields are supported, like `metadata.name`, `metadata.namespace`, `status.phase` and `spec.nodeName`.

```bash
kubectl get pods -A --field-selector status.phase=Failed
kubectl get pods -A --field-selector spec.nodeName=worker-2
kubectl delete pods --field-selector status.phase=Succeeded
```

## 246: What are the kinds of kubectl patch?

- `--type=strategic` (default): understands Kubernetes lists, for example merges containers by `name`
- `--type=merge`: a JSON merge patch. Lists are replaced as a whole.
- `--type=json`: a JSON Patch with explicit operations

```bash
kubectl patch deploy web -p '{"spec":{"replicas":4}}'
kubectl patch deploy web --type=json -p '[{"op":"replace","path":"/spec/template/spec/containers/0/image","value":"web:1.6"}]'
```

Strategic merge patch does not work on custom resources. Use merge or JSON patch for those.

## 247: What is server-side apply?

With server-side apply, the API server does the merge and tracks which manager owns which field (`managedFields`). If two tools try to set the same field to different values, you get a conflict instead of one silently overwriting the other.

```bash
kubectl apply --server-side -f deployment.yaml
kubectl apply --server-side --force-conflicts -f deployment.yaml
```

Controllers and GitOps tools use it so they can share objects safely. It also avoids the size limit of the `last-applied-configuration` annotation that client-side apply uses.

## 248: How do you wait for something in a script?

`kubectl wait` blocks until a condition is true or a timeout runs out.

```bash
kubectl wait --for=condition=available deployment/web --timeout=120s
kubectl wait --for=condition=complete job/migrate --timeout=300s
kubectl wait --for=delete pod/old-pod --timeout=60s
kubectl wait --for=jsonpath='{.status.phase}'=Running pod/db-0
```

It is much better than `sleep` in CI scripts.

## 249: How do you find the Pods using the most memory or restarting the most?

```bash
kubectl top pods -A --sort-by=memory | head
kubectl get pods -A --sort-by='.status.containerStatuses[0].restartCount'
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{.status.containerStatuses[0].restartCount}{"\n"}{end}'
```

For anything regular, use Prometheus queries instead of kubectl one-liners.

## 250: What are kubectl plugins and krew?

Any executable on your PATH named `kubectl-<name>` becomes `kubectl <name>`. krew is a package manager for these plugins. Popular ones:

- `ctx` and `ns`: switch contexts and namespaces quickly
- `neat`: removes clutter from `kubectl get -o yaml`
- `tree`: shows owner relationships
- `stern`: tails logs from many Pods at once

```bash
kubectl krew install ctx ns neat
kubectl ns shop
```

## 251: What is the .kuberc file?

`~/.kube/kuberc` holds your personal kubectl preferences, kept apart from the kubeconfig that holds clusters and credentials. You can define aliases and default flags, for example always using server-side apply or interactive delete. It is enabled by default in recent versions and can be turned off with `KUBECTL_KUBERC=false`.

```yaml
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
defaults:
  - command: delete
    options:
      - name: interactive
        default: "true"
aliases:
  - name: getn
    command: get
    options:
      - name: output
        default: wide
```

## 252: How do you work with many clusters from one machine?

- Cloud CLIs add entries to your kubeconfig: `aws eks update-kubeconfig`, `gcloud container clusters get-credentials`, `az aks get-credentials`.
- `KUBECONFIG` can list several files separated by `:` and kubectl merges them.
- Use clear context names like `prod-eu` and `staging-us`.
- Show the current context in your shell prompt so you do not run a command against prod by mistake.

```bash
export KUBECONFIG=~/.kube/config:~/.kube/prod-eu.yaml
kubectl config get-contexts
kubectl --context prod-eu get nodes
```

## 253: How would you organize namespaces for several teams?

A common pattern is one namespace per team per app or per environment, like `payments-prod` and `payments-staging`. For each namespace, set:

- RoleBindings giving the team access
- A ResourceQuota and LimitRange
- Default-deny NetworkPolicies plus the needed allows
- Pod Security labels
- Labels for cost reporting (team, cost center)

Avoid putting everything in `default`, and avoid one huge shared namespace.

## 254: What is multi-tenancy in Kubernetes and what are its limits?

Multi-tenancy means several teams or customers share one cluster. Soft multi-tenancy (trusted internal teams) uses namespaces, RBAC, quotas, NetworkPolicies and Pod Security. That is usually enough inside one company.

Hard multi-tenancy (untrusted tenants) is harder because all tenants share the kernel, the control plane and cluster-wide objects like CRDs. Options are separate clusters, virtual clusters (vCluster) that give each tenant its own API server, or sandboxed runtimes like gVisor or Kata Containers.

## 255: How do you reduce the cost of a Kubernetes cluster?

- Right-size requests. Over-requesting is the biggest waste, since nodes fill up on paper while sitting idle.
- Use autoscaling for both Pods (HPA, KEDA) and nodes (Cluster Autoscaler, Karpenter).
- Use spot or preemptible instances for workloads that tolerate interruptions.
- Scale dev and staging environments down at night.
- Use cheaper instance types, such as ARM (Graviton, Ampere), with multi-arch images.
- Keep traffic in the same zone and clean up unused PVCs and load balancers.
- Track cost per namespace with tools like OpenCost or Kubecost.

## 256: How do you run workloads on spot instances safely?

Spot nodes can be taken away with short notice (2 minutes on AWS). To use them:

- Run only stateless, replicated workloads there, and keep enough replicas on on-demand nodes.
- Use several instance types and zones to lower the chance of losing everything at once.
- Install a termination handler (Karpenter and managed node groups have one built in) so nodes are drained when the notice comes.
- Handle SIGTERM properly and keep shutdown short.
- Use taints and tolerations or node affinity to control which workloads may go there.

## 257: What are node pools and why use several?

A node pool (node group) is a set of nodes with the same instance type and config. Several pools let you separate workloads: general purpose, memory-heavy, GPU, spot, or system add-ons. You steer Pods with labels, taints and tolerations.

```yaml
nodeSelector:
  pool: memory-optimized
tolerations:
  - key: pool
    value: memory-optimized
    effect: NoSchedule
```

## 258: How do Pods use GPUs?

Traditionally through a device plugin, like the NVIDIA one, which advertises `nvidia.com/gpu` as a resource on the node. Pods request it in limits:

```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```

GPUs cannot be overcommitted or shared by default. Dynamic Resource Allocation (DRA) is the newer, more flexible way: Pods ask for devices through `ResourceClaim` objects, which can describe GPU models, memory, sharing and partitions. The NVIDIA GPU Operator installs drivers, the device plugin and monitoring for you.

## 259: Can Kubernetes run Windows containers?

Yes. The control plane always runs on Linux, but you can add Windows worker nodes. Windows Pods must be scheduled only on Windows nodes, which you do with the `kubernetes.io/os: windows` node selector. Some features differ, for example there is no privileged mode, and some volume types and networking options are limited.

```yaml
nodeSelector:
  kubernetes.io/os: windows
```

## 260: What is a service mesh?

A service mesh handles service-to-service traffic for you: mutual TLS, retries, timeouts, traffic splitting, and metrics and tracing for every call, without code changes. It works by putting a proxy in the traffic path, either as a sidecar in every Pod or as a per-node proxy.

Popular meshes are Istio, Linkerd and Cilium Service Mesh. They add moving parts and some latency, so use one when you actually need those features across many services.

## 261: What is the difference between sidecar mode and ambient mode in Istio?

In sidecar mode, every Pod gets an Envoy proxy container. You get full features per Pod, but every Pod uses extra CPU and memory, and mesh upgrades need Pod restarts.

In ambient mode, a per-node proxy called ztunnel handles mTLS and basic layer 4 traffic, and optional waypoint proxies handle layer 7 features like HTTP routing for the services that need them. It uses fewer resources and needs no Pod changes. Ambient mode is stable in current Istio releases.

## 262: How do you get mutual TLS between services?

The easiest way is a service mesh, which issues certificates to each workload and encrypts traffic between proxies automatically. Without a mesh, you can use cert-manager to issue certificates to apps and configure TLS in the apps yourself. Some CNI plugins, like Cilium and Calico, can encrypt all Pod traffic between nodes with WireGuard or IPsec, which gives encryption but not per-service identity.

## 263: How should an app design its health endpoints for Kubernetes?

- `/healthz` for liveness: checks only that the process is not stuck. It should be fast and must not call databases or other services.
- `/ready` for readiness: checks that the app can do its job. It can check that config is loaded and connection pools are open. Be careful with deep dependency checks, because if a shared dependency fails, all Pods turn unready at once and the Service has no endpoints.
- On SIGTERM, make readiness fail, keep serving for a moment, then shut down.

Keep these endpoints off the public ingress.

## 264: How does the twelve-factor app approach fit Kubernetes?

Most of the factors map directly:

- Config in the environment: ConfigMaps and Secrets
- Backing services as attached resources: Services and external endpoints
- Stateless processes: Deployments, with state in databases and volumes
- Port binding: containerPort and Services
- Concurrency: horizontal scaling with replicas
- Disposability: fast start, graceful SIGTERM handling
- Logs as event streams: write to stdout
- Admin processes: Jobs

Apps built this way are much easier to run on Kubernetes.

## 265: How do you run database migrations when deploying to Kubernetes?

Options:

- A Job that runs before the new version is rolled out, triggered by the pipeline, a Helm pre-upgrade hook or an Argo CD PreSync hook
- An init container in the app Pod (simple, but every replica tries to run it, so the migration tool must use a lock)
- A separate migration step in CI

Whichever you use, make migrations backward compatible (expand and contract), because during a rolling update old and new versions run at the same time against the same database.

## 266: What tools help with local development on Kubernetes?

- Skaffold: watches your code, rebuilds images and redeploys to a local or remote cluster
- Tilt: similar, with a web UI and a config written in Starlark
- Telepresence and mirrord: run your service on your laptop while it talks to a remote cluster as if it ran inside it
- Docker Compose for simple local work, with Kubernetes only in shared environments

Using kind or k3d locally keeps the feedback loop short.

## 267: How do you validate manifests in CI?

- `kubeconform` checks manifests against the Kubernetes and CRD schemas
- `kubectl apply --dry-run=server` checks against a real API server, including admission
- `conftest` (OPA) or `kyverno test` check your own rules, like "every Deployment must set resources"
- `helm lint` and `helm template` for charts
- Tools like Trivy or Checkov find security issues in manifests

```bash
kustomize build overlays/prod | kubeconform -strict -summary -
```

## 268: What are Kyverno and OPA Gatekeeper?

Both are policy engines that run as admission webhooks and can block, change or audit objects.

- Kyverno writes policies as Kubernetes YAML and can also mutate objects, generate new objects and verify image signatures.
- Gatekeeper uses OPA and the Rego language. It is very flexible but has a steeper learning curve.

Typical policies: require resource limits, block the `latest` tag, allow only trusted registries, require certain labels.

## 269: What are ValidatingAdmissionPolicy and MutatingAdmissionPolicy?

They are built-in admission policies written in CEL (Common Expression Language) that run inside the API server, so there is no webhook to deploy and keep available. ValidatingAdmissionPolicy is stable since 1.30 and MutatingAdmissionPolicy is stable since 1.36.

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicy
metadata:
  name: max-replicas
spec:
  failurePolicy: Fail
  matchConstraints:
    resourceRules:
      - apiGroups: ["apps"]
        apiVersions: ["v1"]
        operations: ["CREATE", "UPDATE"]
        resources: ["deployments"]
  validations:
    - expression: "object.spec.replicas <= 20"
      message: "replicas must be 20 or less"
```

You attach it with a `ValidatingAdmissionPolicyBinding`, which says where it applies.

## 270: How does garbage collection with owner references work?

Objects created by a controller get an `ownerReferences` entry pointing to their owner: a Pod points to its ReplicaSet, the ReplicaSet points to its Deployment. When the owner is deleted, the garbage collector deletes the dependents.

```bash
kubectl delete deployment web                          # background cascade (default)
kubectl delete deployment web --cascade=foreground     # wait for children first
kubectl delete deployment web --cascade=orphan         # leave the ReplicaSet and Pods
```

## 271: A Pod is stuck in Terminating. What do you do?

First find out why:

- The node is down or unreachable, so the kubelet cannot confirm the deletion
- A finalizer on the Pod is not removed
- The app ignores SIGTERM and the grace period is very long
- A volume cannot be unmounted

```bash
kubectl describe pod my-pod
kubectl get pod my-pod -o jsonpath='{.metadata.finalizers}'
```

As a last resort, `kubectl delete pod my-pod --grace-period=0 --force` removes it from the API. Be careful with StatefulSet Pods: if the old Pod is still running on a cut-off node, a new one with the same identity may start and both may write to the same data.

## 272: A namespace is stuck in Terminating. Why?

A namespace is deleted only after all objects in it are gone. Usually something blocks that:

- An object with a finalizer whose controller is no longer running, often a CRD instance after the operator was uninstalled
- An API service (like metrics-server) that is down, so the namespace controller cannot list all resource types

```bash
kubectl get namespace shop -o jsonpath='{.status.conditions}'
kubectl api-resources --verbs=list --namespaced -o name | xargs -n 1 kubectl get -n shop --ignore-not-found
```

Fix the cause, such as reinstalling the operator or removing the stuck finalizers, instead of forcing the namespace's own finalizer away.

## 273: What do common container exit codes mean?

- `0`: finished successfully
- `1`: general app error
- `126`: command found but not executable
- `127`: command not found, often a wrong `command` or a missing binary
- `137`: killed with SIGKILL (128 + 9), usually OOMKilled or a timeout after SIGTERM
- `139`: segmentation fault
- `143`: exited after SIGTERM (128 + 15), normal during shutdown

`kubectl describe pod` shows the last exit code and reason.

## 274: What happens to evicted Pods and how do you clean them up?

Evicted Pods stay in the API in the `Failed` phase so you can see why they were evicted. Their controller creates new Pods in their place. The Pod garbage collector removes old failed Pods once their number passes a threshold, but you can also clean up by hand:

```bash
kubectl delete pods -A --field-selector status.phase=Failed
```

Many evictions are a sign that requests are too low or nodes are too small.

## 275: What is an image volume?

An image volume mounts the content of an OCI image or artifact as a read-only volume, without running it. It is stable since Kubernetes 1.36. It is useful for shipping data, like ML models or static files, separately from the app image.

```yaml
volumes:
  - name: model
    image:
      reference: registry.example.com/models/sentiment:v3
      pullPolicy: IfNotPresent
containers:
  - name: app
    image: my-app:1.0
    volumeMounts:
      - name: model
        mountPath: /models
```

It needs a container runtime version that supports it.

## 276: What are Pod readiness gates?

A readiness gate adds an extra condition that must be true before a Pod counts as ready, set by an outside controller. The AWS Load Balancer Controller uses this so a Pod is only ready once it is registered and healthy in the load balancer target group, which avoids dropped traffic during rollouts.

```yaml
spec:
  readinessGates:
    - conditionType: "target-health.elbv2.k8s.aws/my-tg"
```

## 277: What are hostNetwork and hostPort, and when should you use them?

- `hostNetwork: true` puts the Pod in the node's network namespace. It sees all of the node's interfaces and its ports clash with other host processes.
- `hostPort` maps one container port to the same port on the node.

They are used by network plugins, some ingress controllers and node agents. Normal apps should avoid them. They limit scheduling (one Pod per port per node) and are blocked by the baseline Pod Security Standard.

## 278: Should you pass secrets as environment variables or files?

Files are usually safer:

- Env variables can leak through crash dumps, debug pages, child processes and logs that print the environment.
- Mounted files can be updated without a restart (unless you use `subPath`), and file permissions can be set.

Env variables are simpler and many libraries expect them. If you use them, make sure the app never prints its environment.

## 279: How do you handle user uploads in an app with many replicas?

Do not write uploads to the container filesystem or an `emptyDir`, since each replica would have different files and they would be lost on restart. Options:

- Object storage (S3, GCS, Azure Blob), which is the best choice in most cases
- A `ReadWriteMany` volume like EFS, Filestore or NFS, if the app must use a filesystem

A `ReadWriteOnce` volume does not work, because only one node can mount it.

## 280: How do you back up a Kubernetes cluster?

Back up two things:

1. Cluster state: your Git repo (with GitOps) and etcd snapshots for self-managed clusters
2. Persistent data: volume snapshots or database-level backups

Velero is the common tool. It backs up API objects to object storage and snapshots or copies volumes. It can restore into the same or a new cluster.

```bash
velero backup create shop-daily --include-namespaces shop
velero restore create --from-backup shop-daily
```

Test restores regularly, because a backup you never restored is not proven to work.

## 281: How do you upgrade a Kubernetes cluster?

1. Read the release notes and check for removed APIs and changed defaults.
2. Upgrade add-ons that need it first (CNI, CSI drivers, ingress controller), checking which versions they support.
3. Upgrade the control plane one minor version at a time. You cannot skip minor versions.
4. Upgrade the nodes, usually by adding new nodes and draining old ones, which relies on PDBs.
5. Watch for errors and check that workloads are healthy.

Nodes can lag the API server by up to three minor versions, which lets you upgrade the control plane first and nodes later.

## 282: How do you find manifests that use deprecated or removed APIs?

- The API server exposes a metric, `apiserver_requested_deprecated_apis`, and adds warnings to responses when a client uses a deprecated API.
- Tools like Pluto and kubent scan manifests, Helm releases and live clusters.
- Managed services show upgrade insights (EKS has a page for this).

```bash
pluto detect-helm -o wide
pluto detect-files -d k8s/
```

## 283: How do DaemonSet updates work?

DaemonSets support two strategies:

- `RollingUpdate` (default): replaces Pods node by node. `maxUnavailable` sets how many nodes can be without the Pod at once, and `maxSurge` lets the new Pod start before the old one stops.
- `OnDelete`: a new Pod is created only when you delete the old one by hand.

```yaml
updateStrategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 10%
```

For critical agents like the CNI, a slow rollout limits the damage of a bad version.

## 284: How can your own app do leader election on Kubernetes?

Use a `Lease` object from the `coordination.k8s.io` API. Replicas try to take the lease and keep renewing it. Whoever holds it is the leader, and if it stops renewing, another replica takes over. client-go has a ready-made `leaderelection` package, and libraries exist for other languages.

It is useful when only one replica should run a scheduled task or consume from a source, while the others wait as hot standbys. The ServiceAccount needs RBAC permission to get, create and update Leases.

## 285: How do you find node-level problems like a broken disk or kernel issue?

Check node conditions:

```bash
kubectl describe node worker-1   # Conditions: Ready, MemoryPressure, DiskPressure, PIDPressure
```

The Node Problem Detector, a DaemonSet, watches kernel logs and system services and reports problems as node conditions and events, for example a kernel deadlock, a read-only filesystem or a container runtime that is not responding. Automation such as auto-repair in managed clusters can then replace bad nodes.

## 286: How do you expose a non-HTTP service like a database or MQTT broker?

- Inside the cluster: a normal ClusterIP Service works for any TCP, UDP or SCTP port.
- Outside the cluster: a `LoadBalancer` Service (usually a layer 4 load balancer like an AWS NLB) or a NodePort.
- Gateway API `TCPRoute`, `UDPRoute` and `TLSRoute`, depending on what your implementation supports. `TLSRoute` can route by SNI without ending TLS.

Ingress only handles HTTP and HTTPS.

## 287: How do hostname and subdomain work for Pods?

By default the Pod's hostname is its name. You can set `hostname` and `subdomain`. If a headless Service with the same name as the subdomain exists in the namespace, the Pod gets a DNS record like `web-1.my-subdomain.my-namespace.svc.cluster.local`. StatefulSets set this up automatically using `serviceName`.

```yaml
spec:
  hostname: web-1
  subdomain: my-subdomain
```

## 288: In what order do init containers, sidecars and app containers start and stop?

1. Init containers start one by one in the order listed. A regular init container must finish before the next one starts.
2. A sidecar (init container with `restartPolicy: Always`) only has to start, and pass its startup probe if it has one, before the next init container begins. It keeps running.
3. After all init containers, the app containers start.
4. On termination, app containers stop first, then sidecars stop in reverse order.

This lets a proxy or log shipper be up before the app starts and still be running while the app shuts down.

## 289: How do you size memory for a JVM or Node.js app in a container?

The runtime must know about the container limit, or it will size its heap for the whole node and get OOMKilled.

- Java: current JVMs read cgroup limits. Use `-XX:MaxRAMPercentage=75` so the heap leaves room for metaspace, threads and native memory.
- Node.js: recent versions take the container limit into account when picking a default heap size, but setting `--max-old-space-size` (in MB) a bit below the limit is still common and makes the behavior explicit.

Leave headroom between the heap and the limit for memory outside the heap.

## 290: How do you give an outside service a name inside the cluster?

Use an `ExternalName` Service for a DNS name. For a fixed IP, create a Service without a selector and an EndpointSlice by hand:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: legacy-db
spec:
  ports:
    - port: 5432
---
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: legacy-db-1
  labels:
    kubernetes.io/service-name: legacy-db
addressType: IPv4
ports:
  - port: 5432
endpoints:
  - addresses: ["10.20.30.40"]
```

Apps connect to `legacy-db:5432` and you can move the database later without changing them.

## 291: What is the difference between client and server dry run?

- `--dry-run=client` builds the object locally and prints it. It does not contact the server for validation.
- `--dry-run=server` sends the request to the API server, which runs validation, defaults and admission webhooks, but does not save the object.

```bash
kubectl apply -f deploy.yaml --dry-run=server
```

Server dry run catches much more, such as policy violations, quota problems and webhook rejections.

## 292: How do you delete objects that you removed from your manifests?

`kubectl apply` does not delete objects that are no longer in your files. Options:

- GitOps tools with pruning, like Argo CD with `prune: true` or Flux, which is the usual answer
- Helm, which deletes objects removed from the chart on upgrade
- `kubectl apply --prune` with an ApplySet, which records which objects belong to a set so they can be pruned safely

```bash
KUBECTL_APPLYSET=true kubectl apply -f k8s/ --prune --applyset=shop-app -n shop
```

ApplySet-based pruning is still alpha in kubectl and has to be turned on with the `KUBECTL_APPLYSET` env variable. The older `--prune -l` label approach is easy to get wrong and can delete more than you expect.

## 293: What is the difference between mutating and validating admission webhooks?

Both are HTTP callbacks the API server calls before saving an object.

- Mutating webhooks run first and can change the object, for example inject a sidecar, add labels or set defaults.
- Validating webhooks run after that and can only accept or reject.

If a webhook with `failurePolicy: Fail` is down, matching requests fail. That can block deployments or even system components, so run webhooks with several replicas and exclude critical namespaces with selectors.

## 294: How do you allow only images from trusted registries?

Use an admission policy. With a ValidatingAdmissionPolicy:

```yaml
validations:
  - expression: >-
      object.spec.containers.all(c, c.image.startsWith('registry.example.com/')) &&
      (!has(object.spec.initContainers) ||
       object.spec.initContainers.all(c, c.image.startsWith('registry.example.com/')))
    message: "images must come from registry.example.com"
```

Kyverno and Gatekeeper have ready-made policies for this. Kyverno can also check image signatures made with Sigstore cosign, so you know the image came from your pipeline.

## 295: How do you run batch Jobs on separate nodes from your web apps?

Create a node pool for batch work with a taint and a label. Give the Job template a matching toleration and node selector. That way batch Jobs cannot use the web nodes and web Pods cannot land on batch nodes.

```yaml
spec:
  template:
    spec:
      nodeSelector:
        workload: batch
      tolerations:
        - key: workload
          value: batch
          effect: NoSchedule
      restartPolicy: Never
```

With an autoscaler, the batch pool can scale to zero when no Jobs are running.

## 296: When do you need more than one cluster?

- Separating prod from non-prod
- Several regions for latency or disaster recovery
- Strong isolation for compliance or for untrusted tenants
- Limiting the blast radius of a bad upgrade or misconfiguration
- Very large scale

Multiple clusters bring their own work: GitOps across clusters (Argo CD ApplicationSets, Flux), cross-cluster service discovery (Multi-Cluster Services API, Cilium Cluster Mesh, Istio multi-cluster) and global load balancing in front.

## 297: How do you find out who changed or deleted something in the cluster?

Use the API server audit log. It records who made each request, what they did and when. You set what gets logged with an audit policy file (levels: None, Metadata, Request, RequestResponse). On managed clusters you turn it on in the cloud console and read it in the cloud's logging service.

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  - level: Metadata
    resources:
      - group: ""
        resources: ["secrets", "configmaps"]
  - level: RequestResponse
    verbs: ["create", "update", "patch", "delete"]
```

Log Secrets only at the `Metadata` level, or their values end up in the log.

## 298: What is the Kubernetes API deprecation policy?

Stable (GA) API versions are not removed within a major version. Beta APIs must be supported for at least 9 months or 3 releases after they are deprecated, whichever is longer. Alpha APIs can be removed in any release without notice.

In practice this means beta APIs you depend on can disappear after a few releases, so keep an eye on deprecation warnings and move to the stable version as soon as it exists.

## 299: How do you control outgoing traffic from Pods to the internet?

- NetworkPolicy egress rules with `ipBlock`, for allowing or blocking IP ranges
- CNI-specific policies that understand DNS names, like Cilium `toFQDNs` or Calico's DNS policies, so you can allow `api.stripe.com` instead of a list of IPs
- An egress gateway or NAT gateway so all traffic leaves from known IPs, which helps when third parties allowlist your IPs
- A service mesh egress gateway for layer 7 control

```yaml
egress:
  - to:
      - ipBlock:
          cidr: 0.0.0.0/0
          except: [169.254.169.254/32] # block the cloud metadata endpoint
```

## 300: How are certificates handled inside a cluster and how do you rotate them?

Control plane parts talk over TLS with certificates signed by the cluster CA. In kubeadm clusters, those certificates are valid for one year. `kubeadm upgrade` renews them, or you can run `kubeadm certs renew all` and restart the control plane static Pods. The kubelet can rotate its own client certificate automatically, and serving certificate rotation can be turned on in the kubelet config.

```bash
kubeadm certs check-expiration
kubeadm certs renew all
```

Managed clusters handle all of this for you. Expired control plane certificates are a classic cause of a self-managed cluster suddenly stopping working.

# Advanced Questions (301-450)

## 301: What happens step by step when you run kubectl apply on a new Deployment?

1. kubectl reads the file, works out the changes and sends a request to the API server.
2. The API server authenticates you, checks RBAC, runs mutating admission, validates the object, runs validating admission and writes it to etcd.
3. The Deployment controller sees the new Deployment through its watch and creates a ReplicaSet.
4. The ReplicaSet controller creates Pod objects with no node set.
5. The scheduler sees unscheduled Pods, picks a node for each and writes a binding.
6. The kubelet on that node sees its new Pod, asks the CRI runtime to create the sandbox, the CNI plugin sets up networking, volumes are mounted, images are pulled and containers start.
7. The kubelet reports status. When readiness passes, the EndpointSlice controller adds the Pod IP, and kube-proxy updates its rules.

No component calls another directly. They all talk through the API server and react to changes.

## 302: What does it mean that Kubernetes controllers are level-triggered?

A controller does not react to "what changed", it looks at the current desired state and current actual state and works to close the gap. If it misses an event or crashes, it will just compare again next time and still do the right thing.

This is why reconcile functions must be idempotent: running them twice with the same input should have the same result. It also explains why Kubernetes is eventually consistent. Things converge over time rather than happening in one transaction.

## 303: What are informers and why do controllers use them?

An informer does a LIST of a resource once, then a WATCH for changes, and keeps a local in-memory cache. Controllers read from this cache instead of calling the API server each time, and get event handlers for add, update and delete. Shared informers let many controllers in one process share a single watch and cache per resource type.

Changes are put on a work queue, keyed by object name, so several quick changes to the same object lead to one reconcile. This is what lets Kubernetes scale to many controllers without overloading the API server.

## 304: What is resourceVersion and how does Kubernetes handle concurrent updates?

Every object has a `metadata.resourceVersion` that changes on every write. When you update an object, the API server checks that your resourceVersion matches the stored one. If someone else changed it in between, you get a `409 Conflict` and must read the object again and retry.

This is optimistic concurrency: no locks, just detect conflicts and retry. Watches also use resourceVersion to resume from a known point. `generation`, on the other hand, only changes when the `spec` changes, and controllers report the generation they last handled in `status.observedGeneration`.

## 305: How does the API server serve reads and watches efficiently?

The API server keeps a watch cache: an in-memory copy of objects per resource, fed by one watch to etcd. Most LIST and WATCH requests are served from this cache instead of hitting etcd. Recent releases made consistent reads from the cache the default and added streaming lists, so large LISTs do not need to build one huge response in memory.

On startup, the watch cache must fill before it can serve. Since 1.37 the API server returns `429 Too Many Requests` with `Retry-After` until it is ready, so clients should back off and retry instead of hammering it.

## 306: How does the API server handle a request?

1. TLS and authentication: who are you (client certificate, bearer token, OIDC, webhook)
2. API Priority and Fairness: which queue the request goes into
3. Authorization: are you allowed (Node, RBAC, Webhook authorizers, in order)
4. Mutating admission: built-in plugins, MutatingAdmissionPolicies and webhooks change the object
5. Schema validation and defaulting
6. Validating admission: built-in plugins, ValidatingAdmissionPolicies and webhooks accept or reject
7. Write to etcd and return the result

Any step can reject the request, and the error message tells you which one.

## 307: How do users authenticate to Kubernetes?

Kubernetes does not store users. It trusts outside sources:

- X.509 client certificates (common in kubeadm admin configs, but hard to revoke)
- OIDC tokens from an identity provider like Okta, Entra ID, Keycloak or Dex
- Webhook token authentication
- Cloud IAM (EKS access entries, GKE with Google accounts, AKS with Entra ID)
- ServiceAccount tokens for workloads

The structured authentication config (`AuthenticationConfiguration`) lets you set up several OIDC issuers with CEL rules for claims, without restarting the API server for changes. For people, OIDC with short-lived tokens and group claims mapped to RBAC is the usual best practice.

## 308: What authorization modes does Kubernetes have?

- `Node`: lets kubelets read only the objects they need for Pods on their node
- `RBAC`: role-based rules, the main mode for users and ServiceAccounts
- `Webhook`: asks an outside service, used by some managed platforms
- `ABAC`: old file-based policies, rarely used

Authorizers run in the order configured. The first one that allows or denies decides, and if none does, the request is denied. The structured authorization config lets you chain several webhooks with CEL match conditions.

## 309: What are the Node authorizer and NodeRestriction admission plugin?

Together they limit what a kubelet can do. The Node authorizer lets a kubelet read only Secrets, ConfigMaps and PVCs used by Pods bound to its node. NodeRestriction stops a kubelet from changing other nodes, or Pods not on its node, and from setting certain labels on its own Node object (like `node-restriction.kubernetes.io/` labels).

This means if one node is compromised, the attacker cannot read every Secret in the cluster or pretend to be another node.

## 310: How does etcd stay consistent?

etcd uses the Raft consensus algorithm. One member is the leader and handles all writes. A write is committed only when a majority (quorum) of members have saved it. If the leader fails, the rest elect a new one.

With 3 members you can lose 1, with 5 you can lose 2. An even number does not help: 4 members still tolerate only 1 failure. If quorum is lost, etcd stops accepting writes and the Kubernetes control plane cannot change anything, although running Pods keep running.

## 311: What affects etcd performance?

- Disk write latency: etcd syncs every write to disk, so it needs fast SSDs. Slow disks cause leader elections and timeouts. Watch `wal_fsync_duration_seconds`.
- Network latency between members, which is why members are usually in the same region
- Database size: the default quota is 2 GiB (configurable, up to about 8 GiB is common). Going over makes etcd read-only.
- Many large objects, like big ConfigMaps or huge CRD instances. A single object is limited to about 1.5 MiB.
- Compaction (removing old revisions) and defragmentation (returning space)

The API server compacts history automatically, but defragmentation is a manual or scheduled task in self-managed clusters.

## 312: How do you back up and restore etcd?

```bash
ETCDCTL_API=3 etcdctl snapshot save /backup/etcd-$(date +%F).db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

To restore, stop the API servers, run `etcdutl snapshot restore` into a new data directory on each member, point etcd at it and start everything again. The restored cluster is at the snapshot's point in time, so anything created later is gone, and controllers will reconcile the real world back to that state. Snapshots contain all Secrets, so encrypt and protect them.

## 313: How do you design a highly available control plane?

- Three or more control plane nodes, spread over availability zones
- etcd with three or five members, either on the control plane nodes (stacked) or on separate machines (external, more isolation but more machines)
- A load balancer in front of the API servers
- Scheduler and controller manager run on every control plane node but use leader election, so only one is active at a time

Managed services do this for you. Even with an HA control plane, a single cluster is still one failure domain for config mistakes, so think about multi-cluster for the most critical systems.

## 314: How does the scheduler framework work?

The scheduler runs each Pod through a series of plugin extension points:

- `PreEnqueue` and `QueueSort`: whether and in what order Pods enter the queue
- `PreFilter` and `Filter`: remove nodes that cannot run the Pod (resources, taints, affinity, volume topology)
- `PostFilter`: runs when no node fits, this is where preemption happens
- `PreScore`, `Score` and `NormalizeScore`: rank the remaining nodes
- `Reserve` and `Permit`: hold resources and optionally wait (used for gang scheduling)
- `PreBind`, `Bind` and `PostBind`: write the binding

You can turn plugins on and off and change their weights in a `KubeSchedulerConfiguration` with profiles, or write your own plugins in Go.

## 315: How do you change how the scheduler places Pods?

- Use scheduler profiles in `KubeSchedulerConfiguration`, and pick one per Pod with `spec.schedulerName`.
- Change the `NodeResourcesFit` scoring strategy: `LeastAllocated` spreads Pods out (the default), `MostAllocated` packs them together so autoscalers can remove empty nodes.
- Run a second scheduler for special workloads.

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: bin-packing
    pluginConfig:
      - name: NodeResourcesFit
        args:
          scoringStrategy:
            type: MostAllocated
            resources:
              - name: cpu
                weight: 1
              - name: memory
                weight: 1
```

On managed clusters you often cannot change the default scheduler, so you would run your own as a Deployment.

## 316: How does preemption work in detail?

When a Pod cannot be scheduled, the scheduler looks for a node where evicting some lower-priority Pods would make room. It picks the node where the evicted Pods have the lowest priority and cause the fewest PDB violations. It then deletes those Pods (honoring their graceful termination) and sets `status.nominatedNodeName` on the pending Pod. The Pod is scheduled once space is free.

PDBs are respected on a best-effort basis: if there is no other way, preemption can still break a PDB. Pods with `preemptionPolicy: Never` wait in the queue without evicting others.

## 317: What is gang scheduling and how does Kubernetes support it?

Some workloads, like distributed training jobs, only work if all their Pods run at the same time. If only half of them get scheduled, they sit idle and hold resources forever. Gang scheduling means "schedule all of them or none".

Kubernetes added a `Workload` API with `PodGroup` for this, and gang scheduling and workload-aware preemption are beta in 1.37. Before that, and still common today, projects like Kueue (queueing and quotas for batch Jobs), Volcano and the scheduler-plugins coscheduling plugin provide it.

## 318: What is Dynamic Resource Allocation?

DRA is the new way to request special hardware like GPUs, FPGAs or network cards. Instead of a simple count like `nvidia.com/gpu: 1`, a driver publishes `ResourceSlice` objects that describe each device and its attributes. Pods reference a `ResourceClaim` (or a `ResourceClaimTemplate`), which uses CEL to select devices, for example "a GPU with at least 40 GiB memory". `DeviceClass` objects hold shared defaults.

The scheduler allocates matching devices while placing the Pod. DRA supports sharing one device between Pods, partitionable devices, admin access, device taints and prioritized alternatives. The core API is stable, and most of these extra features reached beta or stable in 1.36 and 1.37.

## 319: How does the kubelet manage Pods internally?

The kubelet gets Pods from the API server (and static Pod files), and for each Pod a worker runs a sync loop: create the Pod sandbox through CRI, which also triggers the CNI plugin, mount volumes, pull images, start init containers, then the app containers. The Pod Lifecycle Event Generator (PLEG) notices container state changes, either by polling the runtime or through CRI events in newer setups, and triggers syncs.

The kubelet also runs probes, enforces eviction thresholds, rotates logs, garbage-collects unused images and dead containers, and reports Node and Pod status. A "PLEG is not healthy" message means the runtime is too slow to answer, often because of too many containers or a stuck runtime.

## 320: How do the kubelet, containerd and runc fit together?

1. The kubelet calls containerd over the CRI gRPC API.
2. containerd's CRI plugin pulls images, unpacks snapshots and creates the Pod sandbox (a pause container that holds the network namespace).
3. For each container, containerd starts a shim process (`containerd-shim-runc-v2`). The shim stays as the container's parent, so containerd can restart without killing containers.
4. The shim calls runc, which sets up namespaces, cgroups, seccomp and mounts using the OCI runtime spec, then executes the process.

A `RuntimeClass` can point to a different handler, like gVisor's `runsc` or Kata Containers, while keeping the rest of the flow the same.

## 321: How do requests and limits map to cgroups v2?

- CPU request becomes `cpu.weight`, a relative share used only when CPUs are busy.
- CPU limit becomes `cpu.max`, a quota per period (by default 100ms). Using the quota early in a period means waiting until the next period, which is throttling.
- Memory limit becomes `memory.max`. Going over it triggers the OOM killer.
- With Memory QoS (beta and on by default in 1.37), the memory request is used for `memory.min` or `memory.low`, and `memory.high` is set below the limit so the kernel slows the container and reclaims memory before an OOM kill.

Pods also get a Pod-level cgroup, and the QoS classes have their own parent cgroups.

## 322: What is the status of cgroup v1 in Kubernetes?

cgroup v1 is deprecated. Since 1.35, the kubelet setting `failCgroupV1` defaults to `true`, so the kubelet refuses to start on a cgroup v1 node unless you turn that off. Support is planned to be removed fully in a future release.

Newer features like Memory QoS, PSI metrics, swap support and better OOM handling only work on cgroup v2. If you run old OS images (for example older Amazon Linux 2 based nodes), move to a distribution that uses cgroup v2 by default.

## 323: What are the CPU manager and Topology manager?

By default, containers share all CPUs on a node. With the CPU manager `static` policy, a Guaranteed Pod that requests whole CPUs (like `cpu: "4"`) gets exclusive cores, which reduces context switches and cache misses for latency-sensitive work.

The Topology manager makes sure CPUs, memory and devices (like GPUs or NICs) for a Pod come from the same NUMA node. Policies range from `none` to `single-numa-node`. These matter for high-performance networking, trading systems and ML training, not for typical web apps.

## 324: What are PSI metrics and why are they useful?

Pressure Stall Information (PSI) is a Linux cgroup v2 feature that shows how much time tasks spend waiting for CPU, memory or I/O. Since 1.36 (stable), the kubelet exposes PSI for nodes, Pods and containers.

PSI is often a better signal than usage. A container using 50% CPU might still be waiting a lot because of throttling, and memory pressure shows up in PSI before an OOM kill happens. You can use it for alerts and to tune requests and limits.

## 325: Does Kubernetes support swap?

For a long time the kubelet refused to run with swap on. Node swap support is now stable, but off unless you turn it on. With `swapBehavior: LimitedSwap` in the kubelet config, only Burstable Pods can use swap, in proportion to their memory request. Guaranteed and BestEffort Pods, and high-priority Pods, do not use swap. It requires cgroup v2.

It is useful to soften short memory spikes, but it can hide memory leaks and make performance less predictable.

## 326: What are user namespaces in Pods?

With `hostUsers: false`, the Pod's processes run in a separate user namespace. Root (UID 0) inside the container maps to an unprivileged high UID on the host. If an attacker escapes the container, they are a nobody on the node, not root.

```yaml
spec:
  hostUsers: false
  containers:
    - name: app
      image: my-app:1.0
```

This is stable since 1.36. It needs a recent kernel, a runtime that supports it and filesystems that support idmapped mounts. It is one of the best ways to reduce the risk of container escapes.

## 327: What kube-proxy modes are there today?

- `iptables`: the long-time default on Linux. It works everywhere, but rule updates get slow with many thousands of Services.
- `nftables`: the newer mode, stable since 1.33. It scales better and updates faster. This is the direction for the future.
- `ipvs`: uses the kernel's IPVS load balancer. It is deprecated since 1.37 and planned to be disabled by default around 1.40 and removed later. Clusters using it should move to nftables.
- `kernelspace`: for Windows nodes.

Many clusters skip kube-proxy completely and use an eBPF dataplane like Cilium.

## 328: How does a packet to a ClusterIP Service reach a Pod?

The ClusterIP is not assigned to any interface. When a Pod sends a packet to it, rules set up by kube-proxy (iptables or nftables) in the node's network stack match the destination IP and port and DNAT it to one of the backend Pod IPs, picked at random. conntrack remembers the choice, so replies are translated back and later packets of the same connection go to the same Pod. Then the CNI plugin routes the packet to the Pod, on the same node or across nodes.

Because the choice is made per connection, long-lived connections (HTTP/2, gRPC, database pools) stay on one Pod.

## 329: How does an eBPF dataplane like Cilium replace kube-proxy?

Cilium loads eBPF programs into the kernel that handle Service load balancing directly. For traffic from Pods, it can translate the Service IP to a backend IP at socket connect time, so no per-packet NAT is needed. It keeps Service and endpoint data in eBPF maps that update in constant time, which avoids the slow rule rebuilds of iptables at large scale.

It also enforces NetworkPolicies, including layer 7 and DNS-based rules, and gives detailed flow visibility through Hubble. The trade-off is depending on newer kernels and a more complex component.

## 330: What is the difference between overlay and routed Pod networking?

- Overlay (VXLAN, Geneve): Pod traffic between nodes is wrapped in another packet. It works on any network, but costs some CPU and reduces the MTU.
- Routed / native: Pod IPs are real routable addresses, either from the cloud VPC (AWS VPC CNI, Azure CNI) or announced with BGP (Calico). There is no encapsulation, so it is faster, but you need enough IP addresses and network support.

VPC-native setups can run out of IPs, because every Pod uses a VPC address. Features like prefix delegation, secondary CIDRs or overlay modes help with that.

## 331: What conntrack problems can you hit in Kubernetes?

- A full conntrack table on busy nodes drops new connections. The kernel logs `nf_conntrack: table full`. Raise `nf_conntrack_max`, which kube-proxy partly does for you.
- A race in the kernel when two UDP packets from the same socket (like DNS A and AAAA queries) go out at the same moment, causing one to be dropped and a 5 second DNS timeout. NodeLocal DNSCache or `single-request-reopen` in resolv.conf help.
- Stale UDP conntrack entries after a backend Pod changes, so traffic keeps going to a dead Pod until the entry expires.

## 332: What is NodeLocal DNSCache?

It runs a DNS cache as a DaemonSet on every node, listening on a link-local IP. Pods send DNS queries to the cache on their own node instead of crossing the network to CoreDNS. This cuts latency, avoids the conntrack race for UDP DNS and greatly reduces load on CoreDNS. Cache misses go to CoreDNS over TCP.

It is especially worth it in large clusters or apps that make many DNS lookups.

## 333: How does dual-stack networking work in Kubernetes?

When the cluster has both IPv4 and IPv6 ranges for Pods and Services, each Pod gets one address of each family. Services choose with `ipFamilyPolicy` (`SingleStack`, `PreferDualStack`, `RequireDualStack`) and `ipFamilies`.

```yaml
spec:
  ipFamilyPolicy: PreferDualStack
  ipFamilies: [IPv6, IPv4]
```

The first family listed is the primary one. Your CNI plugin, cloud load balancers and apps all need to support IPv6 for it to work end to end.

## 334: How can you grow the Service IP range of a running cluster?

Service IPs used to come from one fixed range set with an API server flag, and changing it was risky. Now Service IP ranges are API objects (`ServiceCIDR`), and each allocated IP is an `IPAddress` object. This is stable since 1.33.

You add a new range by creating another `ServiceCIDR` object. New Services can get IPs from either range, without restarting the API server.

```yaml
apiVersion: networking.k8s.io/v1
kind: ServiceCIDR
metadata:
  name: extra-range
spec:
  cidrs:
    - 10.200.0.0/16
```

## 335: Why is Service externalIPs being deprecated?

`spec.externalIPs` lets anyone who can create a Service claim any IP address. kube-proxy then sends traffic for that IP to their Pods, even traffic meant for an outside system. This is CVE-2020-8554, a man-in-the-middle risk in multi-tenant clusters that cannot be fixed in the design.

The field is deprecated from 1.36 with warnings, and removal is planned for 1.43. Until then, block it with an admission policy (there is a built-in `DenyServiceExternalIPs` admission plugin) and use LoadBalancer Services or the Gateway API instead.

## 336: Which RBAC permissions are dangerous even if they look harmless?

- `create pods` in a namespace: the Pod can mount any Secret in that namespace and run as any ServiceAccount there, so it equals reading all Secrets and using all those identities.
- `pods/exec` and `pods/attach`: a shell in someone else's containers.
- `escalate` and `bind` on roles: you can grant yourself more than you have.
- `impersonate`: you can act as other users or groups, including admins.
- Write access to Deployments, DaemonSets or CronJobs: same as creating Pods.
- `nodes/proxy`: direct access to the kubelet API.
- `list secrets`: returns full Secret values, not just names.
- Write access to webhooks configs: you can intercept or change every object.

Review RBAC with tools like `kubectl-who-can` or rbac-tool and give the least access needed.

## 337: How do you protect the kubelet API?

The kubelet API (port 10250) can run commands in any container on the node. To protect it:

- Turn off anonymous auth and use webhook authentication and authorization, so requests are checked against the API server.
- Use fine-grained kubelet authorization (stable since 1.36). Monitoring tools can get only read access such as `nodes/metrics` or `nodes/pods` instead of the broad `nodes/proxy`, which also allows exec.
- Block access to the port from Pods and the outside with network rules.
- Turn off the read-only port 10255.

## 338: Why is the cloud metadata endpoint a risk and how do you protect it?

On cloud VMs, `169.254.169.254` serves the node's credentials. If a Pod can reach it, an attacker who gets into any container can steal the node's IAM role, which usually has broad permissions.

Protections:

- On AWS, require IMDSv2 with a hop limit of 1, so Pods (one extra network hop) cannot reach it
- Block the IP with NetworkPolicy egress rules
- Use workload identity (IRSA, EKS Pod Identity, GKE Workload Identity) so Pods do not need node credentials at all
- Give the node role as few permissions as possible

## 339: How do you secure the software supply chain for Kubernetes workloads?

- Build images in CI from pinned base images and scan them with tools like Trivy or Grype
- Create an SBOM and provenance attestations during the build
- Sign images with Sigstore cosign, ideally keyless with the CI's OIDC identity
- Verify signatures at admission with Kyverno, the Sigstore policy-controller or Ratify, so only signed images from your pipeline can run
- Deploy by digest, not tag
- Limit registries and keep an inventory of what runs where

Frameworks like SLSA describe levels of supply chain security you can aim for.

## 340: How do you detect attacks at runtime in a cluster?

Static checks miss things that happen while containers run. Runtime security tools watch system calls with eBPF or kernel modules and alert on suspicious behavior:

- Falco: rules like "a shell was started in a container", "a sensitive file was read", "an unexpected outbound connection"
- Tetragon (Cilium): observes and can also block, for example kill a process that opens a certain file

Send alerts to your SIEM and combine them with audit logs to see the full picture of an incident.

## 341: What is a RuntimeClass and when do you use a sandboxed runtime?

A `RuntimeClass` picks which container runtime handler to use for a Pod. Normal containers share the host kernel. Sandboxed runtimes add another layer:

- gVisor (`runsc`): a user-space kernel that intercepts system calls
- Kata Containers: each Pod runs in a lightweight VM

```yaml
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: gvisor
handler: runsc
overhead:
  podFixed:
    memory: 64Mi
    cpu: 100m
```

```yaml
spec:
  runtimeClassName: gvisor
```

Use them for untrusted code, like customer-provided functions or CI jobs. They cost some performance and do not support every feature. The `overhead` field makes the scheduler count the extra resources.

## 342: How does KMS v2 encryption work for Secrets?

The API server encrypts each Secret with a data encryption key (DEK) using AES-GCM. The DEK is encrypted by a key encryption key (KEK) held in an external KMS, like AWS KMS, Cloud KMS or Vault, through a KMS plugin. Only the encrypted DEK is stored next to the data.

KMS v2 reuses a DEK for many writes and caches it, so the API server does not call the KMS on every request. That fixes the performance problems of KMS v1, which is deprecated. Rotating the KEK in the KMS is transparent. To re-encrypt all objects with new keys, use storage version migration.

## 343: What are Pod Certificates and ClusterTrustBundles?

Both are stable in 1.37.

- Pod Certificates let the kubelet request an X.509 certificate for a Pod from a signer and mount it through a projected volume, rotating it automatically. Apps get a workload identity for mTLS without a mesh or cert-manager.
- `ClusterTrustBundle` is a cluster-scoped object holding CA certificates, which Pods can mount through a projected volume. It is a standard way to share trust roots, instead of copying CA files into ConfigMaps in every namespace.

```yaml
volumes:
  - name: certs
    projected:
      sources:
        - podCertificate:
            signerName: example.com/workload
            keyType: ED25519
            credentialBundlePath: credentials.pem
```

## 344: What is external signing of ServiceAccount tokens?

Normally the API server signs ServiceAccount tokens with a private key on its own disk. Since 1.36 (stable), the API server can call an external signer over gRPC, so the key can live in an HSM or cloud KMS and never touch the control plane machines. It also makes key rotation easier. This matters because those tokens are trusted by cloud providers for workload identity.

## 345: How do you check a cluster against security best practices?

- The CIS Kubernetes Benchmark lists config checks for the control plane, etcd, kubelet and policies. kube-bench runs those checks.
- Trivy, Kubescape and similar tools scan the cluster and manifests for misconfigurations and known CVEs.
- Managed providers offer their own benchmarks and posture tools.

Combine scanning with policies at admission, so new problems are blocked rather than only found later.

## 346: Should the API server be reachable from the internet?

Better not. Options:

- A private endpoint only, reachable over VPN, a bastion or a private network link
- If it must be public, restrict source IP ranges
- Strong authentication through OIDC with MFA, no long-lived certificates or static tokens
- CI systems inside the network or using GitOps, so they do not need inbound access

Exposed API servers are scanned constantly. A single leaked kubeconfig or an anonymous-auth misconfiguration is enough to compromise the cluster.

## 347: What are the limits of standard NetworkPolicy?

- Only layer 3 and 4: you cannot match HTTP paths or methods
- Allow-only: there are no explicit deny rules, and you cannot set rule priority
- Namespaced and owned by app teams, so a cluster admin cannot set rules that teams cannot override
- No DNS names, only IP blocks
- No logging of drops in the API itself

CNI-specific policies (Cilium, Calico) fill these gaps. The SIG Network policy API project is working on cluster-wide admin policies with priorities and deny rules, so platform teams can set guardrails above team policies.

## 348: How does a well-written controller's reconcile loop look?

```go
func (r *BackupReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    var b examplev1.Backup
    if err := r.Get(ctx, req.NamespacedName, &b); err != nil {
        return ctrl.Result{}, client.IgnoreNotFound(err)
    }

    if !b.DeletionTimestamp.IsZero() {
        // clean up outside resources, then remove our finalizer
        return r.finalize(ctx, &b)
    }

    // create or update child objects to match spec
    if err := r.ensureCronJob(ctx, &b); err != nil {
        return ctrl.Result{}, err // returning an error requeues with backoff
    }

    b.Status.ObservedGeneration = b.Generation
    meta.SetStatusCondition(&b.Status.Conditions, metav1.Condition{
        Type: "Ready", Status: metav1.ConditionTrue, Reason: "Reconciled",
    })
    return ctrl.Result{}, r.Status().Update(ctx, &b)
}
```

Key points: read current state, be idempotent, set owner references on children so they are watched and garbage collected, update status through the status subresource, and return errors to retry with backoff.

## 349: Why do controllers use finalizers?

A finalizer lets a controller clean up things outside Kubernetes before an object disappears, like a cloud load balancer, a DNS record or a database user. When you delete the object, Kubernetes only sets `deletionTimestamp`. The controller sees it, does the cleanup and removes its finalizer. Then the object is actually deleted.

The risk is that if the controller is removed or broken, objects stay stuck in Terminating forever. Uninstall order matters: delete the custom objects first, then the operator.

## 350: How should a custom resource report its status?

- Use the `status` subresource, so spec and status are updated separately and users cannot overwrite status by applying their spec
- Use standard `conditions` (`type`, `status`, `reason`, `message`, `lastTransitionTime`, `observedGeneration`) like `Ready` or `Progressing`
- Set `status.observedGeneration` so clients can tell whether the status reflects the latest spec
- Add `additionalPrinterColumns` to the CRD so `kubectl get` shows useful columns

This lets tools like `kubectl wait --for=condition=Ready`, Argo CD health checks and Flux work with your resources.

## 351: How do you version a CRD and change its schema over time?

A CRD can serve several versions, like `v1alpha1` and `v1`, but only one is the storage version. When versions differ in shape, you add a conversion webhook that converts objects between them. Clients can use any served version and the API server converts on the fly.

Steps for a breaking change:

1. Add the new version as served, with a conversion webhook.
2. Switch the storage version to the new one.
3. Migrate stored objects so they are rewritten in the new version (storage version migration).
4. Stop serving the old version, then remove it from `status.storedVersions` and the CRD.

Adding optional fields does not need a new version.

## 352: How do you validate custom resources with CEL?

You add `x-kubernetes-validations` rules to the CRD schema. They run inside the API server, so you do not need a validating webhook for most rules. `oldSelf` lets you write rules about updates, such as making a field immutable.

```yaml
openAPIV3Schema:
  type: object
  properties:
    spec:
      type: object
      x-kubernetes-validations:
        - rule: "self.minReplicas <= self.maxReplicas"
          message: "minReplicas must not be greater than maxReplicas"
      properties:
        minReplicas:
          type: integer
        maxReplicas:
          type: integer
        region:
          type: string
          x-kubernetes-validations:
            - rule: "self == oldSelf"
              message: "region cannot be changed"
```

CEL rules have a cost limit, so the API server can reject rules that might be too expensive. Setting `maxItems` and `maxLength` keeps costs low.

## 353: What is storage version migration?

Objects in etcd are stored in whatever version was the storage version when they were last written. After an upgrade changes the storage version, or after you rotate encryption keys, old objects stay in the old format until something rewrites them. Storage version migration rewrites every object of a resource so they are all stored in the current version and encryption.

Since 1.37, the migrator is built in and the `StorageVersionMigration` API (`storagemigration.k8s.io/v1`) is on by default. Before that you had to run a separate migrator or a script that read and wrote every object.

## 354: When would you use an aggregated API server instead of a CRD?

CRDs cover most needs: storing structured data with validation and having a controller act on it. An aggregated API server is a separate server registered through an `APIService` object. The main API server proxies requests for that group to it.

Use one when the data should not live in etcd or needs custom storage, when responses are computed on the fly (metrics-server serves `metrics.k8s.io` this way), or when you need custom verbs and subresources. It is much more work to build and run, and if it is down, it can affect things like namespace deletion and API discovery.

## 355: What is API Priority and Fairness?

APF protects the API server from overload. Requests are sorted into priority levels by `FlowSchema` objects (based on user, group, namespace or resource), and each level gets a share of the server's concurrency. Inside a level, requests are queued fairly per flow, so one noisy client cannot starve others.

```bash
kubectl get flowschemas
kubectl get prioritylevelconfigurations
```

System components like the kubelet and leader election have their own protected levels. If a controller is hammering the API, you can give it its own FlowSchema with a low limit. When a level is full, clients get `429` responses.

## 356: What are the scalability limits of a single Kubernetes cluster?

The tested limits are around:

- 5,000 nodes
- 150,000 Pods in total
- 110 Pods per node (default, configurable)
- 300,000 containers

In practice, problems usually show up earlier because of the number of objects, how often they change, large objects, many watchers, heavy LIST calls from badly written controllers, and etcd size. Many large companies prefer several medium-sized clusters to one huge one.

## 357: Why are large LIST requests a problem and how do clients avoid them?

A LIST of all Pods in a big cluster can return hundreds of megabytes. Building that response costs API server memory and CPU, and if it bypasses the watch cache, it also loads etcd. Many clients doing it at once can crash the API server.

Better ways:

- Use informers: one LIST at start, then a WATCH
- Paginate with `limit` and `continue`
- Filter with label and field selectors
- Read from the watch cache, which is the default for consistent reads in recent versions
- Streaming lists, which send items one by one instead of building one huge response

## 358: How can you make Pods start faster?

- Smaller images, and base layers shared between services so they are already on the node
- Pull images in advance, with a DaemonSet that pulls them or a node image that includes them
- Lazy pulling (stargz, SOCI), which starts the container before the whole image is downloaded
- Allow parallel image pulls in the kubelet (`serializeImagePulls: false`)
- A registry mirror or cache close to the nodes
- Avoid slow init containers and long startup work in the app
- Use a startup probe with a short period, so readiness is detected quickly

Measure first. `kubectl describe pod` events show how long each step took.

## 359: How do you make autoscaling react faster when new nodes take minutes to start?

New nodes take one to several minutes, which is too slow for sudden spikes. Common tricks:

- Overprovisioning: run low-priority placeholder Pods (using the `pause` image) that reserve capacity. When real Pods need room, they preempt the placeholders right away, and the autoscaler adds nodes for the evicted placeholders in the background.
- Scale on leading metrics like request rate or queue length instead of CPU
- Keep `minReplicas` high enough for normal peaks
- Use scheduled scaling for known events

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: overprovisioning
value: -10
preemptionPolicy: Never
globalDefault: false
```

## 360: How does the HPA calculate the number of replicas?

The basic formula is:

```
desiredReplicas = ceil(currentReplicas * currentMetricValue / targetMetricValue)
```

For example, 4 replicas at 90% average CPU with a 60% target gives `ceil(4 * 90 / 60) = 6`. With several metrics, the HPA takes the highest result. If the ratio is within the tolerance (10% by default, configurable since it became stable in 1.37), nothing changes. Pods that are not ready or have no metrics yet are handled conservatively, so starting Pods do not cause wrong decisions. Then `behavior` policies and stabilization windows limit how fast the change happens.

## 361: Can the HPA scale a workload to zero?

Classic HPA has `minReplicas` of at least 1. Scale to zero is beta and enabled by default in 1.37: you can set `minReplicas: 0`, but only with Object or External metrics. CPU and memory cannot work, because a workload with zero Pods has no CPU usage to measure. When scaled to zero, the HPA sets a `ScaledToZero` condition.

Before this, and still common, KEDA was the usual way to scale to zero based on queue length or other events. Remember that the first request after scaling to zero has to wait for a Pod to start.

## 362: How do you detect and fix CPU throttling?

Look at the container's cgroup stats or the cAdvisor metrics:

```promql
rate(container_cpu_cfs_throttled_periods_total[5m])
  / rate(container_cpu_cfs_periods_total[5m])
```

A high ratio means the container often hits its CPU limit inside a 100ms period. This can happen even when average usage looks low, because a burst of many threads can use up the quota in a few milliseconds. Fixes: raise or remove the CPU limit, lower thread count in the app (GOMAXPROCS, worker pools) to match the limit, or use the static CPU manager policy for Guaranteed Pods.

## 363: How do you deal with noisy neighbors on shared nodes?

- Set realistic requests so the scheduler does not overpack nodes
- Use memory limits and ephemeral storage limits to contain runaway Pods
- Separate heavy or bursty workloads into their own node pools
- Use PriorityClasses so important Pods win under pressure
- Watch PSI metrics, throttling and node pressure
- For disk and network I/O, which Kubernetes does not limit well, separate the workloads or use CNI bandwidth annotations where supported

## 364: How do you design an app on Kubernetes to survive the loss of a zone?

- Run nodes in at least three zones
- Spread replicas across zones with topology spread constraints
- Have enough replicas that the remaining zones can handle full load, or let the autoscaler add capacity quickly (and check that the cloud has capacity in other zones)
- Use zone-aware storage: zonal disks cannot move, so stateful apps need replication between zones at the app level
- Use PDBs so maintenance does not make things worse during an incident
- Test it by draining or cordoning a whole zone

## 365: How would you set up disaster recovery across regions?

Kubernetes does not do cross-region failover by itself. Common setups:

- Active-passive: a second cluster in another region with the same GitOps config, data replicated asynchronously (database replicas, object storage replication), and DNS or a global load balancer that switches over
- Active-active: clusters in several regions serving traffic, with a database that supports multi-region writes or careful splitting of data by region

Write down your RTO and RPO, keep the second region running with real config through GitOps, and practice the failover. A failover you never tested will not work when you need it.

## 366: How do you run a stateful clustered system like Kafka or etcd safely on Kubernetes?

- StatefulSet with stable identities and per-Pod volumes, or better, a mature operator
- Pod anti-affinity or topology spread so members are on different nodes and zones
- A PDB that keeps quorum, for example `maxUnavailable: 1` for a 3-member cluster
- `podManagementPolicy` and readiness probes that reflect real cluster membership
- Graceful shutdown long enough for leadership handover
- Fast, local or zonal storage with the right performance class
- Backups that do not depend on the cluster itself

Upgrades and node maintenance must be one member at a time, waiting for the cluster to be healthy before moving on.

## 367: A StatefulSet rollout is stuck after a bad update. Why, and how do you fix it?

With `OrderedReady` and `RollingUpdate`, the controller waits for the updated Pod to be ready before continuing. If the new version never becomes ready (crash, bad config), the rollout stops there. Even after you fix the template, the controller may wait forever for the broken Pod to become ready before replacing it.

Fix: correct the template, then delete the stuck Pod by hand so it is recreated with the fixed version. Test StatefulSet changes with `partition` first, so a bad version only hits one Pod.

## 368: What happens to Pods when a node shuts down or dies?

- Graceful node shutdown: if the kubelet notices the OS is shutting down (through systemd inhibitor locks), it terminates Pods with their grace periods first, giving critical Pods time at the end. You configure `shutdownGracePeriod` and `shutdownGracePeriodCriticalPods` in the kubelet config.
- Sudden failure: the node stops sending heartbeats. After about 40 seconds it is marked `NotReady` and gets a `node.kubernetes.io/unreachable` taint. Pods tolerate that taint for 300 seconds by default, then they are evicted and replaced elsewhere.
- StatefulSet Pods and Pods with attached volumes may stay stuck, since Kubernetes cannot be sure they stopped. If you know the node is really off, add the `node.kubernetes.io/out-of-service` taint so Kubernetes force-deletes the Pods and detaches the volumes.

## 369: How does CSI work?

The Container Storage Interface splits storage drivers out of Kubernetes. A CSI driver usually has:

- A controller part (Deployment) with sidecars: external-provisioner (creates volumes for PVCs), external-attacher (attaches disks to nodes), external-resizer and external-snapshotter
- A node part (DaemonSet) that mounts and formats volumes on each node, registered with the kubelet through node-driver-registrar

The flow for a new PVC: provision the disk, attach it to the node where the Pod is scheduled (`VolumeAttachment`), then the kubelet asks the node plugin to stage and publish (mount) it into the Pod.

## 370: What does a Multi-Attach error mean?

`Multi-Attach error for volume ... Volume is already exclusively attached to one node` means a `ReadWriteOnce` volume is still attached to another node, so the new Pod cannot use it. It often happens when a Pod moves after its old node failed, or during a rolling update where the new Pod lands on a different node while the old one still holds the volume.

Fixes: wait for the old Pod to terminate and the volume to detach, use the out-of-service taint for dead nodes, use the `Recreate` strategy for single-replica Deployments with RWO volumes, or use a StatefulSet.

## 371: When would you use local persistent volumes?

Local PVs use disks attached directly to a node, like NVMe drives. They are much faster than network storage and cheaper, but the data is tied to that node. If the node dies, the data is gone and the Pod cannot move.

They suit systems that replicate data themselves, like Cassandra, Kafka, Elasticsearch or a database cluster with replicas. The scheduler places Pods on the node where their volume is through node affinity on the PV. Tools like the local static provisioner or OpenEBS LocalPV handle creating them.

## 372: Your API has latency spikes every few minutes. What might cause it in Kubernetes?

Things to check:

- CPU throttling from limits that are too tight
- Garbage collection pauses in the runtime, especially when memory is near the limit
- DNS: ndots search lookups, conntrack drops causing 5 second timeouts, CoreDNS overloaded
- Pods being restarted by liveness probes, or rollouts and autoscaling changing endpoints
- Noisy neighbors on the same node, or node-level jobs like image garbage collection
- Connection pools being rebuilt when Pods move

Match the timing of spikes against throttling metrics, DNS latency, Pod restarts and events.

## 373: Users get 502 errors during every deployment. How do you fix it?

Usually one of these:

1. Pods are removed from the load balancer later than they stop serving. Add a `preStop` sleep so Pods keep serving while endpoints update everywhere.
2. The app exits immediately on SIGTERM without finishing requests in progress. Handle SIGTERM gracefully.
3. New Pods get traffic before they are really ready. Fix the readiness probe so it only passes when the app can serve, and consider `minReadySeconds`.
4. Keep-alive connections from the proxy to a Pod that is shutting down. Make the app close idle connections on shutdown, and set proxy timeouts accordingly.
5. With cloud load balancers targeting Pods directly, use readiness gates so the load balancer health checks pass before old Pods go away.

Also check that `maxUnavailable` is 0 and that there is enough capacity for surge Pods.

## 374: A node shows NotReady. How do you investigate?

```bash
kubectl describe node worker-3     # conditions, events, last heartbeat
kubectl debug node/worker-3 -it --image=ubuntu:24.04   # if the node still runs Pods
```

On the node (SSH or debug Pod with chroot):

```bash
systemctl status kubelet containerd
journalctl -u kubelet --since "30 min ago"
df -h; free -m
```

Common causes: the kubelet or container runtime crashed, the disk is full, memory pressure killed system processes, expired kubelet certificates, network problems between the node and the API server, or the CNI plugin is not ready. On cloud clusters, it is often fastest to drain and replace the node, then find the cause from logs afterward.

## 375: A container is OOMKilled but its memory graph never reached the limit. Why?

- The graph shows an average or is sampled every 30 to 60 seconds, so a short spike is missed.
- The graph shows `working_set` while the kernel counts all charged memory, including kernel memory.
- A memory-backed `emptyDir` (tmpfs) counts against the container's memory.
- Another process in the container (a child process or a shell script) used the memory.
- The node itself ran out of memory and the kernel's OOM killer picked this container, even though it was under its own limit.

Check `kubectl describe pod` for the reason, the kernel log on the node (`dmesg` or `journalctl -k`) and node memory at that time.

## 376: Pods are stuck in ContainerCreating. What do you check?

`kubectl describe pod` events usually say why. Common causes:

- Volume problems: PVC not bound, volume still attached to another node, CSI driver errors, NFS server unreachable
- A Secret or ConfigMap referenced in a volume does not exist
- CNI problems: no IPs left in the Pod range or VPC subnet, CNI plugin not running on the node
- A very large image that is still downloading
- A `RuntimeClass` handler not installed on the node

For CNI issues, check the CNI DaemonSet Pods on that node and their logs.

## 377: kubectl commands are slow and the API server is under heavy load. What do you do?

1. Check API server metrics: request rate per user and verb, latency, `apiserver_flowcontrol_rejected_requests_total` for APF rejections.
2. Look for a client making many LIST calls or creating lots of watches, often a buggy controller or a script polling with `kubectl get` in a loop.
3. Check etcd health: disk latency, database size, leader changes.
4. Check object counts. Thousands of old Events, completed Jobs, or a CRD with huge objects can hurt.
5. Check webhooks: a slow admission webhook adds latency to every write it matches.

Short-term, limit the bad client with an APF FlowSchema. Long-term, fix the client to use informers.

## 378: Your EKS cluster ran out of Pod IP addresses. What are your options?

With the AWS VPC CNI, every Pod uses a VPC IP, and each instance type has limits on how many IPs it can hold. Options:

- Turn on prefix delegation so each network interface gets /28 prefixes instead of single IPs, which raises Pod density
- Add secondary CIDR ranges (for example from 100.64.0.0/10) to the VPC and use custom networking so Pods use those subnets
- Use larger subnets for new node groups
- Use IPv6, which removes the problem
- Lower `WARM_IP_TARGET` and similar settings so nodes do not hold many unused IPs
- Switch to an overlay CNI mode if routable Pod IPs are not needed

Plan IP ranges at the start, since changing them later is painful.

## 379: etcd reports "mvcc: database space exceeded". What happened and how do you fix it?

etcd went over its storage quota and switched to read-only mode, raising a `NOSPACE` alarm. The control plane can no longer make changes. Usual causes: lots of objects or revisions written quickly (a controller in an update loop, huge numbers of Events), or very large objects.

Fix:

```bash
etcdctl endpoint status --write-out=table
etcdctl compact <latest-revision>
etcdctl defrag --cluster
etcdctl alarm disarm
```

Then find and stop what caused the growth, and consider a larger quota. On managed clusters, contact support and fix the cause on your side.

## 380: A broken admission webhook blocked deployments across the cluster. How do you prevent this?

When a webhook with `failurePolicy: Fail` is down, every matching request fails. If it matches Pods in all namespaces, even system components cannot restart.

Prevention:

- Exclude `kube-system` and the webhook's own namespace with `namespaceSelector`
- Use `objectSelector` and `matchConditions` (CEL) to only match what you need
- Set short `timeoutSeconds`
- Run the webhook with several replicas, a PDB and high priority
- Use `failurePolicy: Ignore` for non-security webhooks
- Prefer built-in ValidatingAdmissionPolicy and MutatingAdmissionPolicy, which have no external service to fail

During an incident, an admin can delete the `ValidatingWebhookConfiguration` or `MutatingWebhookConfiguration` to unblock the cluster.

## 381: A Secret was committed to a public Git repository. What do you do?

1. Rotate the credential immediately at its source (database password, API key, cloud key). Removing it from Git is not enough, it is already public.
2. Update the Kubernetes Secret and roll the workloads that use it.
3. Check logs at the provider for any use of the leaked credential.
4. Remove it from Git history if you want, but treat it as compromised no matter what.
5. Fix the process: use External Secrets, Sealed Secrets or SOPS, add secret scanning to CI and pre-commit hooks, and enable push protection on the Git host.

## 382: A Deployment rollout is stuck halfway. How do you debug it?

```bash
kubectl rollout status deployment/api
kubectl describe deployment api       # conditions, ProgressDeadlineExceeded
kubectl get rs -l app=api             # old vs new ReplicaSet counts
kubectl describe pod <new-pod>        # why it is not ready
```

Common reasons: new Pods fail readiness, cannot be scheduled (no capacity for surge Pods), cannot pull the image, or a quota blocks new Pods (check the ReplicaSet events). Fix the cause or run `kubectl rollout undo`. With `maxUnavailable: 0`, a stuck rollout keeps the old Pods serving, so users are usually not affected.

## 383: Load is uneven across Pods even though the Service balances it. Why?

Service load balancing happens per connection, not per request. Clients with long-lived connections (HTTP/2, gRPC, keep-alive pools, database clients) stay on the Pods they connected to first. After scaling up, new Pods get little traffic because existing connections never move.

Fixes: client-side load balancing over all endpoints (using a headless Service), a layer 7 proxy or service mesh that balances per request, or limiting connection age on the server so clients reconnect from time to time (for example gRPC `MaxConnectionAge`).

## 384: How do you load balance gRPC traffic in Kubernetes?

gRPC uses HTTP/2, which sends many requests over one connection, so the normal Service ends up sending all traffic from one client to one Pod. Options:

- A service mesh (Istio, Linkerd) or Envoy-based proxy that balances per request
- A Gateway API `GRPCRoute` through a gateway implementation that balances per request
- Client-side balancing: point the client at a headless Service (`dns:///api-headless:50051`) with a `round_robin` policy, so it connects to every Pod
- Server-side `MaxConnectionAge` so clients reconnect and spread out over time

## 385: How do you handle WebSockets and other long-lived connections during deploys?

Long connections block graceful shutdown. A Pod that is shutting down may hold thousands of open sockets.

- Set `terminationGracePeriodSeconds` long enough to drain, or close connections on purpose on SIGTERM and let clients reconnect
- Make clients reconnect with backoff and jitter, so they do not all reconnect at the same moment
- Roll out slowly (small `maxSurge`) so reconnect waves stay small
- Configure proxy timeouts on the ingress or gateway to match idle times
- Keep connection state outside the Pod (Redis pub/sub, for example) so any Pod can take over

## 386: What is your checklist for zero-downtime deployments on Kubernetes?

- At least 2 replicas, spread across nodes and zones
- `maxUnavailable: 0` and enough capacity for surge Pods
- Readiness probe that reflects real readiness
- `preStop` sleep plus graceful SIGTERM handling, grace period longer than both
- PDB for planned disruptions
- Backward compatible database migrations and API changes
- Readiness gates when using cloud load balancers that target Pods
- Automatic rollback on failed rollout or bad metrics

## 387: How would you build an internal developer platform on top of Kubernetes?

The goal is that app teams ship without knowing every Kubernetes detail:

- Golden path templates (a service template with Dockerfile, chart, CI pipeline and dashboards)
- GitOps for deployments, with a simple per-app config file
- A developer portal like Backstage for the service catalog and templates
- Guardrails through admission policies instead of manual reviews
- Self-service namespaces with quotas, RBAC and network policies created automatically
- Self-service infrastructure (databases, queues) through Crossplane or cloud operators
- Shared observability with standard labels

Treat the platform as a product: talk to its users, measure what slows them down, and avoid hiding Kubernetes so much that debugging becomes impossible.

## 388: How would you design a cluster setup for 200 microservices and 20 teams?

- Separate clusters for prod and non-prod, maybe per region
- Namespaces per team or per service, created from a template with RBAC, quotas, network policies and Pod Security labels
- One shared Helm chart or Kustomize base for services so most YAML is standard
- GitOps with Argo CD ApplicationSets or Flux, one folder per service per environment
- Policy engine for guardrails
- Shared ingress or gateway, cert-manager, external-dns and External Secrets as platform add-ons
- Central observability with metrics, logs and traces, with per-team dashboards and alerts
- Cost visibility per namespace

The platform team owns the clusters and add-ons. Teams own their namespaces and services.

## 389: What is Cluster API?

Cluster API is a Kubernetes project for creating and managing Kubernetes clusters with Kubernetes-style objects. A management cluster runs controllers, and you define `Cluster`, `MachineDeployment` and provider-specific objects (AWS, Azure, vSphere, bare metal and others). Controllers create the machines, bootstrap Kubernetes and handle upgrades by rolling machines.

It is useful for platform teams running many clusters in a consistent way, especially on-premises.

## 390: How do you manage clusters as code?

- Terraform or OpenTofu to create the cloud network, the managed cluster, node groups and IAM
- GitOps (Argo CD or Flux) for everything inside the cluster: add-ons and apps
- Cluster API or Crossplane if you want Kubernetes itself to manage clusters
- A clear split between the infra repo and the app deployment repos

Avoid managing in-cluster resources from Terraform when you already use GitOps, because two tools owning the same objects leads to fights and drift.

## 391: What is Crossplane?

Crossplane extends Kubernetes to manage outside infrastructure. Providers add CRDs for cloud resources (an RDS instance, an S3 bucket, a Cloud SQL database), and Crossplane controllers keep the real resources in sync with the objects. Platform teams build compositions, simple custom APIs like `PostgresInstance` with a few fields, that create all the underlying cloud pieces with company defaults.

App teams can then ask for a database with a small YAML file in the same GitOps flow as their app.

## 392: How do you enforce governance in large clusters without slowing teams down?

- Start policies in audit mode, show violations to teams, then enforce
- Give clear error messages with a link to docs on how to fix the problem
- Provide templates and shared charts that already pass the policies
- Allow exceptions through a reviewed process (Kyverno `PolicyException`, for example) instead of turning policies off
- Run the same policy checks in CI, so problems are found before deploy
- Keep the policy set small and focused on real risks

## 393: How do you split cluster costs between teams?

Costs come from nodes, storage, load balancers and network. Tools like OpenCost or Kubecost split node costs per Pod based on the larger of requests and usage, then sum by namespace or label.

Make it work by:

- Requiring `team` and `cost-center` labels through policy
- Counting idle capacity and shared add-ons as a platform cost, or spreading it by usage
- Showing teams their numbers regularly, since over-requested resources are where most savings are

Requests matter more than usage for cost, because requests decide how many nodes you need.

## 394: How do you run LLM inference workloads on Kubernetes?

- GPU nodes with the right drivers, usually through the NVIDIA GPU Operator, and DRA or device plugins for allocation
- Model serving runtimes like vLLM, Text Generation Inference or KServe, often with an operator
- Store large model weights in object storage or image volumes, and cache them on nodes to cut startup time
- GPU sharing with MIG (hardware partitions) or time slicing for small models
- Autoscale on GPU utilization, queue depth or tokens per second, not CPU
- The Gateway API Inference Extension adds model-aware routing, like sending requests to the replica with the most free cache

GPUs are expensive, so scheduling, bin packing and scale to zero matter more than usual.

## 395: How do you run batch and HPC workloads on Kubernetes?

Plain Jobs work for simple cases. For shared clusters with many teams and limited capacity, add:

- Kueue: queues Jobs and admits them only when there is quota, with fair sharing between teams and priorities
- Gang scheduling (Kueue, Volcano or the built-in Workload API) for multi-Pod jobs
- JobSet or the Kubeflow Training Operator for distributed training with several roles
- Indexed Jobs and `backoffLimitPerIndex` for parallel tasks
- Spot nodes with checkpointing in the job

Batch nodes in their own pool with autoscaling keep batch from hurting online services.

## 396: How do you run Kubernetes at the edge?

Edge sites have small hardware, unreliable networks and no staff on site. Common choices:

- Lightweight distributions: k3s, k0s, MicroK8s
- Single-node clusters, managed centrally through GitOps (Fleet, Flux, Argo CD) pulling from Git when the network is up
- KubeEdge or OpenYurt when you want one control plane in the cloud managing edge nodes that can work offline
- Local image registries or pre-loaded images so sites do not depend on the internet

Design apps to keep working when the connection to the center is down.

## 397: How do you upgrade many clusters safely?

- Keep clusters as similar as possible (same add-ons, managed through GitOps)
- Test upgrades in a non-prod cluster with real workloads first
- Upgrade in waves: dev, staging, a low-risk prod cluster, then the rest
- Check deprecated APIs and add-on compatibility before each wave
- Prefer replacing nodes over upgrading them in place
- For big jumps or risky changes, consider blue-green clusters: build a new cluster, move workloads over with GitOps, shift traffic, then delete the old one

## 398: What is the Kubernetes version skew policy?

- kube-apiserver instances in an HA cluster can differ by at most one minor version during an upgrade.
- The kubelet and kube-proxy can be up to three minor versions older than the API server, but never newer.
- The controller manager, scheduler and cloud controller manager can be at most one minor version older than the API server.
- kubectl is supported one minor version older or newer than the API server.

That is why you upgrade the control plane first and nodes after, one minor version at a time for the control plane.

## 399: What are feature gates?

Feature gates are switches for features in Kubernetes components. Alpha features are off by default, beta features are usually on (except new beta APIs), and stable features become locked on and the gate is removed later.

```bash
kube-apiserver --feature-gates=SomeAlphaFeature=true
```

Alpha features are not meant for production and may change or disappear. Managed services usually do not let you turn on alpha gates. When a gate becomes locked on, you can no longer turn the feature off, which you should know before upgrading.

## 400: What is the mixed version proxy?

During an upgrade of an HA control plane, different API servers can serve different sets of APIs for a short time. A request for a resource that only the newer server knows might hit an older one and fail with a 404, or the garbage collector might make wrong decisions based on missing APIs. The mixed version proxy (beta in 1.36) makes an API server forward such requests to a peer that can serve them, so clients see a consistent API during upgrades.

## 401: What is KYAML?

KYAML is a stricter style of YAML for Kubernetes, and `kubectl get -o kyaml` is stable in 1.37. It is still valid YAML, so every tool can read it, but it avoids the usual traps: strings are always quoted (so `NO` or `1.10` are not turned into a boolean or a number), and it uses flow style with brackets and braces, so wrong indentation cannot silently change the meaning.

```bash
kubectl get deployment web -o kyaml
```

It is useful for generated files and for teams that keep getting bitten by YAML type guessing.

## 402: Which control plane metrics would you watch?

- API server: request rate, error rate (5xx), latency by verb and resource (`apiserver_request_duration_seconds`), APF rejections, inflight requests
- etcd: `wal_fsync_duration_seconds`, `backend_commit_duration_seconds`, leader changes, database size
- Scheduler: pending Pods, scheduling latency, failed scheduling attempts
- Controller manager: work queue depth and latency per controller
- Admission webhooks: latency and rejection rate
- Nodes: number of NotReady nodes, kubelet PLEG latency

On managed clusters you see only some of these, but API server metrics are usually exposed.

## 403: How would you define SLOs for a Kubernetes platform?

Pick things platform users actually feel:

- API availability: share of successful API requests
- Deployment success: share of rollouts that finish within a set time
- Pod startup time: time from creation to ready for a standard workload
- Scheduling latency for Pods that fit
- Ingress or gateway availability and latency
- DNS success rate inside the cluster

Set targets like "99.9% of API requests succeed over 30 days", alert on error budget burn rate and use the budget to decide when to slow down risky platform changes.

## 404: How do you test that your setup really survives failures?

Use chaos engineering in a controlled way. Tools like Chaos Mesh or LitmusChaos can kill Pods, add network latency or packet loss, stress CPU and memory, or kill nodes.

Start with simple experiments in staging: delete a Pod, drain a node, kill a zone's nodes, break DNS for one namespace. Write down what you expect to happen, run the test, and fix what surprised you. Move to production only with small, controlled experiments and an easy way to stop them.

## 405: What are Pod-level resources?

Normally you set requests and limits per container. With Pod-level resources, you set `spec.resources` for the whole Pod, and containers share that budget. It is handy for Pods with several containers where you do not want to tune each one, such as sidecars with spiky usage.

```yaml
spec:
  resources:
    requests:
      cpu: "1"
      memory: 1Gi
    limits:
      cpu: "2"
      memory: 2Gi
  containers:
    - name: app
      image: my-app:1.0
    - name: proxy
      image: envoyproxy/envoy:v1.35-latest
```

Container-level values can still be set inside it. In-place resize of Pod-level resources is beta. Check that your cluster version and feature gates support it before using it.

## 406: Why did sidecars used to break Jobs, and how do native sidecars fix it?

A Job is done when all its containers exit. A classic sidecar, like a proxy or log shipper in `containers`, never exits by itself, so the Job never completed. People used workarounds like shared files that told the sidecar to quit.

Native sidecars (init containers with `restartPolicy: Always`) are not counted when deciding if the Pod has finished. When the main container exits, the kubelet stops the sidecars and the Job completes. They also start before the main container, so a proxy is ready when the app starts.

## 407: What are the security risks of ephemeral debug containers?

`kubectl debug` can attach a container with any image to any Pod, share the process namespace of the target and see its files through `/proc`. Whoever can do that can read the app's memory, Secrets and tokens.

Control it with RBAC on the `pods/ephemeralcontainers` subresource, give it only to on-call engineers, log it in audit logs and use admission policies to limit which debug images and debug profiles are allowed. Pod Security Admission also checks ephemeral containers, so a restricted namespace will not accept a privileged debug container.

## 408: How do nodes get credentials for private registries without imagePullSecrets?

The kubelet supports image credential provider plugins. The kubelet calls a plugin binary (for example the ECR, GCR/Artifact Registry or ACR provider) that returns short-lived registry credentials based on the node's cloud identity.

Newer releases also let the credential provider use the Pod's own ServiceAccount token, so image pulls can be authorized per workload instead of per node. That means one team's Pods cannot pull another team's private images just because they run on the same node.

## 409: What are Pod scheduling gates?

`schedulingGates` keep a Pod from being considered by the scheduler until every gate is removed. The Pod exists with status `SchedulingGated` but uses no scheduler time.

```yaml
spec:
  schedulingGates:
    - name: example.com/quota-check
```

An outside controller, such as a quota system or a batch queue, removes the gate when the Pod is allowed to run. It is cleaner than creating Pods that sit unschedulable and keep the scheduler busy.

## 410: What is the descheduler?

The scheduler only places Pods when they are created. Over time, the cluster gets unbalanced: nodes added later are empty, affinity rules are no longer met, some nodes are overloaded. The descheduler is a separate project that evicts Pods according to policies (for example `RemoveDuplicates`, `LowNodeUtilization`, `RemovePodsViolatingTopologySpreadConstraint`), so the scheduler can place them better.

It respects PDBs and priorities. Run it as a CronJob or Deployment and start with conservative policies, because evictions disturb running workloads.

## 411: How do you use huge pages in Kubernetes?

Some apps, like databases and DPDK network apps, run faster with huge pages (2Mi or 1Gi memory pages). The node must have them pre-allocated. Pods request them like a resource, and requests must equal limits.

```yaml
resources:
  requests:
    memory: 1Gi
    hugepages-2Mi: 512Mi
  limits:
    memory: 1Gi
    hugepages-2Mi: 512Mi
volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
```

Huge pages cannot be overcommitted, so plan node capacity for them.

## 412: How can you change how quickly Pods are evicted from a failed node?

By default, Pods get tolerations for `node.kubernetes.io/not-ready` and `node.kubernetes.io/unreachable` with `tolerationSeconds: 300`. So Pods on a dead node are only replaced after about five minutes plus detection time. You can set your own values per Pod:

```yaml
tolerations:
  - key: node.kubernetes.io/unreachable
    operator: Exists
    effect: NoExecute
    tolerationSeconds: 30
  - key: node.kubernetes.io/not-ready
    operator: Exists
    effect: NoExecute
    tolerationSeconds: 30
```

Shorter times recover faster but cause more churn during short network problems. For stateful apps, be careful: a node that only lost the network might still be running the old Pod.

## 413: Why does a Pod with a large volume take minutes to start, and how do you fix it?

When you set `fsGroup`, the kubelet by default changes ownership and permissions of every file in the volume on each mount. With millions of files that takes a long time.

Set `fsGroupChangePolicy: OnRootMismatch`, so the kubelet only does the recursive change when the volume's root folder does not already have the right owner:

```yaml
securityContext:
  fsGroup: 2000
  fsGroupChangePolicy: OnRootMismatch
```

Some CSI drivers can apply the group at mount time instead. SELinux relabeling causes a similar slowdown, which mount-time labels fix.

## 414: How does Kubernetes avoid slow SELinux relabeling of volumes?

On SELinux systems, volumes used to be relabeled file by file so a container could access them, which can take very long. Since 1.37, with the CSI driver opting in (`seLinuxMount: true` on the CSIDriver), the kubelet mounts the volume with `-o context=<label>`, which applies the label to the whole mount at once.

The catch is that Pods sharing a volume must use the same SELinux label. A Pod can keep the old behavior with `spec.securityContext.seLinuxChangePolicy: Recursive`, for example when several Pods with different labels must share a volume.

## 415: How do Secrets get from the API server to a container?

The kubelet only gets Secrets for Pods scheduled on its node, which the Node authorizer enforces. It watches or fetches them from the API server over TLS. Secret volumes are written to a tmpfs (memory) on the node, not to disk, and mounted into the container. Env variables from Secrets are set when the container starts.

That means anyone with root on the node can read the Secrets of Pods on that node, and Secrets in env variables are also visible through `/proc` on the node. Node security is part of Secret security.

## 416: How can a PodDisruptionBudget block node drains, and how do you avoid it?

If a PDB allows zero disruptions, a drain waits forever. Examples: `minAvailable` equal to the number of replicas, `maxUnavailable: 0`, a single-replica Deployment with `minAvailable: 1`, or a PDB covering Pods that are already unhealthy.

Avoid it by:

- Making sure PDBs always allow at least one disruption when the app is healthy
- Running at least 2 replicas for anything with a PDB
- Setting `unhealthyPodEvictionPolicy: AlwaysAllow`, so Pods that are already not ready can be evicted even if the budget is used up

```yaml
spec:
  maxUnavailable: 1
  unhealthyPodEvictionPolicy: AlwaysAllow
```

Managed node upgrades usually force-evict after a timeout, which can cause the outage the PDB was meant to prevent.

## 417: How do you roll out config changes as safely as code changes?

Config changes cause many outages, because they often skip the checks code gets. To make them safe:

- Keep config in Git and review it like code
- Make config changes trigger a normal rollout (hash annotations or generated names), so readiness checks and rollback apply
- Use immutable, versioned ConfigMaps, so old Pods keep the old config during a rollout and rollback brings the old config back
- Validate config in CI and at app startup, and fail readiness on bad config
- Use canary rollouts for risky changes

## 418: How do you protect services from traffic spikes at the edge?

- Rate limiting per client or per API key at the gateway or ingress (most Gateway API implementations and service meshes support it)
- Request size limits and timeouts
- Retries with backoff and retry budgets, so retries do not multiply the load
- Circuit breaking in the mesh or client
- Load shedding in the app: return 429 or 503 early when overloaded instead of slowing down for everyone
- Autoscaling with enough headroom, and minimum replicas for known peaks

Kubernetes autoscaling is too slow for sudden spikes on its own.

## 419: How do you protect long-running jobs from node drains and scale-downs?

- Give batch Pods a PDB, or the Cluster Autoscaler annotation `cluster-autoscaler.kubernetes.io/safe-to-evict: "false"` (Karpenter uses `karpenter.sh/do-not-disrupt: "true"`)
- Use a long `terminationGracePeriodSeconds` so the job can checkpoint on SIGTERM
- Write checkpoints regularly so a restarted Pod can continue
- Use a Pod failure policy that ignores `DisruptionTarget` so evictions do not count as failures
- Run jobs on node pools that are not consolidated aggressively

Jobs that cannot checkpoint should be short, or run on on-demand nodes.

## 420: Why does the HPA keep fighting with your GitOps tool over replicas?

If your Deployment manifest sets `replicas: 3` and an HPA changes it to 8, the GitOps tool sees drift and sets it back to 3, then the HPA changes it again.

Fix: remove `replicas` from the manifest when an HPA manages the Deployment. With server-side apply, the field is then owned only by the HPA. Argo CD can also ignore the field with `ignoreDifferences`. Note that removing `replicas` from an existing manifest with client-side apply can reset it to 1 once, so do it carefully.

## 421: Why does Argo CD show resources as out of sync even right after a sync?

Common reasons:

- Defaults or mutations added by the API server or a mutating webhook (sidecar injection, added labels, default values) that are not in Git
- Fields changed by controllers, like `replicas` by an HPA or `caBundle` injected into webhook configs
- Different formatting of values, like `cpu: 1000m` versus `cpu: "1"`

Fix with server-side diff (more accurate), `ignoreDifferences` for fields that others own, or by writing manifests with the same values the server uses.

## 422: What are the limits of Helm at scale?

- Release state is stored in Secrets (one per revision), which can hit the 1 MiB object limit for huge charts
- Templates get hard to read and test, with lots of `if` blocks and indentation bugs
- CRDs in the `crds/` folder are installed but never upgraded by Helm
- `helm upgrade` can fail halfway and leave a release in a pending state
- Values files for many environments drift and duplicate each other

Mitigations: keep charts small, use a values schema, render with `helm template` in CI, manage CRDs separately, and let a GitOps tool drive Helm.

## 423: How do you rotate a database password with no downtime?

1. Create a second credential, or use a database feature that allows two valid passwords at the same time.
2. Update the Secret (through External Secrets or your secret store) to the new credential.
3. Roll the app, or let it reload the mounted file, so it starts using the new one.
4. Check that nothing uses the old credential anymore (database logs or metrics).
5. Remove the old credential.

Dynamic credentials from Vault, or cloud IAM authentication to the database, remove most manual rotation work.

## 424: What happens to the database when you scale an app to 100 Pods?

Each Pod opens its own connection pool. 100 Pods with a pool of 20 means 2,000 connections, which can exceed the database's limit or eat its memory, and autoscaling makes it worse during spikes.

Fixes:

- Smaller pools per Pod
- A connection pooler between the app and the database, like PgBouncer or RDS Proxy
- A max replica count in the HPA that the database can handle
- Watching connection counts when changing autoscaling

## 425: What are SPIFFE and SPIRE?

SPIFFE is a standard for workload identity: each workload gets an ID like `spiffe://example.org/ns/shop/sa/api` and a short-lived certificate (SVID) proving it. SPIRE is a common implementation. It checks a workload's identity using attestation (for example by asking the kubelet about the Pod) and issues certificates.

It gives one identity system across Kubernetes clusters, VMs and clouds, used for mTLS between services. Istio and other meshes use SPIFFE IDs internally.

## 426: How do you meet compliance rules like PCI DSS on Kubernetes?

- Separate in-scope workloads, ideally in their own cluster, or at least on dedicated nodes with strict NetworkPolicies
- Encrypt data in transit (mTLS) and at rest (KMS for Secrets, encrypted volumes)
- Strong access control: SSO with MFA, least-privilege RBAC, no shared admin accounts
- Audit logs kept for the required time
- Image scanning, signed images and admission policies
- Runtime detection and file integrity monitoring
- Regular reviews, with evidence you can show auditors, like policy reports and access reviews

Keep the scope small, since everything that can reach in-scope systems becomes part of the audit.

## 427: How do you test that a cluster works correctly after changes?

- Conformance tests with Sonobuoy or Hydrophone, which run the official end-to-end conformance suite
- Smoke tests after every upgrade: deploy a test app, check DNS, Service routing, ingress, storage and autoscaling
- Synthetic checks that run all the time, like a canary app that is deployed and probed every few minutes
- Policy and config tests in CI for add-ons

Certified Kubernetes distributions have passed the conformance tests, which is why workloads move between them without changes.

## 428: When is Kubernetes the wrong choice?

- A small app with a small team, where a PaaS (Cloud Run, App Runner, Fly.io, Heroku-like services) or a single VM with Docker Compose is much simpler
- No one on the team has time to learn and run it
- Workloads that do not fit containers well, or need special hardware without Kubernetes support
- When managed serverless already covers the needs at lower cost

Kubernetes pays off with many services, teams and environments, where a common platform saves more effort than it costs to run.

## 429: How do you move an app from VMs to Kubernetes?

1. Containerize it: externalize config, write logs to stdout, handle SIGTERM, keep no local state.
2. Move state out: sessions to Redis, files to object storage, and keep the database where it is at first.
3. Write the manifests or chart with probes, resources and a PDB.
4. Run it in Kubernetes next to the VMs and shift traffic slowly with weighted DNS or a load balancer.
5. Watch metrics and compare with the VMs.
6. Turn off the VMs when everything has moved.

Do not try to move every service at once. Start with a stateless, low-risk one.

## 430: How do you move workloads to a new cluster with no downtime?

1. Build the new cluster with the same add-ons and policies through GitOps.
2. Deploy the apps to the new cluster from the same Git config.
3. Handle state: point both clusters to the same external databases, or replicate data and plan a short cutover for stateful parts.
4. Shift traffic gradually with weighted DNS or a global load balancer.
5. Watch errors and latency, and keep the old cluster ready for rollback.
6. Remove the old cluster once traffic is fully moved.

This is also the basis of blue-green cluster upgrades.

## 431: How do you fail over traffic between clusters?

- DNS-based: Route 53, Cloud DNS or similar with health checks and weighted or failover records. Simple, but clients cache DNS.
- Global load balancers: cloud global load balancers or a CDN with several origins, with faster failover based on health checks
- Multi-cluster gateways or meshes: Istio multi-cluster or Cilium Cluster Mesh, failing over at the service level inside the network

Health checks should test real functionality, not just that the load balancer answers.

## 432: How would you prepare a Kubernetes app for a big planned traffic event?

- Load test at expected peak plus a margin, in a production-like environment
- Raise `minReplicas` before the event so you do not rely on autoscaling from a low base
- Make sure node groups have enough max size and the cloud account has enough quota
- Pre-scale databases, caches and connection poolers
- Freeze risky changes and upgrades
- Check rate limits and dependencies like third-party APIs
- Prepare dashboards, alerts and runbooks, and have people on call

Scale back down afterward.

## 433: How do you choose a CNI plugin?

Questions to ask:

- Does the managed service have a default (VPC CNI, Azure CNI) that integrates with the cloud network?
- Do you need NetworkPolicy, and do you need layer 7 or DNS-based policies?
- Do you want to replace kube-proxy with eBPF for performance and visibility?
- Routable Pod IPs or overlay? How many IPs do you have?
- Encryption between nodes (WireGuard, IPsec)?
- Multi-cluster networking?
- What does your team already know?

Cilium is a common choice for feature-rich setups, Calico for policy and BGP, and the cloud CNIs when you want the simplest managed option.

## 434: What are the trade-offs of fully managed node options like GKE Autopilot or EKS Auto Mode?

With these, the provider manages nodes too: scaling, upgrades, OS patching and often core add-ons. You pay per Pod resources (Autopilot) or for managed nodes, and you can focus on workloads.

Trade-offs:

- Less control: some features are blocked, like privileged Pods, certain host access or custom kernels
- Pricing can be higher for steady, well-packed workloads, and lower for spiky or small ones
- Debugging at node level is harder

It suits teams that want Kubernetes APIs without running nodes. Large platforms with special needs often keep their own node pools.

## 435: What is the pause container?

Every Pod has a sandbox, and on Linux runtimes it is a tiny "pause" container started first. It holds the Pod's network namespace (and sometimes other namespaces), so app containers can join it and restart without losing the Pod IP. With a shared process namespace, it also acts as PID 1 and reaps zombie processes.

You do not see it in `kubectl`, but you see it with `crictl pods` on the node.

## 436: How does the kubelet clean up images and containers?

The kubelet removes unused images when disk usage goes over `imageGCHighThresholdPercent` (85% by default) until it is below `imageGCLowThresholdPercent` (80%). Images used by running containers are never removed. You can also set a maximum age for unused images. Dead containers are cleaned up as well.

If nodes keep hitting disk pressure, look at large images, many different image versions, large logs and `emptyDir` usage, or give nodes bigger disks.

## 437: How are container logs rotated, and what happens with very chatty apps?

The kubelet rotates container log files based on `containerLogMaxSize` (default 10Mi) and `containerLogMaxFiles` (default 5). `kubectl logs` only shows what is still on the node, so older logs are gone unless an agent shipped them.

A very chatty app can rotate faster than the log agent reads, which loses logs, and it uses disk and CPU for logging. Lower the log level, sample noisy logs, and make sure the agent can keep up.

## 438: Can a node have more requested resources than it has?

No, requests can never add up to more than allocatable, that is how the scheduler decides. But limits can add up to much more than the node has, which is called overcommit. If many Burstable Pods use more than their requests at the same time, the node runs out: CPU is shared out by weight, while memory pressure leads to evictions and OOM kills.

So requests should reflect normal usage, and memory limits should not be far above requests for important apps.

## 439: How do you test a Kubernetes controller?

- Unit tests for the pieces of reconcile logic
- envtest from controller-runtime, which starts a real API server and etcd without nodes, so you can test reconcile against real API behavior, including CRD validation
- End-to-end tests in a kind cluster, deploying the controller and checking real resources
- Tests for edge cases: conflicts (409), objects deleted mid-reconcile, missing permissions, many objects

Run the controller with `-race` in Go tests, since controllers often have concurrency bugs.

## 440: How does a program talk to the Kubernetes API from inside a Pod?

Inside a Pod, the client library finds the API server through the `KUBERNETES_SERVICE_HOST` and `KUBERNETES_SERVICE_PORT` env variables, and uses the ServiceAccount token and CA certificate mounted at `/var/run/secrets/kubernetes.io/serviceaccount/`.

```go
config, err := rest.InClusterConfig()
if err != nil {
    log.Fatal(err)
}
clientset, err := kubernetes.NewForConfig(config)
if err != nil {
    log.Fatal(err)
}
pods, err := clientset.CoreV1().Pods("shop").List(ctx, metav1.ListOptions{})
```

Official clients exist for Go, Python, Java, JavaScript and others. The ServiceAccount needs RBAC permissions for whatever the program does.

## 441: When are Kubernetes Secrets not enough?

Kubernetes Secrets are fine for many apps, but they have limits:

- Anyone who can create Pods in the namespace can read them
- No built-in rotation, versioning or access audit on reads beyond audit logs
- No dynamic, per-use credentials

When you need dynamic database credentials, detailed access audit, automatic rotation or one source shared by Kubernetes and non-Kubernetes systems, use a secret manager like Vault or a cloud secret manager directly, through its agent, CSI driver or SDK.

## 442: How does the kubelet decide which process the OOM killer kills?

The kubelet sets `oom_score_adj` for container processes based on QoS:

- Guaranteed Pods get a very low score (-997), so they are killed last
- BestEffort Pods get the highest (1000), so they are killed first
- Burstable Pods get a value based on their memory request compared to node memory, so Pods that requested less are killed sooner

This is for the case where the whole node runs out of memory before the kubelet can evict. With cgroup v2, the kernel can also kill the whole container cgroup at once instead of a single process, so a container does not limp along with half its processes dead.

## 443: How do you keep Kubernetes events longer than an hour?

Events expire from the API (default one hour) to keep etcd small. To keep them:

- Run an event exporter (like kubernetes-event-exporter) that sends events to your log backend
- Many log agents and the OpenTelemetry Collector (k8sobjects or k8s events receivers) can collect events too
- Managed clusters often ship events to the cloud logging service

Stored events are very useful after an incident, for example to see when Pods were evicted or failed to schedule.

## 444: How do you find out which NetworkPolicy is dropping traffic?

Standard Kubernetes has no drop logs, so you need tools from your CNI:

- Cilium: `hubble observe --verdict DROPPED --namespace shop` shows dropped flows and the reason
- Calico: policy logging actions and flow logs
- Cloud CNIs have their own policy logs

Without those, test connectivity step by step from a debug Pod and read the policies that select both the source and destination Pods. Remember that both the egress rules of the source and the ingress rules of the destination must allow the traffic.

## 445: How do you profile an app running in a Kubernetes Pod?

- If the app has a profiling endpoint (Go pprof, Node.js inspector, Java JFR), port-forward to it and collect a profile
- Use `kubectl debug` with a tools image that shares the process namespace, to run `perf`, `py-spy` or `async-profiler` against the process
- Continuous profiling with Pyroscope, Parca or a vendor, often with eBPF agents running as a DaemonSet so no app changes are needed

```bash
kubectl port-forward pod/api-7d9f 6060:6060
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30
```

Profile under real load, and keep in mind CPU limits can change what you see.

## 446: How do you manage the versions of cluster add-ons?

Add-ons like the CNI, CSI drivers, CoreDNS, ingress or gateway, cert-manager and monitoring are part of the platform and need upgrades too.

- Manage them all through GitOps with pinned chart versions
- Use Renovate or Dependabot to open PRs for new versions
- Check each add-on's supported Kubernetes versions before a cluster upgrade
- Roll add-on upgrades through dev and staging clusters first
- On managed clusters, use the provider's managed add-ons where they fit

Old, forgotten add-ons are a common reason cluster upgrades get blocked.

## 447: When would you run an agent as a sidecar and when as a DaemonSet?

- DaemonSet: one agent per node serves all Pods. Uses fewer resources overall and is easier to upgrade. Good for logs, node metrics and security agents.
- Sidecar: one agent per Pod. Gives per-Pod config, identity and isolation, and the agent scales with the app. Good for proxies with per-workload identity or app-specific helpers.

The trend in service meshes is moving from sidecars to per-node proxies (Istio ambient) to save resources, with per-service proxies only where layer 7 features are needed.

## 448: How should a CI system get access to deploy to a cluster?

Avoid long-lived kubeconfigs stored as CI secrets. Better options:

- GitOps: CI only pushes to Git and the in-cluster agent deploys, so CI needs no cluster access at all
- OIDC federation: the CI's OIDC token (for example from GitHub Actions) is exchanged for short-lived cloud credentials, which map to a cluster identity (EKS access entries, GKE IAM)
- A dedicated identity per pipeline with RBAC limited to the namespaces it deploys to

Log all deployments and make it impossible for CI to change RBAC or cluster-wide resources.

## 449: Walk through deploying a new service to production on Kubernetes.

1. Build an image with a small, non-root base and push it with a Git SHA tag. Scan and sign it.
2. Write a Deployment with resources, probes, security context, graceful shutdown and spread constraints.
3. Add a Service, an HTTPRoute (or Ingress) with TLS from cert-manager, and DNS through external-dns.
4. Add config through ConfigMaps and Secrets from your secret store.
5. Add an HPA, a PDB and NetworkPolicies.
6. Add a ServiceMonitor, dashboards, alerts and log fields.
7. Commit to the deploy repo, and let GitOps roll it out to staging, then to production after checks.
8. Watch the rollout and error rates, with a clear rollback path.

## 450: What changed in Kubernetes recently that you should know about?

Some notable changes from the last few releases (1.33 to 1.37):

- Native sidecar containers, in-place Pod resize, user namespaces, nftables kube-proxy mode and ServiceCIDR objects are stable
- Image volumes, MutatingAdmissionPolicy, PSI metrics, fine-grained kubelet authorization and VolumeGroupSnapshot became stable in 1.36
- Pod Certificates, ClusterTrustBundles, built-in storage version migration, configurable HPA tolerance and `kubectl -o kyaml` became stable in 1.37, with HPA scale to zero and gang scheduling in beta
- Dynamic Resource Allocation for GPUs and other devices is stable and growing fast
- The `gitRepo` volume is removed, Service `externalIPs` is deprecated, kube-proxy IPVS mode and kube-dns are deprecated, and cgroup v1 nodes fail by default
- The community ingress-nginx controller was retired in March 2026, and the Gateway API is the recommended path for new setups

Read the release notes and the deprecation guide before every upgrade, because defaults change between minor versions.
