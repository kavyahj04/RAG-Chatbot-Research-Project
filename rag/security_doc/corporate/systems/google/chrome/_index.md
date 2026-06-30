---
title: "Google Chrome"
---

## Duplicate Chrome Profile Created

This guide to help team members who had an extra Google Chrome profile created and they end up losing all their bookmarks.

## Steps

🚨 **READ ME:** Read all the steps below running through the steps, we cannot recover a deleted Chrome profile if you delete the wrong one. 🚨

### Deleting the newly created profile 

1. Open Chrome.
2. Click your profile picture in the top-right corner in Chrome → **Manage Chrome Profiles**.
3. Assuming that you did not add a personal profile to Chrome, you should see two profiles; one likely labeled **Person 1** and the other **gitlab.com**.
    ![image](/images/security/corporate/systems/google/chrome/image-1.png)
4. **Person 1** is your original pofile and will contain your bookmarks, history, biometrics, etc.
5. **gitlab.com** should then be the new profile.
6. To confirm which Chrome profile is the correct one to delete, click on the three dots next to the profile name and select "Delete" and then verify the number of bookmarks ,etc. 
7. The correct profile to delete will have **fewer** bookmarks, Auto-fill Data, etc
        ![image](/images/security/corporate/systems/google/chrome/image-2.png)
        ![image](/images/security/corporate/systems/google/chrome/image-3.png)

### Loading the correct profile

1. Open the old profile that has all your bookmarks/browsing history, etc. Based on the example above it would be **Person 1**. 
2. When you get the **Your organization requires a profile** pop-up, check off the **Add existing browsing data to managed profile** box.
    ![image](/images/security/corporate/systems/google/chrome/image-4.png)
3. When prompted to **Turn on Sync**, click **Yes, I'm in**. This will back up your bookmarks, browsing history, etc. into your work Google account.
    ![image](/images/security/corporate/systems/google/chrome/image-5.png)
4. Your bookmarks, browsing history, etc. should now be restored.
