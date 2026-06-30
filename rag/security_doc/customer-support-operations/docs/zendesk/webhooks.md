---
title: Webhooks
description: Operations documentation page for Zendesk webhooks
canonical_path: "/handbook/security/customer-support-operations/docs/zendesk/webhooks"
---

{{% alert title="Note" color="primary" %}}

This is an informational page for Zendesk webhooks. It may not reflect the way we actually manage Zendesk webhooks/

If you are looking for information about managing it, please see [webhooks workflow](../../workflows/zendesk/webhooks)

{{% /alert %}}

## What are Zendesk webhooks

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks-to-interact-with-third-party-systems):

> A webhook sends an HTTP request to a specified URL in response to an event, such as a trigger or automation firing in Zendesk Support. Web developers typically use webhooks to invoke behavior in another system.

## Creating a webhook via Zendesk

For information on creating a webhook in Zendesk, please see the [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks-to-interact-with-third-party-systems#topic_bwm_1tv_dpb).

## Editing a webhook via Zendesk

To edit a webhook in Zendesk, you first need to go to the Admin Center ([Zendesk Global](https://gitlab.zendesk.com/admin/) / [Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From there, you need to go to the Webhooks page (Apps and integrations > Webhooks > Webhooks).

From here, locate the webhook in question, hover over it, and click the 3 dots on the right-hand side of the row. Doing so will have a menu pop up with the `Edit` option.

Doing so will bring up the webhook editor. You can now edit the webhook, test the changes (see [Testing a webhook](#testing-a-webhook) for more info), and then save your changes by clicking the blue `Update` button t the bottom-right of the page.

## Deleting a webhook via Zendesk

To delete a webhook in Zendesk, you first need to go to the Admin Center ([Zendesk Global](https://gitlab.zendesk.com/admin/) / [Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From there, you need to go to the Webhooks page (Apps and integrations > Webhooks > Webhooks).

From here, locate the webhook in question, hover over it, and click the 3 dots on the right-hand side of the row. Doing so will have a menu pop up with the `Delete` option.

Clicking this will cause a pop-up  to appear asking you to confirm the deletion. Click the red `Delete webhook` button to do so.

## Testing a webhook

For information on creating a webhook in Zendesk, please see the [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks-to-interact-with-third-party-systems#topic_ijl_fcx_dpb).

## Viewing a webhook's activity

To view a webhook's activity in Zendesk, you first need to go to the Admin Center ([Zendesk Global](https://gitlab.zendesk.com/admin/) / [Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From there, you need to go to the Webhooks page (Apps and integrations > Webhooks > Webhooks).

From here, locate the webhook in question, and click on its name. On this page, click the `Activity` tab to see all the runs of the webhook. You can click on the Invocation ID of the run to get more information on said run (on the side menu that appears, click the timestamp for more details).
