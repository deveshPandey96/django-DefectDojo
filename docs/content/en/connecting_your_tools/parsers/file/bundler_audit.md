---
title: "Bundler-Audit"
toc_hide: true
---
Import the text output generated with bundle-audit check

### Sample Scan Data
Sample Bundler-Audit scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/bundler_audit).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
