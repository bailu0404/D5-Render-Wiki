# How to view and optimize graphics card usage?

### View graphics card usage

- Open Task Manager - Performance - GPU - View Dedicated GPU Memory Usage

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fp24j9V3GDjtyiPdHCb4n%252Fimage.png%3Falt%3Dmedia%26token%3D2a198120-d54e-4aa8-bbec-effa777fc71a&width=768&dpr=3&quality=100&sign=5d495001&sv=2)

GPU

- Windows' own video memory detection data may not be accurate, we recommend using [GPU-Z](https://www.techpowerup.com/gpuz/).

> Detecting the sensor - memory used parameter can help with better video memory management.

> ⚠️ > If your dedicated GPU memory usage has reached 80% and above, the core advantage of the graphics card has decreased and will be in an unstable state; at this time, D5 may lag or render slower, and there may be pop-ups reporting errors or flashbacks.

---

### Optimize graphics memory usage

The following settings are available for optimization：

- Start D5 Render with administrator privileges and restart your computer. The program will automatically modify the TDR values, which can improve the stability to a great extent.
- Turn on DLSS.
- Depth of field, Tyndall effect, and other settings can take up a lot of video memory, so use your discretion.
- Higher resolution mapping will also take up video memory, you can replace the mapping of materials farther away from the camera with a lower resolution mapping and try to avoid using replacement.
- More reflective scenes will reduce efficiency, you can turn the specular of materials far from the camera to 0 to cancel the reflection.
- Windows' own GPU usage data may not be accurate, we recommend using [GPU-Z](https://www.techpowerup.com/gpuz/). Check the sensor-memory used parameter for better memory management.