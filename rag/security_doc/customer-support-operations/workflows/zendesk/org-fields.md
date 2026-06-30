---
title: Organization fields
description: Operations workflow page for Zendesk organization fields
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/org-fields"
---

{{% alert title="Note" color="primary" %}}

All organization field changes are handled via a standard deployment.

{{% /alert %}}

## Creating an organization field

For these, you will need to create a corresponding organization field file in the sync repo.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

## Editing an organization field

For these, you will need to locate the corresponding organization field file in the sync repo and make changes to it.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

## Deactivating an organization field

{{% alert title="Note" color="primary" %}}

Be very cautious on these. You can break a considerable amount of things by deactivating an organization field that is still actually in use.

{{% /alert %}}

To deactivate an organization field, you must make the following changes in the corresponding organization field file in the sync repo:

1. Move the organization field file from the active folder to the the corresponding location in the inactive folder (if it does not exist, create it)
1. Change the value of the `active` attribute in the YAML file to `false`

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

## Deleting an organization field

{{% alert title="Note" color="danger" %}}

We do not delete organization fields except during an annual review of our organization fields. Any other time, leave it as deactivated.

If you are looking for information about the annual review of organization fields, please see [Annual Review workflow](../annual-review)

{{% /alert %}}

The process to delete an organization field is exactly as described in the [organization fields documentation page](../../docs/zendesk/org-fields#deleting-organization-fields).

## Exception deployment

To perform an exception deployment for organization fields, navigate to the organization fieldsa project in question, go to the scheduled pipelines page, and click the play button. This will trigger a sync job for the organization fields.

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/orgs/fields)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/orgs/fields)
