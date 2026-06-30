---
title: Forms
description: Operations workflow page for Zendesk forms
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/forms"
---

{{% alert title="Note" color="primary" %}}

All form changes are handled via a standard deployment.

{{% /alert %}}

## Creating a form

For these, you will need to create a corresponding form file in the sync repo.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Editing a form

For these, you will need to locate the corresponding form file in the sync repo and make changes to it.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Deactivating a form

To deactivate an form, you must make the following changes in the corresponding form file in the sync repo:

1. Move the form file from the active folder to the the corresponding location in the inactive folder (if it does not exist, create it)
1. Change the value of the `active` attribute in the YAML file to `false`
1. Change the `ticket_field_ids` seciton to be:

   ```yaml
   - 'Status'
   - 'Group'
   - 'Assignee'
   - 'Ticket status'
   - 'Subject'
   - 'Description'
   ```

1. Change the `end_user_conditions` section to be `[]`
1. Change the `agent_conditions` section to be `[]`

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

## Deleting a form

{{% alert title="Note" color="danger" %}}

We do not delete forms except during an annual review of our forms. Any other time, leave it as deactivated.

If you are looking for information about the annual review of forms, please see [Annual Review workflow](../annual-review)

{{% /alert %}}

The process to delete a form is exactly as described in the [forms documentation page](../../docs/zendesk/forms#deleting-a-ticket-form).

## Exception deployment

To perform an exception deployment for forms, navigate to the forms project in question, go to the scheduled pipelines page, and click the play button. This will trigger a sync job for the forms.

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/tickets/forms-and-fields)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/tickets/forms-and-fields)
