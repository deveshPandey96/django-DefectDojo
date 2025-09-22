---
title: "Veracode SourceClear"
toc_hide: true
---
Import Project CSV or JSON report

### Sample Scan Data
Sample Veracode SourceClear scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/veracode_sca).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- vulnerability ids
- component name
- component version
- severity
