---
title: "What is TDR and how to solve the TDR(Timeout Detection Recovery) problem when rendering?"
category: "Features"
date: "September 15, 2025"
author: "Hao Wang"
source: "https://www.d5render.com/posts/how-to-solve-the-tdr-timeout-detection-recovery-problem"
---

# What is TDR and how to solve the TDR(Timeout Detection Recovery) problem when rendering?

Most graphics software users have probably seen a notification at some point warning that their computer's TDR delay value is too low. This notification is also likely to appear when rendering high-resolution images or videos in [****D5 Render****](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=how-to-solve-the-tdr-timeout-detection-recovery-problem).

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/685140a7a84aa13e04802945_6396bf42d53b2c147dab1bb2_1.png)

To resolve this issue and ensure a good [****D5 Render****](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=how-to-solve-the-tdr-timeout-detection-recovery-problem) experience , follow these steps to increase the TDR recovery value:

1. Close [****D5****](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=how-to-solve-the-tdr-timeout-detection-recovery-problem) Render and look for its shortcut on your desktop or in the Windows start menu.

2. Right-click on it and choose ****Run as administrator.****

**Please note that this action requires administrator permission for your Windows account. If you are not an administrator, please switch to the administrator account or contact your company's IT department.**

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/68c7bef0c6402efc7f1abc4f_68513fe9ad593317be2e8642_Group%25206%2520(1).png)

3. When the D5 Render welcome page appears, wait about 5 seconds, close D5 Render, and ****restart your computer**** . Now you don't have to worry about TDR crashes anymore.

**Please note that this action will not take effect until the computer is restarted.**

## What is TDR?

TDR stands for Timeout Detection Recovery, which is a Windows system protection mechanism. It shuts down the GPU driver when GPU computation takes too long to respond.

Generally speaking, it can take minutes, or even hours, for a graphics card to render a project. However, Windows will think it's not working because the graphics card doesn't respond within a few seconds.

In this case, [****D5 Render****](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=how-to-solve-the-tdr-timeout-detection-recovery-problem) will close with the GPU driver.

Before the invention of the TDR mechanism, we could only restart the computer after a GPU failure. Therefore, this feature is very useful for ordinary users. However, for GPU parallel computing development and debugging, especially for 3D visualization software that places heavy demands on video cards, such as D5 Render (real-time ray-traced rendering), the default value may be too low. Therefore, you should follow the steps above to increase the time your computer waits for the GPU to respond.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/68303faa47a5b195a970a73f_5eecdaf48460cde5ebd566ecca70b9970fb9750ab3560ae775b8339e1c4c2483f728f271dbcdaa6639e8703ac5556d0d2124139cda25d4878829b40aab33fde49f2181b862a2e16cb3884460ae931e006b4ce2af355fdf1f7c1ef462d573a24d.png)

## How to manually control the TDR value

In case you want to control the settings manually, here are the tips and steps to manually check and edit the TDR value.

Please be aware that editing the registry can have serious and unexpected consequences that may prevent your system from booting and may require reinstalling the entire operating system if you are unsure how to edit it. However, the registry keys mentioned on this page should not cause these types of problems. D5 Render is not responsible for any damage caused to your system by modifying the registry.

### 1. Open the registry editor of your Windows system (administrator permission is required)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/685140a7a84aa13e04802980_6396bf4434667b58ffece9c9_6.png)

‍

### 2. Navigate to this key:

Computer\ HKEY\_LOCAL\_MACHINE\ SYSTEM\ CurrentControlSet\ Control\ GraphicsDrivers

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/685140a7a84aa13e04802951_6396bf435cf3b1d68c79d8a1_7.png)

‍

### 3. Add or edit the TdrDelay value

Right click on the TDRDelay key > Modify, then ****change to decimal**** and ****enter the value data as 60.****

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/685140a7a84aa13e04802961_6396bf433a8b1175ab57f3bf_8.png)

If the ****TDR Delay**** key doesn’t exist, create a new one via ****Edit > New > DWORD (32-bit) Value**** . Name it “ ****TDR Delay**** .”

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/685140a7a84aa13e0480291f_6396bf44d716ffb31596a03d_9%2520(1).png)

‍

### 4. Add or edit the tdrddiDelay value

Do the same as in step 3 for ****TDRDDI Delay**** value.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/685140a7a84aa13e0480291f_6396bf44d716ffb31596a03d_9%2520(1).png)

‍

### 5. Close the Registry Editor and then restart your computer

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/685140a6a84aa13e04802918_6396bf454d856348267817e5_10.png)

Once you've completed the previous steps, it will now look like this. Remember to restart your computer; otherwise, the change won't take effect.

## Tips

1. To return TDR to its default values, you can go to the registry editor and set TDRDelay to 2 seconds, TdrddiDelay to 5 seconds, or delete both keys directly.

2. If you continue to receive this error message or if other software on your computer requires a higher TDR value, you can increase it to 120 s.

3. These settings can be restored after updating or formatting the system, as well as updating the video driver. Therefore, we may need to change the settings again after these changes.

Reference: [****Testing and Debugging TDR During Controller Development****](https://learn.microsoft.com/en-us/windows-hardware/drivers/display/tdr-registry-keys)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/68303faa47a5b195a970a73f_5eecdaf48460cde5ebd566ecca70b9970fb9750ab3560ae775b8339e1c4c2483f728f271dbcdaa6639e8703ac5556d0d2124139cda25d4878829b40aab33fde49f2181b862a2e16cb3884460ae931e006b4ce2af355fdf1f7c1ef462d573a24d.png)