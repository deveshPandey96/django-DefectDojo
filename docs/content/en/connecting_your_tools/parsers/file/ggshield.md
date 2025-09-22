---
title: "Ggshield"
toc_hide: true
---
Import [Ggshield](https://github.com/GitGuardian/ggshield) findings in JSON format.

### Sample Scan Data
Sample Ggshield scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/ggshield).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
