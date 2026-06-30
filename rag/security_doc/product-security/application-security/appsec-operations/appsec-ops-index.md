---
title: "Application Security Operations"
description: Application Security Team Operations home page
---
<!-- markdownlint-disable MD052 -->
Last updated: May 27, 2025

The [**Application Security Subdepartment**](../../application-security/) is made up of two teams, the [**Secure Development and Design Team**](sdd-services.md) and the [**Product Security Incident Response Team (PSIRT)**](psirt-services.md). These two teams work together to anticipate and prevent the introduction of vulnerabilities during design and development, as well as identify, assess, and respond to security vulnerabilities discovered in GitLab products and services.

## Helpful Quicklinks for GitLab Engineers

- [**Application Security Reviews**](../appsec-reviews.md)
- [**Application Security Stable Counterparts**](../stable-counterparts.md)
- [**Threat modeling**](../threat-modeling/_index.md)
- **Backlog reviews:** When necessary a backlog review can be initiated, please see the [Vulnerability Management Page](../vulnerability-management.md) for more details.
- [**GitLab AppSec Inventory**](../inventory.md)
- [**Responding to customers security scanners review requests**](../responding-customers-scan-review-requests.md)
- [**Root Cause Analysis for Critical Vulnerabilities**](../../../root-cause-analysis.md)

Learn how to identify or remediate security issues using real examples with GitLab's [Reproducible Vulnerabilities](../reproducible-vulnerabilities.md).

Learn how GitLab is implementing [Reproducible Builds](../reproducible-builds.md) for our build processes.

Learn more about the automation initiatives that the Application Security team uses on the [Application Security Automation and Monitoring page](../application-security-automation-monitoring.md)

### GitLab Secure Tools coverage

As part of our [dogfooding effort](/handbook/product/product-processes/dogfooding-for-r-d/), [Secure Tools](https://docs.gitlab.com/ee/user/application_security/) are set up on many different GitLab projects (see our [policies](../inventory.md#policies). This list is too dynamic to be included in this page, and is now maintained in the [GitLab AppSec Inventory](/handbook/product/ux/navigation/inventory/).

Projects without the expected configurations can be found in the [inventory violations list](https://gitlab.com/gitlab-com/gl-security/product-security/inventory/-/issues) (internal link).

## Useful resources for AppSec engineers

[**Application Security Engineer Runbooks**](../runbooks/)

[**Application Security Engineer Job Families**](../../../../../../content/job-families/security/application-security.md)

### PTO

Team members that are taking PTO for 5 days or more must both discuss time off with their manager prior to scheduling to ensure visibility and adequate team operational coverage **and** [create a PTO coverage issue](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/appsec-team/-/issues/new?issuable_template=pto_coverage) to organize their coverage during their time off. The PTO coverage issue should :

- List any potential requests that could come to the team while on PTO
- The team member taking PTO should organize their work accordingly and ensure the PTO coverage issue contains the context required to handle the work
- Assign primary and secondary responsible team members

AppSec team members should add any important information related to the work they are covering for the person on PTO and AppSec manager(s) should add any important announcement to see upon their return.

### Team Bookmarks

- [The AppSec private group that contains other private subgroups and projects](https://gitlab.com/gitlab-com/gl-security/product-security/appsec)
- [The `appsec-lab` group on Staging. This has an Ultimate license.](https://staging.gitlab.com/appsec-lab)
- [Bug bounty council search](https://gitlab.com/gitlab-com/gl-security/engineering/-/issues?label_name%5B%5D=Bug+Bounty+Council)
- [Upcoming patch release](https://gitlab.com/gitlab-org/gitlab/-/issues?sort=created_date&state=opened&label_name%5B%5D=upcoming+security+release)
- [GitLab Project Security dashboard](https://gitlab.com/gitlab-org/gitlab/-/security/dashboard/?project_id=278964&scope=dismissed&page=1&days=90)
- [Security issue board that tracks ongoing issues (HackerOne and others)](https://gitlab.com/groups/gitlab-org/-/boards/1216545?label_name[]=security)
- [The latest releases](https://gitlab.com/gitlab-org/gitlab/-/tags)
- [Overview of a project member permissions](https://gitlab.com/help/user/permissions)
- [The DevOps stages and their different groups](/handbook/product/categories/). This page contains information on the development teams, their areas of focus, and their team members as well as the AppSec stable counterparts. It is used to assign issues to the stable counterparts.
- [The product features listed by groups that own them](/handbook/product/categories/features/)
- [List of merged security issues in `gitlab-org`](https://gitlab.com/groups/gitlab-org/-/merge_requests?scope=all&state=merged&label_name[]=security&milestone_title=%23upcoming). **Note:** It can include results from the security mirror `gitlab-org/security/`.
- Application Security KPIs & Other Metrics - [Embedded KPIs which can be filtered by section, stage, or group](https://10az.online.tableau.com/#/site/gitlab/views/appsectest2rawdata/AppSec-ApplicationandContainerVulnerabilityDashboard?:iid=4).
- Milestone Planning - The GitLab Application Security team plans work based around Milestones, see [this page for a description of that process](/handbook/security/product-security/application-security/milestone-planning/)

The list above is not exhaustive and is subject to be modified as our processes keep evolving.

## Meeting Recordings

The following recordings are available internally only:

- [AppSec Sync](https://drive.google.com/drive/folders/1sxnBhPNDofWg5JmKqrhEl5y4_aWldTbt)
- [AppSec Leadership Weekly](https://drive.google.com/drive/folders/1jyNYP2AOqoOPqr4qGMuh7PGha_j-7brb)

## Content Review and Updates

This page will be reviewed quarterly to ensure alignment with company and divisional priorities, the GitLab Security product roadmap, and relevant business and operational changes. Updates may occur more frequently as business operations evolve.

*Next scheduled review: June 30, 2025*
