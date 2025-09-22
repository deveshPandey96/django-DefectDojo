---
title: "Openscap Vulnerability Scan"
toc_hide: true
---
Import Openscap Vulnerability Scan in XML formats.

### Sample Scan Data
Sample Openscap Vulnerability Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/openscap).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
