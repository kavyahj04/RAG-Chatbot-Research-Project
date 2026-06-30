---
title: User fields
description: Operations workflow page for Zendesk user fields
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/user-fields"
---

{{% alert title="Note" color="primary" %}}

All user field changes are handled via a standard deployment.

{{% /alert %}}

## Creating a user field

For these, you will need to create a corresponding user field file in the sync repo.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

## Editing a user field

For these, you will need to locate the corresponding user field file in the sync repo and make changes to it.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

## Deactivating a user field

{{% alert title="Note" color="primary" %}}

Be very cautious on these. You can break a considerable amount of things by deactivating a user field that is still actually in use.

{{% /alert %}}

To deactivate a user field, you must make the following changes in the corresponding user field file in the sync repo:

1. Move the user field file from the active folder to the the corresponding location in the inactive folder (if it does not exist, create it)
1. Change the value of the `active` attribute in the YAML file to `false`

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

## Deleting a user field

{{% alert title="Note" color="danger" %}}

We do not delete user fields except during an annual review of our user fields. Any other time, leave it as deactivated.

If you are looking for information about the annual review of user, please see [Annual Review workflow](../annual-review)

{{% /alert %}}

The process to delete a user field is exactly as described in the [user fields documentation page](../../docs/zendesk/user-fields#deleting-user-fields).

## Exception deployment

To perform an exception deployment for user fields, navigate to the user fieldsa project in question, go to the scheduled pipelines page, and click the play button. This will trigger a sync job for the user fields.

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/users/fields)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/ousersrgs/fields)
