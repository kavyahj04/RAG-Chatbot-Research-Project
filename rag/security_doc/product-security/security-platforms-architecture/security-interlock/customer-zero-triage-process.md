---
title: "Customer Zero Triage Process"
description: "Runbook for the Security Team to triage and assign Customer Zero Requests"
---

## New Customer Zero Requests

When Customer Zero requests are created using our [request templates](../security-interlock/request-customer-zero-validation.md), they are automatically labeled with `C0Workflow::Backlog`, which makes them visible on [this issue board](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-requests/-/boards/9306316) (internal only).

Triagers may choose to subscribe to the `~C0Workflow::Backlog` label and/or periodically monitor the board to identify new issues that need to be triaged.

## How to Triage New Issues

1. Select an issue that does NOT start with the prefixes `DRAFT:` or `WIP:`. Those issues are ones that submitters have started, but they still need to provide additional information before we review them. That's fine! We'd prefer to have visibility into what's coming anyway.
1. Apply the label `~"C0Workflow::Initial Triage"` to indicate that someone is already triaging this issue so no one duplicates your efforts. You can do this manually or by moving the Issue to the next column on the [issue board](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-requests/-/boards/9306316) (internal only). If your triage takes more than just a few minutes, assign the issue to yourself so this shows up in your TODOs and you don't lose track.
1. Review the information provided in the Issue and determine if sufficient information has been provided for someone to work it. For example, are all of the key fields populated? Do you understand the feature and have all of the information you'd need to do a review?
   - **If Not**: Tag the requestor and key contacts in a comment and ask them clarifying questions. Apply the label `~"C0::Waiting on Requestor"` to the Issue manually or by moving it to the next column on the [issue board](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-requests/-/boards/9306316) (internal only). Ask that they tag you directly when they've provided the additional information so you can re-review and follow the next steps.
1. Once you have determined there is sufficient information in the Issue, first set the milestone appropriately, given both the Timeline Requirements in the Issue and our [SLOs](../security-interlock/request-customer-zero-validation/#timeline-expectations), which state requests received at least 10 calendar days before the next milestone starts should have feedback provided within the next milestone. Requests received later than that will typically be prioritized for milestone+2.
1. Determine which team(s) are best suited to provide the appropriate feedback. If you are unsure which teams' feedback is required, ask in `#product-security-department-only`. Once you have determined the appropriate team(s), take the following steps:

    | Team | Steps |
    | ------- | ------- |
    | AppSec | 1. Apply the `~"Application Security Team"` label<br/> 2. Tag `@gitlab-com/gl-security/product-security/appsec` and ask them to incorporate into their milestone planning |
    | PSIRT | Tag `@gitlab-com/gl-security/product-security/appsec/psirt-group` and ask them to incorporate into their milestone planning |
    | Vuln Management | Tag `@gitlab-com/gl-security/product-security/vulnerability-management` and ask them to incorporate into their milestone planning |
    | ProdSecEng | 1. Apply the `~"team::Product Security Engineering"` label<br/> 2. Tag `@gitlab-com/gl-security/product-security/product-security-engineering` and ask them to incorporate into their milestone planning |
    | Not Listed | Tag team members individually, and update this Handbook page if you receive alternate instructions |

1. Apply the label `~"C0Workflow::On Deck"` to indicate this has been triaged and assigned.

You're Done!
