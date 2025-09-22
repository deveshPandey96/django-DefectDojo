---
title: "Bugcrowd"
toc_hide: true
---
Import Bugcrowd results in CSV format.

### Sample Scan Data
Sample Bugcrowd scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/bugcrowd).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
