---
title: Organizations
description: Operations documentation page for Zendesk organizations
canonical_path: "/handbook/ssecurity/customer-support-operations/docs/zendesk/organizations"
---

{{% alert title="Note" color="primary" %}}

This is an informational page for Zendesk organizations. It may not reflect the way we actually manage Zendesk organizations.

- If you are looking for information about organization deletions, please see [Organization deletions](org-deletion)
- If you are looking for information about maintaining organizations, please see [ZD-SFDC Sync](zd-sfdc-sync)

{{% /alert %}}

## What are Zendesk organizations?

Organizations are simply a collection of users in Zendesk (much like groups). We use them to also store metadata (synced from Salesforce), which is used to determine such things as SLA, ARR, etc.

an organization in Zendesk

## Creating an organization in Zendesk

{{% alert title="Note" color="danger" %}}

You can cause some serious issues doing this action. Avoid doing this unless another workflow specifically states to do so.

{{% /alert %}}

For information on creating an organization, please see [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408882246298-Creating-organizations#topic_1yx_452_ck).

## Editing an organization in Zendesk

{{% alert title="Note" color="danger" %}}

You can cause some serious issues doing this action. Avoid doing this unless another workflow specifically states to do so.

{{% /alert %}}

For information on editing an organization, please see [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408846640410-Managing-organizations#topic_cab_ihe_bc).

## Merging an organization in Zendesk

{{% alert title="Note" color="danger" %}}

You can cause some serious issues doing this action. Avoid doing this unless another workflow specifically states to do so.

{{% /alert %}}

For information on merging an organization, please see [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/6216929727898-Merging-organizations#topic_vt2_xzh_hzb).

## Deleting an organization in Zendesk

{{% alert title="Note" color="danger" %}}

You can cause some serious issues doing this action. Avoid doing this unless another workflow specifically states to do so.

{{% /alert %}}

For information on deleting an organization, please see [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408846640410-Managing-organizations#topic_ys3_pqc_4qb).

## Organization Notes

### Zendesk Global

There are two forms of organization notes we utilize:

- Customer Support Operations organization notes
- Support Team organization notes

Support Operations organizations notes are managed via Zendesk in the `Notes` and `Details` fields on the organization itself.

When an organization has a ticket created, the ticket processor runs to parse both of these into internal comments on the ticket itself.

### Zendesk US Government

We manage all internal notes on Zendesk itself due to data privacy concerns. As such, we separate them as such:

- `Notes` are for Support Team organization notes
- `Details` are for Customer Support Operations organization notes

When an organization has a ticket created, the ticket processor runs to parse both of these into internal comments on the ticket itself.

## Permissions

By default, organizations are setup so that the users within it can only see and comment on their own tickets.

For more information on this, please see [Shared organizations workflow](../../workflows/zendesk/shared-organizations).

## Domain matching

While Zendesk does have the functionality to do domain matching, we have determined that the security risks inherent in this feature outweigh the benefits that would be received from its use.

Because of this decsion, as of August 2020, GitLab will not longer apply a domain on a Zendesk organization. Any organization that had this applied prior to this date will have it as a legacy feature.
