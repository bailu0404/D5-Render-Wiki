# How to do when a low TDR is detected?

### What to do when a low TDR is detected?

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F0F2NWKKAvMOu4FLrSNRM%252Fimage.png%3Falt%3Dmedia%26token%3Dcff99e96-5195-4804-8365-61aaf95782aa&width=768&dpr=3&quality=100&sign=9937584&sv=2)

TDR

Most users of graphics software may have once seen a notification which warns that the computer's TDR delay value is too low. It is also likely to pop up when you render high-resolution images or videos in D5 Render.

To solve this problem and ensure a good experience in D5 Render, please follow these steps to increase the TDR recovery value:

1. Close D5 Render and find its shortcut on the desktop or in the Windows start menu.

2. Right-click on it and choose ****Run as administrator.****

> Please note that this action needs administrator permission of your Windows account, and if you are not an admin, please switch to the admin account, or contact the IT department of your company.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf439db8fecd9330191e_2.PNG&width=300&dpr=3&quality=100&sign=63710272&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf44c92e130abda60c71_3.PNG&width=300&dpr=3&quality=100&sign=b10aa1a8&sv=2)

3. After the welcome page of D5 Render appears, wait for about 5seconds, then close D5 Render and ****reboot your computer****. Now you do not need to worry about TDR crash issue anymore.

> Please note that this action will not take effect until the computer is rebooted.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf459db8fe1f47301928_4.gif&width=768&dpr=3&quality=100&sign=4a2309ce&sv=2)

### What is TDR?

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf43fd907e459a7d6b04_5.PNG&width=768&dpr=3&quality=100&sign=7986c46c&sv=2)

TDR stands for Timeout Detection Recovery, which is a protection mechanism from Windows system. It will shut down the GPU driver when GPU computation takes too long to respond.

Generally speaking, the graphics card may need minutes, or even hours, to render a project. But the Windows system will think it is not working because the graphics card does not respond in a few seconds.

In this case,D5 Render will be closed with the GPU driver.

Before the TDR mechanism was invented, we could only reboot the computer after GPU crashed. So this feature is very useful for ordinary users. But for the development and debugging of GPU parallel computing, especially 3D visualization software that has a large demand for video cards, such as D5 Render (real-time ray tracing rendering), the default value may be too low. Therefore, you need to follow the above steps to increase how long your computer waits for the GPU to respond.

### How to manually control the TDR value

In case you would like to control the settings manually, here are the tips and steps to manually check and edit the TDR value.

> Please note that editing the registry can have serious, unexpected consequences that can prevent the system from starting and may require reinstalling the whole operating system if you are unsure of how to modify it. The registry keys mentioned on this page shouldn't create these kinds of issues however.
>
> D5 Render takes no responsibility for any damage caused to your system by modifying the system registry.

1. Open the Registry Editor of your Windows system (administrator permission required)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf4434667b58ffece9c9_6.png&width=768&dpr=3&quality=100&sign=6eeaecf4&sv=2)

2. Navigate to this key:

Computer\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf435cf3b1d68c79d8a1_7.png&width=768&dpr=3&quality=100&sign=1baee444&sv=2)

3. Add or Edit the TdrDelay value

Right click on the TdrDelay key > Modify, then switch ****to Decimal**** and ****enter the Value data as 60.****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf433a8b1175ab57f3bf_8.png&width=768&dpr=3&quality=100&sign=2ae3f346&sv=2)

If the ****TdrDelay**** key doesn't exist, please create a new one through ****Edit >New > DWORD (32bit) Value**** . Name it "****TdrDelay****".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf44d716ffb31596a03d_9.png&width=768&dpr=3&quality=100&sign=ebf438b6&sv=2)

4. Add or Edit the TdrDdiDelay value

Do the same as Step 3 for the ****TdrDdiDelay**** value.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf44d716ffb31596a03d_9.png&width=768&dpr=3&quality=100&sign=ebf438b6&sv=2)

5. Close the Registry editor, then reboot your computer

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf454d856348267817e5_10.png&width=768&dpr=3&quality=100&sign=f78b650a&sv=2)

After the above steps are finished, it will now look like this. Remember to reboot your computer, otherwise the change will not take effect.

### Tips

1. To revert the TDR to its default values, you can go to the Registry editor and adjust TdrDelay to 2s, TdrDdiDelay to 5s; or delete the two keys directly.

2. If you still encounter this error message, or other software on your computer requires a higher TDR value, you can increase it to 120s.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fassets-global.website-files.com%2F62cc341ca212fe5f03df86e6%2F6396bf46d6a20c232c5ec0d9_12.png&width=768&dpr=3&quality=100&sign=70d3250a&sv=2)

3. This setting may be restored after system update or re-formatting, as well as video driver update. Therefore, we may need to change the setting again after them.

Reference: [Testing and debugging TDR during driver development](https://learn.microsoft.com/en-us/windows-hardware/drivers/display/tdr-registry-keys)