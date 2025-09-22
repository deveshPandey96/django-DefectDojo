---
title: "Gosec Scanner"
toc_hide: true
---
Import Gosec Scanner findings in JSON format.

### Sample Scan Data
Sample Gosec Scanner scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/gosec).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
