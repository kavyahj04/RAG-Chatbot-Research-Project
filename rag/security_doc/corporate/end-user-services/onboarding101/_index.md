---
title: "GitLab IT Onboarding 101"
---

## Welcome To GitLab

Congratulations on joining GitLab! This page is dedicated to the IT onboarding experience, here at GitLab we use many applications and the latest hardware to enable you to complete your work to the best of your ability! While it may seen a little bit overwhelming at the start the Team member enablement team is here to make the process as easy as possible!

## Table of Contents

1. [Before you begin](#before-you-begin)
1. [Laptop Setup: MacBook](#laptop-setup-macbook)
   - [Activate your Okta Account](#macbook-step-1-activate-your-okta-account)
   - [MacBook Initial Setup](#macbook-step-2-initial-setup)
   - [System Configuration](#macbook-step-3-system-configuration)
   - [Google Account Setup](#macbook-step-4-google-account-setup)
   - [Okta Account Verification](#macbook-step-5-okta-account-verification)
   - [Access GitLab Email & GitLab.com Account](#macbook-step-6-access-gitlab-email--gitlabcom-account)
1. [Laptop Setup: Linux](#laptop-setup-linux)
   - [Activate your Okta Account](#linux-step-1-activate-your-okta-account)
   - [Okta Setup](#linux-step-2-okta-setup)
   - [Google Account Setup](#linux-step-3-google-account-setup)
   - [Access GitLab Email & GitLab.com Account](#linux-step-4-access-gitlab-email--gitlabcom-account)

## Before You Begin

You will receive an Okta activation email in your personal email. This is the first step to gaining access to GitLab's systems.

## Laptop Setup: MacBook

> **IMPORTANT**: You will not have access to your work MacBook until your start date. On your start date,  please follow this guide.

### MacBook Step 1: Activate Your Okta Account

1. On a mobile device, check your personal email for an Okta activation email.
1. Click the link in the email to set your password
1. After setting your password, your browser will redirect to the Okta Dashboard. **IMPORTANT: Do not open Gmail (G Suite SSO Mail) or any Google application (G Suite SSO Drive, G Suite SSO Calendar, G Suite SSO Account) before finishing the laptop setup process in Step 2. Opening these applications too early will lock you out of your laptop.**
1. You will receive a follow-up email from Okta with the subject **Security Method enrolled**.

### MacBook Step 2: Initial Setup

> **IMPORTANT**: If `Remote Management` is not available on your laptop, please use the [Jamf MDM Setup Guide](/handbook/security/corporate/systems/jamf/setup/) to manually enroll your device.

<ol>
  <li>Power on your GitLab laptop</li>
  <li>Complete the initial macOS setup:
    <ol type="a">
      <li>Choose your preferred language</li>
      <li>Select your country or region</li>
      <li>Choose accessibility options (or click **Not Now**)</li>
      <li>Select your WiFi network</li>
      <li>On the **Remote Management** screen, click **Enroll**</li>
    </ol>
  </li>
  <li>Log into GitLab Okta:
    <ol type="a">
      <li>Use the full GitLab email address (e.g., yourname@gitlab.com)</li>
      <li>Enter the password you created on your personal device</li>
      <li>Click <b>Sign in</b></li>
    </ol>
  </li>
  <li>Set up your computer account:
    <ol type="a">
      <li>Create a password for your local Mac account</li>
      <li>Click <b>Continue</b></li>
      <li>Use the full GitLab email address (e.g., yourname@gitlab.com)</li>
      <li>Enter the password you created on your personal device</li>
      <li>Click <b>Sign in</b></li>
    </ol>
  </li>
  <li>Set up your computer account:
    <ol type="a">
      <li>Create a password for your local Mac account</li>
      <li>Click <b>Continue</b></li>
    </ol>
  </li>
  <li>Configure system settings:
    <ol type="a">
      <li>On the <b>Enable Location Services</b> screen, check <b>Enable Location Services on this Mac</b></li>
      <li>Click <b>Continue</b></li>
      <li>On the <b>Touch ID</b> screen, click <b>Continue</b></li>
      <li>Enroll in Touch ID by placing your finger on the scanner (this is required)</li>
      <li>On the <b>Choose Your Look</b> screen, select <b>Light</b>, <b>Dark</b>, or <b>Auto</b></li>
      <li>Click <b>Continue</b></li>
    </ol>
  </li>
</ol>

### MacBook Step 3: System Configuration

<ol>
  <li>On the <b>Welcome to your new Mac!</b> screen, wait while applications are automatically installed
    <ol type="a">
      <li>This should take a few minutes</li>
      <li>When finished, click <b>Done</b></li>
    </ol>
  </li>
  <li>System Restart:
    <ol type="a">
      <li>A pop-up will inform you that your machine needs to restart within the next minute</li>
      <li>Wait for the automatic restart or initiate it yourself</li>
      <li>After restart, log back in</li>
    </ol>
  </li>
  <li>Enable FileVault:
    <ol type="a">
      <li>Click <b>Enable Now</b></li>
      <li>This should take a few minutes</li>
      <li>When finished, click <b>Done</b></li>
    </ol>
  </li>
  <li>System Restart:</li>
    <ol type="a">
      <li>A pop-up will inform you that your machine needs to restart within the next minute</li>
      <li>Wait for the automatic restart or initiate it yourself</li>
      <li>After restart, log back in</li>
    </ol>
   </li>
  <li>Enable FileVault
    <ol type="a">
      <li>Click <b>Enable Now</b> when prompted to enable FileVault (disk encryption)</li>
    </ol>
  </li>
</ol>

### MacBook Step 4: Google Account Setup

1. Open Google Chrome
1. On the **Sign in to Chrome** window, click **Sign in**
1. Enter your GitLab email address
1. If Okta Verify opens, click **Not now** or close it
1. Sign in to Okta with your username and password
1. Click **Agree** on the Google Workspace policy that appears
1. On the **Verify it's you** screen, click **Continue**
1. On the **Enhanced Ad Privacy in Chrome** notice, click **Got it**
1. When you see **Your organization will manage this profile**, click **Continue**
1. On the **Turn on Sync** window, click **Yes, I'm in**

### MacBook Step 5: Okta Account Verification

<ol>
  <li>In Chrome, go to https://gitlab.okta.com and wait for Okta Verify to open
    <ol type="a">
      <li>On the <b>Welcome to Okta Verify</b> window, click <b>Get Started</b></li>
      <li>In Chrome, enter your Okta password and click <b>Verify</b></li>
      <li>In the Okta Verify window, click <b>Enable</b> for <b>Enable Touch ID confirmation</b></li>
      <li>Close the <b>Complete</b> tab in Chrome</li>
    </ol>
  </li>
  <li>Complete security verification:
    <ol type="a">
      <li>In Chrome, click <b>Verify it's you with a security method</b></li>
      <li>Select <b>Password</b> and click <b>Verify</b></li>
      <li>In Okta Verify, click <b>Yes, it's me</b> (or provide your fingerprint)</li>
    </ol>
  </li>
  <li>Set up additional security methods:
    <ol type="a">
      <li>On the <b>Set up Security methods</b> screen, click <b>Set up</b> for <b>Security Key or Biometric authenticator</b></li>
      <li>Click <b>Set up</b> again to confirm</li>
      <li>On the <b>Create a passkey for gitlab.okta.com</b> pop-up, click <b>Save another way</b></li>
      <li>Select <b>Your Chrome profile</b> followed by <b>Continue</b></li>
    </ol>
   </li>
</ol>

### MacBook Step 6: Access GitLab Email & GitLab.com Account

1. Access your GitLab email by clicking **G Suite SSO Mail** in Okta
1. Check your GitLab email for an email titled "**Welcome to GitLab Onboarding, `yourname`!**"
1. Follow the instructions in the email to set up your GitLab.com account and access your Onboarding Issue

## Laptop Setup: Linux

This guide assumes that you are using Ubuntu. Please adjust the sytax of any commands to match your distro of choice.

### Linux Step 1: Activate Your Okta Account

1. On a mobile device, check your personal email for an Okta activation email.
1. Click the link in the email to set your password
1. After setting your password, your browser will redirect to the Okta Dashboard
1. You will receive a follow-up email from Okta with the subject **Security Method enrolled**

### Linux Step 2: Okta Setup

<ol>
  <li>On your Linux laptop, download and install Google Chrome</li>
    <ol style="a">
      <li><code>wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb</code></li>
      <li><code>sudo dpkg -i google-chrome-stable_current_amd64.deb</code></li>
      <li><code> sudo apt --fix-broken install</code></li>
    </ol>
  </li>
  <li>Open Google Chrome, and navigate to https://gitlab.okta.com</li>
  <li>Complete security verification:
    <ol style="a">
      <li>Click <b>Verify it's you with a security method</b></li>
      <li>Select <b>Password</b> and click <b>Verify</b></li>
   </ol>
  </li>
  <li>Set up additional security methods:
    <ol style="a">
      <li>On the <b>Set up Security methods</b> screen, click <b>Set up</b> for <b>Security Key or Biometric authenticator</b></li>
      <li>Click <b>Set up</b> again to confirm</li>
      <li>On the <b>Create a passkey for gitlab.okta.com</b> pop-up, click <b>Continue</b></li>
   </ol>
  </li>
</ol>

### Linux Step 3: Google Account Setup

1. Open Google Chrome
1. On the **Sign in to Chrome** window, click **Sign in**
1. Enter your GitLab email address
1. Sign in to Okta with your username and password
1. Click **Agree** on the Google Workspace policy that appears
1. On the **Verify it's you** screen, click **Continue**
1. On the **Enhanced Ad Privacy in Chrome** notice, click **Got it**
1. When you see **Your organization will manage this profile**, click **Continue**
1. On the **Turn on Sync** window, click **Yes, I'm in**

### Linux Step 4: Access GitLab Email & GitLab.com Account

1. Check your GitLab email for an email titled "**Welcome to GitLab Onboarding, `yourname`!**"
1. Follow the instructions in the email to set up your GitLab.com account and access your Onboarding Issue

### Congratulations

You have completed the initial setup process for your GitLab account and laptop. If you encounter any issues, please contact us via the #it_help Slack channel or it-help@gitlab.com.

### Next Steps

To access company applications on your mobile device as per Day 2 of your onboarding, please follow the [Mobile Device Onboarding](/handbook/security/corporate/end-user-services/onboarding101/onboarding-mobile-devices) guide.

## Need Help?

If you need further assistance with setting up your laptop please join our weekly onboarding call scheduled every Tuesday (Check your Calendar!) or reach out to us in Slack in the #it_help channel or via it-help@gitlab.com.
