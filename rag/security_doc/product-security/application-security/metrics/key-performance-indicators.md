---
title: "Application Security - Key Performance Indicators"
---

## Key Performance Indicators

These metrics track our team's capacity to handle critical security workloads.

### Merge Request Review Coverage Rate

This KPI tracks our ability to review security-relevant merge requests that introduced a vulnerability, with or without prior security review. It is tracked through a security review miss rate that we target to get as close to 0% as possible, as that would mean that any merge request that was reviewed by the application security team did not end up introducing a vulnerability.

#### What I Need To Do To Have This KPI Measured?

1. __Merge Request Classification Requirements__
   - `AppSecWorkType::VulnFixVerification` must be applied to security fix verification Merge Requests
   - `AppSecWorkType::SecurityMRReview` must be applied to all other security code reviews, including those performed during triage rotation or as part of the stable counter part MR review.

Those two labels are applied as part of our capacity metrics and our day-to-day operation. You can find more details on the [capacity metric dedicated page](capacity.md) on the [Type of Work Classification](capacity.md#type-of-work-classification). To understand how we work and how we are applying those labels, you can consult our dedicated page about [Milestone Planning](../milestone-planning.md).

1. __Vulnerability Source Tracking__
   - Apply `appsec-kpi::vulnerability-introduced` label to Merge Requests identified as introducing vulnerabilities

1. __Vulnerability Prevention Tracking__
   - Apply `appsec-kpi::vulnerability-prevented` label to Merge Requests where vulnerabilities were identified and prevented during security review

#### Calculation Method

```text
`Security Review Miss Rate` = (Merged Vulnerability-introducing Merge Requests with Application Security review / Total vulnerability-introducing Merge Requests) * 100
```

Where:

- Total vulnerability-introducing Merge Requests = Merge Requests labeled with `appsec-kpi::vulnerability-introduced`
- Vulnerability-introducing Merge Requests _without_ Application Security review = `appsec-kpi::vulnerability-introduced` Merge Requests lacking both `AppSecWorkType::SecurityMRReview` or `AppSecWorkType::VulnFixVerification`
- Merged Vulnerability-introducing Merge Requests with Application Security review = `appsec-kpi::vulnerability-introduced` Merge Requests with either `AppSecWorkType::SecurityMRReview` or `AppSecWorkType::VulnFixVerification`
