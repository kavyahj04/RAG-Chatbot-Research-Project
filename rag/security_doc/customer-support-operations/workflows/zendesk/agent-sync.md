---
title: Agent Sync
description: Operations workflow page for agent sync
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/agent-sync"
---

{{% alert title="Note" color="primary" %}}

Agent sync changes are classified as ad-hoc. Once changes are made to the repo, they will be applied on the next run.

{{% /alert %}}

## Runtimes

Agent sync runs during the following times:

- Zendesk Global: Runs a 0000 UTC every day (`0 0 * * *`)
- Zendesk US Government: Runs a 0000 Pacific every day (`0 0 * * *`)

## Request for changes

Requests to make changes to the agent sync (or components therein) require specific levels of approval:

- Changes to signatures: Support Director
- Changes to displayed name: Support Director
- Changes to mid-ticket feedback information: Support Director
- Changes to tagging: Support Director and Support Data Specialist
- Changes to Zendesk field values: Sr. Support Engineering Manager - Operations
- Anything else: Support Manager

The approval is required to procced. If it has not been granted, the request should be rejected.

## Making changes

Making the changes would be done by modifying the script files within the project. You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).
