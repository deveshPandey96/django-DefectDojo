---
title: "Anchore Enterprise Policy Check"
toc_hide: true
---
Anchore-CLI JSON policy check report format.

### Sample Scan Data
Sample Anchore Enterprise Policy Check scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/anchore_enterprise).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- severity
- component name
- file path
