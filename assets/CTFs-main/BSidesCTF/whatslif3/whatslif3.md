## Question
Cannot recall what the question was 😅
## Solution

1. Download the provided APK i.e. whatslif3.apk
2. Fire up MobSF to get an analysis of the apk file.
![Alt text](mobsf_brief.png)

The screenshot above shows a part of how it should look like after analysis is done.

3. Read through the rest of the analysis. When you get to the **Strings** section, you find a variable called **check_guess** with a base64 encoded value.
![Alt text](base64.png)

4. Base64 decode the value. You get **BSidesNBI{this_didn't_kill_them}**
![Alt text](base64_decoded.png)

5. Install the APK file and run it. Enter **BSidesNBI{this_didn't_kill_them}** and press submit.
![Alt text](phone.png)

6. You are presented with another image.
![Alt text](base58.png)

7. From the text "Find a good recipe to cook your flag", I realised that CyberChef could be the solution and indeed it was.
![Alt text](solved.png)

Flag: BSidesNRB{c4r3full_hubr1s_w1ll_t4k3_us_0u7}




