---
title: "Crashtest Security"
toc_hide: true
---
Import JSON Report Import XML Report in JUnit Format

### Sample Scan Data
Sample Crashtest Security scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/crashtest_security).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
