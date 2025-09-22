---
title: "Retire.js"
toc_hide: true
---
Retire.js JavaScript scan (\--js) output file can be imported in JSON format.

### Sample Scan Data
Sample Retire.js scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/retirejs).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
