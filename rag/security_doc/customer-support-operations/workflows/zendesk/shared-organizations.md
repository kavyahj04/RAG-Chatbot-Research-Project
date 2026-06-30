---
title: Shared Organizations
description: Operations workflow page for Zendesk shared organizations
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/shared-organizations"
---

By default, organizations are setup so that the users within it can only see and comment on their own tickets. This security measure often doesn't work for some organizations though.

Because of that, we have the ability to setup Shared Organizations, a term meaning the users in an organization have heightened permissions and can do see and/or comment on tickets that are not theirs.

## Pre-checks

{{% alert title="Note" color="danger" %}}

There is a security and legal component to this feature. As such, you must ensure all pre-checks are done every single time. When in doubt, get a Fullstack Engineer to review the situaiton.

{{% /alert %}}

Before we can proceed to enable a shared organization, three criteria must be met:

- The requester has confirmed which type of shared organization is desired
- The requester, on behalf of their organization, has approved the inherent security risk shared organizations present
- There is not an organization note/detail stating we will not enable a shared organization for them

If any of those criteria have not been met, we cannot proceed.

If all of those criteria are met, make sure to update the ticket metadata to indicate all of that.

## Enabling a shared organization

To enable a shared organization:

1. Navigate to the organization
1. Click the text next to `Users` at the top-left
1. Select `Can view all org tickets`
1. On the drop-down below, select the correct option depending on the type they requested
1. Add a new item in the `Details` field containing the following:
   > Shared organization (TYPE) enabled DATE as per TICKET
   - Replace `TYPE` with either `read only` or `read+write`
   - Replace `DATE` with today's ISO formatted date (YYYY-MM-DD)
   - Replace `TICKET` with the ticket's URL
1. Add a public comment on the ticket confirming it has been enabled
1. Mark the ticket as Solved

## Disabling a shared organization

To disable a shared organization:

1. Navigate to the organization
1. Click the text next to `Users` at the top-left
1. Select `Can view own tickets only`
1. Add a new item in the `Details` field containing the following:
   > Shared organization disabled DATE as per TICKET
   - Replace `DATE` with today's ISO formatted date (YYYY-MM-DD)
   - Replace `TICKET` with the ticket's URL
1. Add a public comment on the ticket confirming it has been disabled
1. Mark the ticket as Solved
