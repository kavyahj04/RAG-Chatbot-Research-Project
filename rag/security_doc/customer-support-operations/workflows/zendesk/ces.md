---
title: CES Surveys
description: Operations workflow page for CES Surveys
canonical_path: "/handbook/security/customer-support-operations/workflows/zendesk/ces"
---

{{% alert title="Note" color="primary" %}}

All changes to the CES form are classified as ad-hoc. Once changes are merged into the default branch, the form will be generated and live.

All changes to the CES processor are classified as ad-hoc. Once the changes are merged into the default branch, the code will begin being used.

All changes to the CES Survey Zendesk components (automations, ticket fields, triggers, etc.) are handled via a standard deployment.

All changes to the CES Survey zaps are classified as ad-hoc.

{{% /alert %}}

## CES Processor changes

Making the changes would be done by modifying the files within [the project](https://gitlab.com/gitlab-support-readiness/processors/ces-processor). You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

## CES Survey Form changes

Making the changes would be done by modifying the files within [the project](https://gitlab.com/gitlab-support-readiness/forms/ces-survey). You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

Once the MR is merged, they will then be used to populate the form.

## Zendesk Automations changes

Please see our [Zendesk automations workflow](./automations)

## Zendesk Ticket Fields changes

Please see our [Zendesk ticket fields workflow](./ticket-fields)

## Zendesk Triggers changes

Please see our [Zendesk triggers workflow](./triggers)

## Workato changes

Please see our [Workato workflow](../workato)
