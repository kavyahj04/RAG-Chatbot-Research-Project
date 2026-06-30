---
title: "Information Security and Artificial Intelligence Management System"
controlled_document: true
---

## Purpose

GitLab has adopted the ISO/IEC 27001:2022 standard for our information security management system (ISMS) and ISO/IEC 42001:2023 for our artificial intelligence management system (AIMS) to provide GitLab team members, customers and community members with a high level of assurance on the robustness of our information security policies, standards and procedures, and the strength of our control environment. The purpose of this document is to define the boundaries and objectives of GitLab's information security and artificial intelligence management system.

## Scope

The scope of GitLab's ISMS is limited to the production resources that directly support GitLab SaaS subscriptions: GitLab.com and GitLab Dedicated.

The scope of GitLab's AIMS covers GitLab's role as an AI provider for the AI service GitLab Duo and its components.

### Assets

Assets within the scope of the management system include: customer data, software, people, and internal information assets to host and operate the cloud-based solution.

External assets that are subject to shared responsiblity include cloud service providers and artificial intelligence providers. The scope of shared responsibility considerations include: assets maintained and stored in the cloud computing environment, infrastructure assets management, processes that run on a multi-tenant virtualized environment, cloud service administration, and development and enhancement of AI models.

### Excluded from Scope

As an all remote company, there are no physical office locations in the scope of the management system. Contracted third party data center services to include physical and environmental controls are not in scope and are managed by the third party service providers.

### Locations

GitLab's headquarter mailing address is in scope and covers all sub organizations. Please note this is a mailing address only, there is no physical location to visit:

- GitLab Inc, 268 Bush Street #350, San Francisco, CA 94104, United States of America

### Organizational Units

Business functions included in the scope of the management system include:

