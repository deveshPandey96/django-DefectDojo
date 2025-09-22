---
title: "DSOP Scan"
toc_hide: true
---
Import XLSX findings from DSOP vulnerability scan pipelines.

### Sample Scan Data
Sample DSOP Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/dsop).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- vulnerability ids
