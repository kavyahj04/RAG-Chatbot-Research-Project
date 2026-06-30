---
title: Pagerduty
description: Operations documentation page for Pagerduty
canonical_path: "/handbook/security/customer-support-operations/docs/pagerduty/"
---

{{% pageinfo color="warning" %}}

This is an information page for the Pagerduty components Customer Support Operations utilizes.

If you are looking for information about using or managing them, please see [workflows](../../workflows).

{{% /pageinfo %}}

## Schedules

We currently utilize the following schedules:

- [Customer Support Operations](https://gitlab.pagerduty.com/schedules/PXYIFEP)
  - Timezone: UTC
  - Layers:
    - AMER
      - Rotation type: weekly
      - Handoff time: Monday 04:00 PM
      - Restrict on-call shifts to specific times:
        - from 04:00 PM to 12:00 AM
    - APAC 1
      - Rotation type: weekly
      - Handoff time: Monday 12:00 AM
      - Restrict on-call shifts to specific times:
        - from 12:00 AM to 4:00 AM
    - APAC 2
      - Rotation type: weekly
      - Handoff time: Monday 04:00 AM
      - Restrict on-call shifts to specific times:
        - from 04:00 AM to 08:00 AM
    - EMEA
      - Rotation type: weekly
      - Handoff time: Monday 08:00 AM
      - Restrict on-call shifts to specific times:
        - from 08:00 AM to 04:00 PM

## Escalation Policies

We currently utilize the following escalation policies:

- [Customer Support Operations](https://gitlab.pagerduty.com/escalation_policies/PKNCI0R)
  - Immediately after an incident is triggered
  - Notify the following users or schedules
    - [Customer Support Operations](https://gitlab.pagerduty.com/schedules#PXYIFEP) 
    - escalates after 10 minutes
  - Notify the following users or schedules
    - Jason Colyer
    - escalates after 10 minutes
  - Notify the following users or schedules
    - Lyle Kozloff
    - escalates after 10 minutes
  - If no one acknowledges, repeat this policy 5 times

## Services

We currently utilize the following services:

- [Customer Support Operations](https://gitlab.pagerduty.com/service-directory/PIETVIG)
  - Integrations
    - None
  - Workflows
    - None
  - Settings
    - Assign and Notify
      - Assign to escalation policy: [Customer Support Operations](https://gitlab.pagerduty.com/escalation_policies/PKNCI0R)
      - How should responders be notified: High-urgency notifications, escalate as needed
      - When incidents are not actioned, automatically:
        - All options unchecked
    - Reduce Noise
      - Currently not grouping alerts on this service.
    - Coordinate Responders and Stakeholders
      - Conference Bridge Dial-In Number: none
      - Conference Bridge Meeting URL: none
    - Event Management
      - Not used
    - Remediate
      - Documentation link: No documentation link listed for this service 
      - Custom Incident Actions: No custom incident actions on this service
  - Service Dependencies
    - None
