---
title: "Application Security Team Organization"
description: Application Security page on how the team is organized
---

This page provides you with the resources:

- To understand how the work of the team is organised
- To know in which repositories we are performing our work

## Work Organization

The Application Security team organizes the work on a monthly milestone basis. To know more how we do it, please consult our specific milestone planning page [here](milestone-planning.md)

## Important Repositories

The Application Security team maintains several key repositories that support [our mission](_index.md#application-security-mission). These repositories enable collaboration with Engineering and Product teams while maintaining our security standards and processes.

### Team organization and planning

**Purpose**: Central repository for team operations, issue tracking, and cross-team collaboration  
**Location**: [appsec-team tracker](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/appsec-team)  
**Key Uses**:

- Track team initiatives and operational improvements
- Coordinate cross-team collaboration efforts
- Plan milestone work

### Application Security reviews

**Purpose**: Repository to request and perform AppSec reviews  
**Location**: [appsec-team reviews](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/appsec-reviews/)  
**Key Uses**:

- Feature design reviews
- Architecture assessments

Learn more about our security review process in our [dedicated page](appsec-reviews.md)).

### Security Tools & Automation

**Purpose**: Houses our automation tooling  
**Location**: [Tooling repository](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/tooling)  
**Key Uses**:

- Automation scripts

### Threat Modeling Resources

**Purpose**: Templates and documentation for threat modeling activities  
**Location**: [Threat modeling repository](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/threat-models)  
**Learn More**: [Threat Modeling Process](./threat-modeling/)

### PSIRT Operations

**Purpose**: Central repository for PSIRT team operations and issue tracking.  
**Location**: `gitlab-com/gl-security/product-security/appsec/psirt`  
**Learn More**: [PSIRT Services](./appsec-operations/psirt-services/)

## Useful Information For External Customers

### Public Security Resources

- [GitLab Security Disclosure](https://about.gitlab.com/security/disclosure/)
  - Details our coordinated security disclosure policy and process
- [HackerOne Bug Bounty Program](https://hackerone.com/gitlab)
  - Our Bug Bounty HackerOne program policy
- [GitLab Release and Patch Releases Process](/handbook/engineering/releases/)
  - Consult our Handbook page dedicated to our Release and Patch Release Process
  
### Documentation

- [How to Secure our Application Using GitLab Application Security Features](https://docs.gitlab.com/ee/user/application_security/secure_your_application.html)
- GitLab Instance Hardening Recommendations:
  - Our [official documentation](https://docs.gitlab.com/security/hardening/) (shipped with each version and available in self-managed instance documentation)
  - Our [Handbook recommendations](https://about.gitlab.com/security/hardening/)
