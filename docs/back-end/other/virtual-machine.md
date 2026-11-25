# Virtual Machine Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 interview questions and answers about virtual machines: 150 easy, 150 moderate and 150 advanced. It covers hypervisors, KVM and QEMU, VMware, Hyper-V, VirtualBox, Proxmox, cloud VMs like AWS EC2, and a little about process VMs like the JVM and V8. Answers are based on QEMU 11.x, Proxmox VE 9.x, VirtualBox 7.2 and current cloud APIs, and code examples use the command line or Node.js.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a virtual machine?](#1-what-is-a-virtual-machine)
- [2: What is a hypervisor?](#2-what-is-a-hypervisor)
- [3: What is the difference between a host and a guest?](#3-what-is-the-difference-between-a-host-and-a-guest)
- [4: What is a Type 1 hypervisor?](#4-what-is-a-type-1-hypervisor)
- [5: What is a Type 2 hypervisor?](#5-what-is-a-type-2-hypervisor)
- [6: Why do companies use virtual machines?](#6-why-do-companies-use-virtual-machines)
- [7: What is virtualization?](#7-what-is-virtualization)
- [8: What are the main parts of a virtual machine?](#8-what-are-the-main-parts-of-a-virtual-machine)
- [9: What is a vCPU?](#9-what-is-a-vcpu)
- [10: What is a virtual disk?](#10-what-is-a-virtual-disk)
- [11: What is a snapshot of a VM?](#11-what-is-a-snapshot-of-a-vm)
- [12: What is the difference between a snapshot and a backup?](#12-what-is-the-difference-between-a-snapshot-and-a-backup)
- [13: What is a VM template?](#13-what-is-a-vm-template)
- [14: What does cloning a VM mean?](#14-what-does-cloning-a-vm-mean)
- [15: What is an ISO file and how is it used with VMs?](#15-what-is-an-iso-file-and-how-is-it-used-with-vms)
- [16: What is a guest operating system?](#16-what-is-a-guest-operating-system)
- [17: Can a VM run a different OS than the host?](#17-can-a-vm-run-a-different-os-than-the-host)
- [18: What is the difference between virtualization and emulation?](#18-what-is-the-difference-between-virtualization-and-emulation)
- [19: What is KVM?](#19-what-is-kvm)
- [20: What is QEMU?](#20-what-is-qemu)
- [21: What is VirtualBox?](#21-what-is-virtualbox)
- [22: What is VMware ESXi?](#22-what-is-vmware-esxi)
- [23: What is Microsoft Hyper-V?](#23-what-is-microsoft-hyper-v)
- [24: What is Proxmox VE?](#24-what-is-proxmox-ve)
- [25: What is Xen?](#25-what-is-xen)
- [26: What is a cloud VM?](#26-what-is-a-cloud-vm)
- [27: What is an EC2 instance?](#27-what-is-an-ec2-instance)
- [28: What is a machine image?](#28-what-is-a-machine-image)
- [29: What is the difference between a VM and a container?](#29-what-is-the-difference-between-a-vm-and-a-container)
- [30: Which is more secure, a VM or a container?](#30-which-is-more-secure-a-vm-or-a-container)
- [31: What is hardware-assisted virtualization?](#31-what-is-hardware-assisted-virtualization)
- [32: What are Intel VT-x and AMD-V?](#32-what-are-intel-vt-x-and-amd-v)
- [33: How do you check if your Linux machine supports hardware virtualization?](#33-how-do-you-check-if-your-linux-machine-supports-hardware-virtualization)
- [34: What happens if virtualization is disabled in the BIOS?](#34-what-happens-if-virtualization-is-disabled-in-the-bios)
- [35: What is a virtual network interface card (vNIC)?](#35-what-is-a-virtual-network-interface-card-vnic)
- [36: What is NAT networking in a VM?](#36-what-is-nat-networking-in-a-vm)
- [37: What is bridged networking?](#37-what-is-bridged-networking)
- [38: What is host-only networking?](#38-what-is-host-only-networking)
- [39: What is a virtual switch?](#39-what-is-a-virtual-switch)
- [40: What are guest additions or guest tools?](#40-what-are-guest-additions-or-guest-tools)
- [41: What is the QEMU guest agent?](#41-what-is-the-qemu-guest-agent)
- [42: What does it mean to suspend a VM?](#42-what-does-it-mean-to-suspend-a-vm)
- [43: What is the difference between pausing and suspending a VM?](#43-what-is-the-difference-between-pausing-and-suspending-a-vm)
- [44: What is a thin-provisioned disk?](#44-what-is-a-thin-provisioned-disk)
- [45: What is a thick-provisioned disk?](#45-what-is-a-thick-provisioned-disk)
- [46: What is overcommitment in virtualization?](#46-what-is-overcommitment-in-virtualization)
- [47: What is a hypervisor's job in managing memory?](#47-what-is-a-hypervisors-job-in-managing-memory)
- [48: What is a VM console?](#48-what-is-a-vm-console)
- [49: What is VNC in the context of VMs?](#49-what-is-vnc-in-the-context-of-vms)
- [50: What is SPICE?](#50-what-is-spice)
- [51: What is libvirt?](#51-what-is-libvirt)
- [52: What is virsh?](#52-what-is-virsh)
- [53: What is virt-manager?](#53-what-is-virt-manager)
- [54: What is Vagrant?](#54-what-is-vagrant)
- [55: What does a basic Vagrantfile look like?](#55-what-does-a-basic-vagrantfile-look-like)
- [56: What is the difference between shutting down and powering off a VM?](#56-what-is-the-difference-between-shutting-down-and-powering-off-a-vm)
- [57: What is ACPI in a VM?](#57-what-is-acpi-in-a-vm)
- [58: What is BIOS vs UEFI in a VM?](#58-what-is-bios-vs-uefi-in-a-vm)
- [59: What is a virtual TPM?](#59-what-is-a-virtual-tpm)
- [60: What is a VM's MAC address?](#60-what-is-a-vms-mac-address)
- [61: What is a live migration?](#61-what-is-a-live-migration)
- [62: What is a cold migration?](#62-what-is-a-cold-migration)
- [63: What is high availability (HA) for VMs?](#63-what-is-high-availability-ha-for-vms)
- [64: What is a VM cluster?](#64-what-is-a-vm-cluster)
- [65: What is shared storage and why do VM clusters need it?](#65-what-is-shared-storage-and-why-do-vm-clusters-need-it)
- [66: What is nested virtualization?](#66-what-is-nested-virtualization)
- [67: What is WSL 2?](#67-what-is-wsl-2)
- [68: How does Docker Desktop on macOS use a VM?](#68-how-does-docker-desktop-on-macos-use-a-vm)
- [69: What is a process virtual machine?](#69-what-is-a-process-virtual-machine)
- [70: What is the difference between a system VM and a process VM?](#70-what-is-the-difference-between-a-system-vm-and-a-process-vm)
- [71: What is the JVM?](#71-what-is-the-jvm)
- [72: Is V8 a virtual machine?](#72-is-v8-a-virtual-machine)
- [73: What is the Node.js vm module?](#73-what-is-the-nodejs-vm-module)
- [74: What is a VM host's capacity?](#74-what-is-a-vm-hosts-capacity)
- [75: What is a VM's "size" or "flavor"?](#75-what-is-a-vms-size-or-flavor)
- [76: What does it mean to resize a VM?](#76-what-does-it-mean-to-resize-a-vm)
- [77: How do you grow a disk of a Linux VM?](#77-how-do-you-grow-a-disk-of-a-linux-vm)
- [78: What is a VM's boot order?](#78-what-is-a-vms-boot-order)
- [79: What is PXE boot?](#79-what-is-pxe-boot)
- [80: What is cloud-init?](#80-what-is-cloud-init)
- [81: What does a simple cloud-init user-data file look like?](#81-what-does-a-simple-cloud-init-user-data-file-look-like)
- [82: What is user data in AWS EC2?](#82-what-is-user-data-in-aws-ec2)
- [83: What is the instance metadata service?](#83-what-is-the-instance-metadata-service)
- [84: What is the difference between stopping and terminating an EC2 instance?](#84-what-is-the-difference-between-stopping-and-terminating-an-ec2-instance)
- [85: What is EBS?](#85-what-is-ebs)
- [86: What is instance store?](#86-what-is-instance-store)
- [87: What is a public IP vs a private IP for a cloud VM?](#87-what-is-a-public-ip-vs-a-private-ip-for-a-cloud-vm)
- [88: What is a security group?](#88-what-is-a-security-group)
- [89: How do you connect to a Linux VM?](#89-how-do-you-connect-to-a-linux-vm)
- [90: How do you connect to a Windows VM?](#90-how-do-you-connect-to-a-windows-vm)
- [91: What is a bastion host?](#91-what-is-a-bastion-host)
- [92: What are the main benefits of VMs for developers?](#92-what-are-the-main-benefits-of-vms-for-developers)
- [93: What are the downsides of VMs?](#93-what-are-the-downsides-of-vms)
- [94: What is VM sprawl?](#94-what-is-vm-sprawl)
- [95: What is a "golden image"?](#95-what-is-a-golden-image)
- [96: What is Packer?](#96-what-is-packer)
- [97: What is Terraform's role with VMs?](#97-what-is-terraforms-role-with-vms)
- [98: What is a hypervisor host's management network?](#98-what-is-a-hypervisor-hosts-management-network)
- [99: What is vCenter Server?](#99-what-is-vcenter-server)
- [100: What is a virtual appliance?](#100-what-is-a-virtual-appliance)
- [101: What are OVF and OVA files?](#101-what-are-ovf-and-ova-files)
- [102: What is a hypervisor's datastore?](#102-what-is-a-hypervisors-datastore)
- [103: What files make up a VMware VM?](#103-what-files-make-up-a-vmware-vm)
- [104: What is the qcow2 format?](#104-what-is-the-qcow2-format)
- [105: What is a raw disk image?](#105-what-is-a-raw-disk-image)
- [106: How do you create a disk image with qemu-img?](#106-how-do-you-create-a-disk-image-with-qemu-img)
- [107: How do you convert a disk image between formats?](#107-how-do-you-convert-a-disk-image-between-formats)
- [108: What is VHDX?](#108-what-is-vhdx)
- [109: What is VDI?](#109-what-is-vdi)
- [110: What is Virtual Desktop Infrastructure (VDI)?](#110-what-is-virtual-desktop-infrastructure-vdi)
- [111: What is a virtual CD/DVD drive?](#111-what-is-a-virtual-cddvd-drive)
- [112: What is USB passthrough?](#112-what-is-usb-passthrough)
- [113: What are shared folders?](#113-what-are-shared-folders)
- [114: What is a hypervisor's resource pool?](#114-what-is-a-hypervisors-resource-pool)
- [115: What is a CPU reservation for a VM?](#115-what-is-a-cpu-reservation-for-a-vm)
- [116: What is a VM resource limit?](#116-what-is-a-vm-resource-limit)
- [117: What are shares in VM resource management?](#117-what-are-shares-in-vm-resource-management)
- [118: What is a vCPU to physical core ratio?](#118-what-is-a-vcpu-to-physical-core-ratio)
- [119: What is a hypervisor's CPU ready time?](#119-what-is-a-hypervisors-cpu-ready-time)
- [120: What is steal time in a Linux VM?](#120-what-is-steal-time-in-a-linux-vm)
- [121: What is a noisy neighbor?](#121-what-is-a-noisy-neighbor)
- [122: What is a dedicated host?](#122-what-is-a-dedicated-host)
- [123: What is a spot instance?](#123-what-is-a-spot-instance)
- [124: What is a reserved instance or savings plan?](#124-what-is-a-reserved-instance-or-savings-plan)
- [125: What is an Availability Zone?](#125-what-is-an-availability-zone)
- [126: What is an auto scaling group?](#126-what-is-an-auto-scaling-group)
- [127: What is a launch template?](#127-what-is-a-launch-template)
- [128: What is the virtio standard?](#128-what-is-the-virtio-standard)
- [129: What is an emulated device?](#129-what-is-an-emulated-device)
- [130: What is a paravirtualized device?](#130-what-is-a-paravirtualized-device)
- [131: What is paravirtualization?](#131-what-is-paravirtualization)
- [132: What is full virtualization?](#132-what-is-full-virtualization)
- [133: Can you run macOS in a VM?](#133-can-you-run-macos-in-a-vm)
- [134: Can you run Windows in a VM on an Apple Silicon Mac?](#134-can-you-run-windows-in-a-vm-on-an-apple-silicon-mac)
- [135: What is UTM?](#135-what-is-utm)
- [136: What is Apple's Virtualization framework?](#136-what-is-apples-virtualization-framework)
- [137: What is Multipass?](#137-what-is-multipass)
- [138: What is Firecracker?](#138-what-is-firecracker)
- [139: What is a microVM?](#139-what-is-a-microvm)
- [140: What is Kata Containers?](#140-what-is-kata-containers)
- [141: What is the host operating system's role in a Type 2 hypervisor?](#141-what-is-the-host-operating-systems-role-in-a-type-2-hypervisor)
- [142: What is a VM's uptime and why does it matter?](#142-what-is-a-vms-uptime-and-why-does-it-matter)
- [143: What is scheduled maintenance for cloud VMs?](#143-what-is-scheduled-maintenance-for-cloud-vms)
- [144: What is the difference between rebooting and stop/start of an EC2 instance?](#144-what-is-the-difference-between-rebooting-and-stopstart-of-an-ec2-instance)
- [145: How do you list running EC2 instances with Node.js?](#145-how-do-you-list-running-ec2-instances-with-nodejs)
- [146: How do you start and stop an EC2 instance with Node.js?](#146-how-do-you-start-and-stop-an-ec2-instance-with-nodejs)
- [147: What is a hypervisor's VM log used for?](#147-what-is-a-hypervisors-vm-log-used-for)
- [148: What is the VM BIOS/UEFI boot screen useful for?](#148-what-is-the-vm-biosuefi-boot-screen-useful-for)
- [149: What is time sync in a VM and why does it matter?](#149-what-is-time-sync-in-a-vm-and-why-does-it-matter)
- [150: What is the most common first step when a VM is slow?](#150-what-is-the-most-common-first-step-when-a-vm-is-slow)

### Moderate Questions (151-300)

- [151: How do KVM and QEMU work together?](#151-how-do-kvm-and-qemu-work-together)
- [152: How do you start a simple KVM VM with QEMU directly?](#152-how-do-you-start-a-simple-kvm-vm-with-qemu-directly)
- [153: How do you create a VM with virt-install?](#153-how-do-you-create-a-vm-with-virt-install)
- [154: What does a libvirt domain XML look like?](#154-what-does-a-libvirt-domain-xml-look-like)
- [155: What is the difference between virsh define and virsh create?](#155-what-is-the-difference-between-virsh-define-and-virsh-create)
- [156: What are the i440fx and q35 machine types?](#156-what-are-the-i440fx-and-q35-machine-types)
- [157: Why do you pin a QEMU machine type version like pc-q35-11.0?](#157-why-do-you-pin-a-qemu-machine-type-version-like-pc-q35-110)
- [158: What are the CPU models host-passthrough and host-model?](#158-what-are-the-cpu-models-host-passthrough-and-host-model)
- [159: What are x86-64 microarchitecture levels like x86-64-v2 and v3?](#159-what-are-x86-64-microarchitecture-levels-like-x86-64-v2-and-v3)
- [160: How do you install virtio drivers on a Windows guest?](#160-how-do-you-install-virtio-drivers-on-a-windows-guest)
- [161: What is the difference between virtio-blk and virtio-scsi?](#161-what-is-the-difference-between-virtio-blk-and-virtio-scsi)
- [162: What is an I/O thread in QEMU?](#162-what-is-an-io-thread-in-qemu)
- [163: What are the QEMU disk cache modes?](#163-what-are-the-qemu-disk-cache-modes)
- [164: What is io_uring in QEMU?](#164-what-is-io_uring-in-qemu)
- [165: How does a qcow2 backing file work?](#165-how-does-a-qcow2-backing-file-work)
- [166: What are internal vs external snapshots in qcow2?](#166-what-are-internal-vs-external-snapshots-in-qcow2)
- [167: How do you take a disk-only snapshot with virsh?](#167-how-do-you-take-a-disk-only-snapshot-with-virsh)
- [168: What is a crash-consistent vs application-consistent snapshot?](#168-what-is-a-crash-consistent-vs-application-consistent-snapshot)
- [169: Why are long-lived snapshots bad?](#169-why-are-long-lived-snapshots-bad)
- [170: What happens when you delete a snapshot?](#170-what-happens-when-you-delete-a-snapshot)
- [171: How does memory ballooning work?](#171-how-does-memory-ballooning-work)
- [172: What is Kernel Same-page Merging (KSM)?](#172-what-is-kernel-same-page-merging-ksm)
- [173: What is transparent page sharing in VMware?](#173-what-is-transparent-page-sharing-in-vmware)
- [174: What is memory hot-add?](#174-what-is-memory-hot-add)
- [175: What is virtio-mem?](#175-what-is-virtio-mem)
- [176: What is CPU hot-add?](#176-what-is-cpu-hot-add)
- [177: How do you configure a Linux bridge for VMs?](#177-how-do-you-configure-a-linux-bridge-for-vms)
- [178: What is Open vSwitch?](#178-what-is-open-vswitch)
- [179: How do VLANs work with VMs?](#179-how-do-vlans-work-with-vms)
- [180: What is macvtap?](#180-what-is-macvtap)
- [181: What is the libvirt default network?](#181-what-is-the-libvirt-default-network)
- [182: How do you find the IP address of a libvirt VM?](#182-how-do-you-find-the-ip-address-of-a-libvirt-vm)
- [183: What is SR-IOV?](#183-what-is-sr-iov)
- [184: What is PCI passthrough?](#184-what-is-pci-passthrough)
- [185: What is an IOMMU?](#185-what-is-an-iommu)
- [186: What are IOMMU groups?](#186-what-are-iommu-groups)
- [187: What is VFIO?](#187-what-is-vfio)
- [188: How do you use a GPU in a VM?](#188-how-do-you-use-a-gpu-in-a-vm)
- [189: What is NUMA and why does it matter for VMs?](#189-what-is-numa-and-why-does-it-matter-for-vms)
- [190: What is vNUMA?](#190-what-is-vnuma)
- [191: What is CPU pinning?](#191-what-is-cpu-pinning)
- [192: What are huge pages and how do they help VMs?](#192-what-are-huge-pages-and-how-do-they-help-vms)
- [193: What is the difference between sockets, cores and threads in a VM's CPU topology?](#193-what-is-the-difference-between-sockets-cores-and-threads-in-a-vms-cpu-topology)
- [194: Should you give a VM as many vCPUs as possible?](#194-should-you-give-a-vm-as-many-vcpus-as-possible)
- [195: How do you right-size a VM?](#195-how-do-you-right-size-a-vm)
- [196: How does live migration of memory work step by step?](#196-how-does-live-migration-of-memory-work-step-by-step)
- [197: What is needed for live migration to work?](#197-what-is-needed-for-live-migration-to-work)
- [198: How do you live migrate a VM with virsh?](#198-how-do-you-live-migrate-a-vm-with-virsh)
- [199: What is VMware vMotion and Storage vMotion?](#199-what-is-vmware-vmotion-and-storage-vmotion)
- [200: What is VMware DRS?](#200-what-is-vmware-drs)
- [201: What are affinity and anti-affinity rules?](#201-what-are-affinity-and-anti-affinity-rules)
- [202: What is a Proxmox VE cluster?](#202-what-is-a-proxmox-ve-cluster)
- [203: What is quorum in a VM cluster?](#203-what-is-quorum-in-a-vm-cluster)
- [204: What is fencing in an HA cluster?](#204-what-is-fencing-in-an-ha-cluster)
- [205: How do you manage Proxmox VMs from the command line?](#205-how-do-you-manage-proxmox-vms-from-the-command-line)
- [206: How do you use cloud-init with Proxmox?](#206-how-do-you-use-cloud-init-with-proxmox)
- [207: What is Proxmox Backup Server?](#207-what-is-proxmox-backup-server)
- [208: What is a dirty bitmap in QEMU?](#208-what-is-a-dirty-bitmap-in-qemu)
- [209: What is Changed Block Tracking (CBT)?](#209-what-is-changed-block-tracking-cbt)
- [210: How do backup tools back up a running VM?](#210-how-do-backup-tools-back-up-a-running-vm)
- [211: What is the 3-2-1 backup rule for VMs?](#211-what-is-the-3-2-1-backup-rule-for-vms)
- [212: Why should you test VM restores?](#212-why-should-you-test-vm-restores)
- [213: What is VM replication?](#213-what-is-vm-replication)
- [214: What is the difference between RPO and RTO for VMs?](#214-what-is-the-difference-between-rpo-and-rto-for-vms)
- [215: What is Ceph and how is it used with VMs?](#215-what-is-ceph-and-how-is-it-used-with-vms)
- [216: How does ZFS help with VM storage?](#216-how-does-zfs-help-with-vm-storage)
- [217: What is LVM-thin for VM disks?](#217-what-is-lvm-thin-for-vm-disks)
- [218: What is the TRIM or discard option for virtual disks?](#218-what-is-the-trim-or-discard-option-for-virtual-disks)
- [219: What is VMware VMFS?](#219-what-is-vmware-vmfs)
- [220: What is vSAN?](#220-what-is-vsan)
- [221: What is hyper-converged infrastructure (HCI)?](#221-what-is-hyper-converged-infrastructure-hci)
- [222: What is the difference between iSCSI and NFS for VM storage?](#222-what-is-the-difference-between-iscsi-and-nfs-for-vm-storage)
- [223: What is multipathing in VM storage?](#223-what-is-multipathing-in-vm-storage)
- [224: What are Hyper-V Generation 1 and Generation 2 VMs?](#224-what-are-hyper-v-generation-1-and-generation-2-vms)
- [225: How do you create a Hyper-V VM with PowerShell?](#225-how-do-you-create-a-hyper-v-vm-with-powershell)
- [226: What are Hyper-V virtual switch types?](#226-what-are-hyper-v-virtual-switch-types)
- [227: What is Hyper-V Dynamic Memory?](#227-what-is-hyper-v-dynamic-memory)
- [228: What are Hyper-V checkpoints?](#228-what-are-hyper-v-checkpoints)
- [229: What is Hyper-V Replica?](#229-what-is-hyper-v-replica)
- [230: What is a Hyper-V failover cluster?](#230-what-is-a-hyper-v-failover-cluster)
- [231: What is VMware Tools and why is it important?](#231-what-is-vmware-tools-and-why-is-it-important)
- [232: What is vmxnet3?](#232-what-is-vmxnet3)
- [233: What is PVSCSI?](#233-what-is-pvscsi)
- [234: How do you script VMware vSphere?](#234-how-do-you-script-vmware-vsphere)
- [235: What is VBoxManage?](#235-what-is-vboxmanage)
- [236: How do you forward a port in VirtualBox NAT mode?](#236-how-do-you-forward-a-port-in-virtualbox-nat-mode)
- [237: Can VirtualBox and Hyper-V run on the same Windows machine?](#237-can-virtualbox-and-hyper-v-run-on-the-same-windows-machine)
- [238: What are the common Vagrant commands?](#238-what-are-the-common-vagrant-commands)
- [239: How do you provision a Vagrant VM with Ansible?](#239-how-do-you-provision-a-vagrant-vm-with-ansible)
- [240: What does a basic Packer template look like?](#240-what-does-a-basic-packer-template-look-like)
- [241: How do you launch an EC2 instance with Node.js?](#241-how-do-you-launch-an-ec2-instance-with-nodejs)
- [242: How do you wait until an EC2 instance is running in Node.js?](#242-how-do-you-wait-until-an-ec2-instance-is-running-in-nodejs)
- [243: How do you read instance metadata with IMDSv2 from Node.js?](#243-how-do-you-read-instance-metadata-with-imdsv2-from-nodejs)
- [244: Why was IMDSv2 introduced?](#244-why-was-imdsv2-introduced)
- [245: What are EC2 status checks?](#245-what-are-ec2-status-checks)
- [246: What is EC2 auto recovery?](#246-what-is-ec2-auto-recovery)
- [247: What is the EC2 serial console?](#247-what-is-the-ec2-serial-console)
- [248: What are EC2 instance families?](#248-what-are-ec2-instance-families)
- [249: What are burstable instances?](#249-what-are-burstable-instances)
- [250: What is AWS Graviton?](#250-what-is-aws-graviton)
- [251: What is an Azure VM scale set?](#251-what-is-an-azure-vm-scale-set)
- [252: What is Google Compute Engine live migration?](#252-what-is-google-compute-engine-live-migration)
- [253: What is the difference between a VM image and a VM snapshot in the cloud?](#253-what-is-the-difference-between-a-vm-image-and-a-vm-snapshot-in-the-cloud)
- [254: How do you share or copy a cloud image to another region?](#254-how-do-you-share-or-copy-a-cloud-image-to-another-region)
- [255: What is a placement group in AWS?](#255-what-is-a-placement-group-in-aws)
- [256: What is AWS Nitro?](#256-what-is-aws-nitro)
- [257: What is a bare-metal cloud instance?](#257-what-is-a-bare-metal-cloud-instance)
- [258: How do you choose between VMs and containers for a new service?](#258-how-do-you-choose-between-vms-and-containers-for-a-new-service)
- [259: How does Kubernetes relate to VMs?](#259-how-does-kubernetes-relate-to-vms)
- [260: What is KubeVirt?](#260-what-is-kubevirt)
- [261: What is OpenStack?](#261-what-is-openstack)
- [262: What is the difference between a private cloud and plain virtualization?](#262-what-is-the-difference-between-a-private-cloud-and-plain-virtualization)
- [263: How do you automate VM provisioning end to end?](#263-how-do-you-automate-vm-provisioning-end-to-end)
- [264: What does a Terraform config for an AWS VM look like?](#264-what-does-a-terraform-config-for-an-aws-vm-look-like)
- [265: What is immutable infrastructure with VMs?](#265-what-is-immutable-infrastructure-with-vms)
- [266: What is configuration drift?](#266-what-is-configuration-drift)
- [267: How do you monitor VMs?](#267-how-do-you-monitor-vms)
- [268: Why can CPU usage inside a VM be misleading?](#268-why-can-cpu-usage-inside-a-vm-be-misleading)
- [269: How do you check steal time and other VM stats in Linux?](#269-how-do-you-check-steal-time-and-other-vm-stats-in-linux)
- [270: How do you find out if a Linux machine is a VM?](#270-how-do-you-find-out-if-a-linux-machine-is-a-vm)
- [271: How do you check from Node.js if it runs inside a VM?](#271-how-do-you-check-from-nodejs-if-it-runs-inside-a-vm)
- [272: How do you troubleshoot a VM that will not boot?](#272-how-do-you-troubleshoot-a-vm-that-will-not-boot)
- [273: What does "kernel panic: VFS unable to mount root fs" mean after migrating a VM?](#273-what-does-kernel-panic-vfs-unable-to-mount-root-fs-mean-after-migrating-a-vm)
- [274: How do you migrate a VM from VMware to KVM or Proxmox?](#274-how-do-you-migrate-a-vm-from-vmware-to-kvm-or-proxmox)
- [275: What is virt-v2v?](#275-what-is-virt-v2v)
- [276: What is libguestfs?](#276-what-is-libguestfs)
- [277: What is sysprep and why do you need it for Windows templates?](#277-what-is-sysprep-and-why-do-you-need-it-for-windows-templates)
- [278: What do you clean in a Linux VM before making a template?](#278-what-do-you-clean-in-a-linux-vm-before-making-a-template)
- [279: Why does a duplicate machine-id cause problems?](#279-why-does-a-duplicate-machine-id-cause-problems)
- [280: What is the difference between a full clone and a linked clone in practice?](#280-what-is-the-difference-between-a-full-clone-and-a-linked-clone-in-practice)
- [281: How do you set up a lab of VMs for testing a cluster?](#281-how-do-you-set-up-a-lab-of-vms-for-testing-a-cluster)
- [282: What are VM tags or labels used for?](#282-what-are-vm-tags-or-labels-used-for)
- [283: How do you control costs of cloud VMs?](#283-how-do-you-control-costs-of-cloud-vms)
- [284: How do you schedule VMs to stop at night in AWS with Node.js?](#284-how-do-you-schedule-vms-to-stop-at-night-in-aws-with-nodejs)
- [285: How do you handle spot instance interruptions?](#285-how-do-you-handle-spot-instance-interruptions)
- [286: How do you handle a VM that is low on disk space?](#286-how-do-you-handle-a-vm-that-is-low-on-disk-space)
- [287: What is swap inside a VM vs host swapping?](#287-what-is-swap-inside-a-vm-vs-host-swapping)
- [288: How do you secure a hypervisor host?](#288-how-do-you-secure-a-hypervisor-host)
- [289: How do you secure a guest VM?](#289-how-do-you-secure-a-guest-vm)
- [290: What is VM disk encryption?](#290-what-is-vm-disk-encryption)
- [291: How do you encrypt EBS volumes by default?](#291-how-do-you-encrypt-ebs-volumes-by-default)
- [292: What is Secure Boot in a VM?](#292-what-is-secure-boot-in-a-vm)
- [293: What is a VM escape?](#293-what-is-a-vm-escape)
- [294: How do you reduce the risk of VM escape?](#294-how-do-you-reduce-the-risk-of-vm-escape)
- [295: What is sVirt?](#295-what-is-svirt)
- [296: How are VMs isolated from each other on the network?](#296-how-are-vms-isolated-from-each-other-on-the-network)
- [297: What is the difference between a VM and a sandbox?](#297-what-is-the-difference-between-a-vm-and-a-sandbox)
- [298: Why is the Node.js vm module not a security sandbox?](#298-why-is-the-nodejs-vm-module-not-a-security-sandbox)
- [299: What is the difference between a VM and a Windows Sandbox?](#299-what-is-the-difference-between-a-vm-and-a-windows-sandbox)
- [300: How do you decide between on-prem virtualization and cloud VMs?](#300-how-do-you-decide-between-on-prem-virtualization-and-cloud-vms)

### Advanced Questions (301-450)

- [301: What are the Popek and Goldberg virtualization requirements?](#301-what-are-the-popek-and-goldberg-virtualization-requirements)
- [302: Why was classic x86 not virtualizable under Popek and Goldberg?](#302-why-was-classic-x86-not-virtualizable-under-popek-and-goldberg)
- [303: How did VMware solve x86 virtualization before hardware support?](#303-how-did-vmware-solve-x86-virtualization-before-hardware-support)
- [304: How did Xen paravirtualization solve the same problem?](#304-how-did-xen-paravirtualization-solve-the-same-problem)
- [305: How does Intel VT-x work at a high level?](#305-how-does-intel-vt-x-work-at-a-high-level)
- [306: What is the VMCS?](#306-what-is-the-vmcs)
- [307: What is a VM exit and why is it expensive?](#307-what-is-a-vm-exit-and-why-is-it-expensive)
- [308: What are common causes of VM exits?](#308-what-are-common-causes-of-vm-exits)
- [309: How do you see VM exit statistics on a KVM host?](#309-how-do-you-see-vm-exit-statistics-on-a-kvm-host)
- [310: What is shadow paging?](#310-what-is-shadow-paging)
- [311: What are EPT and NPT?](#311-what-are-ept-and-npt)
- [312: What is the cost of two-dimensional page walks?](#312-what-is-the-cost-of-two-dimensional-page-walks)
- [313: What is VPID and why does it matter?](#313-what-is-vpid-and-why-does-it-matter)
- [314: How does interrupt virtualization work, and what is APICv?](#314-how-does-interrupt-virtualization-work-and-what-is-apicv)
- [315: What are posted interrupts?](#315-what-are-posted-interrupts)
- [316: How does KVM handle an MMIO access from the guest?](#316-how-does-kvm-handle-an-mmio-access-from-the-guest)
- [317: What is the KVM API at a basic level?](#317-what-is-the-kvm-api-at-a-basic-level)
- [318: What are ioeventfd and irqfd?](#318-what-are-ioeventfd-and-irqfd)
- [319: How does virtio work internally?](#319-how-does-virtio-work-internally)
- [320: What are split and packed virtqueues?](#320-what-are-split-and-packed-virtqueues)
- [321: What is vhost?](#321-what-is-vhost)
- [322: What is vhost-user and when do you use it?](#322-what-is-vhost-user-and-when-do-you-use-it)
- [323: What is vDPA?](#323-what-is-vdpa)
- [324: What is virtiofs and how does it differ from 9p?](#324-what-is-virtiofs-and-how-does-it-differ-from-9p)
- [325: How do you design a hypervisor host's NUMA layout for a big database VM?](#325-how-do-you-design-a-hypervisor-hosts-numa-layout-for-a-big-database-vm)
- [326: How do you pin vCPUs, emulator threads and I/O threads in libvirt?](#326-how-do-you-pin-vcpus-emulator-threads-and-io-threads-in-libvirt)
- [327: What is isolcpus and when is it used with VMs?](#327-what-is-isolcpus-and-when-is-it-used-with-vms)
- [328: What is halt polling in KVM?](#328-what-is-halt-polling-in-kvm)
- [329: What is the cost of time-sharing many small vCPUs?](#329-what-is-the-cost-of-time-sharing-many-small-vcpus)
- [330: What is pause-loop exiting?](#330-what-is-pause-loop-exiting)
- [331: How does the guest know about time in a VM?](#331-how-does-the-guest-know-about-time-in-a-vm)
- [332: What problems happen with TSC in VMs?](#332-what-problems-happen-with-tsc-in-vms)
- [333: Why can time in a VM jump after resume or migration, and how do you handle it?](#333-why-can-time-in-a-vm-jump-after-resume-or-migration-and-how-do-you-handle-it)
- [334: How does post-copy live migration work?](#334-how-does-post-copy-live-migration-work)
- [335: When does pre-copy live migration fail to converge?](#335-when-does-pre-copy-live-migration-fail-to-converge)
- [336: What is auto-converge in QEMU migration?](#336-what-is-auto-converge-in-qemu-migration)
- [337: How does KVM track dirty memory for migration?](#337-how-does-kvm-track-dirty-memory-for-migration)
- [338: How do you migrate a VM between hosts with different CPU generations?](#338-how-do-you-migrate-a-vm-between-hosts-with-different-cpu-generations)
- [339: What breaks if you live migrate a VM with host-passthrough to an older CPU?](#339-what-breaks-if-you-live-migrate-a-vm-with-host-passthrough-to-an-older-cpu)
- [340: How does storage live migration work in QEMU?](#340-how-does-storage-live-migration-work-in-qemu)
- [341: How does QEMU live backup work with blockdev-backup?](#341-how-does-qemu-live-backup-work-with-blockdev-backup)
- [342: How do you design VM backups for a database server?](#342-how-do-you-design-vm-backups-for-a-database-server)
- [343: How do fsfreeze hooks work with the QEMU guest agent?](#343-how-do-fsfreeze-hooks-work-with-the-qemu-guest-agent)
- [344: What is the risk of freezing file systems inside a VM?](#344-what-is-the-risk-of-freezing-file-systems-inside-a-vm)
- [345: How does Ceph RBD handle VM snapshots and clones?](#345-how-does-ceph-rbd-handle-vm-snapshots-and-clones)
- [346: How do you size a Ceph cluster for VM workloads?](#346-how-do-you-size-a-ceph-cluster-for-vm-workloads)
- [347: Why is write latency often the main limit for VM storage?](#347-why-is-write-latency-often-the-main-limit-for-vm-storage)
- [348: How do you benchmark VM disk performance with fio?](#348-how-do-you-benchmark-vm-disk-performance-with-fio)
- [349: How do you tune network performance for a KVM VM?](#349-how-do-you-tune-network-performance-for-a-kvm-vm)
- [350: What is multi-queue virtio-net and why does it help?](#350-what-is-multi-queue-virtio-net-and-why-does-it-help)
- [351: How does live migration work with SR-IOV devices?](#351-how-does-live-migration-work-with-sr-iov-devices)
- [352: What is VFIO device migration?](#352-what-is-vfio-device-migration)
- [353: How does a vGPU work?](#353-how-does-a-vgpu-work)
- [354: What are the trade-offs of GPU passthrough in production?](#354-what-are-the-trade-offs-of-gpu-passthrough-in-production)
- [355: What is NVIDIA MIG and how does it relate to VMs?](#355-what-is-nvidia-mig-and-how-does-it-relate-to-vms)
- [356: How do confidential VMs work?](#356-how-do-confidential-vms-work)
- [357: What is the difference between AMD SEV, SEV-ES and SEV-SNP?](#357-what-is-the-difference-between-amd-sev-sev-es-and-sev-snp)
- [358: What is Intel TDX?](#358-what-is-intel-tdx)
- [359: What is remote attestation for confidential VMs?](#359-what-is-remote-attestation-for-confidential-vms)
- [360: What are the limits of confidential VMs?](#360-what-are-the-limits-of-confidential-vms)
- [361: How do Spectre and Meltdown affect virtualization?](#361-how-do-spectre-and-meltdown-affect-virtualization)
- [362: What is L1TF and why did it lead to disabling SMT on some hosts?](#362-what-is-l1tf-and-why-did-it-lead-to-disabling-smt-on-some-hosts)
- [363: What is core scheduling?](#363-what-is-core-scheduling)
- [364: Why do cloud vCPUs often equal hyper-threads, not cores?](#364-why-do-cloud-vcpus-often-equal-hyper-threads-not-cores)
- [365: How do you check how vCPUs map to cores in an EC2 instance?](#365-how-do-you-check-how-vcpus-map-to-cores-in-an-ec2-instance)
- [366: What is the attack surface of a hypervisor, and how do newer VMMs shrink it?](#366-what-is-the-attack-surface-of-a-hypervisor-and-how-do-newer-vmms-shrink-it)
- [367: How does Firecracker isolate each microVM?](#367-how-does-firecracker-isolate-each-microvm)
- [368: How do you start a Firecracker microVM?](#368-how-do-you-start-a-firecracker-microvm)
- [369: How can you control Firecracker from Node.js?](#369-how-can-you-control-firecracker-from-nodejs)
- [370: How do microVM snapshots make serverless cold starts faster?](#370-how-do-microvm-snapshots-make-serverless-cold-starts-faster)
- [371: Why is uniqueness a problem when restoring many VMs from one snapshot?](#371-why-is-uniqueness-a-problem-when-restoring-many-vms-from-one-snapshot)
- [372: What is gVisor and how does it compare to a microVM?](#372-what-is-gvisor-and-how-does-it-compare-to-a-microvm)
- [373: How would you design a multi-tenant code execution service?](#373-how-would-you-design-a-multi-tenant-code-execution-service)
- [374: What is Cloud Hypervisor?](#374-what-is-cloud-hypervisor)
- [375: What is rust-vmm?](#375-what-is-rust-vmm)
- [376: How does nested virtualization work in hardware?](#376-how-does-nested-virtualization-work-in-hardware)
- [377: Why is nested virtualization slow for I/O-heavy workloads?](#377-why-is-nested-virtualization-slow-for-io-heavy-workloads)
- [378: How do you enable nested virtualization on KVM?](#378-how-do-you-enable-nested-virtualization-on-kvm)
- [379: How does Hyper-V's enlightenment interface help Windows guests on KVM?](#379-how-does-hyper-vs-enlightenment-interface-help-windows-guests-on-kvm)
- [380: What is the Hyper-V root partition model?](#380-what-is-the-hyper-v-root-partition-model)
- [381: What is VMBus?](#381-what-is-vmbus)
- [382: How does Virtualization-Based Security (VBS) use the hypervisor?](#382-how-does-virtualization-based-security-vbs-use-the-hypervisor)
- [383: Why does enabling VBS or Hyper-V affect VMware Workstation and VirtualBox?](#383-why-does-enabling-vbs-or-hyper-v-affect-vmware-workstation-and-virtualbox)
- [384: How do ESXi's scheduler and "co-scheduling" work?](#384-how-do-esxis-scheduler-and-co-scheduling-work)
- [385: What is co-stop in VMware?](#385-what-is-co-stop-in-vmware)
- [386: How would you investigate a VM that is slow only at certain times of day?](#386-how-would-you-investigate-a-vm-that-is-slow-only-at-certain-times-of-day)
- [387: How does memory overcommit go wrong, step by step?](#387-how-does-memory-overcommit-go-wrong-step-by-step)
- [388: How do you protect important VMs from the host OOM killer on KVM?](#388-how-do-you-protect-important-vms-from-the-host-oom-killer-on-kvm)
- [389: What is Pressure Stall Information (PSI) and how is it useful for VM hosts?](#389-what-is-pressure-stall-information-psi-and-how-is-it-useful-for-vm-hosts)
- [390: What is free page reporting?](#390-what-is-free-page-reporting)
- [391: How does a hypervisor know how much memory a guest really uses?](#391-how-does-a-hypervisor-know-how-much-memory-a-guest-really-uses)
- [392: What is memory tiering in virtualization?](#392-what-is-memory-tiering-in-virtualization)
- [393: What is CXL and how might it change virtualization?](#393-what-is-cxl-and-how-might-it-change-virtualization)
- [394: How do you plan capacity for a virtualization cluster?](#394-how-do-you-plan-capacity-for-a-virtualization-cluster)
- [395: What is N+1 in VM cluster design?](#395-what-is-n1-in-vm-cluster-design)
- [396: How does VMware HA detect host failures?](#396-how-does-vmware-ha-detect-host-failures)
- [397: What is VM Component Protection (VMCP)?](#397-what-is-vm-component-protection-vmcp)
- [398: What is VMware Fault Tolerance?](#398-what-is-vmware-fault-tolerance)
- [399: What is COLO in QEMU?](#399-what-is-colo-in-qemu)
- [400: Why is app-level high availability usually better than VM-level HA?](#400-why-is-app-level-high-availability-usually-better-than-vm-level-ha)
- [401: How do you design for zone failure with cloud VMs?](#401-how-do-you-design-for-zone-failure-with-cloud-vms)
- [402: What is the "cattle vs pets" idea for VMs?](#402-what-is-the-cattle-vs-pets-idea-for-vms)
- [403: How do you do zero-downtime deployments with VMs?](#403-how-do-you-do-zero-downtime-deployments-with-vms)
- [404: How do you trigger an AWS auto scaling instance refresh from Node.js?](#404-how-do-you-trigger-an-aws-auto-scaling-instance-refresh-from-nodejs)
- [405: How do you gracefully drain a VM before it is terminated in an auto scaling group?](#405-how-do-you-gracefully-drain-a-vm-before-it-is-terminated-in-an-auto-scaling-group)
- [406: How should a Node.js app running on a VM handle shutdown signals?](#406-how-should-a-nodejs-app-running-on-a-vm-handle-shutdown-signals)
- [407: What is the difference between VM-level and app-level scaling metrics?](#407-what-is-the-difference-between-vm-level-and-app-level-scaling-metrics)
- [408: How do you size Node.js processes on a multi-vCPU VM?](#408-how-do-you-size-nodejs-processes-on-a-multi-vcpu-vm)
- [409: How does V8's memory limit relate to the VM's memory?](#409-how-does-v8s-memory-limit-relate-to-the-vms-memory)
- [410: How does the JVM decide heap size on a VM vs in a container?](#410-how-does-the-jvm-decide-heap-size-on-a-vm-vs-in-a-container)
- [411: What is JIT compilation in a process VM?](#411-what-is-jit-compilation-in-a-process-vm)
- [412: How does V8's tiered execution pipeline work?](#412-how-does-v8s-tiered-execution-pipeline-work)
- [413: What are hidden classes and inline caches in V8?](#413-what-are-hidden-classes-and-inline-caches-in-v8)
- [414: How does garbage collection work in V8?](#414-how-does-garbage-collection-work-in-v8)
- [415: How is a stack-based VM different from a register-based VM?](#415-how-is-a-stack-based-vm-different-from-a-register-based-vm)
- [416: How would you write a tiny stack-based VM in JavaScript?](#416-how-would-you-write-a-tiny-stack-based-vm-in-javascript)
- [417: Is WebAssembly a virtual machine?](#417-is-webassembly-a-virtual-machine)
- [418: How do you run WebAssembly in Node.js?](#418-how-do-you-run-webassembly-in-nodejs)
- [419: How do Wasm runtimes compare to microVMs for isolation?](#419-how-do-wasm-runtimes-compare-to-microvms-for-isolation)
- [420: What is a "unikernel"?](#420-what-is-a-unikernel)
- [421: How does the guest boot process work in QEMU with UEFI?](#421-how-does-the-guest-boot-process-work-in-qemu-with-uefi)
- [422: What is direct kernel boot and when is it used?](#422-what-is-direct-kernel-boot-and-when-is-it-used)
- [423: How do you reduce VM boot time?](#423-how-do-you-reduce-vm-boot-time)
- [424: What is the QMP protocol?](#424-what-is-the-qmp-protocol)
- [425: How do you hotplug a disk into a running KVM VM?](#425-how-do-you-hotplug-a-disk-into-a-running-kvm-vm)
- [426: How do you securely expose a VM's console to users in a web app?](#426-how-do-you-securely-expose-a-vms-console-to-users-in-a-web-app)
- [427: How do you build a simple API in Node.js that controls libvirt VMs?](#427-how-do-you-build-a-simple-api-in-nodejs-that-controls-libvirt-vms)
- [428: How do you call the Proxmox VE API from Node.js?](#428-how-do-you-call-the-proxmox-ve-api-from-nodejs)
- [429: How would you design a self-service VM platform for internal developers?](#429-how-would-you-design-a-self-service-vm-platform-for-internal-developers)
- [430: How do you patch hundreds of VMs safely?](#430-how-do-you-patch-hundreds-of-vms-safely)
- [431: How do you patch hypervisor hosts without VM downtime?](#431-how-do-you-patch-hypervisor-hosts-without-vm-downtime)
- [432: How do you handle VMs that cannot be live migrated during host maintenance?](#432-how-do-you-handle-vms-that-cannot-be-live-migrated-during-host-maintenance)
- [433: What are the trade-offs of local NVMe storage vs shared storage for VMs?](#433-what-are-the-trade-offs-of-local-nvme-storage-vs-shared-storage-for-vms)
- [434: What is the I/O blender effect?](#434-what-is-the-io-blender-effect)
- [435: How do you troubleshoot high storage latency in a VMware environment?](#435-how-do-you-troubleshoot-high-storage-latency-in-a-vmware-environment)
- [436: What is a common cause of slow Windows VMs on KVM, and how do you fix it?](#436-what-is-a-common-cause-of-slow-windows-vms-on-kvm-and-how-do-you-fix-it)
- [437: How would you debug a VM that randomly freezes for a few seconds?](#437-how-would-you-debug-a-vm-that-randomly-freezes-for-a-few-seconds)
- [438: How do you investigate a guest kernel crash in a VM?](#438-how-do-you-investigate-a-guest-kernel-crash-in-a-vm)
- [439: How does the hypervisor protect itself from a guest flooding it with exits or I/O?](#439-how-does-the-hypervisor-protect-itself-from-a-guest-flooding-it-with-exits-or-io)
- [440: How do you limit disk IOPS for a KVM VM?](#440-how-do-you-limit-disk-iops-for-a-kvm-vm)
- [441: How does network QoS work for VMs?](#441-how-does-network-qos-work-for-vms)
- [442: How do overlay networks like VXLAN work for VMs across hosts?](#442-how-do-overlay-networks-like-vxlan-work-for-vms-across-hosts)
- [443: How do you handle MTU issues in VM networks?](#443-how-do-you-handle-mtu-issues-in-vm-networks)
- [444: How does a cloud provider implement VPC networking for VMs?](#444-how-does-a-cloud-provider-implement-vpc-networking-for-vms)
- [445: What licensing traps should you watch for with VMs?](#445-what-licensing-traps-should-you-watch-for-with-vms)
- [446: How would you plan a migration away from VMware vSphere?](#446-how-would-you-plan-a-migration-away-from-vmware-vsphere)
- [447: How do you evaluate whether a workload should stay on VMs or move to containers?](#447-how-do-you-evaluate-whether-a-workload-should-stay-on-vms-or-move-to-containers)
- [448: How would you design a CI system that runs untrusted pull request builds in VMs?](#448-how-would-you-design-a-ci-system-that-runs-untrusted-pull-request-builds-in-vms)
- [449: Your company runs 2,000 VMs and the cloud bill is too high. What do you do?](#449-your-company-runs-2000-vms-and-the-cloud-bill-is-too-high-what-do-you-do)
- [450: How do you explain the full path of a disk write from an app in a KVM guest to the physical disk?](#450-how-do-you-explain-the-full-path-of-a-disk-write-from-an-app-in-a-kvm-guest-to-the-physical-disk)

---

# Easy Questions (1-150)

## 1: What is a virtual machine?

A virtual machine (VM) is a computer made in software. It has its own virtual CPU, memory, disk and network card, and it runs its own operating system, just like a real computer. Many VMs can run on one physical machine at the same time, and each one thinks it has the hardware to itself.

## 2: What is a hypervisor?

A hypervisor is the software that creates and runs virtual machines. It sits between the hardware and the VMs, splits up the CPU, memory, disk and network, and makes sure one VM cannot touch another VM's resources. Examples are KVM, VMware ESXi, Microsoft Hyper-V, Xen and VirtualBox.

## 3: What is the difference between a host and a guest?

The host is the physical machine (and its operating system, if it has one) that runs the hypervisor. The guest is the operating system running inside a VM. For example, if you run Ubuntu in VirtualBox on a Windows laptop, Windows is the host and Ubuntu is the guest.

## 4: What is a Type 1 hypervisor?

A Type 1 hypervisor, also called a bare-metal hypervisor, runs directly on the hardware without a normal operating system under it. Because there is no extra layer, it is faster and more stable, so it is used in data centers and clouds. VMware ESXi, Xen, Hyper-V and KVM are usually counted as Type 1.

## 5: What is a Type 2 hypervisor?

A Type 2 hypervisor, or hosted hypervisor, runs as an app on top of a normal operating system like Windows, macOS or Linux. It is easy to install and good for development and testing on a laptop. VirtualBox, VMware Workstation, VMware Fusion and Parallels Desktop are Type 2 hypervisors.

## 6: Why do companies use virtual machines?

Mostly to use hardware better and to keep things separate. Without VMs, a server often runs one app and sits at 10-15% CPU. With VMs, you can run many isolated workloads on one server, move them between servers, take snapshots, and create new machines in minutes instead of buying hardware.

## 7: What is virtualization?

Virtualization is the general idea of making a software version of something physical: a computer, a disk, a network or a desktop. Server virtualization (VMs) is the best known kind, but there is also storage virtualization, network virtualization and desktop virtualization.

## 8: What are the main parts of a virtual machine?

A VM is made of a few things:

- A configuration file that says how many vCPUs, how much RAM, which disks and which network cards it has
- One or more virtual disk files
- Firmware (BIOS or UEFI) that boots it
- Virtual devices like network cards, disk controllers and a display
- Optionally, saved state files for snapshots or suspend

## 9: What is a vCPU?

A vCPU is a virtual CPU core given to a VM. The hypervisor schedules vCPUs on the real CPU cores of the host, a bit like how an OS schedules threads. A VM with 4 vCPUs sees 4 cores, but they are time-shared with other VMs on the same host.

## 10: What is a virtual disk?

A virtual disk is a file (or a block device on the host) that the guest sees as a real hard drive. The guest formats it and writes files to it, not knowing it is just a big file. Common formats are qcow2 (QEMU/KVM), VMDK (VMware), VHDX (Hyper-V) and VDI (VirtualBox).

## 11: What is a snapshot of a VM?

A snapshot saves the state of a VM at a point in time: its disk, and often its memory and settings too. You can go back to it later if something breaks. Snapshots are great before an upgrade or a risky change, but they are not a replacement for real backups, because they usually live on the same storage as the VM.

## 12: What is the difference between a snapshot and a backup?

A snapshot is a quick point-in-time marker that depends on the original disk and usually sits next to it. If the storage dies, the snapshot dies too. A backup is a full, separate copy stored somewhere else that you can restore even if the whole host is lost. Use snapshots for short-term rollback and backups for real protection.

## 13: What is a VM template?

A template is a "golden" VM that is set up once with an OS, updates and common tools, and then used to create new VMs quickly. Templates are usually read-only so nobody changes them by mistake. VMware, Proxmox and most clouds (as machine images) support them.

## 14: What does cloning a VM mean?

Cloning makes a copy of an existing VM. A full clone copies the whole disk and is independent from the source. A linked clone shares the source disk and only stores its own changes, so it is created faster and uses less space but depends on the parent.

## 15: What is an ISO file and how is it used with VMs?

An ISO file is an image of a CD or DVD. To install an OS in a VM, you attach the installer ISO to the VM's virtual CD drive and boot from it, just like inserting a disc into a real computer. You can also attach ISOs with drivers or tools.

## 16: What is a guest operating system?

The guest OS is the operating system installed inside a VM. It can be different from the host OS, so you can run Windows on a Linux host or Linux on a Mac. The guest must support the CPU architecture the hypervisor presents, usually the same as the host's.

## 17: Can a VM run a different OS than the host?

Yes, that is one of the main reasons people use VMs. A Linux host can run Windows, BSD or other Linux distributions as guests. The limit is CPU architecture: a hypervisor normally runs guests for the same architecture as the host (x86 on x86, ARM on ARM). Running other architectures needs emulation, which is much slower.

## 18: What is the difference between virtualization and emulation?

With virtualization, guest code runs directly on the real CPU most of the time, and the hypervisor only steps in for special instructions, so it is fast. With emulation, software translates every guest instruction into host instructions, so you can run an ARM guest on an x86 host, but it is much slower. QEMU can do both: emulation alone, or fast virtualization with KVM.

## 19: What is KVM?

KVM (Kernel-based Virtual Machine) is a module in the Linux kernel that turns Linux into a hypervisor. It uses the CPU's hardware virtualization features (Intel VT-x or AMD-V). KVM handles the CPU and memory part, and a user-space program, usually QEMU, provides the virtual devices. Most Linux clouds run on KVM.

## 20: What is QEMU?

QEMU is an open source machine emulator and virtualizer. On its own it can emulate many CPU types in software. Together with KVM, it becomes a fast hypervisor where QEMU provides the virtual hardware (disks, network cards, display) and KVM runs the guest code on the real CPU.

## 21: What is VirtualBox?

VirtualBox is a free, open source Type 2 hypervisor from Oracle. It runs on Windows, macOS, Linux and Solaris hosts and is popular for local development and learning. Version 7.2 added support for Windows on Arm hosts and an updated interface. The Extension Pack (USB 3, some remote features) has a separate personal-use license.

## 22: What is VMware ESXi?

ESXi is VMware's Type 1 hypervisor that installs directly on servers. It is managed with vCenter Server, and together they form vSphere, one of the most used enterprise virtualization platforms. VMware is now owned by Broadcom, which changed its licensing to subscription bundles.

## 23: What is Microsoft Hyper-V?

Hyper-V is Microsoft's hypervisor. It is built into Windows Server and into Windows 10/11 Pro and Enterprise. Even though you turn it on from Windows, it is a Type 1 hypervisor: once enabled, Hyper-V runs under Windows, and Windows itself becomes a special VM called the root (parent) partition.

## 24: What is Proxmox VE?

Proxmox Virtual Environment is an open source virtualization platform based on Debian. It runs KVM virtual machines and LXC containers and gives you a web interface, clustering, high availability, backups and built-in Ceph and ZFS support. Many people use it as an alternative to VMware.

## 25: What is Xen?

Xen is an open source Type 1 hypervisor. It runs directly on the hardware and uses a special privileged VM called Dom0 to manage the other guests (DomU). AWS EC2 used Xen for many years before moving to its KVM-based Nitro hypervisor. XCP-ng and Citrix Hypervisor are built on Xen.

## 26: What is a cloud VM?

A cloud VM is a virtual machine you rent from a cloud provider instead of running your own hypervisor. Examples are AWS EC2 instances, Azure Virtual Machines and Google Compute Engine instances. You pick a size and an image, and the provider handles the hardware and the hypervisor.

## 27: What is an EC2 instance?

An EC2 instance is a virtual machine in AWS. You launch it from an Amazon Machine Image (AMI), choose an instance type like t3.micro or m7i.large that sets the vCPUs and memory, and attach storage and networking. You pay per second or per hour while it runs.

## 28: What is a machine image?

A machine image is a saved template of a VM disk (and sometimes settings) used to launch new VMs. In AWS it is called an AMI, in Azure a managed image or gallery image, and in Google Cloud an image. Images let you launch many identical servers quickly.

## 29: What is the difference between a VM and a container?

A VM has its own full operating system with its own kernel, running on virtual hardware. A container shares the host's kernel and only packages the app and its libraries. Containers start in milliseconds and are smaller, while VMs give stronger isolation and can run a different OS or kernel.

## 30: Which is more secure, a VM or a container?

In general, VMs give stronger isolation, because each VM has its own kernel and the hypervisor is a small, hardened layer. Containers share the host kernel, so a kernel bug can let one container affect others. That is why many clouds run containers inside VMs or in lightweight VMs like Firecracker.

## 31: What is hardware-assisted virtualization?

It means the CPU has special features that make virtualization fast and simple. Intel calls it VT-x and AMD calls it AMD-V (SVM). With these, the CPU can run guest code directly and automatically switch to the hypervisor when the guest does something sensitive, instead of the hypervisor having to rewrite guest code.

## 32: What are Intel VT-x and AMD-V?

They are the hardware virtualization extensions in Intel and AMD CPUs. They add a new CPU mode for running guests and instructions to enter and leave it. Almost every modern x86 CPU has them, but they sometimes need to be turned on in the BIOS or UEFI settings.

## 33: How do you check if your Linux machine supports hardware virtualization?

Look for the vmx (Intel) or svm (AMD) CPU flags, and check that the KVM device exists:

```bash
grep -E -c '(vmx|svm)' /proc/cpuinfo   # more than 0 means supported
ls -l /dev/kvm                          # exists when KVM is loaded
lsmod | grep kvm
```

On Ubuntu you can also install `cpu-checker` and run `kvm-ok`.

## 34: What happens if virtualization is disabled in the BIOS?

Hypervisors like KVM, Hyper-V and VMware will not start VMs, or will refuse to run 64-bit guests. VirtualBox may show an error like "VT-x is disabled in the BIOS". The fix is to reboot into the firmware settings and turn on "Intel Virtualization Technology" or "SVM Mode".

## 35: What is a virtual network interface card (vNIC)?

A vNIC is a virtual network card inside the VM. The guest sees it as a normal network adapter with its own MAC address. On the host side, the hypervisor connects it to a virtual switch, a bridge or NAT so the VM can talk to other machines.

## 36: What is NAT networking in a VM?

With NAT, the VM gets a private IP address and the hypervisor translates its traffic to use the host's IP. The VM can reach the internet and the outside network, but outside machines cannot reach the VM directly unless you set up port forwarding. It is the default in VirtualBox and works without any network setup.

## 37: What is bridged networking?

With bridged networking, the VM is connected to the same physical network as the host, as if it were plugged into the same switch. It gets its own IP from the network's DHCP server and other machines can reach it directly. It is useful when the VM runs a server that others need to access.

## 38: What is host-only networking?

Host-only networking creates a private network between the host and its VMs only. VMs can talk to each other and to the host, but not to the internet or the rest of the LAN. It is useful for isolated test labs.

## 39: What is a virtual switch?

A virtual switch is a software switch inside the hypervisor that connects vNICs of VMs to each other and to physical network cards. It works like a real Ethernet switch, forwarding frames by MAC address. Examples are the Linux bridge, Open vSwitch, VMware vSwitch and the Hyper-V Virtual Switch.

## 40: What are guest additions or guest tools?

They are drivers and services you install inside the guest to make it work better with the hypervisor. They give better graphics, mouse integration, shared folders, clipboard sharing, time sync and clean shutdown. Examples are VirtualBox Guest Additions, VMware Tools (or open-vm-tools on Linux) and the QEMU guest agent.

## 41: What is the QEMU guest agent?

The QEMU guest agent (qemu-ga) is a small service running inside the guest that talks to the host over a virtio-serial channel. The host can use it to shut down the VM cleanly, freeze file systems before a backup, read the guest's IP addresses and run some commands. Proxmox and libvirt both use it.

## 42: What does it mean to suspend a VM?

Suspending (or saving) a VM writes its memory and CPU state to disk and stops it. When you resume, it continues exactly where it left off, with all apps still open. It is like closing a laptop lid, and it frees the host's RAM and CPU while suspended.

## 43: What is the difference between pausing and suspending a VM?

Pausing stops the vCPUs but keeps the VM's memory in the host's RAM, so resuming is instant. Suspending saves the memory to disk and frees the RAM, so it survives a host reboot but takes longer to resume.

## 44: What is a thin-provisioned disk?

A thin disk only takes up the space the guest has actually written, and grows as needed up to its maximum size. A 100 GB thin disk with 10 GB of data uses about 10 GB on the host. It saves space but you can run out of real storage if many thin disks grow at once.

## 45: What is a thick-provisioned disk?

A thick disk reserves its full size on the host when it is created. A 100 GB thick disk uses 100 GB right away. It uses more space but gives more predictable performance and you never run out of space because of other disks growing.

## 46: What is overcommitment in virtualization?

Overcommitment means giving VMs more total resources than the host really has, for example 64 vCPUs on a 32-core host, or 300 GB of VM RAM on a 256 GB host. It works because VMs rarely use all their resources at once. Too much overcommit causes slowdowns, especially for memory.

## 47: What is a hypervisor's job in managing memory?

The hypervisor gives each VM its own view of "physical" memory and maps it to real host memory. It keeps VMs from reading each other's memory and can use tricks like ballooning, page sharing and swapping to fit more VMs on a host.

## 48: What is a VM console?

The console is the VM's virtual screen and keyboard. You use it to see boot messages, install the OS or fix a VM whose network is broken. Hypervisors give access through tools like VNC, SPICE, the VMware web console or a serial console. Cloud providers offer a serial console or screenshot feature too.

## 49: What is VNC in the context of VMs?

VNC is a remote desktop protocol. QEMU/KVM can expose the VM's display over VNC so you can connect with a VNC client and see the screen. Proxmox uses noVNC to show the VM console in the browser.

## 50: What is SPICE?

SPICE is a remote display protocol built for VMs, mostly with QEMU/KVM. Compared with VNC, it supports better graphics, audio, USB redirection and clipboard sharing. Tools like virt-manager and virt-viewer use it.

## 51: What is libvirt?

libvirt is an open source API, daemon and set of tools for managing virtualization on Linux. It supports KVM/QEMU, Xen, LXC and others behind one interface. The `virsh` command line tool and the virt-manager GUI both use libvirt.

## 52: What is virsh?

virsh is the command line tool for libvirt. You use it to create, start, stop and inspect VMs (called "domains" in libvirt):

```bash
virsh list --all          # show all VMs
virsh start web01         # start a VM
virsh shutdown web01      # ask the guest to shut down
virsh destroy web01       # force it off, like pulling the power
virsh dominfo web01       # basic info
```

## 53: What is virt-manager?

virt-manager is a desktop GUI for managing KVM/QEMU VMs through libvirt. You can create VMs, attach ISOs and disks, change hardware and open the console. It is handy on a Linux desktop or for managing a remote host over SSH.

## 54: What is Vagrant?

Vagrant is a tool from HashiCorp for creating and managing development VMs from a simple config file called a Vagrantfile. It works with providers like VirtualBox, VMware, Hyper-V and libvirt. One command, `vagrant up`, downloads a base image (a "box") and starts a ready-to-use VM.

## 55: What does a basic Vagrantfile look like?

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-24.04"
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
  end
  config.vm.provision "shell", inline: "apt-get update && apt-get install -y nodejs npm"
end
```

Then `vagrant up` creates the VM and `vagrant ssh` logs you in.

## 56: What is the difference between shutting down and powering off a VM?

Shutting down asks the guest OS to close apps and stop cleanly, through ACPI or the guest agent. Powering off (or "destroy" in libvirt) cuts the virtual power instantly, like pulling the plug, which can cause data loss or file system errors. Use power off only when the guest is stuck.

## 57: What is ACPI in a VM?

ACPI is the standard interface for power management. The hypervisor uses virtual ACPI events to tell the guest "the power button was pressed", so the guest can shut down cleanly. If the guest ignores ACPI (for example a minimal install without acpid), a shutdown request may do nothing.

## 58: What is BIOS vs UEFI in a VM?

These are the two kinds of firmware a VM can boot with. BIOS (often SeaBIOS in QEMU) is the older style. UEFI (OVMF in QEMU) is the modern one, needed for Secure Boot, large GPT boot disks and Windows 11. You usually pick it when creating the VM, and changing it later can make the VM unbootable.

## 59: What is a virtual TPM?

A virtual TPM (vTPM) is a software Trusted Platform Module given to a VM. It stores keys and measurements for features like BitLocker, Secure Boot attestation and Windows 11, which requires TPM 2.0. On QEMU/KVM it is usually provided by swtpm.

## 60: What is a VM's MAC address?

Each vNIC has a MAC address, usually generated by the hypervisor with a vendor prefix, like 52:54:00 for QEMU/KVM or 00:50:56 for VMware. When you clone a VM, make sure the clone gets a new MAC, or two VMs on the same network will conflict.

## 61: What is a live migration?

Live migration moves a running VM from one host to another with almost no downtime. The memory is copied over while the VM keeps running, then the VM pauses for a very short time, the last changes are copied, and it continues on the new host. VMware calls it vMotion, Hyper-V calls it Live Migration.

## 62: What is a cold migration?

A cold migration moves a VM that is powered off. You shut it down, copy or move its disks and config to another host or storage, and start it there. It is simpler and works between hosts with different CPUs, but it has downtime.

## 63: What is high availability (HA) for VMs?

HA means that if a host fails, its VMs are automatically restarted on other healthy hosts in the cluster. It needs shared or replicated storage so other hosts can see the VM disks. There is still downtime while VMs reboot, usually a few minutes.

## 64: What is a VM cluster?

A cluster is a group of hypervisor hosts managed together. They share storage and networks, so VMs can move between them, be balanced across them and be restarted elsewhere if a host fails. vSphere clusters, Proxmox clusters and Hyper-V failover clusters are examples.

## 65: What is shared storage and why do VM clusters need it?

Shared storage is storage that many hosts can access at the same time, like a SAN, NAS (NFS), iSCSI target or a distributed system like Ceph or vSAN. It lets any host run any VM without copying disks, which makes live migration and HA possible.

## 66: What is nested virtualization?

Nested virtualization means running a hypervisor inside a VM, so the VM can itself run VMs. It is useful for labs, CI testing of hypervisor tools or running Docker Desktop or WSL 2 inside a Windows VM. It is slower than normal virtualization and must be enabled on the outer hypervisor.

## 67: What is WSL 2?

WSL 2 (Windows Subsystem for Linux 2) runs a real Linux kernel inside a lightweight VM managed by Hyper-V technology on Windows. It gives near-native Linux performance for development tools. It starts in about a second and shares files and networking with Windows.

## 68: How does Docker Desktop on macOS use a VM?

Containers need a Linux kernel, and macOS does not have one. Docker Desktop runs a small Linux VM in the background using Apple's Virtualization framework, and the containers run inside that VM. That is why file sharing between macOS and containers can be slower than on Linux.

## 69: What is a process virtual machine?

A process VM runs a single program instead of a whole OS. It gives the program a platform-independent environment and goes away when the program ends. The Java Virtual Machine (JVM), the .NET CLR and JavaScript engines like V8 are process VMs. They are different from system VMs made by hypervisors.

## 70: What is the difference between a system VM and a process VM?

A system VM (like a KVM or VMware VM) emulates a whole computer and runs a full OS. A process VM (like the JVM or V8) runs one app, executes bytecode or source code, and handles things like memory management and JIT compilation. The word "virtual machine" means both, so in interviews it is worth asking which one is meant.

## 71: What is the JVM?

The Java Virtual Machine runs Java bytecode (.class files) produced by the Java compiler. It loads classes, checks the bytecode, interprets it and compiles hot code to machine code with a JIT compiler, and manages memory with a garbage collector. Languages like Kotlin and Scala also run on it.

## 72: Is V8 a virtual machine?

Yes, V8 (used by Chrome and Node.js) is often called a JavaScript virtual machine or engine. It parses JavaScript, turns it into bytecode run by the Ignition interpreter, and compiles hot functions to machine code with its optimizing compilers like Maglev and TurboFan. It also has its own garbage collector.

## 73: What is the Node.js vm module?

The built-in `node:vm` module lets you compile and run code in a separate V8 context with its own global object. It is NOT a security sandbox, so do not use it to run untrusted code.

```js
import vm from "node:vm";

const context = vm.createContext({ x: 2 });
const result = vm.runInContext("x * 21", context);
console.log(result); // 42
```

## 74: What is a VM host's capacity?

Capacity is how many VMs or how much workload a host can carry. It depends on CPU cores, RAM, storage speed and network bandwidth. RAM is usually the first limit, because it is harder to overcommit safely than CPU.

## 75: What is a VM's "size" or "flavor"?

It is the set of resources a VM gets: number of vCPUs, amount of RAM and sometimes disk and network limits. AWS calls it an instance type, Azure calls it a VM size and OpenStack calls it a flavor. Picking the right size saves money and avoids slowdowns.

## 76: What does it mean to resize a VM?

Resizing changes the VM's CPU, memory or disk. On most hypervisors and clouds, changing CPU and RAM needs a reboot (or a stop and start in the cloud), unless hot-add is supported. Growing a disk is usually easy, but you also have to grow the partition and file system inside the guest.

## 77: How do you grow a disk of a Linux VM?

First grow the virtual disk on the hypervisor or cloud side, then grow the partition and the file system inside the guest:

```bash
sudo growpart /dev/sda 1        # grow partition 1
sudo resize2fs /dev/sda1        # for ext4
# or for XFS:
sudo xfs_growfs /
```

Shrinking is much harder and risky, so most people avoid it.

## 78: What is a VM's boot order?

The boot order tells the virtual firmware which device to try first: virtual disk, CD/ISO, network (PXE) and so on. When installing from an ISO you put the CD first, and after installation you put the disk first or detach the ISO.

## 79: What is PXE boot?

PXE (Preboot Execution Environment) lets a machine boot from the network instead of a local disk. It gets an IP from DHCP and downloads a boot image from a TFTP or HTTP server. In VM environments it is used to install many VMs automatically.

## 80: What is cloud-init?

cloud-init is a tool that runs inside a VM on first boot and sets it up from data given by the cloud or hypervisor: hostname, users, SSH keys, packages and scripts. Almost all cloud Linux images include it, and Proxmox and libvirt support it too.

## 81: What does a simple cloud-init user-data file look like?

```yaml
#cloud-config
hostname: web01
users:
  - name: deploy
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys:
      - ssh-ed25519 AAAA... you@laptop
packages:
  - nginx
runcmd:
  - systemctl enable --now nginx
```

The first line `#cloud-config` is required so cloud-init knows the format.

## 82: What is user data in AWS EC2?

User data is a script or cloud-init config you pass when launching an instance. cloud-init (or EC2Launch on Windows) runs it on the first boot, so you can install packages and start services automatically. It is limited to 16 KB before base64 encoding.

## 83: What is the instance metadata service?

It is a special HTTP endpoint inside a cloud VM, at `http://169.254.169.254` on AWS, Azure and Google Cloud, that tells the VM about itself: instance ID, region, IPs and temporary credentials from its IAM role. On AWS you should require IMDSv2, which needs a session token.

## 84: What is the difference between stopping and terminating an EC2 instance?

Stopping shuts the VM down but keeps its EBS root volume, so you can start it again later. You stop paying for compute but still pay for storage. Terminating deletes the instance for good, and by default deletes the root volume too.

## 85: What is EBS?

Elastic Block Store is AWS's network block storage for EC2. An EBS volume is like a virtual disk that lives on the network, so it survives instance stops and can be detached and attached to another instance in the same Availability Zone. Common types are gp3 for general use and io2 for high IOPS.

## 86: What is instance store?

Instance store is disk storage physically attached to the host that runs your EC2 instance. It is very fast but temporary: the data is lost when the instance stops, is terminated, or the host fails. Use it for caches, scratch data or replicated data, not for anything you cannot lose.

## 87: What is a public IP vs a private IP for a cloud VM?

A private IP is used inside the cloud network (the VPC) and is not reachable from the internet. A public IP lets the VM be reached from the internet. On AWS, a normal public IP can change when you stop and start the instance, while an Elastic IP stays the same.

## 88: What is a security group?

A security group is a virtual firewall attached to a cloud VM's network interface. It has rules that allow inbound and outbound traffic by protocol, port and source. In AWS, security groups are stateful, so return traffic for an allowed connection is allowed automatically.

## 89: How do you connect to a Linux VM?

Usually with SSH using a key pair:

```bash
ssh -i ~/.ssh/my-key.pem ubuntu@203.0.113.10
```

The default username depends on the image, like `ubuntu` for Ubuntu or `ec2-user` for Amazon Linux. On AWS you can also use Session Manager or EC2 Instance Connect without opening port 22.

## 90: How do you connect to a Windows VM?

Usually with Remote Desktop Protocol (RDP) on port 3389. In the cloud you get the Administrator password from the console (on AWS, decrypted with your key pair) or use a bastion host. Opening RDP to the whole internet is a common mistake that leads to brute force attacks.

## 91: What is a bastion host?

A bastion (or jump host) is a small, hardened VM in a public subnet that you SSH into first, and from there reach VMs in private subnets. It means only one machine is exposed to the internet. Many teams now replace bastions with tools like AWS Session Manager.

## 92: What are the main benefits of VMs for developers?

- You can test on different OSes on one laptop
- You can break things and roll back with a snapshot
- Each project can have its own clean environment
- You can reproduce production-like setups locally
- You can share the same VM setup with the team using tools like Vagrant or Packer

## 93: What are the downsides of VMs?

VMs have overhead: each one runs a full OS that needs RAM, disk and boot time. They take longer to start than containers, images are large, and you have more OSes to patch. Licensing for hypervisors and guest OSes can also cost money.

## 94: What is VM sprawl?

VM sprawl is when an organization ends up with lots of VMs that nobody tracks, many unused or forgotten. They waste resources and money, and they often miss security patches. Tagging, owners, expiry dates and regular cleanup help avoid it.

## 95: What is a "golden image"?

A golden image is a pre-built, tested and patched VM image used as the standard base for new servers. Instead of setting up each server by hand, you build the image once (often with Packer) and launch identical VMs from it.

## 96: What is Packer?

Packer is a HashiCorp tool that builds machine images automatically from a config file. One template can build images for AWS, Azure, Google Cloud, VMware, Proxmox and others. It starts a temporary VM, runs your setup scripts, and saves the result as an image.

## 97: What is Terraform's role with VMs?

Terraform is an infrastructure-as-code tool that creates and manages VMs and their networks, disks and firewalls from config files. You describe what you want, Terraform figures out the changes and applies them. It works with clouds and with on-prem platforms like vSphere and Proxmox through providers.

## 98: What is a hypervisor host's management network?

It is a separate network used to manage the hypervisor: the web UI, SSH, API, cluster traffic and often live migration. It is kept apart from VM traffic for security and so that heavy VM traffic does not break management.

## 99: What is vCenter Server?

vCenter Server is VMware's central management tool for ESXi hosts. It lets you manage many hosts from one place and provides clustering features like vMotion, HA, DRS (load balancing), templates and permissions. It runs as a virtual appliance.

## 100: What is a virtual appliance?

A virtual appliance is a pre-built VM that runs one specific product, like a firewall, load balancer or management server. You import it and start it instead of installing software yourself. They are often distributed as OVA files.

## 101: What are OVF and OVA files?

OVF (Open Virtualization Format) is a standard for packaging a VM: an XML descriptor plus disk files. OVA is the same thing packed into a single tar file. You use them to export a VM from one hypervisor and import it into another, though drivers and hardware settings may still need fixing.

## 102: What is a hypervisor's datastore?

In VMware, a datastore is a storage location where VM files live, like a local disk, an NFS share, a VMFS volume on a SAN or vSAN. Proxmox calls the same idea "storage". Each VM's disks and config are stored on one or more datastores.

## 103: What files make up a VMware VM?

The main ones are:

- `.vmx`: the configuration
- `.vmdk`: the virtual disk (a small descriptor plus a `-flat.vmdk` data file)
- `.nvram`: firmware settings
- `.vmsn` and `-delta.vmdk` or `-sesparse.vmdk`: snapshot data
- `.vswp`: the VM's swap file
- `.log`: VM logs

## 104: What is the qcow2 format?

qcow2 (QEMU Copy On Write version 2) is QEMU's main disk image format. It supports thin provisioning, internal snapshots, backing files (for linked clones), compression and encryption. It is the default for many KVM setups.

## 105: What is a raw disk image?

A raw image is a plain byte-for-byte copy of a disk, with no extra structure. It is simple and fast, and can be sparse on file systems that support it. But it has no built-in snapshots or backing files, so those features must come from the storage layer (LVM, ZFS, Ceph).

## 106: How do you create a disk image with qemu-img?

```bash
qemu-img create -f qcow2 /var/lib/libvirt/images/web01.qcow2 40G
qemu-img info /var/lib/libvirt/images/web01.qcow2
```

This creates a 40 GB thin qcow2 disk that only uses a small amount of space at first.

## 107: How do you convert a disk image between formats?

Use `qemu-img convert`:

```bash
# VMware VMDK to qcow2
qemu-img convert -p -f vmdk -O qcow2 disk.vmdk disk.qcow2

# qcow2 to Hyper-V VHDX
qemu-img convert -p -f qcow2 -O vhdx disk.qcow2 disk.vhdx
```

`-p` shows progress. Converting the disk is often the first step when moving a VM between hypervisors.

## 108: What is VHDX?

VHDX is Hyper-V's virtual disk format, the newer version of VHD. It supports disks up to 64 TB, has a log for protection against corruption during power loss and supports dynamic (thin) and fixed sizes. Azure still uses the older fixed-size VHD format for uploaded disks.

## 109: What is VDI?

VDI is VirtualBox's own disk format (Virtual Disk Image). VirtualBox can also use VMDK, VHD and others. Note that "VDI" also means Virtual Desktop Infrastructure, which is a different thing.

## 110: What is Virtual Desktop Infrastructure (VDI)?

VDI means running user desktops as VMs in a data center or cloud. Users connect from thin clients, laptops or browsers to their remote desktop. It centralizes management and security. Examples are Citrix, Omnissa Horizon (formerly VMware Horizon) and Azure Virtual Desktop.

## 111: What is a virtual CD/DVD drive?

It is a virtual device in the VM where you can "insert" an ISO file. The guest sees it like a real optical drive. It is used to install operating systems, load drivers or mount tool ISOs like guest additions.

## 112: What is USB passthrough?

USB passthrough connects a physical USB device on the host directly to a VM, so the guest can use it as if it were plugged in locally. It is used for license dongles, phones, hardware keys and serial adapters. The device is not available to the host while it is passed through.

## 113: What are shared folders?

Shared folders let a VM access a folder on the host's file system. VirtualBox and VMware provide them through guest tools. On KVM you can use virtiofs. They are handy for development, where you edit code on the host and run it in the VM.

## 114: What is a hypervisor's resource pool?

A resource pool groups VMs so you can give the group a share of CPU and memory with limits, reservations or shares. VMware vSphere and Proxmox (as pools for permissions) use the idea. It helps one team or app not to starve others.

## 115: What is a CPU reservation for a VM?

A reservation guarantees a VM a minimum amount of CPU (in MHz) or memory, even when the host is busy. The hypervisor will not start the VM if it cannot give the reservation. Use it for important VMs, but too many reservations reduce how many VMs fit.

## 116: What is a VM resource limit?

A limit is the maximum CPU or memory a VM can use, even if the host has spare resources. It stops one VM from using too much, but setting it too low makes the VM slow even on an idle host, so it should be used carefully.

## 117: What are shares in VM resource management?

Shares set the relative priority between VMs when resources are tight. A VM with 2000 shares gets twice as much CPU as one with 1000 shares during contention. When there is no contention, shares do nothing.

## 118: What is a vCPU to physical core ratio?

It is how many vCPUs you give out per physical core, like 4:1. A higher ratio fits more VMs but increases the chance of CPU waiting time. General-purpose VMs often work fine at 3:1 to 5:1, while busy databases may need close to 1:1.

## 119: What is a hypervisor's CPU ready time?

CPU ready (VMware term) or steal time (Linux term) is the time a vCPU was ready to run but had to wait because the physical CPU was busy with other VMs. High values mean the host is overloaded or the VM has too many vCPUs.

## 120: What is steal time in a Linux VM?

Steal time (`st` in `top`) is the percentage of time the VM's vCPU waited for the hypervisor to give it real CPU. A few percent is normal on shared clouds. Constant high steal time means a noisy host, and moving to a bigger or dedicated instance can help.

## 121: What is a noisy neighbor?

A noisy neighbor is another VM on the same host that uses so much CPU, disk or network that your VM slows down. It is a common problem in shared environments. Fixes include limits, better placement, dedicated hosts or moving the VM.

## 122: What is a dedicated host?

A dedicated host is a physical server in the cloud reserved only for your VMs. You get control over placement and can use per-socket or per-core software licenses (like some Windows Server or Oracle licenses). It costs more than normal shared instances.

## 123: What is a spot instance?

A spot instance (AWS) or spot VM (Azure, Google Cloud) uses spare cloud capacity at a big discount, often 60-90% off. The cloud can take it back with short notice, two minutes on AWS. It is great for batch jobs, CI and stateless workers that can handle interruptions.

## 124: What is a reserved instance or savings plan?

They are discounts you get by committing to use a certain amount of compute for one or three years. AWS has Reserved Instances and Savings Plans, Azure has Reservations and Savings Plans, and Google has committed use discounts. They make sense for steady, always-on VMs.

## 125: What is an Availability Zone?

An Availability Zone is one or more separate data centers in a cloud region, with their own power and networking. Spreading VMs across zones protects you if one zone fails. Data between zones usually costs money and has slightly more latency.

## 126: What is an auto scaling group?

An auto scaling group (AWS) or virtual machine scale set (Azure) or managed instance group (Google) is a group of identical VMs that grows or shrinks automatically based on load or a schedule. It also replaces unhealthy instances. All VMs start from the same launch template or image.

## 127: What is a launch template?

A launch template in AWS saves the settings for launching an EC2 instance: AMI, instance type, key pair, security groups, user data and so on. Auto scaling groups use it to launch identical instances, and it supports versions.

## 128: What is the virtio standard?

virtio is a standard for virtual devices that are designed for VMs instead of copying real hardware. Guests with virtio drivers get much faster disk and network than with emulated devices like an IDE disk or e1000 network card. Linux has the drivers built in; Windows needs the virtio-win drivers.

## 129: What is an emulated device?

An emulated device is a virtual copy of a real, well-known piece of hardware, like an Intel e1000 network card or an IDE disk controller. Any OS already has drivers for it, so it works out of the box, but it is slow because the hypervisor must emulate every register access.

## 130: What is a paravirtualized device?

A paravirtualized device is a virtual device where the guest knows it is in a VM and uses a simple, efficient interface to talk to the hypervisor, like virtio, VMware's vmxnet3 and PVSCSI or Hyper-V's synthetic devices. It is much faster than emulation but needs special drivers in the guest.

## 131: What is paravirtualization?

Paravirtualization means changing the guest OS so it cooperates with the hypervisor instead of thinking it runs on real hardware. Early Xen used it for the whole OS, before CPUs had virtualization support. Today it is mostly used for devices (virtio) and some features like clocks and spinlocks, while the CPU uses hardware virtualization.

## 132: What is full virtualization?

Full virtualization means the guest OS runs unmodified and does not need to know it is in a VM. The hypervisor fully hides the difference, either with binary translation (old VMware) or with hardware support (VT-x/AMD-V). Most VMs today use full virtualization for the CPU plus paravirtual drivers for devices.

## 133: Can you run macOS in a VM?

Technically yes, but Apple's license only allows macOS VMs on Apple hardware. On a Mac, tools like Parallels Desktop, VMware Fusion, UTM and Apple's Virtualization framework can run macOS guests. AWS also offers EC2 Mac instances that run on real Mac minis.

## 134: Can you run Windows in a VM on an Apple Silicon Mac?

Yes, but you run the ARM version of Windows 11, not the x86 one, using Parallels Desktop, VMware Fusion or UTM. Windows on ARM can then run most x86 apps through its own emulation layer. Running x86 Windows itself would need full emulation and would be very slow.

## 135: What is UTM?

UTM is a free app for macOS and iOS that gives QEMU a simple GUI. On Apple Silicon it uses Apple's Hypervisor framework for fast ARM guests and QEMU emulation for other architectures like x86.

## 136: What is Apple's Virtualization framework?

It is a macOS framework that lets apps create Linux and macOS VMs on Apple Silicon and Intel Macs with little code. Docker Desktop, Lima, Tart and UTM can use it. It is built on top of the lower-level Hypervisor framework.

## 137: What is Multipass?

Multipass is a tool from Canonical to quickly start Ubuntu VMs on Windows, macOS and Linux with one command:

```bash
multipass launch --name dev --cpus 2 --memory 4G --disk 20G
multipass shell dev
```

It uses the platform's native hypervisor (Hyper-V, Apple's framework or KVM) and supports cloud-init.

## 138: What is Firecracker?

Firecracker is an open source virtual machine monitor from AWS that creates very small, fast "microVMs" using KVM. A microVM can start in around 125 ms and uses only a few MB of memory overhead. AWS Lambda and Fargate use it to run customer code with VM-level isolation.

## 139: What is a microVM?

A microVM is a very lightweight VM with only the minimum virtual devices (no USB, no graphics, few legacy devices). That makes it start almost as fast as a container while keeping a separate kernel for strong isolation. Firecracker and Cloud Hypervisor are examples.

## 140: What is Kata Containers?

Kata Containers runs each container or Kubernetes pod inside its own lightweight VM, so you get container tools and workflow with VM isolation. It plugs into containerd or CRI-O and can use hypervisors like QEMU, Cloud Hypervisor or Firecracker.

## 141: What is the host operating system's role in a Type 2 hypervisor?

The host OS controls the hardware and runs the hypervisor as a normal app. The hypervisor asks the host OS for memory, CPU time and device access. That is why a busy host OS, antivirus or updates can slow down the VMs.

## 142: What is a VM's uptime and why does it matter?

Uptime is how long the VM has been running since the last boot. Very long uptime can mean missing kernel patches. In the cloud, a VM can also be restarted or moved by the provider during host maintenance, so apps should not depend on one VM staying up forever.

## 143: What is scheduled maintenance for cloud VMs?

Cloud providers sometimes need to update or retire the physical host under your VM. They may live-migrate it without notice (Google Cloud does this by default), or send you a notice to stop and start the VM before a deadline (AWS scheduled events). Starting the instance again moves it to a new host.

## 144: What is the difference between rebooting and stop/start of an EC2 instance?

A reboot restarts the OS on the same host and keeps the public IP and instance store data. A stop and start shuts it down and, when started, runs it on possibly a different host, gives it a new public IP (unless using an Elastic IP) and wipes instance store data.

## 145: How do you list running EC2 instances with Node.js?

Use the AWS SDK for JavaScript v3:

```js
import { EC2Client, DescribeInstancesCommand } from "@aws-sdk/client-ec2";

const ec2 = new EC2Client({ region: "us-east-1" });

const res = await ec2.send(
  new DescribeInstancesCommand({
    Filters: [{ Name: "instance-state-name", Values: ["running"] }],
  }),
);

for (const r of res.Reservations ?? []) {
  for (const i of r.Instances ?? []) {
    console.log(i.InstanceId, i.InstanceType, i.PrivateIpAddress);
  }
}
```

## 146: How do you start and stop an EC2 instance with Node.js?

```js
import {
  EC2Client,
  StartInstancesCommand,
  StopInstancesCommand,
} from "@aws-sdk/client-ec2";

const ec2 = new EC2Client({ region: "us-east-1" });
const InstanceIds = ["i-0123456789abcdef0"];

await ec2.send(new StopInstancesCommand({ InstanceIds }));
// later
await ec2.send(new StartInstancesCommand({ InstanceIds }));
```

These calls return right away; the state changes in the background.

## 147: What is a hypervisor's VM log used for?

VM logs record events like power changes, device errors, migration steps and crashes. When a VM will not start or behaves oddly, the log is the first place to look. QEMU/libvirt logs are in `/var/log/libvirt/qemu/<name>.log`, VMware has `vmware.log` in the VM folder.

## 148: What is the VM BIOS/UEFI boot screen useful for?

It lets you pick a boot device, enter firmware settings, check Secure Boot or see early boot errors. On most hypervisors you open the console right after power on and press a key like Esc or F2. It helps fix VMs that fail before the OS loads.

## 149: What is time sync in a VM and why does it matter?

VMs can drift from real time, especially after being paused, suspended or migrated. Wrong time breaks TLS certificates, logs, Kerberos and distributed systems. Use NTP or chrony inside the guest and, where possible, a paravirtual clock like kvm-clock, and avoid running two time sync tools at once.

## 150: What is the most common first step when a VM is slow?

Check whether the slowness is inside the guest or on the host. Inside the guest, look at CPU, memory, disk and network with tools like `top`, `vmstat` and `iostat`, and watch steal time. On the host, check CPU ready, memory pressure, swapping and storage latency. Many "slow VM" problems are really overloaded hosts or slow storage.

# Moderate Questions (151-300)

## 151: How do KVM and QEMU work together?

KVM is a kernel module that exposes `/dev/kvm`. QEMU opens it, creates a VM and one thread per vCPU, and asks KVM to run guest code on the real CPU. When the guest touches a device, like writing to a disk or network register, the CPU exits to KVM, and KVM passes it to QEMU, which emulates the device and returns. So KVM does the CPU and memory, QEMU does the devices.

## 152: How do you start a simple KVM VM with QEMU directly?

```bash
qemu-system-x86_64 \
  -enable-kvm -cpu host -smp 2 -m 4G \
  -drive file=ubuntu.qcow2,if=virtio,format=qcow2 \
  -cdrom ubuntu-24.04-live-server-amd64.iso \
  -nic user,model=virtio-net-pci,hostfwd=tcp::2222-:22 \
  -display none -serial mon:stdio
```

This runs a 2-vCPU, 4 GB VM with a virtio disk and user-mode networking, forwarding host port 2222 to the guest's SSH. In real setups libvirt or Proxmox generates these options for you.

## 153: How do you create a VM with virt-install?

```bash
virt-install \
  --name web01 --memory 4096 --vcpus 2 \
  --disk size=40,format=qcow2,bus=virtio \
  --cdrom /isos/ubuntu-24.04-live-server-amd64.iso \
  --os-variant ubuntu24.04 \
  --network bridge=br0,model=virtio \
  --graphics vnc
```

`--os-variant` lets libvirt choose good defaults for that OS. Run `virt-install --osinfo list` (or `osinfo-query os`) to see valid names.

## 154: What does a libvirt domain XML look like?

libvirt stores each VM as XML. A trimmed example:

```xml
<domain type="kvm">
  <name>web01</name>
  <memory unit="GiB">4</memory>
  <vcpu>2</vcpu>
  <os><type arch="x86_64" machine="q35">hvm</type></os>
  <cpu mode="host-passthrough"/>
  <devices>
    <disk type="file" device="disk">
      <driver name="qemu" type="qcow2"/>
      <source file="/var/lib/libvirt/images/web01.qcow2"/>
      <target dev="vda" bus="virtio"/>
    </disk>
    <interface type="bridge">
      <source bridge="br0"/>
      <model type="virtio"/>
    </interface>
  </devices>
</domain>
```

You edit it with `virsh edit web01` and create a VM from it with `virsh define web01.xml`.

## 155: What is the difference between virsh define and virsh create?

`virsh define` registers a persistent VM from XML; it stays in libvirt after reboots and you start it with `virsh start`. `virsh create` starts a transient VM from XML that disappears from libvirt when it is shut down. Most of the time you want `define`.

## 156: What are the i440fx and q35 machine types?

They are two virtual chipsets in QEMU. i440fx emulates an old 1996 Intel chipset with a PCI bus. q35 emulates a newer Intel chipset with PCIe, which is better for PCIe passthrough, Secure Boot and modern guests. New VMs should use q35 unless you need very old OS support.

## 157: Why do you pin a QEMU machine type version like pc-q35-11.0?

The machine type version fixes the exact virtual hardware the guest sees. If QEMU is upgraded, a VM with a pinned version still sees the same hardware, which is needed for live migration between hosts with different QEMU versions and to avoid Windows re-activation. Using an unversioned alias like `q35` gives the newest version.

## 158: What are the CPU models host-passthrough and host-model?

With `host-passthrough`, the guest sees the host CPU exactly, with every feature, which gives the best performance but makes migration between different CPUs unsafe. With `host-model`, libvirt picks a named model close to the host CPU, which is a bit more portable. Named models like `x86-64-v3` or `EPYC` give a fixed feature set so VMs can migrate across a mixed cluster.

## 159: What are x86-64 microarchitecture levels like x86-64-v2 and v3?

They are standard sets of CPU features. v2 adds things like SSE4.2 and POPCNT, v3 adds AVX2, BMI and FMA, and v4 adds AVX-512. QEMU and Proxmox offer CPU models with these names. Some distributions, like RHEL 10, require at least v3, so picking a too-old CPU model can stop a guest from booting.

## 160: How do you install virtio drivers on a Windows guest?

Download the virtio-win ISO from the Fedora project and attach it as a second CD during Windows setup. When Windows does not find the disk, click "Load driver" and pick the viostor or vioscsi driver. After install, run the virtio-win guest tools installer to add the network, balloon and QEMU guest agent drivers.

## 161: What is the difference between virtio-blk and virtio-scsi?

virtio-blk is the simpler and slightly faster path, with one PCI device per disk. virtio-scsi uses one controller that can hold many disks, supports SCSI commands like UNMAP/discard more fully, and scales better to many disks. Proxmox defaults to virtio-scsi-single, which gives each disk its own controller so it can have its own I/O thread.

## 162: What is an I/O thread in QEMU?

By default, QEMU handles device I/O in its main loop. An I/O thread is a separate thread dedicated to one or more disks, so disk work does not compete with other QEMU work. Enabling `iothread` on busy virtio disks often improves latency and throughput.

## 163: What are the QEMU disk cache modes?

The `cache` option controls how the host page cache is used:

- `none`: uses O_DIRECT and skips the host page cache; the usual safe, fast choice
- `writeback`: uses the host cache, fast, still safe if the guest sends flushes
- `writethrough`: every write goes to disk before returning, safe but slow
- `directsync`: like none but every write is synced
- `unsafe`: ignores flushes, fast but data can be lost on host crash; only for throwaway VMs

## 164: What is io_uring in QEMU?

io_uring is a modern Linux async I/O interface. QEMU can use it as the disk AIO backend (`aio=io_uring`), next to `threads` and `native`. It can reduce overhead for fast NVMe storage. Proxmox uses io_uring by default for many storage types.

## 165: How does a qcow2 backing file work?

A qcow2 image can point to a read-only backing file. Reads of unchanged blocks come from the backing file, and writes go to the new overlay. This is how linked clones and some snapshots work:

```bash
qemu-img create -f qcow2 -F qcow2 -b base-ubuntu.qcow2 vm1.qcow2
```

`-F` sets the backing file format, which newer QEMU versions require.

## 166: What are internal vs external snapshots in qcow2?

Internal snapshots are stored inside the same qcow2 file (`qemu-img snapshot -c`). External snapshots create a new overlay file on top of the current disk, and the old file becomes read-only. External snapshots are the recommended way in libvirt and work better with live backups and block commit.

## 167: How do you take a disk-only snapshot with virsh?

```bash
virsh snapshot-create-as web01 before-upgrade \
  --disk-only --atomic --quiesce
```

`--disk-only` makes an external snapshot without saving RAM, `--atomic` makes it all-or-nothing, and `--quiesce` asks the QEMU guest agent to freeze file systems first so the snapshot is consistent.

## 168: What is a crash-consistent vs application-consistent snapshot?

A crash-consistent snapshot captures the disk as if the power was cut: data in memory or in flight is lost, though journaling file systems usually recover. An application-consistent snapshot first asks the guest (through the guest agent, VSS on Windows or scripts) to flush and freeze apps like databases, so the snapshot is clean.

## 169: Why are long-lived snapshots bad?

Each snapshot adds a delta layer that grows with every write. Over time it uses lots of space, slows down reads (the hypervisor checks several layers), and makes deleting the snapshot slow because all changes must be merged back. Keep snapshots for hours or days, not months.

## 170: What happens when you delete a snapshot?

Deleting a snapshot does not delete the changes after it; it merges data so the chain becomes shorter. In VMware, deleting consolidates the delta disk into the parent. In libvirt with external snapshots you use `virsh blockcommit` or `blockpull`. Large deltas can take a long time to merge and add I/O load.

## 171: How does memory ballooning work?

A balloon driver runs inside the guest. When the host needs memory, it tells the driver to "inflate", meaning the driver allocates memory inside the guest and hands those pages back to the host. The guest then has less usable RAM and may swap or drop caches. When pressure is gone, the balloon deflates and the guest gets memory back.

## 172: What is Kernel Same-page Merging (KSM)?

KSM is a Linux feature that scans memory for identical pages, for example from many VMs running the same OS, and merges them into one shared copy-on-write page. It can save a lot of RAM on hosts with similar VMs, but costs some CPU and has had side-channel security concerns, so some setups turn it off.

## 173: What is transparent page sharing in VMware?

It is VMware's version of KSM: identical memory pages are shared between VMs. Because of security research showing cross-VM side channels, VMware turned off sharing between different VMs by default (salting), and now shares pages only within a single VM unless you change it.

## 174: What is memory hot-add?

Memory hot-add lets you increase a running VM's RAM without a reboot. The hypervisor and guest OS both need to support it. In QEMU it works with memory backends and DIMM devices or virtio-mem; in VMware it is an option you enable while the VM is off. Hot-remove is less widely supported.

## 175: What is virtio-mem?

virtio-mem is a paravirtual device that lets the host add or remove guest memory in small blocks while the VM runs. It is more flexible than traditional DIMM hotplug and more reliable than ballooning for resizing memory. It is supported on recent Linux guests and newer Windows drivers.

## 176: What is CPU hot-add?

CPU hot-add adds vCPUs to a running VM. The guest OS must support it. In VMware, enabling CPU hot-add can turn off vNUMA for the VM, which may hurt performance for large VMs, so many admins leave it off for big databases.

## 177: How do you configure a Linux bridge for VMs?

With netplan on Ubuntu:

```yaml
network:
  version: 2
  ethernets:
    eno1: {}
  bridges:
    br0:
      interfaces: [eno1]
      dhcp4: true
```

Apply with `sudo netplan apply`. Then attach VMs to `br0`, and they appear on the same LAN as the host.

## 178: What is Open vSwitch?

Open vSwitch (OVS) is an advanced software switch for Linux. It supports VLANs, tunnels like VXLAN and Geneve, OpenFlow rules and integration with SDN controllers. OpenStack and OVN use it heavily. For simple setups, a Linux bridge is easier.

## 179: How do VLANs work with VMs?

A VLAN tags Ethernet frames with an ID so one physical network can carry many separate networks. The host's physical port is set as a trunk carrying many VLANs, and each VM's vNIC is assigned a VLAN tag on the virtual switch. VMs on different VLANs cannot talk without a router.

## 180: What is macvtap?

macvtap connects a VM directly to a physical interface with its own MAC address, without a bridge. It is simple and fast, but by default the host cannot talk to its own VMs through that interface. libvirt calls it "direct" networking.

## 181: What is the libvirt default network?

libvirt creates a NAT network called `default` on bridge `virbr0`, usually with subnet 192.168.122.0/24. It runs dnsmasq for DHCP and DNS. VMs can reach the internet through the host but are not reachable from outside without port forwarding or routing.

## 182: How do you find the IP address of a libvirt VM?

```bash
virsh domifaddr web01                 # from DHCP leases
virsh domifaddr web01 --source agent  # from the QEMU guest agent
virsh net-dhcp-leases default
```

The agent source works even with bridged networking, where libvirt does not run the DHCP server.

## 183: What is SR-IOV?

SR-IOV (Single Root I/O Virtualization) lets one physical PCIe device, usually a network card, show up as many "virtual functions". Each virtual function can be passed directly to a VM, so the VM gets near-native network speed and low latency, without going through the virtual switch. It is used in clouds and telecom. The downside is harder live migration.

## 184: What is PCI passthrough?

PCI passthrough gives a whole physical PCI device, like a GPU, NVMe drive or network card, directly to one VM. The guest uses its normal driver and gets almost native speed. It needs IOMMU support (Intel VT-d or AMD-Vi) and the device cannot be shared or easily live migrated.

## 185: What is an IOMMU?

An IOMMU is a hardware unit that translates and restricts memory addresses used by devices for DMA. In virtualization, it makes sure a passed-through device can only access the memory of its VM. Intel calls it VT-d, AMD calls it AMD-Vi. You enable it in firmware and with kernel options like `intel_iommu=on`.

## 186: What are IOMMU groups?

An IOMMU group is the smallest set of devices that the IOMMU can isolate from each other. You must pass all devices in a group to the same VM. On consumer motherboards, many devices can end up in one group, which makes passthrough harder.

## 187: What is VFIO?

VFIO is the Linux framework that lets user-space programs like QEMU safely access PCI devices using the IOMMU. To pass a device to a VM, you bind it to the `vfio-pci` driver instead of its normal host driver, and QEMU then gives it to the guest.

## 188: How do you use a GPU in a VM?

There are three main ways:

- Full passthrough: one GPU goes to one VM using VFIO
- vGPU: the GPU is split into slices, for example NVIDIA vGPU or AMD MxGPU, with vendor drivers and licenses
- Paravirtual or API forwarding: like virtio-gpu with VirGL or Venus, for lighter 3D use

Cloud GPU instances like AWS G and P families usually give you passthrough GPUs.

## 189: What is NUMA and why does it matter for VMs?

NUMA (Non-Uniform Memory Access) means a server has several CPU sockets or nodes, each with its own local memory. Accessing memory on another node is slower. If a big VM's vCPUs run on one node but its memory is on another, performance drops. Hypervisors try to keep a VM inside one node or expose a virtual NUMA layout to the guest.

## 190: What is vNUMA?

vNUMA means the hypervisor shows the guest a NUMA layout that matches how its vCPUs and memory are placed on the host. Then the guest OS and apps like databases can make smart choices about memory placement. It matters for VMs bigger than one physical NUMA node.

## 191: What is CPU pinning?

CPU pinning ties a VM's vCPUs to specific physical cores so the host scheduler does not move them around. It reduces latency jitter and cache misses for latency-sensitive workloads like real-time apps or high-speed networking. It also reduces flexibility, so it is used only when needed.

```bash
virsh vcpupin web01 0 4
virsh vcpupin web01 1 5
```

## 192: What are huge pages and how do they help VMs?

Normal memory pages are 4 KB. Huge pages are 2 MB or 1 GB. Backing guest memory with huge pages means fewer page table entries and fewer TLB misses, which speeds up memory-heavy VMs. Linux can use transparent huge pages automatically, or you can reserve static huge pages for VMs.

## 193: What is the difference between sockets, cores and threads in a VM's CPU topology?

You can present vCPUs to the guest as, for example, 1 socket with 8 cores or 2 sockets with 4 cores. The total is the same, but the topology matters for licensing (some software is licensed per socket) and for NUMA. Windows desktop editions also limit how many sockets they use.

## 194: Should you give a VM as many vCPUs as possible?

No. Extra vCPUs that the VM does not need still have to be scheduled, which increases CPU ready time and overhead, and can make the VM slower. Start small, measure, and add vCPUs when the VM really uses them. This is called "right-sizing".

## 195: How do you right-size a VM?

Collect metrics for a few weeks: CPU, memory, disk and network use, including peaks. Compare them with what is allocated. Shrink VMs that rarely use their resources and grow ones that are often at the limit. Cloud tools like AWS Compute Optimizer and Azure Advisor give suggestions automatically.

## 196: How does live migration of memory work step by step?

Most hypervisors use "pre-copy":

1. Copy all of the VM's memory to the target host while it keeps running
2. Track which pages changed (dirty pages) and copy them again
3. Repeat until the remaining dirty pages are small
4. Pause the VM, copy the last pages and CPU state
5. Resume the VM on the target and switch its network to the new host

The pause usually takes milliseconds.

## 197: What is needed for live migration to work?

- Both hosts can access the VM's disks (shared storage), or the disks are copied during migration
- Compatible CPUs, or a CPU model both support
- Same network names and VLANs on both hosts
- Enough free CPU and memory on the target
- A fast, preferably dedicated, migration network
- Compatible hypervisor versions and machine types

## 198: How do you live migrate a VM with virsh?

```bash
virsh migrate --live --persistent --undefinesource \
  web01 qemu+ssh://host2/system
```

Add `--copy-storage-all` if the disks are not on shared storage, so they are copied too. That takes longer because the whole disk goes over the network.

## 199: What is VMware vMotion and Storage vMotion?

vMotion moves a running VM to another ESXi host with no downtime. Storage vMotion moves a running VM's disks to another datastore with no downtime. They can be combined, so you can move a VM between hosts that do not share storage.

## 200: What is VMware DRS?

DRS (Distributed Resource Scheduler) watches CPU and memory use in a vSphere cluster and uses vMotion to balance VMs across hosts. It also chooses the host when a VM powers on. You can add affinity or anti-affinity rules, like "keep these two VMs on different hosts".

## 201: What are affinity and anti-affinity rules?

Affinity rules keep VMs together on the same host, for example an app and its cache for low latency. Anti-affinity rules keep VMs apart, for example two database replicas, so one host failure does not take them both down. Clouds have similar features like AWS placement groups (spread) and Azure availability sets.

## 202: What is a Proxmox VE cluster?

It is a group of Proxmox nodes joined with `pvecm` that share configuration through a replicated file system (pmxcfs) and use Corosync for membership. You manage all nodes from one web UI, migrate VMs between them and use HA. A cluster needs a quorum, so three or more nodes (or two nodes plus a QDevice) is recommended.

## 203: What is quorum in a VM cluster?

Quorum means more than half of the cluster nodes agree they can see each other. Only the part of the cluster with quorum may run HA services and change config. It prevents a "split brain", where two halves of a broken cluster both start the same VM and corrupt its disk.

## 204: What is fencing in an HA cluster?

Fencing makes sure a failed node is really off before its VMs start elsewhere. Methods include power-off through IPMI or a smart PDU, or a hardware watchdog that resets the node when it loses quorum. Proxmox HA uses a watchdog. Without fencing, two copies of the same VM might run at once.

## 205: How do you manage Proxmox VMs from the command line?

Proxmox has the `qm` tool for VMs:

```bash
qm list
qm create 120 --name web01 --memory 4096 --cores 2 \
  --net0 virtio,bridge=vmbr0 --scsihw virtio-scsi-single \
  --scsi0 local-lvm:32 --ostype l26
qm start 120
qm shutdown 120
qm snapshot 120 before-upgrade
```

`pct` is the matching tool for LXC containers.

## 206: How do you use cloud-init with Proxmox?

Create a VM from a cloud image, add a cloud-init drive and set the values:

```bash
qm importdisk 9000 noble-server-cloudimg-amd64.img local-lvm
qm set 9000 --scsi0 local-lvm:vm-9000-disk-0 --ide2 local-lvm:cloudinit \
  --boot order=scsi0 --serial0 socket --vga serial0
qm set 9000 --ciuser deploy --sshkeys ~/.ssh/id_ed25519.pub --ipconfig0 ip=dhcp
qm template 9000
```

Then clone the template with `qm clone 9000 121 --name web02` for each new VM. Newer Proxmox versions also accept `qm disk import` as the name for `importdisk`.

## 207: What is Proxmox Backup Server?

Proxmox Backup Server (PBS) is a backup product for Proxmox VMs and containers. It does incremental, deduplicated backups, using dirty bitmaps so only changed blocks are read for running VMs. It supports encryption, verification, pruning and syncing to another PBS for offsite copies.

## 208: What is a dirty bitmap in QEMU?

A dirty bitmap tracks which blocks of a disk changed since a point in time. Backup tools use it for incremental backups so they read only changed blocks instead of the whole disk. QEMU supports persistent bitmaps in qcow2 so they survive restarts.

## 209: What is Changed Block Tracking (CBT)?

CBT is VMware's feature that records which disk blocks changed since the last backup. Backup tools like Veeam use it to do fast incremental backups. If CBT data gets corrupted, for example after some snapshot errors, it should be reset so backups stay correct.

## 210: How do backup tools back up a running VM?

Usually they:

1. Ask the guest to quiesce through the guest agent or VSS
2. Take a snapshot so the disk state is frozen
3. Let the guest continue while the backup reads from the snapshot
4. Use changed block tracking to copy only new data
5. Remove the snapshot

This gives consistent backups without stopping the VM.

## 211: What is the 3-2-1 backup rule for VMs?

Keep 3 copies of your data, on 2 different types of storage, with 1 copy offsite. Many people now add "1 immutable or air-gapped copy and 0 errors after testing restores" (3-2-1-1-0). Snapshots on the same datastore do not count as a copy.

## 212: Why should you test VM restores?

Because backups that cannot be restored are worthless. Restores can fail because of missing drivers, corrupt chains, wrong encryption keys or app inconsistencies. Regularly restore a VM to an isolated network, boot it and check the app works.

## 213: What is VM replication?

Replication keeps a copy of a VM on another host or site, updated every few minutes or continuously. If the primary site fails, you start the replica. Proxmox has ZFS-based storage replication, Hyper-V has Hyper-V Replica and VMware has vSphere Replication.

## 214: What is the difference between RPO and RTO for VMs?

RPO (Recovery Point Objective) is how much data you can lose, like "at most 15 minutes", which decides how often you back up or replicate. RTO (Recovery Time Objective) is how long it may take to be back up, like "within 1 hour", which decides your restore method.

## 215: What is Ceph and how is it used with VMs?

Ceph is a distributed storage system that spreads data across many servers with replication or erasure coding. Its block storage, RBD, is commonly used for VM disks in Proxmox and OpenStack. Any host in the cluster can access any disk, so live migration and HA work without a separate SAN.

## 216: How does ZFS help with VM storage?

ZFS gives checksums to detect corruption, snapshots, clones, compression and replication. Proxmox can store VM disks as ZFS volumes (zvols), which makes snapshots fast and replication between nodes easy. ZFS likes plenty of RAM and should run on plain disks, not hardware RAID.

## 217: What is LVM-thin for VM disks?

LVM-thin creates thin-provisioned logical volumes on Linux, with fast snapshots and clones. Proxmox uses `local-lvm` (LVM-thin) by default for VM disks on a single node. Watch the pool's data and metadata usage, because a full thin pool can corrupt VMs.

## 218: What is the TRIM or discard option for virtual disks?

When a guest deletes files, the space is free in the guest but still used in the thin disk file on the host. With discard enabled on the virtual disk and `fstrim` (or the discard mount option) in the guest, those freed blocks are passed down and the host can reclaim the space. It also helps SSDs.

## 219: What is VMware VMFS?

VMFS is VMware's clustered file system for block storage like SAN LUNs. Many ESXi hosts can read and write the same VMFS volume at once, with locking so each VM's files are used by only one host. VMFS 6 supports automatic space reclamation (UNMAP).

## 220: What is vSAN?

vSAN is VMware's hyper-converged storage. It pools the local disks of ESXi hosts in a cluster into one shared datastore, with storage policies for things like how many failures to tolerate. It removes the need for a separate SAN.

## 221: What is hyper-converged infrastructure (HCI)?

HCI combines compute, storage and often networking on the same servers, managed as one system. Each node runs VMs and also contributes disks to a distributed storage pool. Examples are vSAN, Nutanix, Proxmox with Ceph and Azure Local (formerly Azure Stack HCI).

## 222: What is the difference between iSCSI and NFS for VM storage?

iSCSI gives block storage: the host sees a LUN as a raw disk and formats it with VMFS, LVM or similar. NFS gives file storage: the host stores VM disk files on a shared folder. NFS is easier to manage and thin-friendly; iSCSI works well with multipathing and block features. Both run over normal Ethernet.

## 223: What is multipathing in VM storage?

Multipathing uses several network or Fibre Channel paths between a host and its storage. If one path fails, I/O continues on another, and paths can share load. On Linux it is `dm-multipath`; VMware has its own native multipathing.

## 224: What are Hyper-V Generation 1 and Generation 2 VMs?

Generation 1 VMs use legacy BIOS and emulated hardware like IDE, for older OSes. Generation 2 VMs use UEFI, Secure Boot, SCSI boot and synthetic devices only, which is faster and needed for Windows 11 and vTPM. You choose the generation at creation and cannot change it later.

## 225: How do you create a Hyper-V VM with PowerShell?

```powershell
New-VM -Name web01 -Generation 2 -MemoryStartupBytes 4GB `
  -NewVHDPath "D:\VMs\web01.vhdx" -NewVHDSizeBytes 60GB `
  -SwitchName "External"
Set-VMProcessor -VMName web01 -Count 2
Add-VMDvdDrive -VMName web01 -Path "D:\ISO\server2025.iso"
Start-VM -Name web01
```

## 226: What are Hyper-V virtual switch types?

- External: connected to a physical network card, so VMs reach the LAN
- Internal: VMs and the host can talk, but not the outside network
- Private: only VMs on the host can talk to each other

There is also a "Default Switch" on Windows clients that gives NAT access automatically.

## 227: What is Hyper-V Dynamic Memory?

Dynamic Memory lets Hyper-V change a VM's RAM while it runs, between a minimum and maximum, based on demand. It uses a balloon-style mechanism and memory hot-add. It helps fit more VMs on a host, but some apps like SQL Server or Exchange are better with fixed memory.

## 228: What are Hyper-V checkpoints?

Checkpoints are Hyper-V's snapshots. Standard checkpoints save disk and memory state. Production checkpoints (the default) use VSS in Windows or file system freeze in Linux to create application-consistent disk snapshots without memory, which are safer for production servers.

## 229: What is Hyper-V Replica?

Hyper-V Replica asynchronously copies a VM's changes to another Hyper-V host, every 30 seconds, 5 minutes or 15 minutes. If the main site fails, you fail over to the replica. It is built in and needs no shared storage.

## 230: What is a Hyper-V failover cluster?

It is a Windows Server Failover Cluster where Hyper-V hosts share storage like Cluster Shared Volumes (CSV) or Storage Spaces Direct. VMs are cluster roles, so if a host fails, they restart on another node, and you can live migrate between nodes.

## 231: What is VMware Tools and why is it important?

VMware Tools (or open-vm-tools on Linux) is the guest software for VMware VMs. It provides paravirtual drivers like vmxnet3 and PVSCSI, clean shutdown, time sync, heartbeats for HA, guest info like IP addresses and quiescing for backups. Without it, many vSphere features do not work properly.

## 232: What is vmxnet3?

vmxnet3 is VMware's paravirtual network adapter. It gives better throughput and lower CPU use than emulated adapters like E1000, and supports features like multi-queue, RSS and large receive offload. Most Linux distributions include the driver; Windows gets it from VMware Tools.

## 233: What is PVSCSI?

PVSCSI (VMware Paravirtual SCSI) is VMware's paravirtual storage controller. It gives higher IOPS and lower CPU use than LSI Logic for busy disks like databases. Windows needs the driver from VMware Tools at install time.

## 234: How do you script VMware vSphere?

The main options are:

- PowerCLI, a PowerShell module: `Connect-VIServer`, `Get-VM`, `New-VM`
- `govc`, a command line tool written in Go
- The vSphere REST API (Automation API)
- Terraform with the vsphere provider
- Ansible with the vmware collections

## 235: What is VBoxManage?

VBoxManage is VirtualBox's command line tool. You can do everything the GUI does:

```bash
VBoxManage createvm --name dev --ostype Ubuntu_64 --register
VBoxManage modifyvm dev --memory 4096 --cpus 2 --nic1 nat
VBoxManage startvm dev --type headless
VBoxManage snapshot dev take clean-install
VBoxManage list runningvms
```

## 236: How do you forward a port in VirtualBox NAT mode?

```bash
VBoxManage modifyvm dev --natpf1 "ssh,tcp,,2222,,22"
ssh -p 2222 user@127.0.0.1
```

The rule format is `name,protocol,host-ip,host-port,guest-ip,guest-port`. For a running VM, use `VBoxManage controlvm dev natpf1 ...` instead.

## 237: Can VirtualBox and Hyper-V run on the same Windows machine?

Yes, but with limits. When Hyper-V (or WSL 2, Windows Sandbox or VBS features) is on, VirtualBox cannot use VT-x directly and falls back to running through the Windows Hypervisor Platform API. That works but is usually slower. Many people choose one hypervisor per machine.

## 238: What are the common Vagrant commands?

```bash
vagrant init bento/ubuntu-24.04  # create a Vagrantfile
vagrant up                       # create and start
vagrant ssh                      # log in
vagrant provision                # re-run provisioners
vagrant halt                     # shut down
vagrant destroy -f               # delete the VM
vagrant snapshot save clean      # take a snapshot
```

## 239: How do you provision a Vagrant VM with Ansible?

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-24.04"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end
```

Vagrant runs Ansible from the host and builds the inventory for you. Use `ansible_local` if Ansible should run inside the VM.

## 240: What does a basic Packer template look like?

```hcl
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = ">= 1.3.0"
    }
  }
}

source "amazon-ebs" "node" {
  region        = "us-east-1"
  instance_type = "t3.small"
  ssh_username  = "ubuntu"
  ami_name      = "node-app-{{timestamp}}"
  source_ami_filter {
    filters = {
      name = "ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"
    }
    owners      = ["099720109477"]
    most_recent = true
  }
}

build {
  sources = ["source.amazon-ebs.node"]
  provisioner "shell" {
    inline = ["sudo apt-get update", "sudo apt-get install -y nodejs"]
  }
}
```

Run `packer init .` and then `packer build .`.

## 241: How do you launch an EC2 instance with Node.js?

```js
import { EC2Client, RunInstancesCommand } from "@aws-sdk/client-ec2";

const ec2 = new EC2Client({ region: "us-east-1" });

const userData = `#!/bin/bash
apt-get update && apt-get install -y nginx`;

const { Instances } = await ec2.send(
  new RunInstancesCommand({
    ImageId: "ami-0123456789abcdef0",
    InstanceType: "t3.micro",
    MinCount: 1,
    MaxCount: 1,
    SubnetId: "subnet-0abc",
    SecurityGroupIds: ["sg-0abc"],
    UserData: Buffer.from(userData).toString("base64"),
    MetadataOptions: { HttpTokens: "required" },
    TagSpecifications: [
      { ResourceType: "instance", Tags: [{ Key: "Name", Value: "web01" }] },
    ],
  }),
);

console.log(Instances[0].InstanceId);
```

`HttpTokens: "required"` forces IMDSv2.

## 242: How do you wait until an EC2 instance is running in Node.js?

The SDK has waiters:

```js
import { EC2Client, waitUntilInstanceRunning } from "@aws-sdk/client-ec2";

const ec2 = new EC2Client({ region: "us-east-1" });

await waitUntilInstanceRunning(
  { client: ec2, maxWaitTime: 300 },
  { InstanceIds: ["i-0123456789abcdef0"] },
);
```

"Running" means the VM has started, not that your app is ready. Use status checks or a health check for that.

## 243: How do you read instance metadata with IMDSv2 from Node.js?

```js
const base = "http://169.254.169.254/latest";

const token = await fetch(`${base}/api/token`, {
  method: "PUT",
  headers: { "X-aws-ec2-metadata-token-ttl-seconds": "21600" },
}).then((r) => r.text());

const instanceId = await fetch(`${base}/meta-data/instance-id`, {
  headers: { "X-aws-ec2-metadata-token": token },
}).then((r) => r.text());

console.log(instanceId);
```

In normal app code, the AWS SDK reads credentials from IMDS automatically, so you rarely need this.

## 244: Why was IMDSv2 introduced?

IMDSv1 answered simple GET requests, so an SSRF bug in an app could trick the server into fetching `169.254.169.254` and leak IAM credentials. IMDSv2 requires a PUT request to get a session token and a header on each call, which most SSRF bugs cannot do. The token response also has a configurable IP hop limit, so you can stop it from reaching containers or proxies that sit an extra network hop away.

## 245: What are EC2 status checks?

EC2 runs two checks: the system status check looks at the AWS host and network, and the instance status check looks at the guest OS, like whether it is reachable and booted. There is also an attached EBS status check. A failed system check usually means you should stop and start the instance to move it to new hardware.

## 246: What is EC2 auto recovery?

Auto recovery automatically moves an instance to new hardware if the system status check fails, keeping its instance ID, private IP, Elastic IP and EBS volumes. Many current instance types have simplified automatic recovery turned on by default. It does not help with problems inside the guest OS.

## 247: What is the EC2 serial console?

It gives you a text console to the instance's serial port from the AWS console or CLI, even if the network or SSH is broken. You can fix boot problems, bad firewall rules or a broken fstab. It must be enabled at the account level and the OS needs a user with a password to log in.

## 248: What are EC2 instance families?

Instance types are grouped by use:

- General purpose: T (burstable), M
- Compute optimized: C
- Memory optimized: R, X, z
- Storage optimized: I, D, Im/Is
- Accelerated: P, G (GPUs), Inf and Trn (AWS chips)

Letters after the number show features: `g` for Graviton ARM CPUs, `a` for AMD, `i` for Intel, `d` for local NVMe and `n` for extra networking.

## 249: What are burstable instances?

T-family instances (like t3, t4g) give a baseline CPU level and earn CPU credits while idle, which they spend to burst above the baseline. They are cheap for low-traffic apps. In "unlimited" mode (the default for T3 and newer) you can keep bursting but pay extra, while in "standard" mode the instance is slowed down when credits run out.

## 250: What is AWS Graviton?

Graviton is AWS's own ARM-based CPU line, used in instance types with a `g` like m8g or c7g. They usually give better price and performance than x86 for many workloads. Node.js, most Linux distributions and Docker images with arm64 builds run fine on them, but native modules must be built for arm64.

## 251: What is an Azure VM scale set?

A Virtual Machine Scale Set is a group of identical or mixed Azure VMs that can scale automatically. In "Flexible" orchestration mode, the current default, it can mix VM sizes and spot and regular VMs, and spreads them across fault domains or zones.

## 252: What is Google Compute Engine live migration?

Google Cloud by default live migrates VMs to another host during host maintenance, so most VMs do not need a reboot. Some types, like most VMs with attached GPUs, cannot live migrate and are stopped or terminated instead, based on the VM's `onHostMaintenance` setting.

## 253: What is the difference between a VM image and a VM snapshot in the cloud?

In AWS, an EBS snapshot is a backup of one volume, stored incrementally in S3. An AMI is a launchable image that refers to one or more snapshots plus settings like architecture and block device mapping. You can create an AMI from snapshots, and creating an AMI from an instance creates snapshots for you.

## 254: How do you share or copy a cloud image to another region?

In AWS you use `CopyImage` to copy an AMI to another region, and `ModifyImageAttribute` to share it with other accounts. Encrypted AMIs also need the KMS key shared. Azure uses Azure Compute Gallery to replicate images to regions, and Google uses images that are global by default.

## 255: What is a placement group in AWS?

A placement group controls how instances are placed on hardware:

- Cluster: close together in one zone for low latency and high bandwidth, used for HPC
- Spread: each instance on different hardware, max 7 per zone, for critical instances
- Partition: groups instances into partitions on separate racks, for big distributed systems like Kafka or HDFS

## 256: What is AWS Nitro?

Nitro is the system behind modern EC2 instances. It moves networking, storage and management to dedicated Nitro cards and uses a small KVM-based hypervisor. This gives VMs almost all of the host's resources, better security (no operator access) and allows bare-metal instances.

## 257: What is a bare-metal cloud instance?

A bare-metal instance, like EC2 `.metal` types, gives you the whole physical server without AWS's hypervisor. It is used for running your own hypervisor, special licensing, performance tools that need hardware access, or workloads that cannot run in a VM. You still get EBS and VPC networking through Nitro.

## 258: How do you choose between VMs and containers for a new service?

Use containers when the app is stateless, you want fast deploys and scaling, and you already have an orchestrator like Kubernetes or ECS. Use VMs when you need a different OS or kernel, strong isolation between tenants, legacy apps that expect a full server, or special hardware. Many teams run containers on VMs and get both.

## 259: How does Kubernetes relate to VMs?

Kubernetes nodes are usually VMs (in the cloud) or physical servers. Pods run as containers on those nodes. Tools like KubeVirt also let Kubernetes run and manage real VMs as pods, so legacy VM workloads and containers can live on the same platform.

## 260: What is KubeVirt?

KubeVirt is a Kubernetes add-on that adds a `VirtualMachine` resource. Each VM runs inside a pod using QEMU/KVM, so you manage it with `kubectl` and it uses Kubernetes networking and storage. Red Hat OpenShift Virtualization is built on it and is a common VMware alternative.

## 261: What is OpenStack?

OpenStack is an open source platform for building a private cloud. Nova manages VMs (usually on KVM), Neutron handles networking, Cinder handles block storage, Glance stores images and Keystone handles identity. It gives you an AWS-like API on your own hardware.

## 262: What is the difference between a private cloud and plain virtualization?

Plain virtualization means you have hypervisors and an admin creates VMs. A private cloud adds self-service: users request VMs through a portal or API, with quotas, billing or showback, multi-tenancy and automation. OpenStack, VMware Cloud Foundation and Apache CloudStack are private cloud platforms.

## 263: How do you automate VM provisioning end to end?

A common pipeline:

1. Packer builds a golden image with the OS and base tools
2. Terraform creates the VMs, networks and disks from that image
3. cloud-init sets hostname, users and keys on first boot
4. Ansible or similar configures the app
5. Monitoring and backups are added automatically

Everything lives in Git so changes are reviewed and repeatable.

## 264: What does a Terraform config for an AWS VM look like?

```hcl
resource "aws_instance" "web" {
  ami                    = "ami-0123456789abcdef0"
  instance_type          = "t3.small"
  subnet_id              = aws_subnet.private.id
  vpc_security_group_ids = [aws_security_group.web.id]
  user_data              = file("cloud-init.yaml")

  metadata_options {
    http_tokens = "required"
  }

  root_block_device {
    volume_type = "gp3"
    volume_size = 30
    encrypted   = true
  }

  tags = { Name = "web01" }
}
```

## 265: What is immutable infrastructure with VMs?

Instead of patching or changing running VMs, you build a new image with the change and replace the old VMs with new ones. This avoids configuration drift and makes rollbacks easy (just deploy the old image). Auto scaling groups with instance refresh make this simple in AWS.

## 266: What is configuration drift?

Drift is when servers that should be identical slowly become different because of manual changes, partial updates or hotfixes. It causes "works on server A but not B" bugs. Infrastructure as code, config management tools and immutable images help prevent it.

## 267: How do you monitor VMs?

Monitor at two levels:

- Hypervisor level: host CPU, CPU ready or steal, memory pressure, ballooning, swapping, datastore latency and network
- Guest level: OS metrics, disk usage, processes, app health and logs

Tools include Prometheus with node_exporter, Zabbix, Datadog, CloudWatch agent and vCenter performance charts.

## 268: Why can CPU usage inside a VM be misleading?

The guest only sees its own vCPUs. If the host is overloaded, the guest may show low usage while being slow, because it is waiting for CPU time it never gets. Always check steal time inside the guest or CPU ready on the hypervisor before deciding a VM needs more vCPUs.

## 269: How do you check steal time and other VM stats in Linux?

```bash
top          # look at the 'st' value
vmstat 1     # 'st' column
mpstat -P ALL 1
cat /proc/stat | head -1   # the 8th number is steal
```

High `st` with low `us` and `sy` means the host is the bottleneck, not your app.

## 270: How do you find out if a Linux machine is a VM?

```bash
systemd-detect-virt   # prints kvm, vmware, microsoft, amazon, none...
hostnamectl           # shows "Virtualization:"
sudo dmidecode -s system-product-name
lscpu | grep -i hypervisor
```

Apps sometimes use this to change behavior, and malware sometimes uses it to hide from analysis sandboxes.

## 271: How do you check from Node.js if it runs inside a VM?

There is no built-in API, but on Linux you can read the DMI info or the CPU flags:

```js
import { readFile } from "node:fs/promises";

async function isVirtual() {
  const cpuinfo = await readFile("/proc/cpuinfo", "utf8");
  if (/\bhypervisor\b/.test(cpuinfo)) return true;
  const product = await readFile(
    "/sys/class/dmi/id/product_name",
    "utf8",
  ).catch(() => "");
  return /kvm|vmware|virtualbox|hvm domu/i.test(product);
}

console.log(await isVirtual());
```

The `hypervisor` CPU flag is set by most hypervisors on x86, but this is a hint, not a guarantee.

## 272: How do you troubleshoot a VM that will not boot?

1. Open the console and read the error
2. Check the boot order and that the right disk is attached
3. Check if firmware changed (BIOS vs UEFI) or Secure Boot blocks it
4. Look at the hypervisor log for device or permission errors
5. Boot from a rescue ISO and check the file system, fstab and bootloader
6. If a change caused it, roll back the snapshot

## 273: What does "kernel panic: VFS unable to mount root fs" mean after migrating a VM?

Usually the guest's initramfs does not include the driver for the new disk controller, for example moving from VMware PVSCSI to KVM virtio. Fix it by temporarily using a controller the guest supports (SATA or IDE), booting, adding the virtio drivers to the initramfs (`dracut -f` or `update-initramfs -u`) and switching back.

## 274: How do you migrate a VM from VMware to KVM or Proxmox?

Common steps:

1. Uninstall VMware Tools (or keep open-vm-tools, which is harmless)
2. For Windows, install virtio drivers before migrating
3. Export the VM (OVF/OVA) or copy the VMDK
4. Convert with `qemu-img convert` or import with `qm importdisk`, `qm importovf` or the Proxmox ESXi import wizard
5. Create the VM with matching firmware (BIOS or UEFI)
6. Boot with SATA disk first if drivers are missing, then switch to virtio
7. Fix network names and IPs in the guest

`virt-v2v` can automate most of this for KVM.

## 275: What is virt-v2v?

virt-v2v is a tool that converts VMs from VMware, Hyper-V, Xen or images into KVM guests. It copies the disks, installs virtio drivers, removes old guest tools where it can and writes a libvirt or OpenStack config. It works for many Linux and Windows guests.

## 276: What is libguestfs?

libguestfs is a set of tools for looking at and changing VM disk images without booting them. You can read files, edit configs, reset passwords or install packages:

```bash
virt-ls -a web01.qcow2 /etc
virt-cat -a web01.qcow2 /etc/fstab
virt-customize -a web01.qcow2 --root-password password:secret \
  --install nginx
virt-sysprep -a template.qcow2   # clean a template
```

## 277: What is sysprep and why do you need it for Windows templates?

Sysprep generalizes a Windows install by removing the unique SID, computer name and hardware-specific settings. Without it, VMs cloned from one template have the same SID, which causes problems in Active Directory and some software. Run `sysprep /generalize /oobe /shutdown` before turning the VM into a template.

## 278: What do you clean in a Linux VM before making a template?

- SSH host keys (so every clone gets new ones)
- `/etc/machine-id` (empty it so systemd regenerates it)
- Shell history, logs and temp files
- Network config tied to a MAC address
- cloud-init state with `cloud-init clean`
- Any secrets or API keys

`virt-sysprep` does most of this automatically.

## 279: Why does a duplicate machine-id cause problems?

`/etc/machine-id` is used by systemd, journald and DHCP clients. If clones share it, they may request the same DHCP lease and get the same IP, and logs from different machines get mixed up. Empty it in templates so each clone generates a new one at first boot.

## 280: What is the difference between a full clone and a linked clone in practice?

A full clone copies all data and is independent, so you can delete the template later; it takes longer and uses more space. A linked clone is created in seconds and saves space, but depends on the template's disk, so the template cannot be deleted or changed, and heavy I/O on the base disk affects all clones. Linked clones fit labs, CI and VDI.

## 281: How do you set up a lab of VMs for testing a cluster?

Use a tool that creates many VMs from code, like Vagrant with a loop, Terraform with libvirt or Proxmox, or Multipass. Put them on a host-only or private network, use linked clones from one template to save space, and take snapshots after setup so you can reset quickly.

## 282: What are VM tags or labels used for?

Tags are key-value metadata on VMs like `env=prod`, `owner=payments`, `cost-center=42`. They help with cost reports, automation (backup all VMs tagged `backup=daily`), access control and cleanup. Cloud providers can enforce required tags with policies.

## 283: How do you control costs of cloud VMs?

- Right-size based on real usage
- Stop dev and test VMs outside working hours
- Use spot instances for interruptible work
- Use savings plans or reservations for steady load
- Move to newer or ARM instance types that are cheaper per performance
- Delete unused disks, snapshots and Elastic IPs
- Tag everything and review cost reports

## 284: How do you schedule VMs to stop at night in AWS with Node.js?

You can run a small Lambda on an EventBridge schedule:

```js
import {
  EC2Client,
  DescribeInstancesCommand,
  StopInstancesCommand,
} from "@aws-sdk/client-ec2";

const ec2 = new EC2Client({});

export const handler = async () => {
  const res = await ec2.send(
    new DescribeInstancesCommand({
      Filters: [
        { Name: "tag:auto-stop", Values: ["true"] },
        { Name: "instance-state-name", Values: ["running"] },
      ],
    }),
  );
  const ids = res.Reservations.flatMap((r) =>
    r.Instances.map((i) => i.InstanceId),
  );
  if (ids.length)
    await ec2.send(new StopInstancesCommand({ InstanceIds: ids }));
  return { stopped: ids };
};
```

AWS also has the Instance Scheduler solution that does this without custom code.

## 285: How do you handle spot instance interruptions?

Watch for the two-minute interruption notice through instance metadata (`/latest/meta-data/spot/instance-action`) or EventBridge, then drain the node: stop taking new work, finish or checkpoint jobs and deregister from the load balancer. Spread across many instance types and zones, and use a capacity-optimized allocation strategy to lower the chance of interruption.

## 286: How do you handle a VM that is low on disk space?

First find what is using space with `df -h` and `du -sh /* | sort -h`. Common causes are logs, old kernels, Docker images and temp files. Clean them up, add log rotation, and if you really need more space, grow the virtual disk and then the partition and file system inside the guest.

## 287: What is swap inside a VM vs host swapping?

Guest swap is when the guest OS moves its own memory pages to its virtual disk. Host swapping is when the hypervisor moves a VM's memory to the host's disk without the guest knowing. Host swapping is much worse, because the guest might swap out pages that are already swapped by the host. It is a sign of too much memory overcommit.

## 288: How do you secure a hypervisor host?

- Keep the hypervisor and firmware patched
- Put management interfaces on a separate, restricted network
- Use strong authentication, MFA and role-based access
- Turn off unused services and features
- Enable Secure Boot and TPM on the host
- Log and monitor admin actions
- Limit who can access VM consoles and datastores

## 289: How do you secure a guest VM?

Treat it like a physical server: keep the OS patched, use SSH keys instead of passwords, run a host firewall, open only needed ports, remove unused packages, use least-privilege IAM roles in the cloud, encrypt disks and send logs to a central system. Do not trust that the hypervisor will protect a badly configured guest.

## 290: What is VM disk encryption?

It means the virtual disk data is encrypted at rest. It can be done inside the guest (LUKS, BitLocker), by the hypervisor (VMware VM Encryption, encrypted qcow2) or by the cloud (EBS encryption with KMS). It protects against stolen disks, snapshots or backups, but not against attacks on the running guest.

## 291: How do you encrypt EBS volumes by default?

Turn on "EBS encryption by default" for each region in the account. Then every new volume and snapshot is encrypted with the default or a chosen KMS key:

```js
import {
  EC2Client,
  EnableEbsEncryptionByDefaultCommand,
} from "@aws-sdk/client-ec2";

await new EC2Client({ region: "us-east-1" }).send(
  new EnableEbsEncryptionByDefaultCommand({}),
);
```

Existing unencrypted volumes are not changed; copy their snapshots with encryption to fix them.

## 292: What is Secure Boot in a VM?

Secure Boot is a UEFI feature that only allows signed bootloaders and kernels to start. In a VM, the virtual UEFI (like OVMF or Hyper-V Gen 2 firmware) holds the keys. It protects against bootkits. Linux distributions with signed shims work fine; custom kernels need to be signed or Secure Boot turned off.

## 293: What is a VM escape?

A VM escape is an attack where code inside a guest breaks out and runs code on the hypervisor or host. It usually exploits a bug in an emulated device, like a virtual floppy (the VENOM bug in QEMU, 2015), a network card or a graphics adapter. It is rare but very serious, because the attacker can then reach all other VMs.

## 294: How do you reduce the risk of VM escape?

- Patch the hypervisor and QEMU quickly
- Remove unused virtual devices like floppy, sound, USB and serial
- Prefer simple paravirtual devices over complex emulated ones
- Run QEMU with sVirt (SELinux or AppArmor) and seccomp sandboxing
- Separate sensitive workloads onto different hosts
- Use microVMs with tiny device models where possible

## 295: What is sVirt?

sVirt is libvirt's use of SELinux or AppArmor to confine each QEMU process with a unique label. Even if a guest escapes into its QEMU process, the MAC policy stops it from reading other VMs' disks or most host files. It is on by default on RHEL, Fedora and Ubuntu.

## 296: How are VMs isolated from each other on the network?

By using separate virtual switches, VLANs or overlay networks (VXLAN, Geneve) per tenant, plus firewall rules on the virtual switch or security groups in the cloud. Features like MAC spoofing protection and port security stop a VM from pretending to be another one.

## 297: What is the difference between a VM and a sandbox?

A VM is one kind of sandbox: a strong one with a separate kernel. Other sandboxes are lighter, like containers, seccomp, gVisor or browser sandboxes. Security tools and malware analysis often use VMs as sandboxes because a bad program inside is less likely to reach the host.

## 298: Why is the Node.js vm module not a security sandbox?

Code in a `vm` context still runs in the same process and V8 isolate. Through tricks like reaching a constructor from a passed-in object (`this.constructor.constructor("return process")()`), it can often get to the real `process` and run any command. For untrusted code, use separate processes, containers, microVMs or a dedicated isolate library with care.

## 299: What is the difference between a VM and a Windows Sandbox?

Windows Sandbox is a quick, throwaway Windows VM built into Windows Pro and Enterprise. It uses Hyper-V technology and shares the host's OS files read-only, so it starts fast and is cleaned when closed. A normal VM is persistent and fully configurable.

## 300: How do you decide between on-prem virtualization and cloud VMs?

On-prem makes sense for steady, predictable workloads, strict data rules, existing hardware and teams to run it. Cloud VMs make sense for changing load, fast growth, global regions, managed services and when you do not want to manage hardware. Many companies use both, and moving costs and data egress fees should be part of the decision.

# Advanced Questions (301-450)

## 301: What are the Popek and Goldberg virtualization requirements?

In 1974, Popek and Goldberg described when a CPU can be efficiently virtualized. A VMM must give equivalence (programs behave the same as on real hardware), resource control (the VMM stays in control) and efficiency (most instructions run directly). Their key theorem says this works with trap-and-emulate if every "sensitive" instruction is also "privileged", meaning it traps when run in user mode.

## 302: Why was classic x86 not virtualizable under Popek and Goldberg?

Before VT-x and AMD-V, x86 had about 17 sensitive instructions that did not trap in user mode. For example, `POPF` silently ignored changes to the interrupt flag instead of trapping, and `SGDT` or `SMSW` let a guest read privileged state. So a simple trap-and-emulate hypervisor could not see or control these actions, and guests could behave wrongly.

## 303: How did VMware solve x86 virtualization before hardware support?

VMware used binary translation. Guest user code ran directly, but guest kernel code was scanned in blocks and problem instructions were rewritten into safe sequences that called the hypervisor. Translated blocks were cached, so the overhead was small for most code. It was clever, but complex, which is why hardware support replaced it.

## 304: How did Xen paravirtualization solve the same problem?

Xen changed the guest kernel itself. Instead of running privileged instructions, the modified kernel made "hypercalls" to Xen, much like system calls to an OS. The guest also knew about real memory frames and cooperated on page tables. It was fast but needed a modified OS, so Windows could not run as a PV guest.

## 305: How does Intel VT-x work at a high level?

VT-x adds two modes: VMX root (for the hypervisor) and VMX non-root (for guests). Both have the normal rings 0-3, so the guest kernel really runs in ring 0. The hypervisor sets up a VMCS structure for each vCPU and runs `VMLAUNCH` or `VMRESUME` to enter the guest. Certain events, set in the VMCS, cause a "VM exit" back to the hypervisor.

## 306: What is the VMCS?

The Virtual Machine Control Structure is a memory area, one per vCPU, that Intel CPUs use for VT-x. It holds the guest state (registers, control registers, segment info), the host state to restore on exit, and controls that decide which events cause VM exits. It also records why the last exit happened. AMD's version is called the VMCB.

## 307: What is a VM exit and why is it expensive?

A VM exit happens when the guest does something the hypervisor must handle, like I/O, some MSR accesses, `CPUID`, or an external interrupt. The CPU saves guest state, loads host state and jumps to the hypervisor. A round trip costs from hundreds to thousands of CPU cycles, plus cache and TLB effects, so reducing exits is a main goal of hypervisor tuning.

## 308: What are common causes of VM exits?

- I/O port and MMIO accesses to emulated devices
- `CPUID`, `RDMSR`/`WRMSR` for some registers
- `HLT` when the guest goes idle
- External interrupts and some interrupt-window events
- EPT violations (page not mapped yet)
- Control register writes
- Timer programming

Linux `perf kvm stat` shows exit reasons and counts per VM.

## 309: How do you see VM exit statistics on a KVM host?

```bash
sudo perf kvm stat record -p $(pgrep -f 'qemu.*web01') sleep 10
sudo perf kvm stat report
```

The report shows each exit reason, how many times it happened and the average time. A large number of `EXTERNAL_INTERRUPT`, `HLT` or `EPT_MISCONFIG` (MMIO) exits often points at a tuning problem.

## 310: What is shadow paging?

Before hardware nested paging, the hypervisor kept a "shadow" page table for each guest page table, mapping guest virtual addresses straight to host physical addresses. The real CPU used the shadow tables. Every time the guest changed its page tables, the hypervisor had to trap and update the shadows, which was slow for workloads that create many processes.

## 311: What are EPT and NPT?

Extended Page Tables (Intel) and Nested Page Tables (AMD, also called RVI) add a second level of address translation in hardware. The guest manages its own page tables (guest virtual to guest physical), and the hypervisor manages EPT/NPT (guest physical to host physical). The CPU walks both, so the hypervisor no longer has to trap guest page table changes.

## 312: What is the cost of two-dimensional page walks?

With nested paging, a TLB miss can need up to 24 memory reads on 4-level tables instead of 4, because each step of the guest walk also needs a host walk. That makes TLB misses much more expensive in VMs. Huge pages on both guest and host reduce the number of levels and misses, which is why they help VMs so much.

## 313: What is VPID and why does it matter?

VPID (Virtual Processor ID, Intel) and ASID (AMD) tag TLB entries with the VM they belong to. Without them, the CPU had to flush the whole TLB on every VM entry and exit. With them, entries from different VMs and the host can stay in the TLB at once, which reduces TLB misses after exits.

## 314: How does interrupt virtualization work, and what is APICv?

Guests expect a local APIC to receive and acknowledge interrupts. Emulating it in software causes many exits. Intel APICv and AMD AVIC let the CPU handle many APIC accesses and deliver interrupts to a running vCPU directly ("posted interrupts") without a VM exit. This greatly lowers overhead for network and disk heavy VMs.

## 315: What are posted interrupts?

Posted interrupts let an interrupt be recorded in a per-vCPU descriptor and delivered to the guest without a VM exit, if the vCPU is running. With VT-d posted interrupts, interrupts from passed-through devices can go straight to the guest too. It is one of the main reasons passthrough gets near-native latency.

## 316: How does KVM handle an MMIO access from the guest?

When the guest writes to an address that is not backed by RAM, the CPU causes an EPT violation or misconfiguration exit. KVM decodes the instruction, checks if a kernel-side device (like an ioeventfd or the in-kernel APIC) handles it, and if not, returns to QEMU with `KVM_EXIT_MMIO`. QEMU emulates the device and calls `KVM_RUN` again. Each step adds latency, which is why virtio avoids frequent MMIO.

## 317: What is the KVM API at a basic level?

User space talks to KVM with ioctls on file descriptors:

1. Open `/dev/kvm` and call `KVM_CREATE_VM` to get a VM fd
2. Map guest memory with `KVM_SET_USER_MEMORY_REGION`
3. Call `KVM_CREATE_VCPU` to get a vCPU fd and mmap its `kvm_run` structure
4. Set registers with `KVM_SET_REGS` and `KVM_SET_SREGS`
5. Loop on `KVM_RUN`, handle the exit reason (I/O, MMIO, HLT) and run again

QEMU, Firecracker, Cloud Hypervisor and crosvm all use this API.

## 318: What are ioeventfd and irqfd?

They connect KVM to event file descriptors. With ioeventfd, a guest write to a certain address (like a virtio "kick") signals an eventfd inside the kernel, without returning to QEMU's main loop. With irqfd, writing to an eventfd injects an interrupt into the guest. Together they let a device backend run in another thread or process with very little overhead.

## 319: How does virtio work internally?

virtio devices use shared memory rings called virtqueues. The guest driver puts buffer descriptors into the ring and "kicks" the device with one notification. The device backend reads the buffers, does the work, puts completions in the used ring and sends one interrupt. Batching many requests per kick and per interrupt is what makes it much faster than emulating real hardware registers.

## 320: What are split and packed virtqueues?

The split virtqueue, the original layout, has three separate areas: the descriptor table, the available ring and the used ring. The packed virtqueue (virtio 1.1) puts everything in one ring, which is more cache-friendly and works better with hardware offload. Both are supported; packed is negotiated as a feature bit.

## 321: What is vhost?

vhost moves the data path of a virtio device out of QEMU. With vhost-net, a kernel thread handles virtio-net packets directly, so packets do not go through QEMU user space. With vhost-user, a separate user-space process like DPDK, OVS-DPDK or virtiofsd handles the device over shared memory. QEMU still does setup and control.

## 322: What is vhost-user and when do you use it?

vhost-user lets a separate process implement a virtio device using a Unix socket for control and shared memory for data. It is used with OVS-DPDK for fast networking, with SPDK for fast storage, and with virtiofsd for file sharing. It keeps complex device code out of QEMU and can poll for very low latency.

## 323: What is vDPA?

vDPA (virtio data path acceleration) lets a hardware device, usually a SmartNIC, implement the virtio data path directly while the control path stays standard. The guest just uses its normal virtio-net driver, but gets near-SR-IOV speed. Because the guest sees virtio, not vendor hardware, live migration is easier than with plain SR-IOV.

## 324: What is virtiofs and how does it differ from 9p?

virtiofs shares a host directory with the guest using FUSE over virtio, with the virtiofsd daemon on the host. It is much faster than the older 9p (virtio-9p) and has better POSIX behavior. It can also use DAX to map file pages directly into guest memory. It is used by Kata Containers and for development setups.

## 325: How do you design a hypervisor host's NUMA layout for a big database VM?

Fit the VM inside one NUMA node if possible (vCPUs and memory). If it must span nodes, expose matching vNUMA to the guest, pin vCPUs and memory per node, and use huge pages. Avoid giving more vCPUs than cores in a node unless needed. Check with `numastat -p <qemu pid>` that memory is local.

## 326: How do you pin vCPUs, emulator threads and I/O threads in libvirt?

```xml
<vcpu placement="static">4</vcpu>
<iothreads>1</iothreads>
<cputune>
  <vcpupin vcpu="0" cpuset="4"/>
  <vcpupin vcpu="1" cpuset="5"/>
  <vcpupin vcpu="2" cpuset="6"/>
  <vcpupin vcpu="3" cpuset="7"/>
  <emulatorpin cpuset="2-3"/>
  <iothreadpin iothread="1" cpuset="2-3"/>
</cputune>
<numatune>
  <memory mode="strict" nodeset="0"/>
</numatune>
```

Keeping emulator and I/O threads off the vCPU cores stops them from causing jitter for the guest.

## 327: What is isolcpus and when is it used with VMs?

`isolcpus` (and newer `nohz_full`, `rcu_nocbs` or cgroup cpusets) keeps the host kernel scheduler and most interrupts off certain cores. Those cores are then used only for pinned vCPUs of latency-sensitive VMs, like telecom network functions or real-time apps. It trades flexibility for very steady latency.

## 328: What is halt polling in KVM?

When a vCPU runs `HLT` (goes idle), KVM can spin for a short time before really putting the thread to sleep, hoping an interrupt arrives soon. This cuts wake-up latency for VMs with frequent short idle periods, at the cost of some host CPU. It is controlled by the `halt_poll_ns` parameter and can be tuned per VM.

## 329: What is the cost of time-sharing many small vCPUs?

Every vCPU switch costs a context switch on the host, plus cache and TLB pollution. Guests with spinlocks can also suffer when the lock holder's vCPU is not scheduled ("lock holder preemption"), while other vCPUs spin. Paravirtual spinlocks and pause-loop exiting help, but a big overcommit ratio always adds latency.

## 330: What is pause-loop exiting?

Spinning code usually runs the `PAUSE` instruction in a loop. Intel PLE (and AMD pause filtering) detects a vCPU spinning on `PAUSE` for a long time and causes a VM exit, so the hypervisor can run another vCPU, ideally the one holding the lock. It reduces wasted CPU in overcommitted hosts.

## 331: How does the guest know about time in a VM?

The guest can use the TSC (time stamp counter), emulated timers like the HPET and PIT, or paravirtual clocks like kvm-clock and Hyper-V's reference TSC page. Paravirtual clocks give the guest scaling info so it can compute stable time even when the vCPU is not running or moves between host CPUs. `cat /sys/devices/system/clocksource/clocksource0/current_clocksource` shows what Linux uses.

## 332: What problems happen with TSC in VMs?

The TSC can differ between hosts or change frequency, so after a live migration or on hosts without "invariant TSC", guest time can jump or drift. Modern CPUs have TSC scaling and offsetting so the hypervisor can present a stable TSC to the guest even after migrating to a host with a different frequency.

## 333: Why can time in a VM jump after resume or migration, and how do you handle it?

While a VM is paused, its clock does not move, so on resume it is behind. Paravirtual clocks and the guest agent can correct it, and `chronyd` with `makestep` can step it. Apps that use wall-clock time for timeouts can break, so use monotonic clocks (`performance.now()` or `process.hrtime.bigint()` in Node.js) for measuring durations.

## 334: How does post-copy live migration work?

In post-copy, the VM's CPU state moves to the target first and it starts running right away. Memory pages are pulled from the source when the guest touches them (using userfaultfd on Linux), and the rest are pushed in the background. It always finishes in a bounded time, even for VMs that change memory very fast, but if the source or network fails during migration, the VM is lost.

## 335: When does pre-copy live migration fail to converge?

If the guest dirties memory faster than the network can send it, the dirty set never shrinks. This happens with big in-memory databases or caches doing many writes. Solutions are a faster migration network, compression, multifd (several streams), auto-converge (slowing the vCPUs down), raising the allowed downtime, or switching to post-copy.

## 336: What is auto-converge in QEMU migration?

Auto-converge throttles the guest's vCPUs step by step when migration does not make progress, so the guest dirties less memory and the copy can catch up. It works but slows the app down during migration. QEMU also has "dirty limit", which throttles only vCPUs that dirty pages fast, using dirty ring tracking.

## 337: How does KVM track dirty memory for migration?

KVM marks guest memory as write-protected (or uses hardware features like Intel PML, Page Modification Logging) and records which pages are written. QEMU reads either a dirty bitmap per memory slot or a per-vCPU dirty ring. The dirty ring scales better for huge VMs because QEMU does not have to scan the whole bitmap each round.

## 338: How do you migrate a VM between hosts with different CPU generations?

Use a common CPU model that both hosts support, instead of host-passthrough. In VMware this is EVC (Enhanced vMotion Compatibility), set per cluster. In libvirt you can compute it with `virsh hypervisor-cpu-baseline`. Features not in the model are hidden from the guest, so apps cannot start using an instruction that the target lacks.

## 339: What breaks if you live migrate a VM with host-passthrough to an older CPU?

The guest may have checked `CPUID` at boot and started using instructions like AVX-512. On a CPU without them, those instructions cause an illegal instruction fault, which crashes the app or the kernel. That is why libvirt refuses such migrations unless you force them, and why mixed clusters use a named CPU model.

## 340: How does storage live migration work in QEMU?

QEMU uses a block job, usually `blockdev-mirror`. It copies the whole disk to the target while tracking writes with a dirty bitmap, then copies the changed blocks again until both are in sync. At that point new writes go to both, and on switchover the VM uses only the target. libvirt's `--copy-storage-all` uses this with an NBD server on the target host.

## 341: How does QEMU live backup work with blockdev-backup?

QEMU can export a point-in-time view of a running disk using copy-before-write: before the guest overwrites a block, the old data is copied aside for the backup. Combined with persistent dirty bitmaps, a tool can read only blocks changed since the last backup, often through an NBD export. Proxmox Backup Server and libvirt's backup API use these features.

## 342: How do you design VM backups for a database server?

Use both layers. At the VM level, take application-consistent snapshot backups with quiescing (guest agent freeze hooks or VSS) for full-machine recovery. At the database level, run native backups and continuous log archiving (for example WAL archiving in PostgreSQL) for point-in-time recovery. VM backups alone usually cannot restore to an exact minute.

## 343: How do fsfreeze hooks work with the QEMU guest agent?

Before a snapshot, the agent runs `guest-fsfreeze-freeze`, which calls hook scripts (for example in `/etc/qemu/fsfreeze-hook.d/`) and then freezes file systems. Hooks can tell a database to flush and pause writes. After the snapshot, `guest-fsfreeze-thaw` unfreezes and runs the thaw hooks. Keep the freeze short, because all writes block while frozen.

## 344: What is the risk of freezing file systems inside a VM?

While frozen, every write blocks. If the snapshot takes too long, apps time out, and if the agent dies, the guest can stay frozen. Freezing the root file system can also block the agent's own logging. Use timeouts, make sure thaw always runs, and test it under load.

## 345: How does Ceph RBD handle VM snapshots and clones?

RBD images support fast snapshots, and a snapshot can be protected and used as the parent of copy-on-write clones. Proxmox and OpenStack use this to create VMs from images in seconds. Clones can later be flattened to remove the dependency. Many snapshots or deep clone chains can slow down operations, so they should be managed.

## 346: How do you size a Ceph cluster for VM workloads?

Plan for IOPS and latency, not just capacity. Use NVMe or SSD OSDs for VM disks, at least three nodes with 3x replication, a fast separate cluster network (25 GbE or more), and enough CPU and RAM per OSD (a few GB each). Leave room so the cluster can heal after a node failure without filling up, usually staying below about 70-80% full.

## 347: Why is write latency often the main limit for VM storage?

Many apps, like databases, wait for each sync write to finish. In a VM, the write goes through the guest, the virtual disk, the host storage stack, the network (for shared storage) and replication to other nodes. Every layer adds latency, so a disk that does many IOPS can still feel slow for single-threaded sync writes. Measure with `fio` at queue depth 1 with sync writes.

## 348: How do you benchmark VM disk performance with fio?

```bash
# Random 4K sync writes, queue depth 1 (database-like latency)
fio --name=lat --filename=/mnt/test --size=4G --direct=1 \
    --rw=randwrite --bs=4k --iodepth=1 --fsync=1 \
    --runtime=60 --time_based --group_reporting

# Random 4K reads, high queue depth (max IOPS)
fio --name=iops --filename=/mnt/test --size=4G --direct=1 \
    --rw=randread --bs=4k --iodepth=64 --ioengine=libaio \
    --runtime=60 --time_based --group_reporting
```

Use `--direct=1` to skip the guest page cache, and test long enough to get past caches on the storage.

## 349: How do you tune network performance for a KVM VM?

- Use virtio-net with vhost-net, or vhost-user/DPDK for very high packet rates
- Enable multi-queue (`queues=N` matching vCPUs) and set `ethtool -L eth0 combined N` in the guest
- Use jumbo frames on the storage or migration network if the whole path supports them
- Consider SR-IOV or vDPA for near-native speed
- Pin vhost threads and vCPUs on the same NUMA node as the NIC

## 350: What is multi-queue virtio-net and why does it help?

By default, a virtio-net device has one transmit and receive queue, so only one vCPU handles its traffic. Multi-queue creates several queue pairs, each handled by a different vCPU and vhost thread. This lets network throughput scale with vCPUs, which matters for busy web servers and proxies.

## 351: How does live migration work with SR-IOV devices?

The hypervisor cannot copy the state of a real NIC's virtual function, so plain SR-IOV blocks live migration. Common workarounds are: bond the VF with a virtio-net device in the guest (failover), unplug the VF before migration and plug a new one after, or use vDPA, which has virtio-compatible state. Some NICs and VFIO now support device state migration, but support is limited.

## 352: What is VFIO device migration?

Newer Linux kernels add a VFIO migration interface that lets a vendor driver save and restore the internal state of a passed-through device. QEMU can then live migrate VMs with these devices, for example some NVIDIA vGPUs and Mellanox NICs. It depends on vendor support, so check before you plan migration for passthrough VMs.

## 353: How does a vGPU work?

With mediated devices (mdev) or SR-IOV-based vGPUs, one physical GPU is split into several virtual GPUs, each with its own share of memory and time slices. The host vendor driver handles scheduling, and each guest runs the vendor's guest driver. It is used for VDI and AI inference. It usually needs vendor licensing, for example NVIDIA vGPU or AI Enterprise.

## 354: What are the trade-offs of GPU passthrough in production?

Pros: native speed and full driver features. Cons: one GPU per VM (unless using MIG or vGPU), no or limited live migration, host maintenance needs VM downtime, some consumer GPUs have reset bugs that need a host reboot, and you must handle IOMMU groups and driver binding. Clouds hide most of this behind instance types.

## 355: What is NVIDIA MIG and how does it relate to VMs?

Multi-Instance GPU (on A100, H100 and newer data center GPUs) splits one GPU into up to seven isolated instances with their own memory and compute slices. Each instance can be given to a VM (with vGPU software) or a container. It gives stronger isolation and more predictable performance than time-slicing.

## 356: How do confidential VMs work?

Confidential VMs encrypt the guest's memory with keys held by the CPU, so the hypervisor, host admins and other VMs cannot read it. The CPU also protects register state and checks memory mappings. Technologies are AMD SEV-SNP, Intel TDX and ARM CCA. Clouds offer them as confidential VM types.

## 357: What is the difference between AMD SEV, SEV-ES and SEV-SNP?

- SEV encrypts guest memory, but the hypervisor can still see register state and remap pages
- SEV-ES also encrypts CPU register state on exits
- SEV-SNP adds integrity protection with a reverse map table, so the hypervisor cannot remap, replay or corrupt guest memory, and adds stronger attestation

SNP is the version to use today.

## 358: What is Intel TDX?

Trust Domain Extensions run guests as "trust domains" isolated from the hypervisor. A CPU-signed module (the TDX module) manages the transitions, and memory is encrypted and integrity-protected. Like SEV-SNP, it supports remote attestation so the guest owner can verify what is running before giving it secrets.

## 359: What is remote attestation for confidential VMs?

The CPU produces a signed report with measurements of the guest's firmware, kernel and settings. A remote verifier checks the signature against the CPU vendor's keys and the measurements against known good values. Only if they match does a key service release secrets like disk encryption keys. Without attestation, encrypted memory gives much weaker guarantees.

## 360: What are the limits of confidential VMs?

They protect memory from the host, but the host still controls scheduling, so it can deny service. Side channels are an ongoing research area. I/O must go through shared, unencrypted buffers (bounce buffers), which costs performance, and device passthrough needs extra features like TDISP. You also must trust the CPU vendor and the guest's own software.

## 361: How do Spectre and Meltdown affect virtualization?

They are CPU side-channel attacks that use speculative execution to read memory that should not be accessible. In VMs, some variants could let a guest read hypervisor or other guests' memory. Fixes include microcode updates, kernel page table isolation, retpolines, IBRS/IBPB, and flushing buffers on VM entry and exit. These fixes cost performance, especially for I/O-heavy VMs.

## 362: What is L1TF and why did it lead to disabling SMT on some hosts?

L1 Terminal Fault (Foreshadow) let a guest read data from the L1 cache, including data from another guest running on the sibling hyper-thread of the same core. Flushing L1 on VM entry fixes the same-thread case, but not the sibling case. So some providers disabled SMT or used core scheduling so siblings only run vCPUs of the same VM.

## 363: What is core scheduling?

Core scheduling makes sure that two hyper-threads of one physical core only run tasks that trust each other, like vCPUs of the same VM. Otherwise the scheduler leaves a sibling idle. It lets hosts keep SMT on while reducing cross-VM side-channel risk. Linux, Hyper-V and ESXi all have forms of it.

## 364: Why do cloud vCPUs often equal hyper-threads, not cores?

On most x86 cloud instance types, one vCPU is one hyper-thread, so 2 vCPUs usually equal 1 physical core. Providers pin both threads of a core to the same VM to avoid cross-tenant side channels. That is why a 2-vCPU instance may not give the performance of 2 real cores. Graviton and some AMD types map one vCPU to one full core.

## 365: How do you check how vCPUs map to cores in an EC2 instance?

```bash
lscpu | grep -E 'Thread|Core|Socket'
```

You can also see it with `DescribeInstanceTypes` (`VCpuInfo.DefaultThreadsPerCore`). Some instance types let you set `CpuOptions` with `ThreadsPerCore: 1` to turn off hyper-threading, which helps some HPC workloads and per-core licenses.

## 366: What is the attack surface of a hypervisor, and how do newer VMMs shrink it?

The attack surface is everything a guest can talk to: device emulation, hypercalls, the instruction emulator and the VMM process. QEMU has a huge device model written in C. Newer VMMs like Firecracker, Cloud Hypervisor and crosvm are written in Rust, support only a few virtio devices, and run in jailed processes with seccomp filters, so there is much less code a guest can attack.

## 367: How does Firecracker isolate each microVM?

Each microVM runs in its own Firecracker process, started by a "jailer" that puts it in a chroot, its own namespaces and cgroups, drops privileges and applies a strict seccomp filter. The VMM only emulates a few devices (virtio-net, virtio-block, virtio-vsock, a serial port and a minimal keyboard controller for reset). So even if a guest escapes into the VMM, it lands in a very limited process.

## 368: How do you start a Firecracker microVM?

You start the process with an API socket and then configure it with HTTP calls:

```bash
firecracker --api-sock /tmp/fc.sock &

curl --unix-socket /tmp/fc.sock -X PUT http://localhost/boot-source \
  -d '{"kernel_image_path":"vmlinux","boot_args":"console=ttyS0 reboot=k panic=1"}'

curl --unix-socket /tmp/fc.sock -X PUT http://localhost/drives/rootfs \
  -d '{"drive_id":"rootfs","path_on_host":"rootfs.ext4","is_root_device":true,"is_read_only":false}'

curl --unix-socket /tmp/fc.sock -X PUT http://localhost/machine-config \
  -d '{"vcpu_count":2,"mem_size_mib":512}'

curl --unix-socket /tmp/fc.sock -X PUT http://localhost/actions \
  -d '{"action_type":"InstanceStart"}'
```

## 369: How can you control Firecracker from Node.js?

The API is HTTP over a Unix socket, so you can use `node:http` with `socketPath`:

```js
import http from "node:http";

function fc(path, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const req = http.request(
      {
        socketPath: "/tmp/fc.sock",
        path,
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Content-Length": Buffer.byteLength(data),
        },
      },
      (res) => {
        res.resume();
        res.statusCode < 300
          ? resolve()
          : reject(new Error(`${res.statusCode}`));
      },
    );
    req.on("error", reject);
    req.end(data);
  });
}

await fc("/machine-config", { vcpu_count: 1, mem_size_mib: 256 });
await fc("/actions", { action_type: "InstanceStart" });
```

## 370: How do microVM snapshots make serverless cold starts faster?

Firecracker can snapshot a running microVM's memory and device state to files. A new microVM can be restored from the snapshot, with memory mapped lazily from the file, so it skips the kernel boot and app startup. AWS Lambda SnapStart uses this idea. The catch is that restored VMs share the same random seeds and unique IDs, so apps must refresh them after restore.

## 371: Why is uniqueness a problem when restoring many VMs from one snapshot?

Every restored VM starts with the same memory, so things like random number generator state, UUIDs created at startup, cached tokens and TLS session keys would be the same. That can break security. Fixes include the VM Generation ID (vmgenid) device that tells the guest kernel to reseed, and runtime hooks (like SnapStart's) to regenerate values after restore.

## 372: What is gVisor and how does it compare to a microVM?

gVisor is a user-space kernel written in Go that intercepts a container's system calls and handles them itself, so the app does not talk to the host kernel directly. It is lighter than a VM and starts fast, but some syscalls are slower or unsupported. MicroVMs give stronger hardware-based isolation and full Linux compatibility but use more memory per instance.

## 373: How would you design a multi-tenant code execution service?

Run each tenant's code in its own microVM (Firecracker or Cloud Hypervisor) or at least gVisor, never only in a shared container or `node:vm`. Add strict CPU, memory, disk and time limits, no network or a filtered one, a read-only base image with a small writable overlay, a warm pool of pre-booted or snapshot-restored VMs for speed, and destroy the VM after each run or tenant.

## 374: What is Cloud Hypervisor?

Cloud Hypervisor is an open source Rust VMM, part of the Linux Foundation, built from rust-vmm crates. It targets modern cloud workloads: virtio devices, VFIO passthrough, hotplug, live migration and Windows guests, without legacy hardware. It sits between Firecracker (minimal) and QEMU (everything).

## 375: What is rust-vmm?

rust-vmm is a project that provides shared Rust crates for building VMMs: KVM bindings, virtio device code, memory management, a Linux loader and more. Firecracker, Cloud Hypervisor and crosvm use or share these components, so security fixes and features can be reused across projects.

## 376: How does nested virtualization work in hardware?

The outer hypervisor (L0) runs a guest hypervisor (L1) that wants to run its own guest (L2). L1's VMX instructions trap to L0, which builds a merged VMCS ("VMCS02") combining L1's settings with its own, and runs L2 directly on the CPU. Exits from L2 go to L0 first, which decides whether to handle them or reflect them to L1. Features like VMCS shadowing reduce the number of these traps.

## 377: Why is nested virtualization slow for I/O-heavy workloads?

Every L2 exit that L1 must handle needs at least two extra world switches through L0, and L1's own handling causes more exits. Nested page tables also stack. CPU-bound code runs close to normal speed, but I/O or frequent exits can be several times slower. Using paravirtual devices and passthrough at both levels helps.

## 378: How do you enable nested virtualization on KVM?

```bash
cat /sys/module/kvm_intel/parameters/nested   # Y or 1 means on
# to turn it on
echo "options kvm_intel nested=1" | sudo tee /etc/modprobe.d/kvm-nested.conf
sudo modprobe -r kvm_intel && sudo modprobe kvm_intel
```

Then give the L1 VM a CPU model with `vmx` (or `svm` on AMD), for example `host-passthrough`. On current kernels nested is enabled by default on both Intel and AMD.

## 379: How does Hyper-V's enlightenment interface help Windows guests on KVM?

Windows detects Hyper-V "enlightenments" through `CPUID` and uses paravirtual features like a reference TSC page, synthetic timers, a paravirtual APIC and relaxed timing checks. KVM can pretend to be Hyper-V for these (`hv_relaxed`, `hv_vapic`, `hv_spinlocks`, `hv_time`, `hv_stimer` and others in libvirt), which noticeably improves Windows guest performance and stability.

```xml
<features>
  <hyperv mode="passthrough"/>
</features>
```

Recent libvirt can turn on all supported ones with `mode="passthrough"`.

## 380: What is the Hyper-V root partition model?

When Hyper-V is enabled, the hypervisor boots first and the Windows OS becomes the root partition, a privileged VM with direct device access. Guest VMs (child partitions) use synthetic devices that send requests over the VMBus to Virtualization Service Providers in the root partition. So I/O for guests is handled by Windows drivers in the root.

## 381: What is VMBus?

VMBus is Hyper-V's channel-based communication bus between partitions. Synthetic devices use shared memory ring buffers and signals over VMBus, similar to virtio. Linux has built-in VMBus drivers (hv_netvsc, hv_storvsc and others), which is why Linux runs well on Hyper-V and Azure.

## 382: How does Virtualization-Based Security (VBS) use the hypervisor?

VBS uses Hyper-V to split Windows into virtual trust levels. Sensitive parts like credential storage (Credential Guard) and code integrity checks (HVCI or Memory Integrity) run in an isolated environment the normal kernel cannot read or change. Even if malware gets kernel access, it cannot steal those secrets easily. It also explains why other hypervisors on Windows must run on top of Hyper-V.

## 383: Why does enabling VBS or Hyper-V affect VMware Workstation and VirtualBox?

Only one hypervisor can own VT-x on the host. When Hyper-V is active, VMware Workstation and VirtualBox must use the Windows Hypervisor Platform API to run guests on top of Hyper-V. This works, but some features and performance may be lower than with direct VT-x access.

## 384: How do ESXi's scheduler and "co-scheduling" work?

ESXi schedules vCPUs as worlds on physical CPUs. For multi-vCPU VMs it uses "relaxed co-scheduling": it tracks how far vCPUs of the same VM drift apart and slows down the ones ahead, so the guest does not see one vCPU stalled for too long (which can trigger guest watchdogs or spinlock problems). Too many vCPUs per VM makes this harder and adds "co-stop" time.

## 385: What is co-stop in VMware?

Co-stop is the time a vCPU was stopped because the scheduler had to wait for other vCPUs of the same VM to catch up. High co-stop usually means the VM has more vCPUs than it needs or the host is overcommitted. Reducing vCPUs often makes such VMs faster.

## 386: How would you investigate a VM that is slow only at certain times of day?

Correlate time-series metrics from the guest and the host for those hours: CPU ready or steal, co-stop, memory ballooning and swapping, datastore latency, and network drops. Then look at what else runs then: backups, snapshot consolidation, antivirus scans, batch jobs in other VMs, or DRS moves. Often the cause is another workload on the same host or storage, not the VM itself.

## 387: How does memory overcommit go wrong, step by step?

As demand rises, the hypervisor first uses free memory, then page sharing, then ballooning (guests start swapping internally), then compression (on ESXi), and finally host-level swapping. Each step is slower. When host swapping starts, guest performance can drop by orders of magnitude. Linux hosts may even call the OOM killer and kill a QEMU process, which looks like a VM crash.

## 388: How do you protect important VMs from the host OOM killer on KVM?

- Do not overcommit memory on hosts with important VMs
- Reserve memory for the host itself
- Lower `oom_score_adj` for important QEMU processes (libvirt can do this)
- Put VMs in cgroups with memory limits so one VM cannot starve the host
- Use huge pages, which are reserved up front and not swapped
- Monitor host memory pressure (PSI) and alert early

## 389: What is Pressure Stall Information (PSI) and how is it useful for VM hosts?

PSI is a Linux kernel feature that shows how much time tasks are stalled waiting for CPU, memory or I/O (`/proc/pressure/cpu`, `memory`, `io`). On a VM host, rising memory or I/O pressure is an early warning of contention before VMs fail. Inside a guest, it tells you if the app is really waiting for resources.

## 390: What is free page reporting?

Free page reporting is a virtio-balloon feature where the guest tells the host which pages it has freed, so the host can reclaim them without the guest having to inflate a balloon. It helps hosts get memory back from idle VMs, especially with overcommit. It is supported in Linux guests and QEMU.

## 391: How does a hypervisor know how much memory a guest really uses?

It does not see inside the guest directly. It can estimate active memory by sampling pages (ESXi does this), read stats from the balloon driver or guest agent, or use free page reporting. Guest "used" memory also includes cache, which can be freed, so host and guest numbers often disagree.

## 392: What is memory tiering in virtualization?

Memory tiering places VM memory across faster and slower memory types, like DRAM and CXL-attached memory or NVMe-backed memory. The hypervisor moves hot pages to fast memory and cold pages to the slow tier. VMware vSphere and the Linux kernel both have tiering features, aimed at fitting more VMs per host for less cost.

## 393: What is CXL and how might it change virtualization?

Compute Express Link is a new interconnect that lets CPUs use memory and accelerators attached over PCIe with cache coherency. For VMs, it allows memory expansion and memory pooling between hosts, so a host can borrow memory instead of being stuck with what is in its DIMMs. Hypervisors are starting to treat CXL memory as a separate NUMA node or tier.

## 394: How do you plan capacity for a virtualization cluster?

Measure real usage, not allocations: CPU peaks, active memory, storage IOPS, latency and growth. Leave headroom for failures (N+1 or N+2 hosts), maintenance and bursts. Set target overcommit ratios per workload type, check vCPU-to-core and memory ratios, and model what happens if the largest host fails. Review it every few months.

## 395: What is N+1 in VM cluster design?

N+1 means the cluster can lose one host and still run all VMs. If you need 4 hosts' worth of resources, you run 5. VMware HA admission control enforces this by blocking VM power-ons that would break the reserve. Larger or critical clusters use N+2 so a failure during maintenance is still covered.

## 396: How does VMware HA detect host failures?

Hosts send network heartbeats to an elected primary. If a host stops responding, HA also checks datastore heartbeats to tell a dead host from a network-isolated one. If the host is dead, its VMs are restarted elsewhere. If it is only isolated, the host may run an "isolation response" (power off or shut down VMs) so they can restart on healthy hosts without split brain.

## 397: What is VM Component Protection (VMCP)?

VMCP in vSphere HA reacts when a host loses access to a datastore (All Paths Down or Permanent Device Loss). Instead of leaving VMs hung, HA can restart them on a host that still sees the storage. It needs settings that balance quick recovery against false alarms during short storage glitches.

## 398: What is VMware Fault Tolerance?

FT runs a live secondary copy of a VM on another host, kept in lockstep through fast checkpointing. If the primary host fails, the secondary takes over instantly with no data loss or reboot. It has limits on vCPUs and needs a fast dedicated network, so it is used for a small number of critical VMs that cannot be clustered at the app level.

## 399: What is COLO in QEMU?

COLO (COarse-grained LOck-stepping) is QEMU's fault tolerance approach. Primary and secondary VMs run at the same time and their network output is compared. While outputs match, nothing is synced. When they differ, a checkpoint syncs the secondary. It is less mature than VMware FT and rarely used in production.

## 400: Why is app-level high availability usually better than VM-level HA?

VM-level HA restarts a VM after a failure, which takes minutes and might bring back a corrupted state. App-level HA (database replicas, multiple stateless app servers behind a load balancer) keeps serving traffic during failures and can survive bugs in one instance or zone. VM HA is a good safety net, but you should not rely only on it for important services.

## 401: How do you design for zone failure with cloud VMs?

Run at least two VMs per tier across different Availability Zones behind a load balancer, use auto scaling groups that span zones, use managed or replicated databases with standby in another zone, and keep state out of single VMs. Test it by removing one zone from the group and checking that traffic keeps flowing.

## 402: What is the "cattle vs pets" idea for VMs?

Pets are servers you name, care for and fix by hand when they break. Cattle are identical, replaceable servers you destroy and recreate from an image when there is a problem. Modern VM setups try to make most servers cattle (auto scaling, immutable images) and keep only a few pets, like legacy databases, with extra care.

## 403: How do you do zero-downtime deployments with VMs?

Common patterns:

- Rolling: replace VMs in batches behind a load balancer, checking health each step
- Blue/green: build a new group of VMs with the new version, switch traffic, keep the old group for rollback
- Canary: send a small share of traffic to new VMs first

On AWS, auto scaling instance refresh and CodeDeploy support these patterns.

## 404: How do you trigger an AWS auto scaling instance refresh from Node.js?

```js
import {
  AutoScalingClient,
  StartInstanceRefreshCommand,
} from "@aws-sdk/client-auto-scaling";

const asg = new AutoScalingClient({ region: "us-east-1" });

const { InstanceRefreshId } = await asg.send(
  new StartInstanceRefreshCommand({
    AutoScalingGroupName: "web-asg",
    Strategy: "Rolling",
    Preferences: {
      MinHealthyPercentage: 90,
      InstanceWarmup: 120,
      AutoRollback: true,
    },
  }),
);

console.log(InstanceRefreshId);
```

It replaces instances so they use the latest launch template version, keeping at least 90% healthy.

## 405: How do you gracefully drain a VM before it is terminated in an auto scaling group?

Use lifecycle hooks. On a `Terminating` hook, the instance moves to a wait state, your code (through EventBridge or a script on the instance) stops taking new work, deregisters from the load balancer, finishes jobs and sends logs, then calls `CompleteLifecycleAction`. The load balancer's deregistration delay also lets open connections finish.

## 406: How should a Node.js app running on a VM handle shutdown signals?

When the VM shuts down, systemd sends SIGTERM to services. The app should stop accepting new connections, finish in-flight requests and close database pools before exiting:

```js
import http from "node:http";

const server = http.createServer((req, res) => res.end("ok"));
server.listen(3000);

process.on("SIGTERM", () => {
  server.close(() => process.exit(0));
  server.closeIdleConnections();
  setTimeout(() => process.exit(1), 25_000).unref();
});
```

Keep the timeout shorter than systemd's `TimeoutStopSec` and the load balancer's drain time.

## 407: What is the difference between VM-level and app-level scaling metrics?

VM-level metrics are CPU, memory and network. They are easy to get but lag behind real demand and do not show app limits like a thread pool or the event loop. App-level metrics like requests per second per instance, queue length or p95 latency are better signals. A common setup is target tracking on request count per target or queue backlog per instance.

## 408: How do you size Node.js processes on a multi-vCPU VM?

Node.js runs JavaScript on one main thread, so one process uses about one vCPU for JS work. On a 4-vCPU VM, run about 4 processes with the `cluster` module, PM2 or systemd templates, and leave some room for the OS and libuv threads. Also set `--max-old-space-size` so the processes together fit in RAM without swapping.

## 409: How does V8's memory limit relate to the VM's memory?

V8 sets a default heap limit based on available memory, but older Node.js versions did not always read container or VM limits correctly. If many Node processes each grow to their default limit, the VM runs out of RAM and the OOM killer steps in. Set `--max-old-space-size` explicitly per process based on the VM size and number of processes.

## 410: How does the JVM decide heap size on a VM vs in a container?

The JVM reads available physical memory and CPU count at startup. On a VM it sees the VM's RAM, and by default uses up to 25% as max heap. In containers, modern JVMs read cgroup limits (container support is on by default). Production setups usually set `-XX:MaxRAMPercentage` or `-Xmx` explicitly to control it.

## 411: What is JIT compilation in a process VM?

A JIT (just-in-time) compiler turns bytecode or JavaScript into machine code while the program runs, focusing on hot code. It uses runtime info like observed types to optimize, which a normal compiler cannot know. If assumptions turn out wrong, the code is "deoptimized" back to slower code. The JVM's C1/C2 and V8's Maglev and TurboFan are JIT compilers.

## 412: How does V8's tiered execution pipeline work?

V8 first parses JavaScript into bytecode for Ignition, its interpreter. Functions that run often are compiled by Sparkplug, a fast non-optimizing compiler, then by Maglev, a mid-tier optimizing compiler, and the hottest code by TurboFan. Type feedback collected while running guides the optimizations, and deoptimization falls back when types change.

## 413: What are hidden classes and inline caches in V8?

V8 gives objects hidden classes (maps) based on their shape, meaning which properties they have in what order. Inline caches remember the shape seen at each property access, so the next access with the same shape is very fast. Code where objects always have the same shape stays "monomorphic" and fast; many different shapes make it "megamorphic" and slow.

## 414: How does garbage collection work in V8?

V8 splits the heap into a young generation and an old generation. New objects go to the young generation, which is cleaned often with a fast "scavenger" that copies live objects. Objects that survive get promoted to the old generation, which is cleaned less often with mark-sweep-compact, mostly done concurrently and incrementally by the Orinoco collector to keep pauses short.

## 415: How is a stack-based VM different from a register-based VM?

In a stack-based VM, like the JVM and WebAssembly, instructions push and pop values on an operand stack, which gives small, simple bytecode. In a register-based VM, like V8's Ignition (which uses an accumulator plus registers) and Lua, instructions name virtual registers, which needs fewer instructions per operation. Both get JIT-compiled into real machine registers anyway.

## 416: How would you write a tiny stack-based VM in JavaScript?

```js
const OP = { PUSH: 0, ADD: 1, MUL: 2, PRINT: 3, HALT: 4 };

function run(code) {
  const stack = [];
  let pc = 0;
  while (true) {
    const op = code[pc++];
    switch (op) {
      case OP.PUSH:
        stack.push(code[pc++]);
        break;
      case OP.ADD:
        stack.push(stack.pop() + stack.pop());
        break;
      case OP.MUL:
        stack.push(stack.pop() * stack.pop());
        break;
      case OP.PRINT:
        console.log(stack[stack.length - 1]);
        break;
      case OP.HALT:
        return stack.pop();
      default:
        throw new Error(`bad opcode ${op} at ${pc - 1}`);
    }
  }
}

// (2 + 3) * 4
run([OP.PUSH, 2, OP.PUSH, 3, OP.ADD, OP.PUSH, 4, OP.MUL, OP.PRINT, OP.HALT]);
```

Real VMs add a program counter, call frames, a heap, type checks and a JIT, but the fetch-decode-execute loop is the same idea.

## 417: Is WebAssembly a virtual machine?

Yes. WebAssembly defines a stack-based virtual instruction set with a sandboxed linear memory, run by engines in browsers, Node.js, and standalone runtimes like Wasmtime and WasmEdge. It is a process VM: it has no OS or hardware, and only gets access to the outside through imported functions (or WASI). That makes it popular for safe plugins and edge computing.

## 418: How do you run WebAssembly in Node.js?

```js
import { readFile } from "node:fs/promises";

const bytes = await readFile("./add.wasm");
const { instance } = await WebAssembly.instantiate(bytes, {});
console.log(instance.exports.add(2, 3)); // 5
```

The module can only use memory and functions you pass in through the imports object, which is why Wasm is a good sandbox for untrusted plugins.

## 419: How do Wasm runtimes compare to microVMs for isolation?

Wasm isolates by software: the engine checks memory bounds and limits what code can call, inside one process. It starts in microseconds and uses little memory. MicroVMs isolate by hardware with a separate kernel, which is stronger but heavier. Engine bugs can break Wasm isolation, so high-risk platforms often add process or VM isolation on top.

## 420: What is a "unikernel"?

A unikernel compiles an app together with only the OS parts it needs into a single image that runs directly on a hypervisor, with no separate user space. It boots fast, is tiny and has a small attack surface. The downsides are harder debugging, limited tooling and less library support. Examples are Unikraft, MirageOS and Nanos.

## 421: How does the guest boot process work in QEMU with UEFI?

QEMU loads the OVMF firmware into flash, with a separate writable copy for UEFI variables per VM. OVMF initializes virtual hardware, reads boot entries from the variable store, loads the bootloader (shim then GRUB on Linux, or the Windows Boot Manager) from the EFI System Partition, which loads the kernel. Losing the per-VM variable file can lose boot entries, so it should be backed up with the VM.

## 422: What is direct kernel boot and when is it used?

QEMU, Firecracker and Cloud Hypervisor can load a kernel and initrd directly into memory and jump to it, skipping firmware and bootloader. It makes boot much faster and is used for microVMs, CI test VMs and kernel development. The downside is that the kernel lives outside the guest disk, so guest updates do not update it.

```bash
qemu-system-x86_64 -enable-kvm -m 1G -nographic \
  -kernel vmlinuz -initrd initrd.img \
  -append "console=ttyS0 root=/dev/vda" \
  -drive file=rootfs.qcow2,if=virtio
```

## 423: How do you reduce VM boot time?

- Use direct kernel boot or a minimal firmware
- Use a small kernel with only needed drivers built in
- Remove legacy devices and slow device probing
- Use a small rootfs and start only needed services
- Skip cloud-init stages you do not need
- Restore from a snapshot instead of booting
- Pre-warm a pool of VMs

MicroVM platforms combine these to get boot times well under a second.

## 424: What is the QMP protocol?

QMP (QEMU Machine Protocol) is a JSON-based control interface for a running QEMU process. Management tools use it to query status, hotplug devices, start migrations, run block jobs and take snapshots. libvirt uses it internally. You can connect directly for debugging:

```bash
virsh qemu-monitor-command web01 --pretty '{"execute":"query-block"}'
```

Changing things directly through QMP behind libvirt's back can confuse libvirt, so use it carefully.

## 425: How do you hotplug a disk into a running KVM VM?

```bash
qemu-img create -f qcow2 /var/lib/libvirt/images/web01-data.qcow2 100G
virsh attach-disk web01 /var/lib/libvirt/images/web01-data.qcow2 vdb \
  --driver qemu --subdriver qcow2 --targetbus virtio --persistent
```

The guest sees a new disk (`/dev/vdb`) right away. `--persistent` also adds it to the saved config so it stays after a reboot.

## 426: How do you securely expose a VM's console to users in a web app?

Do not expose the hypervisor's VNC or SPICE port directly. Put a proxy in between that authenticates the user, checks they own the VM, and creates a short-lived token for a single console session, like Proxmox's ticket system or OpenStack's novncproxy. Use TLS end to end and log console access, because console access often gives the same power as root.

## 427: How do you build a simple API in Node.js that controls libvirt VMs?

The simplest safe way is to call `virsh` with fixed arguments and strict input checks, never passing user input through a shell:

```js
import { execFile } from "node:child_process";
import { promisify } from "node:util";

const run = promisify(execFile);
const NAME = /^[a-z0-9-]{1,40}$/;

export async function vmAction(name, action) {
  if (!NAME.test(name)) throw new Error("invalid vm name");
  if (!["start", "shutdown", "reboot"].includes(action)) {
    throw new Error("invalid action");
  }
  const { stdout } = await run("virsh", ["-c", "qemu:///system", action, name]);
  return stdout.trim();
}
```

Also check that the caller owns the VM. For bigger projects, use the libvirt API directly or a platform API like Proxmox's REST API.

## 428: How do you call the Proxmox VE API from Node.js?

Use an API token with limited permissions:

```js
const host = "https://pve.example.internal:8006";
const token = process.env.PVE_TOKEN; // "user@pve!tokenid=uuid-secret"

const res = await fetch(`${host}/api2/json/nodes/pve1/qemu/120/status/start`, {
  method: "POST",
  headers: { Authorization: `PVEAPIToken=${token}` },
});
const { data } = await res.json(); // a task ID (UPID)
console.log(data);
```

The call returns a task ID; poll `/nodes/pve1/tasks/<upid>/status` to see when it finishes. Use a trusted CA for the Proxmox certificate instead of turning off TLS checks.

## 429: How would you design a self-service VM platform for internal developers?

- A portal or API where developers pick from approved templates and sizes
- Quotas and approval rules per team
- Automation (Terraform, Proxmox or vSphere API) behind the scenes, with all actions logged
- Mandatory tags: owner, project, expiry date
- Automatic expiry and cleanup of dev VMs
- Built-in monitoring, backups and patching
- Network segmentation per environment

This gives speed without uncontrolled VM sprawl.

## 430: How do you patch hundreds of VMs safely?

Group VMs by risk and role, patch a canary group first, then roll out in waves with health checks. Use a tool like Ansible, AWS Systems Manager Patch Manager or Azure Update Manager, take snapshots or backups just before patching, schedule maintenance windows per service, and track compliance reports. For immutable setups, build a new image and roll it out instead.

## 431: How do you patch hypervisor hosts without VM downtime?

Put one host in maintenance mode, which live migrates its VMs to other hosts (with DRS, Proxmox HA or Hyper-V cluster-aware updating). Patch and reboot it, check it is healthy, then bring it back and move to the next host. The cluster needs enough spare capacity (at least N+1) for this to work.

## 432: How do you handle VMs that cannot be live migrated during host maintenance?

VMs with passthrough devices, local storage or special pinning cannot move live. Options are: schedule a downtime window, use app-level failover to another VM first, cold migrate during a quiet time, or plan the design so these VMs are redundant at the app level. Document them so maintenance does not surprise anyone.

## 433: What are the trade-offs of local NVMe storage vs shared storage for VMs?

Local NVMe gives the lowest latency and highest IOPS, and it is cheap. But VMs on local disks cannot live migrate easily or restart on another host after a failure, so the app must handle replication itself, like a database cluster. Shared storage gives mobility and HA but adds latency and cost. Many designs use local storage for scale-out apps and shared storage for everything else.

## 434: What is the I/O blender effect?

When many VMs share the same storage, their separate, nicely sequential I/O streams get mixed into a random I/O pattern at the storage array. Storage that was sized for sequential throughput suddenly faces random I/O and slows down. SSD and NVMe arrays handle this much better than spinning disks, which is one reason flash became standard for virtualization.

## 435: How do you troubleshoot high storage latency in a VMware environment?

Look at the latency split: guest latency (GAVG) = kernel latency (KAVG) + device latency (DAVG). High DAVG means the storage array or fabric is slow. High KAVG means queuing in the ESXi kernel, often from queue depth limits or too many VMs on one datastore. Use `esxtop` to see these per device and per VM, then fix the right layer.

## 436: What is a common cause of slow Windows VMs on KVM, and how do you fix it?

Usually missing paravirtual pieces: emulated IDE disks and e1000 network instead of virtio, no Hyper-V enlightenments, the wrong CPU model, or no balloon or guest agent drivers. Install virtio-win drivers, switch disks to virtio-scsi and NICs to virtio-net, enable Hyper-V enlightenments and use a matching CPU model. The speedup is often large.

## 437: How would you debug a VM that randomly freezes for a few seconds?

Check for pauses at each layer: host CPU contention (steal or ready time), host swapping, storage latency spikes (look for "task blocked for more than 120 seconds" in guest logs), snapshot consolidation or backup freezes, NTP steps, live migrations at the same moments and guest garbage collection in apps. Compare timestamps across hypervisor events and guest logs to find what lines up.

## 438: How do you investigate a guest kernel crash in a VM?

Set up kdump inside the guest so a crash dump is saved, or use the hypervisor to dump guest memory (`virsh dump --memory-only web01 core.dump`). Look at the console log, which you can capture with a serial console to a file. Then analyze the dump with the `crash` tool and the matching kernel debug symbols.

## 439: How does the hypervisor protect itself from a guest flooding it with exits or I/O?

It uses scheduling and cgroups to limit the CPU, memory and I/O each VM process can use, and rate limits on emulated devices (like disk IOPS and bandwidth limits in QEMU or VMware's Storage I/O Control). Hypervisors also limit or ignore abusive requests. Firecracker includes per-device rate limiters for network and block devices.

## 440: How do you limit disk IOPS for a KVM VM?

```bash
virsh blkdeviotune web01 vda \
  --total-iops-sec 2000 --total-bytes-sec 104857600 --live --config
```

This sets a 2000 IOPS and 100 MB/s limit on disk `vda`, both now and in the saved config. Burst settings are also available, so short spikes are allowed while long abuse is stopped.

## 441: How does network QoS work for VMs?

You can shape traffic per vNIC with inbound and outbound bandwidth limits (libvirt `<bandwidth>`, VMware Network I/O Control, Hyper-V bandwidth management), or mark traffic with DSCP and prioritize it on switches. In the cloud, the instance type sets network bandwidth, often with a baseline and burst. Separating management, storage, migration and VM traffic is the first step.

## 442: How do overlay networks like VXLAN work for VMs across hosts?

VXLAN wraps the VM's Ethernet frame inside a UDP packet so it can travel over a routed IP network between hosts. Each tenant network gets a VNI (an ID up to about 16 million), so many tenants can use the same IP ranges. Hosts act as tunnel endpoints (VTEPs). It removes the 4094 VLAN limit and the need to stretch layer 2 across data centers. Remember the extra header reduces the usable MTU.

## 443: How do you handle MTU issues in VM networks?

Overlay protocols like VXLAN and Geneve add 50 or more bytes per packet. If the physical network MTU is 1500 and the VM also uses 1500, large packets get dropped or fragmented, and symptoms look like "small requests work, big ones hang". Fix it by raising the underlay MTU (often to 9000) or lowering the guest MTU (for example 1450), and make sure path MTU discovery is not blocked by firewalls.

## 444: How does a cloud provider implement VPC networking for VMs?

The VM's vNIC is backed by a virtual switch or a SmartNIC (like AWS Nitro cards) that enforces security groups, routes and NAT. Traffic between hosts is encapsulated with an overlay protocol that carries the VPC ID, and a central control plane programs every host with mappings of VM addresses to physical hosts. Guests never see the physical network.

## 445: What licensing traps should you watch for with VMs?

- Some software is licensed per physical core or socket of every host the VM could run on, so live migration across a cluster can increase cost
- Windows Server Datacenter vs Standard licenses differ in how many VMs they cover
- VMware licensing under Broadcom moved to per-core subscriptions with minimum core counts
- Cloud "license included" vs "bring your own license" rules differ by provider
- Oracle databases on VMware are a famous case of disputed licensing

Always check vendor rules before designing clusters.

## 446: How would you plan a migration away from VMware vSphere?

1. Inventory all VMs, dependencies, licenses and special features in use (FT, NSX, vSAN, DRS rules)
2. Pick the target: Proxmox, Hyper-V, Nutanix AHV, OpenShift Virtualization or cloud
3. Build a pilot cluster and test backup, monitoring, networking and HA
4. Convert a few low-risk VMs, check drivers, performance and boot modes
5. Migrate in waves with rollback plans and short downtime windows
6. Update automation (Terraform, Ansible) and runbooks
7. Train the team, then decommission old hosts

## 447: How do you evaluate whether a workload should stay on VMs or move to containers?

Check how the app is built and run: does it keep state on local disk, need a specific kernel or OS, depend on manual setup or use licenses tied to hardware? Stateless 12-factor apps with automated builds move easily. Monoliths with heavy local state, Windows-only dependencies or long startup often stay on VMs, maybe managed better with images and automation. Consider the team's skills and the cost of change too.

## 448: How would you design a CI system that runs untrusted pull request builds in VMs?

Run each job in a fresh, short-lived VM (or microVM) created from a known image and destroyed after the job. Do not give secrets to untrusted PR jobs. Use separate network segments with egress rules, limit CPU, RAM, disk and job time, keep a warm pool of VMs for speed, and never reuse a VM between jobs, because a malicious build could leave a backdoor. GitHub-hosted runners work this way.

## 449: Your company runs 2,000 VMs and the cloud bill is too high. What do you do?

1. Tag and attribute every VM to an owner and service
2. Find idle or forgotten VMs (low CPU and network for weeks) and shut them down after checking with owners
3. Right-size over-provisioned VMs using real metrics
4. Move to newer generations or ARM instances where possible
5. Schedule non-prod VMs to stop outside working hours
6. Use spot for batch and CI, and savings plans for the steady base
7. Clean up orphaned disks, snapshots and IPs
8. Set budgets and alerts so the problem does not come back

## 450: How do you explain the full path of a disk write from an app in a KVM guest to the physical disk?

1. The app calls `write()`; the guest kernel puts data in its page cache
2. On flush or `fsync`, the guest file system sends a block request to the virtio-blk or virtio-scsi driver
3. The driver adds descriptors to the virtqueue and kicks the device (an ioeventfd, so KVM signals QEMU's I/O thread without a full exit to QEMU's main loop)
4. QEMU's block layer processes the request through the format driver (qcow2 or raw) and any throttling or backups
5. QEMU issues the I/O to the host with io_uring or native AIO, often with O_DIRECT (`cache=none`)
6. The host kernel sends it to the device driver, or over the network for Ceph, iSCSI or NFS
7. When the device confirms, QEMU puts a completion in the used ring and injects an interrupt (through irqfd)
8. The guest driver completes the request, and `fsync` returns to the app

Each step is a place where latency can be added, which is why storage tuning in VMs looks at every layer.
