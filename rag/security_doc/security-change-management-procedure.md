---
title: "Security Change Management Procedure"
description: "Change management procedure for the Security Division."
---

## Purpose

The purpose of this document is to outline the procedural change management steps as they relate to the Security Division.

## Scope

This document applies to systems and applications owned by Security and processes owned by Security Departments.

{{% note %}}
Changes related to user access and authorization should continue to be handled via the [access request](/handbook/security/corporate/end-user-services/onboarding-access-requests/access-requests/) process.
{{% /note %}}

Security has defined the following types of changes:

### Minor change

A minor change is a non-material change which occurs through the natural course of business, such as handbook updates. Minor changes may be implemented directly in Production, have no financial impact, are related to general maintenance, and can be easily reversed.

A minor change **does not** require a change management issue and can be handled internally within the relevant team. Security's least privilege access controls support the checks and balances required for managing minor changes.

### Standard change

A standard change is a change that is low risk, relatively common and follows a specified procedure or work instruction, such as a configuration change, security patches, or other types of normal application modifications.

Standard changes have to go through the change management process. They require a **peer review**, **Impacted Team(s) Management (or Code Owner) approval**, and **post-implementation review**.

{{% note %}}
Manager - prior to approving the change request, please ensure that the correct change request template is being used.
{{% /note %}}

### Comprehensive change

A comprehensive change is high risk, high impact, or has a more complex procedure, such as a system or application deprecation, a new system or application onboarding, or net-new Production architecture.

- Infrastructure changes are considered comprehensive changes. They require **peer review**, **Impacted Team(s) Management (or Code Owner) approval**, **Technical Owner Approval**, and **Post-Implementation Review**.

{{% note %}}
Manager - prior to approving the change request, please ensure that the correct change request template is being used.
{{% /note %}}

### Emergency change

