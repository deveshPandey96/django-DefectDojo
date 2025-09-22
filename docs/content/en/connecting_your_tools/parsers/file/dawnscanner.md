---
title: "DawnScanner"
toc_hide: true
---
Import report in JSON generated with -j option

### Sample Scan Data
Sample DawnScanner scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/dawnscanner).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
