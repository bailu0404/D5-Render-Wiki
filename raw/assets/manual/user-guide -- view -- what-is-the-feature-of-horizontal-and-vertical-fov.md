# What is the feature of horizontal and vertical FOV?

In the camera parameters in the upper right corner of the window, the FOV parameter is used to adjust the size of the ****Field of View (FOV)****.

- The default FOV is 90° horizontal.
- You can switch between horizontal and vertical field of view with the button to the right of FOV.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fvig0nTYvMXQ0rQWp7Ksa%252Fimage.png%3Falt%3Dmedia%26token%3D959d7ff6-c07c-467f-bae8-2d9dc99d9e15&width=768&dpr=3&quality=100&sign=9daf0fcf&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FCVfVg2tlZdwqN9AcK1Wh%252Fimage.png%3Falt%3Dmedia%26token%3Dca6824b4-bc87-45f1-a151-b58e0480985b&width=768&dpr=3&quality=100&sign=dd5b077e&sv=2)

## FOV (Horizontal)

Horizontal FOV is locked when the viewport is changed, vertical FOV can be changed freely.

## FOV (Vertical)

Vertical FOV is locked when the viewport is changed, horizontal FOV can be changed freely.

## The value of FOV

In fact, the effect of decreasing FOV is also known as Zoom-in, and the effect of increasing FOV is also known as Zoom-out.

- ****The smaller the FOV****, the smaller the field of view, the smaller the display will be, and ****the objects in the original image will be "enlarged"**** as a result.
- ****The larger the FOV****, the larger the field of view, the larger the display will be, and ****the objects in the original image will be "shrink"**** as a result.

## Common issues

### Q: How to match real and rendered cameras?

Matching real and rendered cameras in D5 can be done by adjusting the "Camera" -> "Focus" parameter to align the frames.

The focal length parameter corresponds to the 35mm film equivalent. You can get the same field of view by entering the meta-information focal length of a real photo into the D5 and matching it to the equivalent parameters of a real-world lens.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FEWhH8LWDVZd3Pec4ksHH%252Fimage.png%3Falt%3Dmedia%26token%3D80e07270-f523-41ad-989d-8ae8a6ea0736&width=768&dpr=3&quality=100&sign=ba1cbe78&sv=2)

Similar issue: What is the difference between horizontal and vertical FOV? How to switch?