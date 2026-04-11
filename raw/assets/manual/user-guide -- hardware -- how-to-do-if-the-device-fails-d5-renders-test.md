# How to do if the device fails D5 Render's test?

## Quick Guide (Click to quickly jump)

[****Hardware and Solution**** (prompts 'Unknown Graphics Card')](https://docs.d5render.com/user-guide/hardware/how-to-do-if-the-device-fails-d5-renders-test#hardware-and-solution)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Ftguz4GTk3QFJlVbwJt2o%252Fimage.png%3Falt%3Dmedia%26token%3D54d86fed-e34b-4388-971b-d8e374e4e32a&width=768&dpr=3&quality=100&sign=74e93c31&sv=2)

[****Software and Solution**** ('Driver Version' or 'System' column is greyed out)](https://docs.d5render.com/user-guide/hardware/how-to-do-if-the-device-fails-d5-renders-test#software-and-solution)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FiIdfe06hhLKUv6ARoKHt%252Fimage.png%3Falt%3Dmedia%26token%3Df09ce757-250e-4f1b-868d-1cdf4c52cec6&width=768&dpr=3&quality=100&sign=1254485c&sv=2)

[****Checklist Overview****](https://docs.d5render.com/user-guide/hardware/how-to-do-if-the-device-fails-d5-renders-test#checklist)

---

## Hardware and Solution

**Prompt: You did not meet the minimum requirements, please upgrade your current hardware.**

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FybXfEFaI19v6rbfZR3Vx%252Fimage.png%3Falt%3Dmedia%26token%3Dad6dd0b1-14ed-45d2-8af6-8bc15d9adc14&width=768&dpr=3&quality=100&sign=707a3c9a&sv=2)

### 1. The graphics card does not meet the requirements to run D5.

****Description:****

In the System Info, the 'Graphics Card' and 'Driver Version' columns are showing as 'Unknown'. This typically indicates that your current graphics card may not be fully compatible with D5 Render.

D5 Render is based on real-time raytracing technology, so the current graphics cards must support real-time raytracing. Minimum requirement↓

BrandType

NVIDIA

GeForce GTX 1060 6GB and above

AMD

RX 6400 and above

Intel

Arc A3 and above

For specific system requirements and ****supported GPU types****, please refer to: [System Requirements for D5 Render | User Manual](https://docs.d5render.com/user-guide/hardware/system-requirements-for-d5-render)

****Solution:****

- Go to the official website to check compatibility: current graphics cards that support DXR can be checked on [NVIDIA](https://www.nvidia.com/en-us/geforce/news/geforce-gtx-dxr-ray-tracing-available-now/), [AMD](https://www.amd.com/en/technologies/directx12), [Intel](https://www.intel.com/content/www/us/en/homepage.html).
- Upgrading to a supported graphics card is recommended for optimal performance.

> ****Note:**** Underperforming graphics cards cannot pass the test, please understand.

****FAQs:****

- ****Why my GTX 1650 graphics card cannot run D5?****

RTX Series 60 cards generally provide better performance than Series 50 cards; for instance, ****GTX 1060**** outperforms ****GTX 1650****.
As GTX 1060 is the minimum requirement for running D5 Render, GTX 1650 cards are not supported and will fail the hardware test.

### 2. Detect a wrong graphics card (multiple graphics cards on the device)

****Description:****

D5 only supports Discrete Graphics Card (GPU), not integrated graphics Card (GPU). A double graphics card device will also fail the test if it defaults to using the integrated graphics card.

****Solution:****

- Please disable the other integrated graphics card in ‘Device Manager’.
- Specify 'Discrete' GPU (High-performance) option as the default in the system settings.
- Restart the device to retest.

> ****Note:**** Please ensure that the GPU used by D5 Render is a discrete graphics card.

---

## Software and Solution

**Prompt: The current graphics card driver cannot support D5 Render due to compatibility issues. Please upgrade the driver to the latest version.**

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6Bu8Y5yudLSKisBuoSXq%252Fimage.png%3Falt%3Dmedia%26token%3Def85380d-3c75-46b3-9df6-439d144b525a&width=768&dpr=3&quality=100&sign=f1fa75b0&sv=2)

### 1. The driver version is too low/out-of-date

****Description:****

In your System Info interface, the Driver Version column not having a grey fill suggests a problem with your current driver. Updating your graphics card driver to version 531.14 is necessary for D5 Render to function normally.

****Solution:****

Visit the graphics card's official website, download and install the most recent driver version.

Please refer to: [How to view and upgrade graphics card driver? | User Manual](https://docs.d5render.com/user-guide/hardware/how-to-view-and-upgrade-graphics-card-driver#header-1)

### 2. The Windows version is too low/out-of-date

****Description:****

- The minimum Windows version is 10.0.19044 (Win10 21H2).
- NVIDIA 531.14 and above graphics card drivers are not compatible with Windows 10 v1909 and below.

****Solution:****

Open Settings → Windows Update → Check for updates or use the [Update Assistant](https://www.microsoft.com/en-us/software-download/windows10) to update it to Windows 10 21H2 and above.

> ****Note:**** It is recommended to update the driver and system simultaneously to a higher version to avoid some errors caused by the incompatibility.

---

## Checklist Overview

- Hardware meets the minimum requirements (must support ray tracing),
- The 'Discrete' GPU has been configured as the default properly.
- Graphics card driver has been updated to an appropriate version,
- Windows system version is 21H2 or higher.