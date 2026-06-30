---
title: Customer Support Operations
description: Everything you wanted to know about GitLab Customer Support Operations
canonical_path: "/handbook/security/customer-support-operations"
---

## Purpose

The purpose of Customer Support Operations is to enable GitLab to provide delightful customer experiences by:

- equipping the Customer Support team with knowledge, tools and data to optimize productivity and efficiently solve customer problems.
- equipping our customers and wider GitLab with the data, knowledge and insights to prevent customer problems before they occur.
- delivering delightful experiences to both our own internal and external customers.

*Our purpose statement is re-evaluated as needed, at minimum every 3 years*

## Meet the team

| Name | Role |
|------|------|
| [Steve Manzuik](https://gitlab.com/smanzuik) | Senior Director, Security |
| [Lyle Kozloff](https://gitlab.com/lyle) | Sr. Manager, Customer Support Operations |
| [Jason Colyer](https://gitlab.com/jcolyer) | Fullstack Engineer, Customer Support Operations |
| [Nabeel Bilgrami](https://gitlab.com/nabeel.bilgrami) | Customer Support Operations Specialist |
| [Alyssa Villa](https://gitlab.com/avilla4) | Customer Support Operations Specialist |
| [Dylan Tragjasi](https://gitlab.com/dtragjasi) | Customer Support Operations Specialist |
| [Sarah Cole](https://gitlab.com/Secole) | Customer Support Operations Specialist |
| [Rene Verschoor](https://gitlab.com/rverschoor) | Customer Support Operations Specialist |

## Working with us

- [Use this template if you want something new or modified](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature)
- [Use this template to file a bug report](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Bug)

Or you can reach out to us in Slack via [#support_operations](https://gitlab.enterprise.slack.com/archives/C018ZGZAMPD).

## Basic issue flow

### Bug Reports

The issue will be created in the `Triage` stage. From here, Customer Support Operations will validate the bug (if it is invalid, the request will be closed).

If it is valid, it will then move to the `Planning` stage (with all appropriate labels put in place), where a gameplan will be made.

Once a gameplan is made, it will jump to the `Development` stage, where the changes will be made.

Once it is ready for review, we will ask the requester (or someone they delegate this to) will validate the changes fix the bug.

Once validated, it will then move to the `Implementation` stage, where it will be implemented into production.

Once that is done, the issue will move to the `Completed` stage (and be closed out).

### Feature requests

The issue will be created in the `Triage` stage. From here, Customer Support Operations will determine if the request has enough information to move onto next stages (if not, we will ask for more information).

Customer Support Operations will then determine if all needed approvals are present. The general logic used is:

- If the request aligns with something on the support roadmap and seems congruent with the intention, then no approval required
- If the request aligns with something on the support roadmap but is not congruent with the intention, then we will ask for one of the following:
  - The support roadmap be updated
  - Support leadership approval be documented on the request
- If the request does not align with something on the support roadmap, then we will ask for an appropriate level of approval from support leadership based on:
  - the amount of work
  - any danger to planned work
  - effect on customer or support workflows

If approved, it will then move to the `Planning` stage (with all appropriate labels put in place), where a gameplan will be made.

Once a gameplan is made and added to the issue, it will then move to the `Scheduling` stage. Here, Customer Support Operations will determine when it can be implemented. After that is decided, an iteration, milestone, and Customer Support Operations DRI will be added to the issue (which indicates the period the work will be done in).

If the iteration is not the current one, then the request will be moved to the `Queued` stage, where it will wait until the iteration the request is assigned to comes up.

Once the iteration period arrives, the request will move to the `Development` stage. Here, work will be done to get the changes into a state where they can be tested and validated. Notes will often be added on what kind of changes were made (and where) to help in later stages.

Once all changes are ready to be validated, we will add the label `Validation::Requested` and make a comment on the issue asking the the requester (or someone they delegate this to) to validate the changes done will meet their requirements for the request. What happens next depends on the results of said validation:

- If approved, the label `Validation::Received` will be added to the issue (and the issue moved to the `Implementation` stage)
- If not approved, the label `Validation::Rejected` will be added to the issue (where it will remain in `Development` to be tweaked for another round of validation).

Once a request is in the `Implementation`, we will add a comment detailing the technical blueprint of what was done (which should include links to merge requests, followup issues, etc.). We will also begin implementation the changes into production (the exact method depends on what is changing).

Once all that is done, the stage moves to `Completed`, where the issue is closed out.
