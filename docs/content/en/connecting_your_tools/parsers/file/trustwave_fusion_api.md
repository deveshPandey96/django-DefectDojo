---
title: "Trustwave Fusion API Scan"
toc_hide: true
---
Trustwave Fusion API report file can be imported in JSON format

### Sample Scan Data
Sample Trustwave Fusion API Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/trustwave_fusion_api).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
