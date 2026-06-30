---
title: Agents
description: Operations documentation page for Zendesk agents
canonical_path: "/handbook/security/customer-support-operations/docs/zendesk/agents"
---

{{% alert title="Note" color="primary" %}}

This is an informational page for the Zendesk agents. It may not reflect the way we actually manage Zendesk agents.

- If you are looking for information about modifying the agent sync, please see [agent sync workflow](../../workflows/zendesk/agent-sync)
- If you are looking for information about provisioning agents, please see [provisioning workflow](../../workflows/zendesk/provisioning)

{{% /alert %}}

In Zendesk, agents are those who have abilities beyond end-users (and thus access the agent workspace).

We largely manage agents via the agent sync (for the Support team) and via provisioning/deprovisioning.

## Agent Sync

{{% alert title="Note" color="primary" %}}

This solely applies to those who have YAML files in [Support team YAML files](../gitlab/support-team-yaml-files/)

{{% /alert %}}

The agent sync is how we manage the Support teams various metadata within Zendesk. This is run on a scheduled pipeline via the corresponding project:

- [Zendesk Global](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/agents)
- [Zendesk Us Federal](https://gitlab.com/gitlab-com/support/support-ops/zendesk-us-federal/agents)

Each run will update the following for the agents:

- GitLab.com user ID
- GitLab.com username
- Groups
- Manager tag
- Name
- Out of Office status
- Signature
- Some user tags
- User region (Zendesk Global only)

Any modifications to a Support agent in Zendesk will be overridden by this.

## Manually creating an agent

{{% alert title="Note" color="danger" %}}

This should never be done unless specifically indicated in workflow, such as the [provisioning workflow](../../workflows/zendesk/provisioning)

{{% /alert %}}

To create an agent in Zendesk:

1. a
