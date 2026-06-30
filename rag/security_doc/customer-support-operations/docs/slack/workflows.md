---
title: Workflows
description: Operations documentation page for Slack workflows
canonical_path: "/handbook/security/customer-support-operations/docs/slack/workflows"
---

{{% pageinfo color="info" %}}

This is an informational page for Slack workflows. It may not reflect the way we actually manage Slack workflows.

If you are looking for information about maintaining Slack workflows (creating, editing, etc.), please see [our workflows](../../workflows/)

{{% /pageinfo %}}

## Building a Slack workflow

To build a brand new workflow, you will first click the 3 horizontal dots on the
left-hand side of your Slack window (the `More` option) and select
`Automations`.

From this page, you will want to click `Workflow builder` button on the
left-hand side of the page, which should make a new window pop-up.

![Accessing Slack workflow builder](/images/security/customer-support-operations/operations/slack_workflows1.gif)

Within the new window, click the green `Create Workflow` button to start the
process.

From here, you will select the various steps you want to occur. Using the
pre-made templates is often the best place to start, but feel free to start from
scratch if you feel comfortable doing so.

Once you are done building all the steps you want in the workflow, you will
click the green `Finish Up` button at the top-right of the window. Doing so will
normally prompt you to add the Name, Description, Image, and Workflow managers.

The exact options you pick depend on the nature of your workflow, but in terms
of workflows managed by Customer Support Operations, we use the following options (you
might need to click `Show more permissions` to see all the options):

- Workflow managers:
  - Jason Colyer
  - Nabeel Hasan
  - Alyssa Villa - Dionela
  - Dylan Tragjasi
  - Sarah Cole
  - Rene Verschoor
  - Lyle Kozloff
- Can find this workflow
  - Everyone in GitLab
- Can copy this workflow
  - Workflow managers only

With all that in place, click the green `Publish` button to activate your
workflow.

Remember to test it all out and update this page to reflect the new workflow (if
it is Customer Support Operations managed)!

## Modifying a Slack workflow

To edit an existing workflow, you will first click the 3 horizontal dots on the
left-hand side of your Slack window (the `More` option) and select
`Automations`.

From this page, you will want to click `Managed by you` button on the left-hand
side of the page and then select the workflow you are wanting to modify (and
then click the `Edit` button), which should make a new window pop-up.

From here, you are in the workflow builder. Make the changes you want to make to
the workflow and then click the green `Publish` button at the top-right of the
window.

Remember to test it all out and update this page to reflect the new workflow (if
it is Customer Support Operations managed)!

## Unpublishing and deleting a Slack workflow

To unpublish or delete a workflow, you will follow the same directions as the
[Modifying a Slack workflow](#modifying-a-slack-workflow) section. Instead of
modifying steps and the like though, you are going to click the 3 horizontal
dots at the top-right of the page, then select the option you are looking for
(either Unpublish or Delete).

Remember to test it all out and update this page to reflect the new workflow (if
it is Customer Support Operations managed)!

### Currently used Slack workflows

This section serves as a form of "backup" for the Slack workflows we manage, as
the current implementation of Slack workflows does not allow an export/import
option.

#### Support Contact Management

Locate at
[Support Contact Management](https://app.slack.com/workflow-builder/E03N1RJJX7C/workflow/Wf06U665AK5J)

1. Choose how to start the workflow
   - When an emoji reaction is used
   - Emoji reaction:
     - :admission_tickets:
   - Channels:
     - #support_gitlab-com
     - #support_leadership
     - #support_licensing-subscription
     - #support_operations
     - #support_self-managed
     - #support_ticket-attention-requests
1. Reply to a message in thread
   - Select a message to reply to: Reference to the message that was reacted to
   - Add a reply:
     > Hello VARIABLE!
     >
     > The management of support contacts for a Zendesk Global organization can
     > only be done by the users of the organization, and will be done via a
     > Support Operations ticket. The information for this can be found at
     > `https://about.gitlab.com/support/managing-support-contacts/`. This page
     > also contains the exact links to use to contact the Support Ops team in
     > regards to contact management. The specific form linked on this page will
     > not automatically close out a case.
     >
     > Note that nothing that is auto-generated on the page, such as the
     > `Choose the reason why you are reaching out to us today`, should be
     > changed to ensure proper ticket routing.
     >
     > Please direct your customer to that page and encourage them to fully read
     > the information therein. From there, they should make a decision on the
     > next course of action in regards to their support contacts that best
     > suits their company.

     - Variables
       - User who sent the message that was reacted to (@display name)

Permissions:

- Managers:
  - Jason Colyer
  - Nabeel Hasan
  - Alyssa Villa - Dionela
  - Dylan Tragjasi
  - Sarah Cole
  - Rene Verschoor
  - Lyle Kozloff
- Can find this workflow
  - Everyone in GitLab
- Can copy this workflow
  - Workflow managers only
