---
title: "Secure Design & Development Team Services Overview"
description: Secure Design & Development Team Services Overview
---
<!-- markdownlint-disable MD052 -->
Last updated: May 27, 2025

## Secure Design & Development Team Services Overview

The Secure Design & Development Team works with GitLab engineers and product teams to *anticipate and prevent* the introduction of vulnerabilities during design and development.

Our responsibility includes four of the five Secure Developer Experience (SDX) pillars. SDX is a developer UX centered approach to traditional DevSecOps practices.

- **SDX: Learn**: security training, governance, policy, documentation, and standards.
- **SDX: Design**: [threat modeling](/handbook/security/product-security/application-security/threat-modeling/_index.md), feature design guidance and consultation, and [design reviews](/handbook/security/product-security/application-security/appsec-reviews.md).
- **SDX: Code**: static analysis, software component analysis and supply chain security, use of approved tools and methodologies in development, deprecation of unsafe functions, etc.
- **SDX: Verify**: dynamic analysis testing, penetration testing, remediation of critical vulnerabilities, and [final security reviews](/handbook/security/product-security/application-security/appsec-reviews.md) prior to release.

## Helpful Quicklinks

- [**Application Security Reviews**](../appsec-reviews.md)
- [**Application Security Stable Counterparts**](../stable-counterparts.md)
- [**Threat modeling**](../threat-modeling/_index.md)
- **Backlog reviews:** When necessary a backlog review can be initiated, please see the [Vulnerability Management Page](../vulnerability-management.md) for more details.
- [**GitLab AppSec Inventory**](../inventory.md)
- [**Responding to customers security scanners review requests**](../responding-customers-scan-review-requests.md)
- [**Root Cause Analysis for Critical Vulnerabilities**](../../../root-cause-analysis.md)

Learn how to identify or remediate security issues using real examples with GitLab's [Reproducible Vulnerabilities](/handbook/security/product-security/application-security/reproducible-vulnerabilities/).

Learn how GitLab is implementing [Reproducible Builds](/handbook/security/product-security/application-security/reproducible-builds/) for our build processes.

Learn more about the automation initiatives that the Application Security team uses on the [Application Security Automation and Monitoring page](/handbook/security/product-security/application-security/application-security-automation-monitoring/)

### GitLab Secure Tools coverage

As part of our [dogfooding effort](/handbook/product/product-processes/dogfooding-for-r-d/), [Secure Tools](https://docs.gitlab.com/ee/user/application_security/) are set up on many different GitLab projects (see our [policies](/handbook/security/product-security/application-security/inventory/#policies)). This list is too dynamic to be included in this page, and is now maintained in the [GitLab AppSec Inventory](/handbook/product/ux/navigation/inventory/).

Projects without the expected configurations can be found in the [inventory violations list](https://gitlab.com/gitlab-com/gl-security/product-security/inventory/-/issues) (internal link).

## How to Contact the Secure Design & Development Team

- Find your Stable Counterpart on the [Product sections, stages, groups, and categories](/handbook/product/categories/) page
- Mention `@gitlab-com/gl-security/product-security/appsec` on GitLab
- Submit an issue in the [AppSec Team repository](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/appsec-team/-/issues)
- Ask in `#sec-appsec` or mentioning `@appsec-team` on Slack
- For cross team collaboration improvement opportunities, use [this template for collaboration improvement opportunities](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/appsec-team/-/issues/new?issuable_template=cross-team-collaboration-improvement)

## Content Review and Updates

This page will be reviewed quarterly to ensure alignment with company and divisional priorities, the GitLab Security product roadmap, and relevant business and operational changes. Updates may occur more frequently as business operations evolve.

*Next scheduled review: June 30, 2025*
