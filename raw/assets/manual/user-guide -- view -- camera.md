# Camera and Views

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFIniD8tIVdTQHAMuZD5J%252FDingtalk_20241024211127.jpg%3Falt%3Dmedia%26token%3D3b3a5b47-e2a3-43ff-8871-eed4e095edd1&width=768&dpr=3&quality=100&sign=ac53f503&sv=2)

## Options

### ****Exposure****

Adjust the overall brightness of the image.

- ****With Auto Exposure switch on****, the renderer automatically analyzes the scene brightness and adjusts it to a moderate value.
- ****With Auto Exposure off****, you can manually adjust the Exposure parameter values.

The lower the Exposure value, the darker the image, and the higher the Exposure value, the brighter the image.

> ⚠️ > - ****Auto Exposure**** is turned on by default in newly created projects.
- ****The "Exposure" settings**** here are linked to the exposure settings in "Effect panel--Post-processing".

### ****FOV(Field of View)****

Adjusts the Field of View (FOV) angle. The default field of view is 90°.

- ****The smaller the "Field of View"****, the smaller the area displayed on the screen, and ****the subject in the original image will be "enlarged"**** accordingly.
- ****The larger "Field of View"****, the larger the area displayed on the screen, and ****the subject in the original image will be "shrink"**** accordingly.

> ℹ️ > In fact, the effect of reducing the FOV is also called Zoom-in, and the effect of increasing the FOV is also called Zoom-out.

### ****Camera Clipping Plane****

The clipping plane in D5 is the near clipping plane, which is arranged perpendicular to the camera. After setting the distance between the camera and the plane, the scene between them will not be visible.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkeWeI4P1nOT8KgORsS%252F-MkeXz9tgu6K0gHx0qQ4%252Fclipping.gif%3Falt%3Dmedia%26token%3Dac63608a-dccf-4662-a76c-578bdc743588&width=768&dpr=3&quality=100&sign=7174fd1f&sv=2)

### ****Depth of Field****

Similar to real-world cameras, depth of field is based on the Focal Distance, blurring the scene in front of and behind the focal point.

- Turn on the Depth-of-Field switch, click ****"Set Focus"****, click the object you want to focus on in the scene, and determine the focus position.
- Also,when clicks ****"Follow Focus"****,it can support the function of auto follow focus.
- Adjust the value of the ****"Blur"**** parameter to change the strength of the depth-of-field effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FfETHkzwPzdZRIG6l5xuL%252F%25E6%259C%25AA%25E6%25A0%2587%25E9%25A2%2598-1.png%3Falt%3Dmedia%26token%3D7353b603-c78f-4864-b749-b3502d9d41ae&width=768&dpr=3&quality=100&sign=2e6b9ae0&sv=2)

depth of field is 0 | depth of field is 5 | depth of field is 10

## View

### ****Perspective and Two-point Perspective****

- The ****"Perspective"**** is the default 3D space display mode.
- When ****"Two-point Perspective"**** is turned on, the vertical perspective lines in space are parallel to the vertical borders of the screen.

### ****Orthogonal view****

Orthogonal is a 2D planar display that contains six common view styles.

> For more information on shortcuts, please refer to:<https://docs.d5render.com/user-guide/preference/how-to-view-and-change-the-default-shortcuts#common-shortcuts-for-d5-render>

Modes

Shotcut

Perspective

P

Two-point Perspective

F8

Top

T

Bottom

Alt + T

Front

F

Back

Alt + F

Left

-

Right

-