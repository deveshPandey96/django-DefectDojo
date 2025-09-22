---
title: "Testssl Scan"
toc_hide: true
---
Import CSV output of testssl scan report.

### Sample Scan Data
Sample Testssl Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/testssl).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
