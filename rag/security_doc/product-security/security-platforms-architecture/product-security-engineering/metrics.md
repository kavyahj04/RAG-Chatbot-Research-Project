---
title: "Metrics"
description: "Metrics measured and tracked bv the GitLab Product Security Engineering team"
---

## Metrics

The Product Security Engineering team currently tracks the following metrics:

- Number of Merge Requests merged into GitLab products directly related to implementing the functionality required by Product Security teams
- Number of Merge Requests for creating security enhancements, defense in depth measures, and paved roads
- The percentage of distinct value propositions in current in-house custom tools that have been contributed to the product

These can be observed in this [Tableau dashboard](https://10az.online.tableau.com/#/site/gitlab/views/ProductSecurityEngineering/ProdSecEngValueDeliveryMetrics?:iid=6).

### Metrics Labels

Labels are a driving force behind our metrics collection. The appropriate label must be applied to the relevant issue, merge request, or epic.

| Type of Work | Label | Where to apply label |
| --- | --- | --- |
| Product Security team requirement: functionality within the product required by GitLab Product Security teams | `~ProdSecEngMetric::ProdSecRequirement` | Issues and Merge Requests, sometimes Epics |
| Defense in Depth: an MR that modifies existing non-vulnerable functionality to be more robust if an "earlier" security control fails | `~ProdSecEngMetric::Defense in Depth` | Issues and Merge Requests, sometimes Epics |
| Paved Road: a new tool, method, class, check that, gives GitLab's contributors an easier way to perform an activity securely | `~ProdSecEngMetric::Paved Road` | Issues and Merge Requests, sometimes Epics |
| Tooling Integration: work done as part of the effort to integrate functionality from custom in-house tooling into a GitLab product | `~ProdSecEngMetric::Tooling Integration` | Issues and Merge Requests, sometimes Epics |
| Custom Tooling: work performed to build, maintain, or augment outside-of-the-product custom tooling needed to satisfy Product Security requirements | `~ProdSecEngMetric::Custom Tooling` | Issues and Merge Requests, sometimes Epics |
| Pending: the work type isn't entirely clear yet, but we don't want to block progress for now | `~ProdSecEngMetric::Pending` | Issues, Merge Requests, and Epics |
| Sunsetting: for issues that represent a specific feature or piece of functionality required to eventually deprecate a custom tool used by Product Security teams | `~ProdSecEngMetric::Sunsetting` | Issues in the [product-security-engineering-team repo](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/product-security-engineering-team/-/issues) |
| Internal: for team tasks, e.g. processes & planning | `~ProdSecEngMetric::Internal` | Issues and Merge Requests, Epics |
