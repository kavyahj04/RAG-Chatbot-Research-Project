---
title: "GitLab IT - Mobile Device Onboarding"
---

To be able to access applications behind Okta (e.g. Slack, GMail, Calendar, etc) on a mobile device; the device needs to be enrolled in Okta Verify, and a passkey needs to be saved on the device.

## Table of Contents

1. [Okta Verify](#okta-verify)
1. [Mobile Passkey and YubiKey Setup](#mobile-passkey-and-yubikey-setup)

### Okta Verify

> These steps apply to Apple and Android devices

<ol>
  <li>Download the Okta Verify app from the App Store (Apple) / Play Store (Android)</li>
  <li>On your laptop, click on the <br>Okta Verify</b> icon at the top of your screen, near the battery indicator and select <b>Open Okta Verify</b></li>
  <li>Click on your account, indicated by your name and email address</li>
  <li>Click <b>Add Account to another device</b></li>
  <li>Verify your identity via Touch ID, and enable bluetooth if prompted
    <ol type="a">
      <li>You should now see a QR code on screen</li>
    </ol>
  </li>
  <li>Ensure that bluetooth is enabled on your mobile device and that the device is on the same Wi-Fi network as the laptop</li>
  <li>Open the Okta Verify app on your mobile device
    <ol type="a">
      <li>If this is your first time using the app, select <b>Add account from another device</b></li>
      <li>If you have used the app before, press the <b>+</b> button near the top of the screen</li>
    </ol>
  </li>
  <li>On the <b>Choose account type</b> screen, select <b>Organization</b></li>
  <li>Select <b>Add account from another device</b> followed by <b>Scan QR code</b></li>
  <li>Scan the QR code on your laptop screen</li>
  <li>On your laptop, enter the 6-digit pin shown on the phone screen</li>
  <li>On your mobile device, enable biometric verification when prompted</li>
  <li>You can verify that your phone is successfully enrolled by going to <a href="https://gitlab.okta.com/enduser/settings">Okta Settings</a> and verifying that your phone is listed under <b>Okta Verify</b></li>
</ol>

### Okta Verify - Manual Setup

> Use these steps in case the mobile app fails to connect to the laptop app or the laptop app is unavailable

<ol>
 <li>Ensure that you have an <a href="#mobile-passkey-and-yubikey-setup">Okta passkey saved on your phone</a></li>
  <li>Download the Okta Verify app from the App Store (Apple) / Play Store (Android)</li>
  <li>Open the Okta Verify app on your mobile device
    <ol type="a">
      <li>If this is your first time using the app, select <b>Get started</b>, and continue until you get to the <b>Choose account type</b> screen</li>
      <li>If you have used the app before, press the <b>+</b> button near the top of the screen</li>
    </ol>
  </li>
  <li>On the <b>Choose account type</b> screen, select <b>Organization</b> and then <b>Skip</b></li>
  <li>Select <b>No, sign in instead</b></li>
  <li>For <b>Organization's sign-in URL</b>, enter <b>gitlab.okta.com</b></li>
  <li>Enter your <b>Okta Username</b> and <b>Password</b> and sign in</li>
  <li>Agree to the terms on screen and enable Touch ID</li>
</ol>

### Mobile Passkey and Yubikey Setup

> Adding a passkey to your mobile device will not give GitLab any access to any data on your phone. For more information, please see https://support.okta.com/help/s/article/Passkey-Management
> The steps below apply to both iOS and Android devices

<ol>
  <li>On your laptop, open Chrome and go to <a href="https://gitlab.okta.com/enduser/settings"> Okta Settings</a></li>
  <li>Next to <b>Security Key or Biometric Authenticator</b>, click <b>Set up another</b></li>
  <li>Verify your identity via your preferred method (e.g. Touch ID, 1Password, etc)</li>
  <li>Click <b>Set up</b> followed by <b>set up</b>
    <ol type="a">
      <li>If the 1Password <b>Save Passkey</b> pop-up appears, click <b>x</b></li>
      <li>If <b>Use Touch ID to sign in?</b> pop-up appears, click <b>Cancel</b></li>
    </ol>
  </li>
  <li>When asked to <b>choose where to save your passkey for gitlab.okta.com</b>, select <b>Use a phone, tablet or security key</b> - A QR code should now appear on screen
    <ol type="a">
      <li><b>YubiKey</b>: Insert your YubiKey and press the button</li>
      <li><b>iOS</b>:
        <ol type="i">
          <li><a href="https://support.apple.com/en-gb/guide/iphone/iph3e504502/ios">Ensure that iOS is up-to-date</a></li>
          <li>Ensure that you have the <b>Password</b> app <a href="https://support.apple.com/en-gb/guide/iphone/iphf538ea8d0/ios">installed and activated in your system settings</a></li>
          <li>Open the camera app and scan the QR code</li>
          <li>Select to save a passkey and follow the steps on your phone to save the passkey</li>
        </ol>
      </li>
      <li><b>Android</b>:
        <ol type="i">
          <li><a href="https://support.google.com/android/answer/7680439?">Ensure that Android is up-to-date</a></li>
          <li>Open the <b>Camera</b> app OR <b>Google Lens</b>, depending on your device</li>
          <li>Scan the QR code and select the option to save a passkey to your Google account</li>
          <li>On Samsung devices, when prompted to <b>Skip the QR code next time<b>, select <b>not now</b> and proceed to save the passkey to your Google account. Please make sure that you save the passkey to Google’s passkey manager and not Samsung Passkey.
        </ol>
     </li>
   </ol>
  </li>
</ol>

## Need Help?

If you need further assistance with setting up your laptop please join our weekly onboarding call scheduled every Tuesday (Check your Calendar!) or reach out to us in Slack in the #it_help channel or via it-help@gitlab.com.
