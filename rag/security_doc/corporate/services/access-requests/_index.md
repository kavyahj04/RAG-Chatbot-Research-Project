---
title: "Access Requests (AR) Services"
---

Access Requests are owned by the Corporate Security Helpdesk team. All onboarding, offboarding and role change (career mobility) requests are owned by the People Connect Team.

If you have any access requests related questions, please reach out to `#it_help` in Slack or the tool provisioner in Slack.

- [FAQs](/handbook/security/corporate/services/ar/faq)
- [Baseline Entitlements](https://internal.gitlab.com/handbook/security/corporate/end-user-services/access-request/baseline-entitlements/)
- [Temporary service providers access requests and onboarding](https://internal.gitlab.com/handbook/security/corporate/end-user-services/access-request/temporary-service-providers/)

## Issue Trackers

- **Team Members (use this by default):** [Access Request Issue Tracker](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues)
- **Temporary Service Providers:** [Lifecycle Issue Tracker](https://gitlab.com/gitlab-com/temporary-service-providers/lifecycle/-/issues)
- **Employment Onboarding:** [Employment Issue Tracker](https://gitlab.com/gitlab-com/team-member-epics/employment/-/issues/?sort=created_date&state=opened&label_name%5B%5D=onboarding&first_page_size=20)
- **Employment Career Mobility:** [Employment Issue Tracker](https://gitlab.com/gitlab-com/team-member-epics/employment/-/issues/?sort=created_date&state=opened&label_name%5B%5D=career-mobility&first_page_size=20)
- **Employment Offboarding:** [Employment Issue Tracker](https://gitlab.com/gitlab-com/team-member-epics/employment/-/issues/?sort=created_date&state=opened&label_name%5B%5D=offboarding&first_page_size=20)

## Team Member Issue Templates

Please submit a team member access request by selecting the appropriate application-specific form [here](https://gitlab.com/gitlab-com/team-member-epics/access-requests). If there isn't a specific application request form for your needs (like Adobe, Slack, or Zoom), you can use the Individual or Bulk Person Access request.

## Role Based Entitlements

- Role based entitlements are a pre-approved set of permissions that are granted to all people in a role. Make sure that whatever set of permissions you are adding to these templates should be granted to anyone with that role.

- Role based entitlements need to be approved only once, when the template is created, and they don't need to be approved again on a case-by-case basis.

- These templates cannot be edited to remove or add extra permissions once created, unless those changes are approved by a manager (or higher) of the team the role belongs to. Note that an approval is still required even if a change comes from a manager or higher on a baseline entitlement template to mitigate the risk of a permission change being pushed through by a single team member.

- We have decided to remove all SOX applications from the Role-Based Entitlements templates.  Therefore, any access that is requested for our SOX-in-scope systems should follow the standard A/R process outlined here in our [handbook](/handbook/security/corporate/end-user-services/onboarding-access-requests/access-requests/#how-do-i-choose-which-template-to-use).  The impact to you is for any access going forward that was granted automatically via a role based entitlement will now need to be requested via a standard A/R so we can ensure approvals are properly captured.

- Please note when editing an existing template or creating a new one do not include access of any kind to a rolebased access template.  Full listing of SOX applications can be found [here](https://gitlab.com/groups/gitlab-com/internal-audit/-/wikis/IT-General-Controls)

## Need help?

- Please mention `@gitlab-com/business-technology/end-user-services` in the issue, with no particular SLA.
- If your request is urgent, post a link to your access request in the `#it_help` channel in Slack with a note on why it is urgent.

## Working on Access Requests

### Department Access Request Boards

- If you need additional labels or have suggestions for improving the process until we can fully automate, please [open an issue](https://gitlab.com/gitlab-com/it/end-user-services/issues/it-help-issue-tracker/-/issues/new).
- ARs are auto-assigned and auto-labeled when possible by department. In some cases, there are multiple provisioners per tool. If a template cannot be auto-assigned, Business Technology will provide a board where the provisioners can review their department's issues by label (ie `dept::to do`. It is up to the department to manage the workflow on who works the issues to completion.
- **Moving an issue from one column to another will remove the first label (per the column header) and add the second label. Please use caution when moving issues between columns.**
- Departments can check their outstanding access request issues by viewing their board below.

{{% panel header="**AR boards: to-do:**" header-bg="success" %}}

1. [Data](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319045)
1. [Finance](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319048)
1. [Infra](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1262513)
1. [IT](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1262521)
1. [Legal](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319051)
1. [PeopleOPs](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1318841)
1. [Prod+Eng](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319057)
1. [Marketing](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1284066)
1. [Sales](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1262518)
1. [Security](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319052)
1. [Support](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319053)
{{% /panel %}}

## Tech Stack Changes

If you need to initiate an Access Request process for a new item in the tech stack:

1. Confirm the tool is added to the [tech stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml)
1. Confirm a team member is included as the `provisioner` `deprovisioner`
1. Document the requirement to submit an Access Request in any relevant handbook pages
