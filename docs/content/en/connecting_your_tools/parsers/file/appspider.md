---
title: "AppSpider (Rapid7)"
toc_hide: true
---
Use the VulnerabilitiesSummary.xml file found in the zipped report
download.

### Sample Scan Data
Sample AppSpider (Rapid7) scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/appspider).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
