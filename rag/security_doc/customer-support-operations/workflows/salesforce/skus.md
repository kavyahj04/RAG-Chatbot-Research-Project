---
title: SKU Mapping
description: Operations workflow page for SKU mapping
canonical_path: "/handbook/security/customer-support-operations/workflows/salesforce/skus"
---

{{% alert title="Note" color="danger" %}}

This directly impacts the calculated support entitlement of our customers in Zendesk. Exercise extreme caution in making changes.

{{% /alert %}}

When a SKU (product rate charge) is created, renamed, deleted, or redefined, we need to update both the [gitlab_support_readiness gem](https://rubygems.org/gems/gitlab_support_readiness) and [Product Rate Charge Name mapping google sheet](https://docs.google.com/spreadsheets/d/1bJEq_q3h2fM3E8xWxYoFgZLdryWi_Cn5WLtzGSjuUUI/edit?usp=sharing) (internal only) to reflect it.

Remember changes here can have an impact on the ZD-SFDC sync, so consider that as well when you are making changes to the SKU mapping.
