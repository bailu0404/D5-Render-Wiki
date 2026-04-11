# Where can I activate Frame Generation? Why can't I find the option for Frame Generation?

> ****Frame Generation:**** Use AI technology to generate additional frames to improve performance, particularly when paired with NVIDIA Reflex to maintain excellent response.

- Added DLSS Frame Generation in Menu > Frame Generation.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FO2aNruYE5KuXhUrg3gAi%252Fimage.png%3Falt%3Dmedia%26token%3Db89587ca-7e1f-401b-80b8-b465a4092bdf&width=768&dpr=3&quality=100&sign=f28825d6&sv=2)

- Only GeForce RTX 40 series GPUs support DLSS Frame Generation. You can switch on the "Hardware-accelerated GPU scheduling" in "System > Settings > Display > Graphics settings".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F9kX4S6UHoQVdeCOOBPbh%252Fimage.png%3Falt%3Dmedia%26token%3Db61f2993-4370-48e6-8406-f2e814fcd68b&width=768&dpr=3&quality=100&sign=d9b51416&sv=2)

- 2.10 Version supports ****DLSS 4**** Frame Generation to enhance FPS by utilizing AI to generate extra frames.

> ℹ️ > ****Note:****

To enhance the real-time FPS by three or four times with DLSS 4, please prepare a GeForce RTX 50 series GPU and follow the steps as below:

- Close D5 Render: Ensure D5 Render is totally closed.
- Open installation directory: Right click on the D5 icon and select "Open File Location" to enter the installation directory.
- Locate to the DLSS 4 file: Navigate to D5 Render\Engine\Plugins\Runtime\Nvidia\Streamline\Binaries\ThirdParty\Win64\DLSS 4
- Duplicate all the files within the DLSS 4 file: Select all the files using shortcut keys Ctrl + A and copy them by pressing Ctrl + C.
- Paste files to target directory: Return to the parent folder D5 Render\Engine\Plugins\Runtime\Nvidia\Streamline\Binaries\ThirdParty\Win64, right click on a blank space to select "Paste," and replace the existing files.
- Restart D5 Render: Start D5 Render and check if the 3x or 4x options can be enabled.

## FAQ

### 1. When “Frame Generation” is enabled, why do some scenes have a tearing sensation in the preview (output is normal)?

Situation 1: Scenes with especially regular meshes/textures have a shaking preview interface (output is normal)

Situation 2: Partial scenes occasionally have stuck/shaking preview interface

Situation 3: Partial scenes have blurry/shaking at the edges of the preview interface.

Suggestion: This is a known issue with the current version of NV GPUs. If you encounter this kind of scene, it is recommended that you turn off the ‘Frame Generation’ when previewing/outputting.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fzb1TXicNlRhG6UJIuyDN%252Fframe%2520generation.gif%3Falt%3Dmedia%26token%3De5ff3247-2675-4327-b9d2-414b9306057b&width=768&dpr=3&quality=100&sign=d87dd70c&sv=2)

Situation 1: shaking preview of scenes with regular meshes/textures

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FREuKCrIG0GlPTipbWvzU%252F11%2520%281%29%2520%281%29%2520%281%29_1-min.gif%3Falt%3Dmedia%26token%3D77d9b1ea-c0d1-4ac1-9afd-5b60cf1eccef&width=768&dpr=3&quality=100&sign=eb87f934&sv=2)

Situation 2: Partial scenes occasionally have stuck/shaking preview