---
title: "ESLint"
toc_hide: true
---
ESLint Json report format (-f json)

### Sample Scan Data
Sample ESLint scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/eslint).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
