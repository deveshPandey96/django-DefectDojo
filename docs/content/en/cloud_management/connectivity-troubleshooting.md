---
title: "Connectivity Troubleshooting"
description: "Reconnect to your ExposureX Instance"
weight: 2
---

If you have difficulty accessing your ExposureX instance, here are some steps you can follow to get reconnected:

## I can access the site, but I can't log in

1. You can reset the password for your account from the login page: **yourcompanyinstance.#/login**. Click 'I forgot my password' in order to begin the process.  
​

![image](images/Connectivity_Troubleshooting.png)

2. Enter your email address, and click "Reset my password".  
​
3. You should receive an email with the subject header "`Password reset on yourcompanyinstance.#`". This email contains a link which you can click to set a new password.  
  

![image](images/Connectivity_Troubleshooting_2.png)

If you don't receive an email, please check your Spam folder. Failing that, have your team's ExposureX admin confirm that you have an account registered on your instance.  



## I can't access my company's cloud.exposurex site

If your company's cloud.exposurex site does not load in your browser, or times out, it may be necessary for your company to change your firewall rules in order to accept your connection.

Firewall rules can be changed in your Cloud Manager at <https://#/accounts/manage_subscriptions>.

If your company uses a shared VPN, proxy server or a similar tool, make sure it’s authorized to connect to ExposureX and that the IP address is included in ExposureX's Firewall rules.

If the problem persists, please contact [support@exposurex.com](mailto:support@exposurex.com) .



## I can't log in to the Cloud Manager

If you can’t access the Cloud Manager, navigate to the Login page at <https://#/accounts/login/> and click **“Forgot your password?”**


![image](images/Connectivity_Troubleshooting_3.png)  
You’ll be prompted to enter your email address, and our team will send you an email with a link to reset your password and enter a new one. 

Please note that this login method only works for the **Cloud Manager**, an admin site which your team members may not all have access to. Directly logging into your instance to use ExposureX is only possible by directly connecting to **yourcompanyinstance.#/login**.



## I've lost access to my MFA codes

* **For the Cloud Manager:** If you lose access to your MFA codes, or Authenticator App, please contact ExposureX Support at [support@exposurex.com](mailto:support@exposurex.com).
* **For a ExposureX Instance:** It is not currently possible to remove MFA access from an account without an MFA code. The best option in this case is to create a new ExposureX login, and re\-grant all necessary permissions to this account.

