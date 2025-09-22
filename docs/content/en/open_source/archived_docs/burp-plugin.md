---
title: "Defect Dojo Burp plugin"
description: "Export findings directly from Burp to ExposureX."
draft: false
weight: 9
exclude_search: true
---

**Please note: The ExposureX Burp Plugin has been sunset and is no longer a supported feature.**

Burp is still a supported tool, and all the results from it can be imported into ExposureX. Burp can produce XML reports and these can be uploaded to ExposureX using the graphical user interface or the API. Our documentation at https://documentation.exposurex.com/integrations/parsers/file/burp/ describes this usage.

This is Burp Plugin to export findings directly to ExposureX.

Installation
------------

In order for the plugin to work , you will need to have Jython set up in
Burp Suite Pro . To use this plugin before it appears in the BApp Store
you will need to do the following :

1.  Go to `Extender` and select the `Extensions`
    tab
2.  Click on `Add` , select `Extension Type:` to
    be `Python` and select the `ExposureXPlugin.py`

Usage
-----

![image](images/burp_plugin_usage.gif)
