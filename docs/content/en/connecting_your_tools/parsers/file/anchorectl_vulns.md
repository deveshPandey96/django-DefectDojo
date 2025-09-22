---
title: "AnchoreCTL Vuln Report"
toc_hide: true
---
AnchoreCTLs JSON vulnerability report format

### Sample Scan Data
Sample AnchoreCTL Vuln Report scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/anchorectl_vulns).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- severity
- component name
- component version
- file path
