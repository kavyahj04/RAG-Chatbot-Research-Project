---
title: Support Team YAML files
description: Operations workflows page for Support Team YAML files
canonical_path: "/handbook/security/customer-support-operations/workflows/gitlab/support-team-yaml-files/"
---

{{% alert title="Note" color="primary" %}}

Support Team YAML file changes are classified as ad-hoc. Once changes are merged into the default branch, they are synced to Redis and live.

This can mean changes can cause severe problems if you have not thoroughly tested them.

{{% /alert %}}

## Request for changes

Requests to make changes to the Support Team YAML files require specific levels of approval.

For the following items, the target's manager must add their approval on the MR:

- Title
- Working Hours
- Focuses
- Zendesk Groups (either instance)
- GitLab works_account_deletion value
- Display name / Alias updates

The approval is required to procced. If it has not been granted, do not proceed on the MR.

## Making changes

{{% alert title="Note" color="primary" %}}

Customer Support Operations is not normally the one making the changes. We usually act in a "review+merge" capacity.

{{% /alert %}}

Making the changes would be done by modifying the files within the project. You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

Once the MR is merged, they will then be synced into Redis (and used in our wider systems).
