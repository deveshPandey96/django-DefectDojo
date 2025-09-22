---
title: "Clair Scan"
toc_hide: true
---
You can import JSON reports of Docker image vulnerabilities found by a Clair scan or the Clair Klar client.

### Sample Scan Data
Sample Clair Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/clair).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- vulnerability ids
- description
- severity
