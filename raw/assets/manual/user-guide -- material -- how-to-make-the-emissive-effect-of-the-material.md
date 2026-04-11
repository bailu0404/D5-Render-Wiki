# How to make the emissive effect of the material?

In the custom material template, turning on the emissive switch will make the material produce a glowing effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FgT2M5aF5DiSplJelhqpG%252F4.gif%3Falt%3Dmedia%26token%3D0a9e85cc-b908-43a8-9423-51fc39b9e820&width=768&dpr=3&quality=100&sign=e7b34f2a&sv=2)

## Intensity

Pull the widget to control the intensity. You can also use a texture map to define the brightness.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FDVWN9cKx5rQOVGfNI6kF%252F6.gif%3Falt%3Dmedia%26token%3Ddd3130f1-e6c1-49a4-b142-c8c5beb50f68&width=768&dpr=3&quality=100&sign=1200c97d&sv=2)

Intensity

## Emissive colour

The specific emissive color can be any RGB color, or a specified color temperature.

## Cast Shadow

"Cast Shadow" controls whether the emissive effect participates in the calculation of illumination (specifically, diffuse light). After choosing this option, the emissive material will be visible in the reflection of the camera and other materials, but it will no longer produce shadows and light bounces.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fkc4NoJhAh6caLlFGjLil%252F7-1.gif%3Falt%3Dmedia%26token%3Dd7b7527d-4086-4194-a0b3-449730b70681&width=768&dpr=3&quality=100&sign=9d836188&sv=2)

Cast Shadow

## FAQs

### 1. Why do the self-emissive materials flicker when rendering animations?

Possible causes:

- ****Surfaces of self-emissive objects overlapped or interspersed with other models.****
- There are large self-emissive planes in the scene that cause abnormal accuracy and thus flicker, try turning off the “Emissive - Cast Shadow”.
- Self-emissive objects are thin, try turning off “Menu-Super Resolution” and re-outputting.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FhARGESbqDeJcjH6SjcS3%252Fimage.png%3Falt%3Dmedia%26token%3D93935692-0acf-4b79-b267-7aae1a8df2b8&width=768&dpr=3&quality=100&sign=60857a54&sv=2)

Self-emissive objects interspersing with other models are easily generating light spots.