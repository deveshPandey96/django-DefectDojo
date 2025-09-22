---
title: "Azure Security Center Recommendations Scan"
toc_hide: true
---
Azure Security Center recommendations can be exported from the user interface in CSV format.

### Sample Scan Data
Sample Azure Security Center Recommendations Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/azure_security_center_recommendations).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
