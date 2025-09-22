---
title: "StackHawk HawkScan"
toc_hide: true
---
Import the JSON webhook event from StackHawk.
For more information, check out our [docs on hooking up StackHawk to Defect Dojo](https://docs.stackhawk.com/workflow-integrations/defect-dojo.html)

### Sample Scan Data
Sample StackHawk HawkScan scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/stackhawk).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- vuln id from tool
- component name
- component version
