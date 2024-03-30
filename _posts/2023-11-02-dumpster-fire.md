---
layout: post
title: Dumpster Fire
date: 2023-11-02 14:42 +0300
categories: [HuntressCTF, Dumpster Fire]
---
## Question
Author: @JohnHammond

We found all this data in the dumpster! Can you find anything interesting in here, like any cool passwords or anything? Check it out quick before the foxes get to it!
File:[dumpster_fire.tar.xz](/assets/CTFs-main/HuntressCTF/Dumpster Fire/dumpster_fire.tar.xz)

## Solution
Extract the contents of the file and you are presented with several directories for a linux machine.
![Alt text](/assets/CTFs-main/HuntressCTF/Dumpster Fire/directories.png)

The juicy information for the challenge is found in the **home** directory -> **challenge** folder.

The information found here is for a Mozilla Firefox User Profile (**bc1m1zlr.default-release**). On realizing this, I had an idea that the flag would be found in the Saved Passwords. To view the Saved Passwords, you need to create a profile then copy+paste the files in **bc1m1zlr.default-release** into the newly created profile.

For information on how to create a profile in Mozilla FireFox, refer to this link: https://support.mozilla.org/en-US/kb/profile-manager-create-remove-switch-firefox-profiles#w_manage-profiles-when-firefox-is-open

In this case, I created a profile called **huntress**.
![Alt text](/assets/CTFs-main/HuntressCTF/Dumpster Fire/huntress_profile.png)

Navigate to the **Root Directory**. The contents of the folder are shown below:
![Alt text](/assets/CTFs-main/HuntressCTF/Dumpster Fire/huntress_root_directory.png)

Copy the files from **bc1m1zlr.default-release** folder and paste the files into **rs4hb5o5.huntress** folder

Go back to the browser and click on **Launch profile in new browser**
![Alt text](/assets/CTFs-main/HuntressCTF/Dumpster Fire/launch_profile.png)

Navigate to **Passwords** and you get credentials for localhost running on port 31337. Unhiding the password, you get the flag.
![Alt text](/assets/CTFs-main/HuntressCTF/Dumpster Fire/flag.png)


flag{35446041dc161cf5c9c325a3d28af3e3}

After this, you can delete the newly created profile.