---
title: Macros
description: Operations workflow page for Zendesk macros
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/macros"
---

{{% alert title="Note" color="primary" %}}

Macro changes are classified as ad-hoc. Once changes are made to the repo, they sync to Zendesk.

{{% /alert %}}

While Zendesk offers a full way to manage macros via the UI, we turn to a more version controlled methodology. That being the case, we utilize thhe support super form, sync repos, and managed content repos.

## Creating a macro

When it comes to creating a macro, there are two methodologies, one for "simple" macros and one for "complex" macros.

A simple macro is one that only would modify the following:

- Ticket assignment (or removal thereof)
- Adding tags to the ticket
- Adding a public or private comment to a ticket

If a macro would do anything other than those listed items, it is deemed "complex" at this time.

### Simple macros

For the creation of simple macros, the requester would utilize the Support Super Form. A submission from there will provide the processor all the information it needs to fully create the macro (including a managed content file if required).

### Complex macros

For the creation of complex macros, the requester would utilize the Support Super Form. This will result in an issue being created for you to work. The issue should contain all the needed information. The processor will have also created a managed content file for you if required.

Once you get the issue, you will need to navigate to the sync repo for the instance(s) the macro is being created on. Here, you will manually create the YAML file for the macro using the infromation provided in the issue.

An example YAML file would be:

```yaml
---
title: General::Verify account self-managed or .com
active: true
description:
actions:
- field: comment_value
  value: MANAGED_CONTENT
- field: status
  value: pending
restriction:
contains_managed_content: true
```

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

Once the file is created and live on the `master` branch of the sync repo, the macro will automatically sync into the production Zendesk instance.

## Editing a macro

For these, you will need to locate the corresponding macro file in the sync repo and make changes to it.

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

The exact nature of what you need to put into the YAML file will vary based on the issue's request.

Be sure to read [Working with sync repo files](../../docs/sync-repo-files) for more information.

Once the file is created and live on the `master` branch of the sync repo, the macro will automatically sync into the production Zendesk instance.

## Deactivating a macro

To deactivate a macro, you must make the following changes in the corresponding macro file in the sync repo:

1. Move the macro from the active folder to the the corresponding location in the inactive folder (if it does not exist, create it)
1. Change the value of the `active` attribute in the YAML file to `false`
1. Change the `actions` section to be:

   ```yaml
   - field: 'brand_id'
     value: 'GitLab Support'
   ```

1. Change the value of the `contains_managed_content` attribute to `false`

You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

Once the changes are live on the `master` branch of the sync repo, the macro will automatically sync into the production Zendesk instance.

## Deleting a macro

{{% alert title="Note" color="danger" %}}

We do not delete macros except during an annual review of our macros. Any other time, leave it as deactivated.

If you are looking for information about the annual review of macros, please see [Annual Review workflow](../annual-review)

{{% /alert %}}

The process to delete a macro is exactly as described in the [macros documentation page](../../docs/zendesk/macros#deleting-a-macro-in-zendesk)

## Repo links

- [Zendesk Global sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-global/macros)
- [Zendesk US Government sync repo](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/macros)
- [Zendesk Global managed content repo](https://gitlab.com/gitlab-com/support/zendesk-global/macros)
- [Zendesk US Government managed content repo](https://gitlab.com/gitlab-com/support/zendesk-us-government/macros)
