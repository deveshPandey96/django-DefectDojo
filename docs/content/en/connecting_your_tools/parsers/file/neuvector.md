---
title: "NeuVector (compliance)"
toc_hide: true
---
Imports compliance scans returned by REST API.

### Sample Scan Data
Sample NeuVector (compliance) scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/neuvector).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- severity
- component name
- component version
