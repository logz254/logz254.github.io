---
layout: post
title: Land Before Time
date: 2023-11-02 14:42 +0300
categories: [HuntressCTF, Land Before Time]
---
## Question
Author: @proslasher

This trick is nothing new, you know what to do: iSteg. Look for the tail that's older than time, this Spike, you shouldn't climb.
File:![Alt text](assets\CTFs-main\HuntressCTF\Land Before Time\dinosaurs1.png)

## Solution
Based of the hint **iSteg**, I did a little research and came across this repository:https://github.com/rafiibrahim8/iSteg

Downloading the GUI jar file from the repository, I was greeted with this interface:
![Alt text](assets\CTFs-main\HuntressCTF\Land Before Time\iSteg.png)

Choosing **Reveal file/message** option then selecting dinosaurs1.png file then click on **Do it**, you get the flag as shown:
![Alt text](assets\CTFs-main\HuntressCTF\Land Before Time\flag.png)


flag{da1e2bf9951c9eb1c33b1d2008064fee}