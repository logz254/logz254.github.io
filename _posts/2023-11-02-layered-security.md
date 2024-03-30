---
layout: post
title: Layered Security
date: 2023-11-02 14:42 +0300
categories: [HuntressCTF, Layered Security]
---
## Question
Author: @JohnHammond

It takes a team to do security right, so we have layered our defenses!
File:[layered_security](/assets\CTFs-main\HuntressCTF\Layered Security\layered_security)

## Solution
Checking the file type, you realize that it is an image file.
![Alt text](/assets\CTFs-main\HuntressCTF\Layered Security\file_type.png)

Opening the file using GNU Image Manipulation Program, you realize that there are 10 images stacked on top of each other. Clicking on the **eye** icon as shown below hides an image.
![Alt text](/assets\CTFs-main\HuntressCTF\Layered Security\stacked_images.png)

Hide each image until you find one with the flag shown on top of it.
![Alt text](/assets\CTFs-main\HuntressCTF\Layered Security\flag.png)

flag{9a64bc4a390cb0ce31452820ee562c3f}