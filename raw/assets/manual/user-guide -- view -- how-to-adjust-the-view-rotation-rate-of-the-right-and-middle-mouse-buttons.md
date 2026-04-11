# How to adjust the view rotation rate of the right and middle mouse buttons？

In D5 versions up to 2.6, mouse sensitivity was slower than in other 3D software, requiring repetitive drags to adjust the view, hindered further by the mouse hitting the screen edge. D5 2.7 improved sensitivity and added a feature for users to customize it for comfort. The upcoming version 2.8 will introduce a sensitivity slider in the UI for easier adjustments.

Mouse sensitivity determines how the distance the user drags the mouse influences the camera's movement. Within D5 Render, mouse sensitivity impacts three features:

### How to Adjust It？

#### Step One:

Right-click on the D5 Render icon and select 'Open File Location'. Use the Notepad to open the config.ini file in the file location and check the Config Path value:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FIBnuNhfzPra3JsiCnP9P%252Fimage.png%3Falt%3Dmedia%26token%3D17c13ed3-d32d-4428-adf2-a07ac23c1220&width=768&dpr=3&quality=100&sign=9d2f62dc&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FIYUT81ZX19z9lzc1Cm7k%252Fimage.png%3Falt%3Dmedia%26token%3D8a6d8b80-3e6f-4d3d-955e-a04c21b1a3eb&width=768&dpr=3&quality=100&sign=cda9eddc&sv=2)

#### Step Two:

Navigate to C:\Users\Your User Account\AppData\Roaming>D5Config and find the file named with the ConfigPath value.

If you can't find it, please go to File > View and check 'Hidden Items'.

#### Step Three:

After opening the correct file, click the usr file and open its usr.ini file with Notepad.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FItvLGv6h6leQCrkuloBn%252Fimage.png%3Falt%3Dmedia%26token%3D8390da59-784c-435e-ac77-62fa74ae3bb6&width=768&dpr=3&quality=100&sign=20105641&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKoxmCfS7dH1Mzf8q0E6E%252Fimage.png%3Falt%3Dmedia%26token%3D46b276f4-9e9a-4fb5-9238-550be77862b5&width=768&dpr=3&quality=100&sign=e9e7001d&sv=2)

#### tep Four:

Navigate to the bottom of the usr.ini file and paste the following parameters:

[viewspeed]

Orbit=1

Fly=1

Walk=1

These parameters support customization. When their values are set to 1, the camera rotation speed will be the same as in D5 2.6. We recommend setting Orbit as 4 and Fly & Walk as 2.4. You can adjust their values as you need. Please note that the value supports one decimal place.

Save the file and the mouse sensitivity will be modified.