# How to use Projector Widget?

Go to Menu > Preference > Widget, and you can check what you have installed, click to toggle on/off and manage your widgets.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FBGFB24WvpiWdwsrBDP2m%252Fimage.png%3Falt%3Dmedia%26token%3D83822fd5-e577-40bf-aade-2665353045e1&width=768&dpr=3&quality=100&sign=4b2ab87f&sv=2)

Projector Widget

---

Go to Menu > Preference > Widget to activate Projector, and insert it into the scene from Navigation bar > Add lights

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FqjyV5IyZNu6y2cp8r1gy%252Fimage.png%3Falt%3Dmedia%26token%3D02a91f5d-f504-4996-9b49-904812444981&width=768&dpr=3&quality=100&sign=41b7d4d6&sv=2)

Projector

Projector is a new type of light source which has a rectangular projection effect. It supports image formats including jpg/png/bmp and video formats including mp4/avi/wmv. After adding a projector to the scene, we can adjust its parameters in Inspector.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FxTnOIEXLM2BV656PFBX7%252Fimage.png%3Falt%3Dmedia%26token%3D90253959-e138-4367-920d-ecfc9dd3c69a&width=768&dpr=3&quality=100&sign=76a8484e&sv=2)

Inspector

- Video: Customized pattern can be uploaded to determine the projection screen.
- Intensity: The luminous intensity of the light source in cd (candela), the maximum brightness can be entered 8000000.
- Cone Angle: Control the cone angle range of the projector's light emitting cone. The cone angle parameter allows you to control the feedback of the projection pattern.
- Attenuation Radius: Limit the range of influence of the light source. Within this range, the light fades according to the normal inverse square law, and beyond this range, the light calculation stops.
- UV: Control the position or size of the image or video within the projection.
- Haze: To create a Haze effect, we need to turn on Volume Light in Environment - > Weather - > Fog beforehand.

---

### FAQs

#### 1.Why are the Stage Lights effect abnormal?

The maximum number of the Stage Light/Projector is 64, if it exceeds the change limit it may cause abnormal preview or output effect.

#### 2.Why the specular reflection Stage Light/Projector effect is not shown in the rendering result?

This effect is not supported in the current version and will be supported in subsequent versions.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKuT8Ux6juu0cF0Aok1da%252Fimage.png%3Falt%3Dmedia%26token%3D2d41e11a-6246-4976-81b5-bbef9d5d4511&width=768&dpr=3&quality=100&sign=737e71a8&sv=2)

Preview and output effect of the current version of Mirror Reflection Stage Light/Projector