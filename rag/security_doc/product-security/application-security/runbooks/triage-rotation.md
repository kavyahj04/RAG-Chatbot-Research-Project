---
title: Triage Rotation
---

Application Security team members are alphabetically assigned as the
responsible individual (DRI) for incoming requests to the Application
Security team, typically for a weekly or fortnightly period.

### Who is on rotation?

Automation manages the scheduling and assignment of rotations:

- ["Who is on rotation now?"](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/tooling/rotation-management/-/wikis/who-is-on-now)
- [Rotation Management FAQ & README](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/tooling/rotation-management)
- [Holiday Coverage](/handbook/security/product-security/application-security/runbooks/holiday-coverage/)

### What are the rotations?

The following rotations are defined:

- (Weekly Assignment) HackerOne + Security Dashboard Review
  - Point of contact for "New" HackerOne reports during that week.
  - Responsible to escalating to other team members and management if the size of
    the either queue spikes.
  - Responsible for reviewing [security dashboards](/handbook/security/product-security/application-security/runbooks/security-dashboard-review/) on a best-effort level
- (Weekly Assignment) Triage Rotation (mentions and issues), by order of priority:
  - First responder to [JiHu Contribution pings](/handbook/ceo/office-of-the-ceo/jihu-support/jihu-security-review-process/) that come into the `#sec-appsec` Slack channel
  - First responder to automated messages posted in the `#public_merge_requests_referencing_confidential_issues` Slack channel
    - Add a check mark emoji if the merge request can be public
    - If the merge request references a legitimate security issue
      - If the issue has a `~security-fix-in-public` label, indicating it [has been approved by an AppSec team member to be fixed in public](/handbook/security/product-security/application-security/vulnerability-management#fixing-in-public), link to the comment granting approval or include a message in Slack denoting that the `~security-fix-in-public` label was added.
      - Decide if it can be public anyway, and apply the `~security-fix-in-public` label retrospectively
      - Otherwise contact SIRT and the merge request author to get the merge request removed.
      - Use the `Urgent - SEOC should be paged right away` option if waiting up to 24 hours for a resolution would be too long.
  - First responder to mentions of the following group aliases:
    - @gitlab-com/gl-security/product-security/appsec on GitLab.com
      - PSIRT and/or SIRT are responsible for addressing external reports of a product vulnerability or customer exploit. See [Hand-off to PSIRT/SIRT during triage rotation](#hand-off-to-psirtsirt-during-triage-rotation)
    - @appsec-team in Slack
  - First responder to mentions from the custom SAST bot:
    - All merge requests with the [`~appsec-sast-ping::unresolved` label](https://gitlab.com/groups/gitlab-org/-/merge_requests?label_name%5B%5D=appsec-sast-ping%3A%3Aunresolved) must be reviewed.
    - Apply the `~appsec-sast-ping::resolved` label once the bot's findings have been resolved.
    - A dashboard with all the bot's findings can be found [here](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/sast-custom-rules/-/issues/80).
  - First responder for issues created needing triage: [~security-triage-appsec issue search](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=security-triage-appsec)
    - Refer to [this page](/handbook/security/engaging-with-security/#reproducibility-on-security-issues) to learn about the different labels that we can apply to issues when they're not vulnerabilities
- (~Fortnightly Assignment) Security Engineer for [Security & Patch Releases](https://about.gitlab.com/releases/#patch-releases)
- (Fortnightly Assignment, Federal AppSec only) Release Certifications
  - Responsible for the [release certification process](/handbook/ceo/office-of-the-ceo/jihu-support/release-certification/)
  - This applies to any release that might have JiHu contributions, including monthly and patch releases
- (Quarterly Assignment) Bug Bounty/AppSec Blog Post

If the Application Security team member has a conflict for the assigned week
they may swap rotation weeks with another team member. This may be done for
any reason including time off or the need for time to focus on a particular task.

Team members should not be assigned on weeks they are responsible for the
scheduled security release.

Team members not assigned as the DRI for the week should continue to triage
reports when possible, especially to close duplicates or handle related reports
to those they have already triaged.

Team members remain responsible for their own assigned reports.

### Hand-off to PSIRT/SIRT during triage rotation

When team members are assigned to Triage rotation and are first responder to mentions of @gitlab-com/gl-security/product-security/appsec on GitLab.com or @appsec-team in Slack, assess whether the ping is an external report of a product vulnerability or customer exploit. In these instances, hand off to @gitlab-com/gl-security/product-security/appsec/psirt-group and/or @gitlab-sirt. 

Direct reports from customers of vulnerabilities found during container scans to the Vulnerability Mangement team.

### Triaging exposed secrets

Exposure of information and secrets is handled a little differently to vulnerabilities, as there is nothing to patch and therefore no need for a GitLab Project Issue, CVSS, or CVE. When you're pinged during your rotation and you see a leaked secret, follow the process described on the [HackerOne runbook](/handbook/security/product-security/application-security/runbooks/hackerone-process/#triaging-exposed-secrets)
