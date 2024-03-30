---
layout: post
title: M Three Sixty Five
date: 2023-11-02 14:42 +0300
categories: [HuntressCTF, M Three Sixty Five]
tags: [huntressctf,ctf,AADInternals]
---
This challenge group comprises of 4 challenges. The 4 challenges are in this order:
1. M Three Sixty Five - General Info
2. M Three Sixty Five - Conditional Access
3. M Three Sixty Five - Teams
4. M Three Sixty Five - The President

Also for these challenges, refer to AADInternals Documentation.

## 1. M Three Sixty Five - General Info
### Question
Author: @David Carter
Welcome to our hackable M365 tenant! Can you find any juicy details, like perhaps the street address this organization is associated with?

### Solution
From the AADInternals Documentation:<br />
"

Get-AADIntTenantDetails (A)

/# Get tenant details<br />
  Get-AADIntTenantDetails
"<br />

Run the command after connecting. Scroll to where the street address is displayed and you get the flag
![Alt text](/assets/CTFs-main/HuntressCTF/M Three Sixty Five/General_info_flag.png)


flag{dd7bf230fde8d4836917806aff6a6b27}


## 2. M Three Sixty Five - Conditional Access
### Question
Author: @David Carter
This tenant looks to have some odd Conditional Access Policies. Can you find a weird one?

### Solution
From the AADInternals Documentation:<br />
"
Get-AADIntConditionalAccessPolicies (A)

/# List the conditional access policies<br />
Get-AADIntConditionalAccessPolicies
"<br />
Run the second command i.e. **Get-AADIntConditionalAccessPolicies**. Check displayName property for the flag
![Alt text](/assets/CTFs-main/HuntressCTF/M Three Sixty Five/Conditional_Access_flag.png)

flag{d02fd5f79caa273ea535a526562fd5f7}


## 3. M Three Sixty Five - Teams
### Question
Author: @David Carter
We observed saw some sensitive information being shared over a Microsoft Teams message! Can you track it down? 

### Solution
From the AADInternals Documentation:<br />
"
Get-AADIntTeamsMessages (T)

/# Get Teams messages<br />
Get-AADIntTeamsMessages | Format-Table id,content,deletiontime,*type*,DisplayName
"<br />
Running the above command, you get the flag.
![Alt text](/assets/CTFs-main/HuntressCTF/M Three Sixty Five/Teams_flag.png)


flag{f17cf5c1e2e94ddb62b98af0fbbd46e1}


## 4. M Three Sixty Five - The President
### Question
Author: @David Carter
One of the users in this environment seems to have unintentionally left some information in their account details. Can you track down The President?

### Solution
From the AADInternals Documentation:<br />
"
/# Get users<br />
Get-AADIntUsers | Select UserPrincipalName,ObjectId,ImmutableId

/# Get user information<br />
Get-AADIntUser -UserPrincipalName "LeeG@company.com"

"<br />

We use the above commands to get the users of the tenant then view user information of each user for a flag.
![Alt text](/assets/CTFs-main/HuntressCTF/M Three Sixty Five/The_President_flag1.png)
![Alt text](/assets/CTFs-main/HuntressCTF/M Three Sixty Five/The_President_flag2.png)

flag{1e674f0dd1434f2bb3fe5d645b0f9cc3}