An emergency change follows the same approval process as [comprehensive](#comprehensive-change) changes.

- It can be entered for approval after the change has been implemented in production.
- Emergency changes are intended to be used only where there is an **immediate critical** need to correct an operational or security issue that is preventing users from working or critical processes from operating.
- Emergency changes require review and **all approvals** after the change has been implemented.

## Roles & Responsibilities

| Role | Responsibility |
| ------ | ------ |
| **[Security Governance](security-assurance/governance/)** | Maintain a security change management procedure to intake and respond to change management activities |
| | Maintain Metrics |
| **[Security Compliance](security-assurance/security-compliance/)** | Provide oversight to ensure changes are being made in accordance with compliance obligations |
| **Requestor** | Complete the change management issue |
| | Work with the Technical Owner to document, test, and obtain approval(s) for the change |
| **Technical Owner** | As defined in the [tech stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml). Review and provide approval prior to the change being implemented |
| | Work with the Requestor to ensure the requested change is documented, tested, and approval(s) have been completed |
| | Ensure Peer Review is completed prior to providing Technical Owner Approval |
| | Document and report any risks or trends identified during change management activities |
| **Peer Review** | Review and ensure the requested change has been documented and there are no undocumented downstream impacts |
| **Post Implementation Review** | Review of the change in production after the change is made to ensure everything is working as expected |

### Approval Matrix

| **Approval Type** | **Description** | **[Minor](#minor-change)** | **[Standard](#standard-change)** | **[Comprehensive](#comprehensive-change)** | **[Emergency](#emergency-change)** |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Peer Review** |    Peer Reviews are performed by a peer of the change Requestor and are intended to identify any potential issues with the planned change or change process. **Note:** The peer review process was established to mitigate the risk of the lack of segregation of duties between Requestor and implementer. The review provides comfort that changes to the production environment are valid. | No | Yes | Yes | Yes |
| **Post-Implementation Review** | Performed by a peer of the change Requestor and is intended to ensure the change is working as expected after the change has been implemented in Production. | No | Yes | Yes | Yes |
| **Impacted Team(s) Management/Code Owner approval** | Approval by Management that is responsible for the particular system or application    | No |    Yes |    Yes |    Yes |
| **Technical Owner Approval** | Approval by the system or application's Technical Owner as defined in the [tech stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml). | No |    No | Yes | Yes |

{{% note %}}
Technical Owner approval is dependent upon the system or application already existing in the tech stack. For new systems or applications that have not yet been assigned a Technical Owner in the tech stack, reach out to the [Security Risk Team](/handbook/security/security-assurance/security-risk/).
{{% /note %}}

## Procedure

To submit a security change request, use one of the links below to create a change request issue:

[Standard Change Request](https://gitlab.com/gitlab-com/gl-security/security-change-management/-/issues/new?issuable_template=standard_change_template)

[Comprehensive Change Request](https://gitlab.com/gitlab-com/gl-security/security-change-management/-/issues/new?issuable_template=comprehensive_change_template)

[Emergency Change Request](https://gitlab.com/gitlab-com/gl-security/security-change-management/-/issues/new?issuable_template=emergency_change_template)

[CorpSec Change Request](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?description_template=corpsec_normal_change)

Follow the instructions in the appropriate issue template to:

- Add the appropriate level of detail to the request
- Assign the appropriate team member(s) to the request in accordance with the [roles and responsibilities](/handbook/security/security-change-management-procedure/#roles--responsibilities) and [approval matrix](/handbook/security/security-change-management-procedure/#approval-matrix) sections

[Security Change Management project](https://gitlab.com/gitlab-com/gl-security/security-change-management)

[CorpSec Change Issues](https://gitlab.com/groups/gitlab-com/gl-security/corp/-/issues/?sort=created_date&state=opened&label_name%5B%5D=corpsec-metric%3A%3Achange&first_page_size=100)

### Communication

If a security change request will impact **all GitLab team members**, please ensure that you communicate the change and its impact by posting in `#whats-happening-at-gitlab` or `#company-fyi-private` if the change is subject to SAFE or considered highly sensitive, before the work begins and after the change is completed.

**Be sure to communicate the change, its rationale, and its impact.**

If a security change request will impact **all Security Division team members**, please ensure that you communicate the change and its impact by posting in `#security-team-only` before the work begins and after the change is completed.

**Be sure to communicate the change, its rationale, and its impact.**

If a security change request will impact **a particular Security Department or individual team members**, please ensure that you communicate the change and its impact in a manner appropriate for those impacted team members.

## CorpSec - Rollout of Mass Deployments

Where possible, mass deployments such as macOS operating system upgrades (i.e. Monterey to Ventura) or net new software rollouts will be done by Divisions. Smaller changes such as security patches or minor updates of existing software are not subject to the same schedule and can be deployed globally after Phase 1 testing is complete. The order of mass deployments will be as follows:

Phase 1: Alpha Testers

Phase 2: Beta Testers

We welcome volunteers to join our Beta Testers group! Please join the #corpsec-beta-testers channel on Slack. The list of Beta Testers is automatically updated daily via script using the list of Team Members in that channel. If you only want to join the #corpsec-beta-testers channel but you do not want to be a part of the testing, please express your intention to opt-out of the testing at any time by stating as much in the channel and tagging a member of IT, or by leaving the channel entirely.

Beta Testers are agreeing to participate in the testing of applications that may not be approved for country-wide implementation in certain jurisdictions. If you are in such a jurisdiction, your participation will be limited to Beta Testing and upon completion of the testing, access and use of the application will be revoked until GitLab receives approval for country-wide implementation of the application.

Phase 3: Security

Phase 4: Legal

Phase 5: Marketing, People Group, & CEO Division

Phase 6: Engineering & Product

Phase 7: Sales & Finance

Phase 8: VIPs

VIP support for significant or disruptive changes will be treated via direct support from the Service Desk team who will schedule a call at a convenient time to ensure the update or deployment is successful with minimal disruption.

## Exceptions

Exceptions to this procedure will be tracked as per the [Information Security Policy Exception Management Process](/handbook/security/controlled-document-procedure/#exceptions).

## References

- [Change Management Policy](/handbook/security/security-and-technology-policies/change-management-policy/)
- [Controlled Documents Procedure](/handbook/security/controlled-document-procedure/)
- [Controlled Documents Annual Review Program](/handbook/security/controlled-document-procedure/#review)
