---
title: "Bearer CLI"
toc_hide: true
---

### File Types
ExposureX parser accepts a .json file.

To export a .json file from Bearer CLI, pass "-f json" to your Bearer command  
See Bearer documentation: https://docs.bearer.com/reference/commands/

### Sample Scan Data
Sample Bearer scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/bearer).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- severity
