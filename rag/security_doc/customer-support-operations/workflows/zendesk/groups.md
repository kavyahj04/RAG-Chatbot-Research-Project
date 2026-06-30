---
title: Groups
description: Operations workflow page for Zendesk groups
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/groups"
---

{{% alert title="Note" color="primary" %}}

All group creations are handled via an ad-hoc deployment.

All group updates are handled via a standard deployment.

{{% /alert %}}

## Creating a group

For these, you will need to create a corresponding group file in the sync repo.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

## Editing a group

{{% alert title="Note" color="danger" %}}

Due to the potential downstream impact, you should _never_ edit a group. If you are looking to make changes to a group's name, you should make a new group and migrate users over to it.

{{% /alert %}}

## Deleting a group

{{% alert title="Note" color="danger" %}}

Due to the potential downstream impact, you should _never_ delete a group.

{{% /alert %}}

## Exception deployment

To perform an exception deployment for groups, navigate to the groups project in question, go to the scheduled pipelines page, and click the play button. This will trigger a sync job for the groups.

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/groups)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/groups)
