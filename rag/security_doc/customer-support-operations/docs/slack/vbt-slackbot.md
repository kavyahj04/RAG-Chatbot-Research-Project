---
title: VBT Slackbot
description: Operations documentation page for very breached ticket slackbot
canonical_path: "/handbook/security/customer-support-operations/docs/slack/vbt-slackbot"
---

<sup>*Introduced via [gitlab-com/support/support-team-meta#5486](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/5486)*</sup>

{{% pageinfo color="info" %}}

This is an informational page for the VBT Slackbot. It may not reflect the way we actually manage it.

If you are looking for information about maintaining it, please see [our workflows](../../workflows/)

{{% /pageinfo %}}

## Where does it live

It lives within the Readiness namespace at the [Very Breached Ticket Slackbot project](https://gitlab.com/gitlab-support-readiness/slack/very-breached-ticket-slackbot).

## How does it work

It runs via the following scheduled pipelines:

| Name | Interval |
|------|----------|
| Managers AMER | `0 14 * * 1-5` Etc/UTC |
| Managers APAC | `30 21 * * 0-4` Etc/UTC |
| Managers EMEA | `0 7 * * 1-5` Etc/UTC |

During each run, a Zendesk view preview is generated using the following criteria:

- ALL
  - Time since SLA breach is greater than 48  hours
  - Ticket form is not Billing
  - Ticket form is not Support Ops
  - Ticket status is less than solved (i.e. new, open, pending, on-hold)
- ANY
  - Ticket stage is Emergencies
  - Ticket stage is FRT

The tickets showing in the Zendesk view preview using those conditions are then used in generating a message that is posted to via Slack in the [#spt_leaders-daily](https://gitlab.enterprise.slack.com/archives/C03LL7Z2291) channel.
