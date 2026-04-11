# Why prompt 'The program cannot be launched because of DLL errors...' or 'Program Startup Failed'?

> ℹ️ > There can be several different reasons for errors related to DLL files. For example, malware corruption on the computer, damaged Windows registry, d3d12.dll file being deleted or misplaced, application errors, etc.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FHILK2FlipXJykxTVXWwW%252Fimage.png%3Falt%3Dmedia%26token%3Dcfbe23e7-d5a5-4adf-89c6-4dd26952c170&width=768&dpr=3&quality=100&sign=9aa86c26&sv=2)

Error pop-up before 2.7 version

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FBJt6Zk9BnWSdMX6isgyr%252Fdll%2520error%25E6%2594%25B9%25E5%2590%258E.png%3Falt%3Dmedia%26token%3D3c1509cb-f9a9-49dc-abf8-8c2155c4ca9c&width=768&dpr=3&quality=100&sign=ccc17d95&sv=2)

Error pop-up now

### ****Solution 1：**** Confirm the CPU model and BIOS version of the current device

Based on recent user reports, when using `Intel Core i9-13900K/KF/KS and i9-14900K/KF/KS processors` to run D5 and other DX12 software, due to environmental problems, the devices may prompt ‘The program cannot be launched because of DLL errors in the system’ or ‘Program Startup Failed’ pop-up messages.

It is recommended to ****update the BIOS to the latest version (released in April)**** or ****disable CPU overclocking, RAM XMP profile and Intel Turbo Boost/restore them to the default values.****

---

### ****Solution 2：****Specific models of laptops

Based on recent user feedback, when running D5 on ****HP Omen and HP Victus**** laptops, there is a tendency for the integrated graphics to be called instead of the dedicated graphics card (D5 only supports reading from the dedicated graphics card), which can lead to abnormal usage of D5.

Solution: [First choice] (Control Center of HP Laptops) - Select ****'Discrete'**** GPU mode in 'OMEN Gaming Hub-Graphics Switcher'.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FRnb6CZpDhrftUohGz81a%252F111.jpg%3Falt%3Dmedia%26token%3D9533632e-8f11-48e4-a57d-ec106e27503d&width=768&dpr=3&quality=100&sign=23e7f49b&sv=2)

Control Center of HP Laptops - Select ****'Discrete'**** GPU mode in 'OMEN Gaming Hub-Graphics Switcher'

> If [ First Choice ] does not work, please select ****'NVIDIA GPU only****' in NVIDIA Control Panel - 3D Settings - Manage Display Mode. If there is no such option, try disabling the integrated graphics card.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Flfr5wIpwak3txSB3HbQ6%252F222.png%3Falt%3Dmedia%26token%3D529bdb20-ac8a-40aa-9abb-f0352a6c9481&width=768&dpr=3&quality=100&sign=b49319dc&sv=2)

select ****'NVIDIA GPU only****' in NVIDIA Control Panel - 3D Settings - Manage Display Mode

---

### ****Solution 3： Try a clean installation of the graphics card driver and change a path to install D5 Render****

- Update the driver through NV’s official software [GeForce Experience](https://www.nvidia.com/en-us/geforce/geforce-experience/), or download and install the driver by manually selecting the appropriate graphics card from [NVIDIA’s official website](https://www.nvidia.com/download/index.aspx)
- Update the driver at AMD’s official website [AMD Drivers and Support](https://www.amd.com/en/support)
- Update the driver at Intel’s official website [Intel® Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)

#### Manually search for drivers:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8yR1R8WCckV2QwnJoaG0%252Fimage.png%3Falt%3Dmedia%26token%3Dbfa8544b-b322-4205-ae14-45a0fa05912f&width=768&dpr=3&quality=100&sign=e53896f0&sv=2)

Clean Installation

---

### ****Solution 4：Try to fix the issue by DXR Repairment tool****

[**Download link**](https://drive.google.com/file/d/1bOkWvdUTQjVLQg11KHMZOPio6wmQIRQ4/view?usp=share_link) 
Original proposal jumps: [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/en-us/topic/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system-files-79aa86cb-ca52-166a-92a3-966e85d4094e)

Instructions:

> Note: Do not close this command prompt window until the verification is 100% complete.

> ⚠️ > If the issue persists after following the previous steps, please provide a detailed description of the configuration and the troubleshooting steps you have taken in the dedicated support post on the forum. We will then follow up accordingly: [Cannot solve the problem using the solutions provided ‘The program cannot be launched because of DLL errors in the system’](https://forum.d5render.com/t/cannot-solve-the-problem-using-the-solutions-provided-the-program-cannot-be-launched-because-of-dll-errors-in-the-system/27855) Thanks for understanding and support.