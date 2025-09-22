---
title: "Outpost24 Scan"
toc_hide: true
---
Import Outpost24 endpoint vulnerability scan in XML format.

### Sample Scan Data
Sample Outpost24 Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/outpost24).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
