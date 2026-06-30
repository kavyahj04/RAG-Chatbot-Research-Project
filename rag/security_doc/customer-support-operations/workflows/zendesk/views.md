---
title: Views
description: Operations workflow page for Zendesk views
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/views"
---

{{% alert title="Note" color="primary" %}}

All views changes are handled via a standard deployment.

{{% /alert %}}

## Creating a view

For these, you will need to create a corresponding view file in the sync repo.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Editing a view

For these, you will need to locate the corresponding view file in the sync repo and make changes to it.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

## Deactivating a view

{{% alert title="Note" color="primary" %}}

Due to the nature of the multi-step process, this will result in a pipeline failure when step 1 is completed. This will be fixed in step 2.

{{% /alert %}}

To deactivate an view, you must perform a two-step process

### Step 1

1. Locate the managed content file for the view
1. Move the file from the active folder to the the corresponding location in the inactive folder (if it does not exist, create it)

You should also do this in a way that creates a MR. You will require someone from Support Leadership to approve this MR before you can merge it.

Only proceed to step 2 once all changes in step one are merged.

### Step 2

1. Locate the YAML file for the view in the sync repo
1. Move the view from the active folder to the the corresponding location in the inactive folder (if it does not exist, create it)
1. Change the value of the `active` attribute in the YAML file to `false`
1. Change the `conditions` section to be:

   ```yaml
   - field: 'brand_id'
     operator: 'is_not'
     value: 'GitLab Support'
    - field: 'status'
      operator: 'less_than'
      value: 'closed'
   ```

1. Change the `restriction` value to be `null`

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

## Deleting a view

{{% alert title="Note" color="danger" %}}

We do not delete views except during an annual review of our views. Any other time, leave it as deactivated.

If you are looking for information about the annual review of views, please see [Annual Review workflow](../annual-review)

{{% /alert %}}

The process to delete a view is exactly as described in the [views documentation page](../../docs/zendesk/views#deleting-a-view).

## Exception deployment

To perform an exception deployment for views, navigate to the views project in question, go to the scheduled pipelines page, and click the play button. This will trigger a sync job for the views.

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/views)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/views)
- [Zendesk Global managed content repo](https://gitlab.com/gitlab-com/support/zendesk-global/views)
- [Zendesk US Government managed content repo](https://gitlab.com/gitlab-com/support/zendesk-us-government/views)