- Security - Chief Information Security Officer; Security Assurance; Product Security; Security Operations; Threat Management Security teams. Division structure is defined [here](/handbook/security/#division-structure)
- Engineering - VP of Development
- Engineering - VP of Infrastructure and Quality
- Finance - VP of Information Technology
- People Operations - VP of Total Rewards and People Operations, Technology and Analytics
- Legal - VP of Legal Operations; Senior Director, Contracts and Legal Operations; Director of Legal, Privacy and Product
- Data Science - Responsible for leveraging ML and AI capabilities in the GitLab product, providing applied AI capabilities, and preventing abuse in the application.

### Interested Parties

This management system governs GitLab security operations. Interested parties include:

- Customers
  - Require GitLab to operate according to this management system to protect their information
- Shareholders/owners of the business
  - Require GitLab to operate in a secure manner to maintain a sustainable business
- Team Members
  - GitLab requires Team Members to operate in a secure manner as defined by this management system. Require GitLab to operate in a secure manner to maintain services and provide continued employment

## Management System Roles and Responsibilities

| Role | Responsibility |
| --- | --- |
| ISMS & AIMS Council | Oversight, implementation and continual improvement of the management system |
| Chief Information Security Officer | Executive sponsor of the management system; coordinate, promote and improve information security |
| Security Management (Code Owners) | Owner of the management system responsible for approving significant changes and exceptions of the management system |
| Security Assurance | Reporting on the performance of the information security management system to top management; security risk assessments and treatment; continuous monitoring and auditing; customer assurance activities; security awareness program; security governance activities |
| Product Security | Manage third party penetration and bug bounty programs; provide input to the software development lifecycle; manage application vulnerability program; administer security champions program; maintain application security tools; identify security risks; infrastructure vulnerability program; maintain infrastructure security tools; identify security risks |
| Security Operations | Monitor, manage and report on security incidents; monitor compliance with security policies through technical tools; identify security risks; monitor and respond to abuse of SaaS subscriptions |
| Corporate Security | Manage identity and access management, role based access control, admin access |
| Duo Product Management| Monitor performance of AI system; maintain AI system; identify AI risks; evaluation of the performance of AI model providers |
| Legal| Responsible for AI governance; third-party contracts; privacy reviews|
| Other management system business units | Implement, operate and/or administer information security requirements; remediate information security findings; collaborate with the Security department |
| All GitLab Team Members | Awareness of responsibilities as it relates to information security; adherence to information security controlled documents; reporting of suspected security violations |

## Implementation Manual Procedure

### Leadership

GitLab is committed to information security. The general objective for the ISMS is to protect GitLab's confidential information and assets against new and existing security and privacy risks while maintaining confidentiality, integrity and availability. Objectives for individual security controls are inherited by the in scope security standards and regulations which are: ISO 27001:2022, and SOC 2 Type 2.

The council, comprised of Security and Privacy (Legal) leadership, shall meet on a minimum of an annual basis to discuss the state of the management system and measure the fulfillment of all management system objectives. The following topics will be covered:

- Review of membership and objectives
- ISMS & AIMS Internal Audit Results
- Significant controlled document updates
- Results of the Annual Security Risk Assessment
- Changes to Risk Heatmap (trends)
- Output from Continuous Control Monitoring
- Observations (CA/PAs)
- Changes that could affect the management system
- Feedback and improvements
- Management system inputs and outputs

### Planning

GitLab has implemented a formal [Security Operational Risk Management ("StORM") program](/handbook/security/security-assurance/security-risk/storm-program/) to identify, rank, track, and treat cybersecurity, IT, and privacy operational risks in support of GitLab's organization-wide objectives. Internal and external issues that could impact GitLab's ability to achieve the intended outcomes of the ISMS and AIMS are identified as part of the StORM or [Observation Management Program](/handbook/security/security-assurance/observation-management-procedure.md). The process for selecting in scope information security controls is executed by the Security Compliance team, leveraging technical functionality from the third party GRC application, and overseen by the Security Risk team. Implementation status is captured in GitLab's GRC application as well as in the Statement of Applicability.

On an annual basis, the CEO will establish company objectives for the year that cascade down to all divisions, including Security and AI teams. These objectives ensure that security and AI management priorities remain aligned with GitLab's overall strategic direction, providing a framework for defining specific actions to support the intended outcomes of both the ISMS and AIMS.

### Support

GitLab has implemented a formal security awareness training program that includes: new hire security awareness training, global annual security awareness training and quarterly targeted phishing exercises. These trainings are administered through a third party portal and include a quiz to test understanding of the security topics presented.

A formal [controlled document procedure](/handbook/security/controlled-document-procedure/) is in place to ensure that there is consistency in developing and maintaining controlled documents at GitLab utilizing a hierarchal approach. All controlled documents are available to all GitLab team members and the public through the [GitLab handbook](/) unless otherwise noted. Updates to controlled documents are managed via [GitLab merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/) which are also accessible to all GitLab team members for the entire workflow. An annual review of controlled documents is required by the owner or assigned representative.

GitLab publishes [Job Families](/handbook/hiring/job-families/) to define roles and responsibilities based on level for all team members. This information is publicly available and the foundation for team member hiring and performance reviews. On a minimum of an annual basis, GitLab management executes [talent assessments](/handbook/people-group/talent-assessment/) with team members to ensure competency to Job Family.

### Operations

The [GitLab team handbook](/) is the central repository for how we run the company. Everything at GitLab is handbook first, to include development of company policies, standards and procedures. Key controlled documents that support the management system include:

- [Data Classification Standard](/handbook/security/standards/data-classification-standard/)
- [Internal Acceptable Use Policy](/handbook/people-group/acceptable-use-policy/)
- [Security Policies](/handbook/security/security-and-technology-policies/security-and-technology-policies-management/)
- [GitLab Code of Business Conduct and Ethics](https://ir.gitlab.com/static-files/7d8c7eb3-cb17-4d68-a607-1b7a1fa1c95d)
- [Infrastructure Change Management Procedure](/handbook/engineering/infrastructure-platforms/change-management/)
- [Security Operational Risk Management (StORM) Program & Procedures](/handbook/security/security-assurance/security-risk/storm-program/)
- [GitLab AI Ethics Principles for Product Development](/handbook/legal/ethics-compliance-program/ai-ethics-principles.md)
- [General Purpose AI Tool Usage Guidelines](https://internal.gitlab.com/handbook/legal-and-corporate-affairs/ai-tool-usage-guidelines/)
- [Approved AI Tools](https://internal.gitlab.com/handbook/company/ai-at-gitlab/#approved-ai-tools)

GitLab has a dedicated Security Compliance team responsible for monitoring design and effectiveness of the [GitLab common control framework](/handbook/security/security-assurance/security-compliance/sec-controls/) to ensure GitLab's security objectives are thoughtfully planned, implemented and monitored.

If using a third-party service to outsource or supplement security processes, a [third party risk assessment](/handbook/security/security-assurance/security-risk/third-party-risk-management/) is executed prior to onboarding. Critical vendors are also reviewed once per calendar year after onboarding, or at contract renewal if it comes first.

### Performance

GitLab monitors, measures, and improves security controls through various continuous monitoring measures, such as:

- [Continuous control testing/Annual management system internal compliance audits](/handbook/security/security-assurance/security-compliance/security-control-lifecycle/)
- [External audits (SOC 2 Type 2, TISAX, customer security assessments)](security-assurance/security-compliance/certifications/)
- [Annual security operational risk assessments](/handbook/security/security-assurance/security-risk/storm-program/)
- [Annual third-party penetration testing](/handbook/security/security-and-technology-policies/penetration-testing-policy/)
- [Ongoing third party scorecard monitoring (BitSight)](/handbook/security/security-assurance/field-security/independent_security_assurance/#third-party-security-ratings)
- [Infrastructure Vulnerability scanning](product-security/vulnerability-management/)
- [Application Vulnerability Scanning](product-security/application-security/vulnerability-management/)
- [HackerOne bug bounty program](/handbook/security/product-security/application-security/runbooks/hackerone-process/)
- [Audit log monitoring](/handbook/security/security-and-technology-policies/audit-logging-policy/)
- ISMS & AIMS Council (annual management review)

### Improvement

GitLab is committed to continually improving the suitability, adequacy and effectiveness of the management system.

As part of GitLab's tier 2 security operational risk program, each risk identified and triaged through the StORM program is required to undergo a [risk response decision](/handbook/security/security-assurance/security-risk/storm-program/#risk-response). This is an activity that will be discussed with each individual risk owner for the risks that they own. Additionally, GitLab identifies and monitors tier 3 risks, also referred to as observations, as per the [Observation Management Procedure](/handbook/security/security-assurance/observation-management-procedure/).

## Exceptions

Exceptions to Information Security policies or procedures will be tracked as per the [Information Security Policy Exception Management Process](/handbook/security/controlled-document-procedure/#exceptions).

## References

- [Controlled Document Procedure](/handbook/security/controlled-document-procedure/)
