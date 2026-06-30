---
title: Triggers
description: Operations workflow page for Zendesk triggers
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/triggers"
---

{{% alert title="Note" color="primary" %}}

All triggers changes are handled via a standard deployment.

{{% /alert %}}

## Creating a trigger

For these, you will need to create a corresponding trigger file in the sync repo.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Editing a trigger

For these, you will need to locate the corresponding trigger file in the sync repo and make changes to it.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Deactivating a trigger

To deactivate an trigger, you must make the following changes in the corresponding trigger file in the sync repo:

1. Move the trigger from the active folder to the the corresponding location in the inactive folder (if it does not exist, create it)
1. Change the value of the `active` attribute in the YAML file to `false`
1. Change the `conditions` seciton to be:

   ```yaml
   - field: 'brand_id'
     operator: 'is_not'
     value: 'GitLab Support'
   ```

1. Change the `actions` section to be:

   ```yaml
   - field: 'brand_id'
     value: 'GitLab Support'
   ```

1. Change the value of the `contains_managed_content` attribute to `false`

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

## Deleting a trigger

{{% alert title="Note" color="danger" %}}

We do not delete triggers except during an annual review of our triggers. Any other time, leave it as deactivated.

If you are looking for information about the annual review of triggers, please see [Annual Review workflow](../annual-review)

{{% /alert %}}

The process to delete a trigger is exactly as described in the [triggers documentation page](../../docs/zendesk/triggers#deleting-a-trigger).

## Exception deployment

To perform an exception deployment for triggers, navigate to the triggers project in question, go to the scheduled pipelines page, and click the play button. This will trigger a sync job for the triggers.

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/triggers)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/triggers)
- [Zendesk Global managed content repo](https://gitlab.com/gitlab-com/support/zendesk-global/triggers)
- [Zendesk US Government managed content repo](https://gitlab.com/gitlab-com/support/zendesk-us-government/triggers)
