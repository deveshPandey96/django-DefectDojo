---
title: "Rubocop Scan"
toc_hide: true
---
Import Rubocop JSON scan report (with option -f json).

### Sample Scan Data
Sample Rubocop Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/rubocop).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- vuln id from tool
- file path
- line
