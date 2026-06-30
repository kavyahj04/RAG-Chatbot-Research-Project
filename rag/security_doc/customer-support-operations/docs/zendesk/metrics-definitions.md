---
title: Metrics definitions
description: Operations documentation page for Zendesk metrics definitions
canonical_path: "/handbook/security/customer-support-operations/docs/zendesk/metrics-defintions"
---

{{% alert title="Note" color="primary" %}}

These are how Zendesk itself defines various metrics, not how GitLab does. GitLab might define them differently.

{{% /alert %}}

## FRT

This is the time a ticket spent from creation until it received its first public reply from an agent.

## NRT

This is the time a ticket spent from a public reply from an end-user until it received a public reply from an agent.

## Requester wait time

This is the total time a ticket spent in the following statues:

- New
- Open
- On-hold

## Agent work time

This is the total time a ticket spent in the following statues:

- New
- Open

## Agent wait time

This is the total time a ticket spent in the following statues:

- Pending

## On-hold time

This is the total time a ticket spent in the following statues:

- On-hold

## Total resolution time

This is the total time a ticket spent in the following statues:

- New
- Open
- Pending
- On-hold

## Periodic update

This is the time a ticket spends between public agent replies.

## Pausable update

This is the time a ticket spends between public agent replies while in the following statuses:

- New
- Open
- On-hold

## Futher reading

- [Understanding which SLA metrics you can measure](https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-SLA-policies)
- [About native Support time duration metrics](https://support.zendesk.com/hc/en-us/articles/4408834848154-About-native-Support-time-duration-metrics)
