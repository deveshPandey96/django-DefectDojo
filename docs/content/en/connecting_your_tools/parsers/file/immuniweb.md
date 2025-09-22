---
title: "Immuniweb Scan"
toc_hide: true
---
XML or JSON Scan Result File from [Immuniweb Scan](https://www.immuniweb.com/).

### Sample Scan Data
Sample Immuniweb Scan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/immuniweb).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
