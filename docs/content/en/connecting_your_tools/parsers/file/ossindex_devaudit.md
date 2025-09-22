---
title: "OssIndex Devaudit"
toc_hide: true
---
Import JSON formatted output from \[OSSIndex
Devaudit\](<https://github.com/sonatype-nexus-community/DevAudit>).

### Sample Scan Data
Sample OssIndex Devaudit scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/ossindex_devaudit).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
