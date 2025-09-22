---
title: "Node Security Platform"
toc_hide: true
---
Node Security Platform (NSP) output file can be imported in JSON format.

### Sample Scan Data
Sample Node Security Platform scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/nsp).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
