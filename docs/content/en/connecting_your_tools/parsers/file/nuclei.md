---
title: "Nuclei"
toc_hide: true
---
Import JSON output of nuclei scan report <https://github.com/projectdiscovery/nuclei>

### Sample Scan Data
Sample Nuclei scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/nuclei).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- severity
- component name
