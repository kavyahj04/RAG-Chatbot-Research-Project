---
title: Ticket fields
description: Operations workflow page for Zendesk ticket fields
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/ticket-fields"
---

{{% alert title="Note" color="primary" %}}

All ticket field changes are handled via a standard deployment.

{{% /alert %}}

## Creating a ticket field

For these, you will need to create a corresponding ticket field file in the sync repo.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Editing a ticket field

For these, you will need to locate the corresponding ticket field file in the sync repo and make changes to it.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Deactivating a ticket field

{{% alert title="Note" color="primary" %}}

Be very cautious on these. You can break a considerable amount of things by deactivating a ticket field that is still actually in use.

{{% /alert %}}

To deactivate a ticket field, you must make the following changes in the corresponding ticket field file in the sync repo:

1. Move the ticket field file from the active folder to the the corresponding location in the inactive folder (if it does not exist, create it)
1. Change the value of the `active` attribute in the YAML file to `false`

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

## Deleting a ticket field

{{% alert title="Note" color="danger" %}}

We do not delete ticket fields except during an annual review of our ticket fields. Any other time, leave it as deactivated.

If you are looking for information about the annual review of ticket fields, please see [Annual Review workflow](../annual-review)

{{% /alert %}}

The process to delete a ticket field is exactly as described in the [ticket fields documentation page](../../docs/zendesk/ticket-fields#deleting-a-ticket-field).

## Exception deployment

To perform an exception deployment for ticket fields, navigate to the ticket fieldsa project in question, go to the scheduled pipelines page, and click the play button. This will trigger a sync job for the ticket fields.

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/tickets/forms-and-fields)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/tickets/forms-and-fields)
