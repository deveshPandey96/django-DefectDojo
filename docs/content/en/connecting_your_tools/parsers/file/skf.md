---
title: "SKF Scan"
toc_hide: true
---
Output of SKF Sprint summary export.

### Sample Scan Data
Sample SKF Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/skf).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
