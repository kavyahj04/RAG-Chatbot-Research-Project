---
title: "GitLab Laptop Management"
---

## Introduction

The EUS team oversees all laptop procurement and management. While certain aspects, such as endpoint management configurations, are supported by other parts of the CorpSec team, we generally act as the point of contact for all related issues.

At GitLab, we use centralized laptop management for company issued devices. If you are in possession of a company issued device, the details below apply to you. However, not all endpoint management technologies GitLab deploys will be required for all devices. Some technologies may be specific to the hardware platform or operating system.

## Laptop Specs

GitLab approves and supports the use of Linux and macOS for team member laptops. To keep GitLab IT Support efficient, Windows is not supported as a laptop OS.

Further information on GitLab authorized operating systems, versions, and exception process is available on the [Approved Operating Systems for GitLab Team Member Endpoint Systems](https://internal.gitlab.com/handbook/security/corporate/operating-systems/) page.

The operating system choices have affected the hardware selection process.

Apple hardware is the recommended choice for GitLab team members. Team members may select a Dell Linux laptop if they are familiar with Linux and are capable of self-support.

### Apple Hardware

We pre-order laptops through our global vendors to ensure quick delivery and a consistent experience for all team members.

**Laptop configurations vary by regional inventory availability.** For example, some regions may have 2024 models in Space Gray while others have 2025 models in Silver. We prioritize providing the most current hardware available for all orders.

Our standard laptop offerings include:

* MacBook Pro 14-inch - 16GB Unified memory / 512GB storage **Standard model**
* MacBook Pro 16-inch - 36GB Unified memory / 1TB storage **Performance model**
* MacBook Pro 14-inch - 36GB Unified memory / 1TB storage **Performance model**

Most roles that require higher performance machines are approved for a 14" or 16" MacBook Pro performance model. Please see this [spreadsheet](https://docs.google.com/spreadsheets/d/1OuC0_iliCzASKfOhDLWO4fBmDS-uL3VGRMI6063R6tk/edit?usp=sharing) (public) to locate your department group and determine which machine you are eligible for.

### Linux Hardware

{{% alert color="warning" %}}
IT strongly encourages team members to select Macs; please only request a Linux laptop if you are experienced in Linux and capable of self-support.
{{% /alert %}}

We have standardized on the [Dell Precision 5690](https://www.dell.com/en-us/shop/dell-computer-laptops/new-precision-5690-workstation/spd/precision-16-5690-laptop/s004p5690usvp) Mobile Workstation laptop. Due to supply constraints, specific models available from these lines may vary.

Dell does not currently sell laptops pre-installed with Linux in some countries; team members will need to install Linux themselves in those cases.

**NOTE: The maximum price of Linux laptops is not to exceed **the price of the equivalent [16" MacBook Pro laptop](#apple-hardware)**.

Our **only approved Linux laptop vendor is Dell**. These laptops generally come pre-loaded with Ubuntu Linux in order to save money on unused Windows licenses.

Dell is GitLab's exclusive Linux vendor for the following reasons:

* Dell has the longest history of shipping laptops with Linux pre-installed among major manufacturers.
* Dell is able to ship laptops to most countries in which GitLab team members live.
* As we move forward with Zero Trust networking solutions, we need to have a stable and unified platform for deployment of software components in the GitLab environment.
    Standardization on a single platform for Linux simplifies this.
* The current Ubuntu LTS is the preferred Linux platform; Ubuntu LTS has a record of stability and quick patching.
* Purchasing laptops from a single vendor opens the possibility of corporate discounts.
* [Dell is a certified Ubuntu vendor](https://certification.ubuntu.com/desktop/models?query=&category=Desktop&category=Laptop&level=&release=18.04+LTS&vendors=Dell) with multiple laptop choices available. They even have their own Ubuntu OEM release of Ubuntu they maintain, and as a result of their effort, the standard Ubuntu Linux 20.04 LTS image natively supports Dell hardware and even firmware updates.
* To date, all of Dell's major security issues have not been related to their hardware.

### Windows for Customer Support and Product Development

Windows cannot be used to access GitLab Corporate services (e.g. Slack, G-Suite, GitLab.com); Windows OS can only be used in addition to a GitLab managed device. We understand specific roles will need to use Windows to ensure platform and ecosystem support for GitLab customers and partners who develop for the Microsoft Ecosystem.

The usage of virtualized Windows is highly preferred and should satisfy most support and development need. Complete details about Windows usage is available on the internal [Approved Operating Systems for GitLab Team Member Endpoint Systems](https://internal.gitlab.com/handbook/security/corporate/operating-systems/#windows-for-customer-support-and-product-development) page.

## Laptop Management Policies

In addition to specific hardware requirements, we also employ various policies and software solutions to ensure that all GitLab devices remain secure.

### Endpoint Management

#### Jamf

[Jamf](https://www.jamf.com/) allows us to remotely manage all of our Macs to perform tasks such as pushing updates, encrypting devices, remotely locking and wiping laptops, etc. All new Macs purchased and shipped by GitLab vendors are automatically enrolled in Jamf. It may be necessary to manually enroll a laptop if it was self-procured. GitLab Corporate services should not be accessed from a Mac that is not enrolled in Jamf.

#### Fleet

[Fleet](https://fleetdm.com/) is an Open-Source remote management system that is required to be installed on all Dell devices in order to be able to access GitLab Corporate services. Similar to Jamf, it allows us to remotely manage enrolled laptops to ensure security compliance, and perform tasks such as remotely locking and wiping machines.

### Backblaze

[Backblaze](https://www.backblaze.com/) is a tool that might be deployed to backup data on your company owned device in the event of a security or legal hold/investigation and only following a request of the Legal and People Ops teams, subject to local data, privacy and employment laws.

### Apple IDs

Laptops should be configured with security in mind.

We require the use of an @gitlab.com Apple ID that is separate from any personal Apple IDs you may have. Some of these reasons include:

* Backups, keychains and documents are all considered sensitive information, and should not be stored in personal services.
* 2FA for remote lock, wipe, or account resets are common methods of account compromises, and ensuring the use of GitLab.com email addresses also ensures we are in control of that aspect of multi-factor authentication.
* Keeping a strong separation between work and personal accounts will help prevent the accidental leak of information from one to the other, in either direction.

Defense in depth, in part, means you make a best effort to be secure at each layer. To read through more instructions, please refer to [security best practices](/handbook/security/corporate/end-user-services/laptop-management/laptop-security/) when configuring your new laptop.
