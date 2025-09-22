---
title: "Hadolint"
toc_hide: true
---
Hadolint Dockerfile scan in json format.

### Sample Scan Data
Sample Hadolint scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/hadolint).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
