---
title: "Invicti"
toc_hide: true
---
Vulnerabilities List - JSON report

### Sample Scan Data

Sample Invicti scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/invicti).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- description
- severity
