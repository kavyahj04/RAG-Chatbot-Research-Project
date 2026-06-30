---
title: Handling Incidents
description: Operations workflow for handling incidents
canonical_path: "/handbook/security/customer-support-operations/workflows/incidents"
---

Whenever an incident occurs, you should follow this process.

## Create an issue

Always create an issue using the [Incident template](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues?issuable_template=Incident). The information you put in it initially does not need to be "complete". It will often be a simplified title and the error/problem itself that is occuring.

## Create an incident

After the issue has been created, you need to publish an incident via incident.io (so it shows on our status page). To do this:

1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page you want to make an incident on
1. Click `Publish incident` at the top-right
1. Fill out a meaningful `Name`
1. Set the `Status` of the incident 
   - Investigating: Report an incident
     - This is normally what you would use as the starting point
   - Identified: Problem has been determined and a fix is being made
   - Monitoring: Fix is implementing and we are monitoring the situation
   - Resolved: Everything is good to go
1. Set a meaningful `Message` for the incident
   - You should include a link to your incident issue here
1. Set the level of impact on `Affected components` (the value needed depends on the impact of the incident)
   - No impact: The incident does not impact this component
   - Degraded performance: The component is working but at lower than standard performance levels
   - Partial outage: Significant parts of the component is not working
   - Full outage: The component is hard down
1. Click `Review incident`
1. Review all information for accuracy
1. Click `Publish incident`

## Determine criticality level

After issue creation, you need to determine the criticality level of the incident. This is done by locating the impacted items on the [Customer Support Operations System Criticality](https://docs.google.com/spreadsheets/d/1ERaPmkcpXlDQo7f7ROsIbyEcM4U03-5xWsKLp9vKOcE/edit?usp=sharing) Google sheet (internal access only).

In the event an incident is impacting multiple systems, use the _highest_ criticality value.

## Work to resolve the problem

With that out of the way, you will work to resolve the problem. Make sure to make ample commnets on the issue as you do.

As you do, remember to provide periodic updates to the incident.

### Updating an incident

To do this:

1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page you want to make an incident on
1. Click `Publish incident` at the top-right
1. Fill out a meaningful `Name`
1. Set the `Status` of the incident
   - Investigating: Report an incident
   - Identified: Problem has been determined and a fix is being made
   - Monitoring: Fix is implementing and we are monitoring the situation
   - Resolved: Everything is good to go
1. Set a meaningful `Message` for the incident
1. Set the level of impact on `Affected components`
   - No impact: The incident does not impact this component
   - Degraded performance: The component is working but at lower than standard performance levels
   - Partial outage: Significant parts of the component is not working
   - Full outage: The component is hard down
1. Click `Review incident`
1. Review all information for accuracy
1. Click `Publish incident`

## Escalate

In some situations, you will not be able to resolve an incident quickly enough and will need to escalate it. The time between escalation levels is going to depend on the criticality level of the incident:

| Criticality level | Time to Resolve | Escalate up to | Time to escalate to next level | Special notes |
|-------------------|-----------------|:--------------:|--------------------------------|---------------|
| Mission Critical | 1-2 hours | Level 4 | 10 minutes without a resolution path | |
| Business Critical | 2-4 hours | Level 3 | 30 minutes without a resolution path  | |
| Business Operational | 24-48 hours | Level 2 | 8 hours without a resolution path  | Move to level 3 is not resolved in time |
| Administrative | 48-72 hours | Level 2 | 24 hours without a resolution path  | Move to level 3 is not resolved in time |

As an example, if you are working an `Administrative` level incident:

- You have 24 hours to try to resolve it yourself
- After 24 hours with no clear path to resolution, you must escalate to level 1
- After 48 hours with no clear path to resolution, you must escalate to level 2
- After 72 hours with no clear path to resolution, you must escalate to level 3. This is because it has now surpassed the documented time to resolve the incident

As another example, if you are working a `Mission Critical` level incident:

- You have 10 minutes to try to resolve it yourself
- After 10 minutes with no clear path to resolution, you must escalate to level 1
- After 20 minutes with no clear path to resolution, you must escalate to level 2
- After 30 minutes with no clear path to resolution, you must escalate to level 3
- After 40 minutes with no clear path to resolution, you must escalate to level 4

### Escalation levels

| Level | Action |
|:-----:|--------|
| 1 | Post in team channel asking for assistance |
| 2 | Page Customer Support Operations Specialist oncall |
| 3 | Page Fullstack Engineer, Customer Support Operations oncall |
| 4 | Page Sr. Support Engineering Manager - Operations |

## Resolve the issue

Once you have resolved the incident, you need to resolve the issue you created. This is normally done by cross-linking MRs to thhe issue or by detailing what was done to fix the problem.

Once that is done, you can close the issue, _unless_ an [After Incident Review](#after-incident-review) is required.

## Resolve the incident

See [Updating an incident](#updating-an-incident). Remember the `Status` to use is `Resolved`.

## After Incident Review

{{% alert title="Note" color="danger" %}}

For criticial level 1 and 2 incidents, as well as incidents that required an escalation to level 3, an after incident review is _required_.

{{% /alert %}}

For this, you will utilize the [Customer Support Operations After Incident Reviews Google doc](https://docs.google.com/document/d/1aUEHYWa-RWpiUUM34yWGMxIYgFnL6qaCCXu954H5Zqo/edit?tab=t.72mh0ffa6o0f) (internal only).

Make a duplicate of the `Template` tab, and then fill it in completely. You can use previous documents as an example of what is needed.

Make sure to notify the Sr. Support Engineering Manager - Operations of the document once you have completely filled it in.
