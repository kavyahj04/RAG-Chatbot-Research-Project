---
title: Automations
description: Operations workflow page for Zendesk automations
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/automations"
---

{{% alert title="Note" color="primary" %}}

All automation changes are handled via a standard deployment.

{{% /alert %}}

## Creating an automation

For these, you will need to create a corresponding automation file in the sync repo.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Editing an automation

For these, you will need to locate the corresponding automation file in the sync repo and make changes to it.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Deactivating an automation

To deactivate an automation, you must make the following changes in the corresponding automation file in the sync repo:

1. Move the automation from the active folder to the the corresponding location in the inactive folder (if it does not exist, create it)
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

## Deleting an automation

{{% alert title="Note" color="danger" %}}

We do not delete automations except during an annual review of our automations. Any other time, leave it as deactivated.

If you are looking for information about the annual review of automations, please see [Annual Review workflow](../annual-review)

{{% /alert %}}

The process to delete an automation is exactly as described in the [automations documentation page](../../docs/zendesk/automations#deleting-an-automation).

## Exception deployment

To perform an exception deployment for automations, navigate to the automations project in question, go to the scheduled pipelines page, and click the play button. This will trigger a sync job for the automations.

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/automations)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/automations)
- [Zendesk Global managed content repo](https://gitlab.com/gitlab-com/support/zendesk-global/automations)
- [Zendesk US Government managed content repo](https://gitlab.com/gitlab-com/support/zendesk-us-government/automations)
