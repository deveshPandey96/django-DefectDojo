---
title: "Google Cloud Artifact Vulnerability Scan"
toc_hide: true
---
Google Cloud has a Artifact Registry that you can enable security scans https://cloud.google.com/artifact-registry/docs/analysis
Once a scan is completed, results can be pulled via API/gcloud https://cloud.google.com/artifact-analysis/docs/metadata-storage and exported to JSON

### File Types
ExposureX parser accepts Google Cloud Artifact Vulnerability Scan data as a .json file.

### Sample Scan Data
Sample reports can be found at https://github.com/ExposureX/django-ExposureX/tree/master/unittests/scans/gcloud_artifact_scan

### Default Deduplication Hashcode Fields
By default, ExposureX identifies duplicate Findings using these [hashcode fields](https://docs.exposurex.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
