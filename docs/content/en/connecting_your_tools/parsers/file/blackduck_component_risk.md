---
title: "Blackduck Component Risk"
toc_hide: true
---
Upload the zip file containing the security.csv and files.csv.

### Sample Scan Data
Sample Blackduck Component Risk scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/blackduck_component_risk).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
