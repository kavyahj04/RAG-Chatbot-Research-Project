---
title: Jamf MDM Setup Guide
---

## Manual Enrollment

Most new MacBooks supplied by GitLab are automatically enrolled in Jamf, there are some exceptions based on how the laptop was purchased. In these cases, laptops must be manually enrolled to be able to access any GitLab Corporate services.

### Prerequisites

1. A MacBook capable of running the latest version of macOS
1. An up-to-date macOS installation - [Update macOS](https://support.apple.com/en-us/108382)
1. A stable internet connection - **Do not attempt to enroll a laptop into Jamf using mobile internet, hotel Wi-Fi, etc.**
1. An active GitLab Okta account
1. A mobile device enrolled in Okta Verify

**Note:** If you need assistance with enrolling a mobile device into Okta Verify, please reach out to #it_help through Slack or email it-help@gitlab.com

### Step 1: Verify Jamf Enrollment

1. Click on the Apple icon on the top-right corner of your Mac and open `System Settings`
1. Select `General` > `Device Management` to check if `MDM Profile` is present
    1. If `Device Management` is not visible in under `General`, the laptop is not enrolled in Jamf and you should proceed to `Step 2: Enrollment`
    1. If `MDM Profile` is installed, the laptop is enrolled in Jamf and no further action is required.

### Step 2: Enrollment

1. Open Google Chrome and go to https://gitlab.jamfcloud.com/enroll
1. Sign in with your Okta credentials
1. Click the `Install` button to downlaod the `enrollmentProfile.mobileconfig` file
1. Click on the downloaded file in your Chrome window or from your downloads folder. You will see a notification pop up in the top right of your screen indicating that a new profile needs to be installed.
1. Go back to `System Settings` > `General` > `Device Management`
1. You will now see `MDM Profile` in the list, waiting to be installed
1. Double-click on `MDM Profile` and select `Install`
1. Enter your laptop login password when prompted and wait for the installation to finish.
1. Once the Jamf profile is installed on the laptop, the laptop should begin the [Installomator process](/handbook/security/corporate/end-user-services/laptop-management/laptop-security/updates/#process-details).
