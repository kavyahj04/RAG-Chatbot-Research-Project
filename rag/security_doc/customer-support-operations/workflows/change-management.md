---
title: Change Mangement
description: Operations workflow for change management
canonical_path: "/handbook/security/customer-support-operations/workflows/change-management"
---

{{% alert title="Note" color="danger" %}}

The exact process for change management can vary from project to project and item to item, so when in doubt, it is best to refer to the specific workflow for the item in question.

{{% /alert %}}

## Types of delpoyments

### Standard deployments

A standard deployment for us happens on the first of every month. We center our milestones around these. We utilize scheduled pipelines for these items so everything is automated. Changes in the repos following standard deployments are all synced to thhe systems via these on the deployment date.

### Ad-hoc deployments

For some items, it makes little sense to delpoy them on specific dates. For these items, they are deployed when the changes are made to the repos (or in the system iteself).

### Exception deployments

There are situations where an item that normally uses a standard deployment needs to be done before the actual deployment date it would normally fall into.

When these situations occur, the general process for them should go as follows:

1. The requester asks for an exception deployment
1. `@dtragjasi` and/or `@jcolyer` will make a comment detailing what the impacts of the exception deployment will be.
   - This is done by reviewing what has been merged and is "queued for deployment" in the various areas the topic entails.
1. The Sr. Support Engineering Manager - Operations will review the request and impacts to make a decision on the feasibility and acceptance of the request. He will present the consequences, impact, etc. to the requester.
1. If the requester agrees with the Sr. Support Engineering Manager - Operations statement, they will confirm they still wish to proceed.

Should all parties approve the request, we will then perform an exception deployment. The exact means of doing so can vary, so please refer to the specific workflow for the item(s) in question.

### Special Deployments

This is a categorization for areas that require very specific deployment methods that fall outside of Standard, Exception, and Ad hoc deployments. For more information on these, see the workflow page of the item itself.

## What uses what type of deployment

To determine the type of deployment something uses, please refer to that item's workflow page.
