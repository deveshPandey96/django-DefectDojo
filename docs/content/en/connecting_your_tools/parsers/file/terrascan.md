---
title: "Terrascan"
toc_hide: true
---
Import JSON output of terrascan scan report <https://github.com/accurics/terrascan>

### Sample Scan Data
Sample Terrascan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/terrascan).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- vuln id from tool
- title
- severity
- file path
- line
- component name
