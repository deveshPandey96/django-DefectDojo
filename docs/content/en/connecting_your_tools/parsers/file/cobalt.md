---
title: "Cobalt.io Scan"
toc_hide: true
---
CSV Report

### Sample Scan Data
Sample Cobalt.io Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/cobalt).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
