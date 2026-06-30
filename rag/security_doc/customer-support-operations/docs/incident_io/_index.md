---
title: incident.io
description: Operations documentation page for incident.io
canonical_path: "/handbook/security/customer-support-operations/docs/incident_io/"
---

{{% pageinfo color="warning" %}}

This is an information page for the incident.io components Customer Support Operations utilizes.

If you are looking for information about managing them, please see [workflows](../../workflows).

If you are looking for information on how it is used in incidents, please see [Handling Incidents](/handbook/security/customer-support-operations/workflows/incidents).

{{% /pageinfo %}}

## Working with incidents

### Creating an incident

To create an incident:

1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page you want to make an incident on
1. Click `Publish incident` at the top-right
1. Fill out a meaningful `Name`
1. Set the `Status` of the incident
   - Investigating: Report an incident
   - Identified: Problem has been determined and a fix is being made
   - Monitoring: Fix is implemented and we are monitoring the situation
   - Resolved: Everything is good to go
1. Set a meaningful `Message` for the incident
1. Set the level of impact on `Affected components`
   - No impact: The incident does not impact this component
   - Degraded performance: The component is working but at lower than standard performance levels
   - Partial outage: Significant parts of the component are not working
   - Full outage: The component is hard down
1. Click `Review incident`
1. Review all information for accuracy
1. Click `Publish incident`
1. Publishing an update to an incident (including resolving it)

### Updating an incident

To update an incident (including resolving it):

1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page the incident is on
1. Click on the incident in question
1. Click the top-right status bar (says what the current status is)
1. Select the new `Status`
1. Enter a meaningful message
1. Click `Review update`
1. Review all information for accuracy
1. Click `Publish update`

### Deleting an incident

To delete an incident:

1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page the incident is on
1. Click on the incident in question
1. Click the `...` at the top-right of the page
1. Click `Delete status page incident`
1. Click `Delete incident`

## Working with maintenance

### Scheduling maintenance

To create (schedule) maintenance:

1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page you want to make an incident on
1. Click on `Maintenance`
1. Click `Schedule maintenance` at the top-right of the page
1. Fill out a meaningful `Name`
1. Ensure `Automatically update status` is checked
1. Set the `Impact window` (keep in mind it is using local time)
1. Set a meaningful `Message`
1. Set the level of impact on `Affected components`
   - No impact: The maintenance does not impact this component
   - Under maintenance: The maintenance does impact this component
1. Click `Review`
1. Review all information for accuracy
1. Click `Publish maintenance`

### Updating maintenance

To update maintenance:

1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page you want to make an incident on
1. Click on `Maintenance`
1. Click the maintenance in question
1. Click the top-right status bar (says what the current status is)
1. Select the new `Status`
1. Enter a meaningful message
1. Click `Review update`
1. Review all information for accuracy
1. Click `Publish update`

### Deleting maintenance

To delete maintenance:

1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page you want to make an incident on
1. Click on `Maintenance`
1. Click the maintenance in question
1. Click the `...` at the top-right of the page
1. Click `Delete status page incident`
1. Click `Delete incident`

## Our Setup

### Components catalog

Source: [Customer Support Operations components](https://app.incident.io/gitlab/catalog/01JXZ8QTFEYF84RP0V80MG1VAP)

This contains all the pieces we would report outages on. The steps to create it were as follows:

1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click [Add a custom type](https://app.incident.io/gitlab/catalog/create)
1. Enter a `Name`
1. Enter a `Description`
1. Under `Categories` click `+ Services`
1. Ensure `Are entries of this type ranked?` checkbox is checked
1. Ensure `Reference entries by name` checkbox is checked
1. Click `Save` at bottom-right

Once created, components are added via the following steps:

1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click the catalog to add components to
1. Click `Create entry` at the top-right
1. Enter a `Name`
1. Click `Create` at the bottom-right
1. Repeat as needed

### Groups catalog

Source: [Customer Support Operations groups](https://app.incident.io/gitlab/catalog/01JXZ8X7HVN23T3773PGXB5NNR)

This contains all the groups we would use (we only use one currently). The steps to create it were as follows:

1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click [Add a custom type](https://app.incident.io/gitlab/catalog/create)
1. Enter a `Name`
1. Enter a `Description`
1. Under `Categories` click `+ Services`
1. Ensure `Are entries of this type ranked?` checkbox is checked
1. Ensure `Reference entries by name` checkbox is checked
1. Click `Save` at bottom-right

Once created, groups are added via the following steps:

1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click the catalog to add groups to
1. Click `Create entry` at the top-right
1. Enter a `Name`
1. Select all components applicable
1. Enter `gitlab.com` for the `Email domains`
1. Click `Create` at the bottom-right
1. Repeat as needed

### Status page

Live at [https://statuspage.incident.io/cust-support-ops/main](https://statuspage.incident.io/cust-support-ops/main) (requires use of gitlab.com email address for authentication)

Source: [Customer Support Operations Status](https://app.incident.io/gitlab/status-pages/01JXZ9CT4V8HHVJYJDP7XY7B4T/overview/now)
￼
This is the actual status page. The steps to create it were as follows:

1. Go to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click [Create customer page](https://app.incident.io/gitlab/status-pages/customer/create)
1. Enter a `Page title`
1. Enter `Status page URL` (if you want to change the auto-generated one)
1. Under `Customer pages`
   - Click `Use an existing catalog type`
   - Set `Which catalog type defines the customers you'd like to create?` to the `Groups` catalog created previously
   - Set `Which catalog attribute represents your components?` to `Components`
   - Set `Which catalog attribute represents allowed email domains?` to `Email domains`
1. Under `Pages`
   - Set the `Page name`
   - Set the `URL`
1. Under `Page setup`
   - Set `Theming` to `Dark mode`
   - Select a `Company logo` (if desired)
   - Select a `Favicon` (if desired)
1. Click `Create status page` at the bottom-right of the page
