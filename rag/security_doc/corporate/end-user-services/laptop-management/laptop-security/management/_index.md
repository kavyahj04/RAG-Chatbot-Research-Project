---
title: Laptop Remote Management and Monitoring
---

## Overview

GitLab has a large and ever growing fleet of laptops (a.k.a. endpoints) that Corporate Security is responsible for maintaining.

We use endpoint management and fleet intelligence tools to help us meet our Zero Trust security policies and compliance needs.

## Mobile Device Management (MDM)

The term "mobile device" is deceiving and actually refers to any "user" device including desktops, laptops, or phones that are enrolled and tracked. This is used for sending a configuration inventory export to the server with details about the hardware specifications, current versions, and a list of applications installed with the current version.

We use this data for asset management and to retroactively review that all machines are using up-to-date versions and configurations meet our compliance policy requirements.

We have the ability to push and automatically install software packages, and most importantly, the ability to remotely [wipe your laptop](/handbook/security/corporate/end-user-services/laptop-management/laptop-wipe/) if needed.

All GitLab purchased laptops are enrolled in MDM during [onboarding](/handbook/security/corporate/end-user-services/onboarding101/) or a laptop [refresh](/handbook/security/corporate/end-user-services/laptop-management/laptop-ordering/#laptop-refreshes).

All GitLab laptops must be [wiped](/handbook/security/corporate/end-user-services/laptop-management/laptop-wipe) in the event they are lost or compromised during a security incident, and before they are [donated](/handbook/security/corporate/end-user-services/laptop-management/laptop-offboarding-returns/#laptop-donations), [returned](/handbook/security/corporate/end-user-services/laptop-management/laptop-offboarding-returns/#laptop-returns), or replaced due to a [repair](/handbook/security/corporate/end-user-services/laptop-management/laptop-repairs/) or [refresh](/handbook/security/corporate/end-user-services/laptop-management/laptop-ordering/#laptop-refreshes) with or without a [buyback](/handbook/security/corporate/end-user-services/laptop-management/laptop-offboarding-returns/#laptop-buybacks).

Your personal laptop should not be enrolled in MDM, and cannot be used for accessing GitLab accounts or business data. If you have a (rare) use case for a second laptop, see the [laptop procurement](/handbook/security/corporate/end-user-services/laptop-management/laptop-ordering) page.

## Endpoint Detection and Response (EDR)

As a vendor platform, SentinelOne is monitoring real-time activity, and is similar in concept to the old days of antivirus and malware software that you used in the past, however it is built for modern day threats and is centrally monitored by Corporate Security and the Security Incident Response Team to allow us to respond to alerts of potential compromise.

This is only used for retroactive security investigations and we do not proactively monitor for your activity. In other words, it's not a "big brother" monitoring approach, it's for having as much forensic breadcrumb trail data as possible in the event that your computer is breached or for a legal hold matter. We have exemption policies in place for countries with stringent personal privacy laws.

* [SentinelOne Handbook Page](/handbook/security/corporate/systems/sentinelone)
* [Personal Privacy Audit Demo Slides](https://docs.google.com/presentation/d/1C2ufNXF28l0KTd5PPTkq1TjUWeWPI44VfwYbsvOzkns/edit)

## Legal Holds and Investigations

If the team member is under an active Legal Hold or possesses material related to an active Company investigation, they must comply with the notice requirements. Failure to comply with an active Legal Hold may expose the team member or the Company to adverse consequences, including civil or criminal penalties and sanctions. Their obligation to follow the procedures outlined in the notice continues until the hold is lifted, even if they depart the Company. If the team member departs the Company, all Company devices and any material they're holding in accordance with any active Legal Hold Notice or active Company investigation should be turned over upon their departure.

## Exceptions

Exceptions to this procedure will be tracked as per the [Information Security Policy Exception Management Process](/handbook/security/).
