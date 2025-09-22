---
title: "GitLab Secret Detection Report"
toc_hide: true
---
GitLab Secret Detection Report file can be imported in JSON format (option --json).

### Sample Scan Data
Sample GitLab Secret Detection Report scans can be found [here](https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/gitlab_secret_detection_report).

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
