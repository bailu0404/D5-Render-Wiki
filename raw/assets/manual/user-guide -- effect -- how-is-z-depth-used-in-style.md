# How is Z Depth used in Style?

## What is Z Depth?

Z Depth map is a picture that records the distance of an object to the camera using the greyscale colour values of the pixels. For example, we can define that points closer to the camera are blacker and points further away from the camera are whiter. We can then get the following Z Depth image:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FMLafBR8dGLtRHN34m9JF%252F174c80ee-c832-496c-aec1-353c3d0be6d1.gif%3Falt%3Dmedia%26token%3Dd9612207-4a75-4431-882e-76b65c569f9e&width=768&dpr=3&quality=100&sign=838b560e&sv=2)

## Where to turn on the Z depth map in D5?

There are ****two places**** in D5 Render related to the Z depth map:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FXt5Cle2E3lK8DZK3pq0a%252Fimage.png%3Falt%3Dmedia%26token%3D390cdd49-5e33-443b-a708-94c99b58dade&width=768&dpr=3&quality=100&sign=968bd6da&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FY8kdYeZ7AZlZWF8PR36z%252F66.png%3Falt%3Dmedia%26token%3D34fe8d60-b822-4410-9b31-6e4baf4bd5e5&width=768&dpr=3&quality=100&sign=557a466e&sv=2)

Image mode Video Sequence Mode (\*Sequence is a Pro function)

## What is the difference between the Z Depth in Style and the Z Depth Channel of the output?

#### Z Depth Style

The Z-Depth screen in Styling is the same as the preview in the D5 viewport, it's just a styling effect that can be toned by post-processing and can be mixed with the Line Drawing mode. We can adjust its exposure, contrast, and even its colour temperature, tint, and other parameters.

As shown below, this is an image that combines Z depth and Outline mode Style, where the main post-processing effects are: dark corners, colour temperature, tint, dispersion and so on.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FhoauNkbT2tOYRO0rZPmz%252Fz1.png%3Falt%3Dmedia%26token%3D2aa94746-f2d5-40ac-8b4e-4fc73205ccaf&width=768&dpr=3&quality=100&sign=664a47b7&sv=2)

#### Z Depth Channel (Z Channel)

In contrast, when outputting images/videos, the custom-selected Z Depth channel is the standard Z Depth map, which is a picture representing the distance from the object to the camera, and is a greyscale map that is not affected by post-tinting parameters.

The pixel colour value of a standard Z Depth Map is proportional to the distance from the object to the camera.

For example, if we specify that a point 0m from the camera is black (with a colour value of 0), and a point about 100m from the camera to infinity is white (with a colour value of 255), then a point about 50m from the camera will appear as grey with a colour value of 128.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKv9tfCq5YkvQNdBqeR4q%252Fz2.png%3Falt%3Dmedia%26token%3D75b1d429-d364-4ed6-b0fb-ff4db5ae6903&width=768&dpr=3&quality=100&sign=d6a01d7&sv=2)

#### Note

## How to use Z Depth slider in Style?

When outputting a Z Depth map, because of the variable dimensions of a 3D scene, the most important parameter is to define the distances of the "black point" and the "white point" to the camera. If the distance between the black and white points is defined properly, the Z Depth map can contain more distance information, which is of rich layers and helpful for post-processing.

****Note:**** To avoid ambiguity, black and white in the following descriptions refer to the colour of the standard Z Depth channel map at the time of image/video output, as they will not be affected by the colour grading parameters.

#### Default Value

For a new scene, D5 defines by default that objects 0 metres from the camera are pure black (colour value 0) and objects 10 metres and more from the camera are pure white (colour value 255), with a linear transition from black to white in between.

By dragging the slider control with the mouse, you can define how far away from the camera you want it to be pure white or pure black, and even swap the left and right positions of the black and white controls so that the near side is white and the far side is black.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F0vrLmCWmaz6qjfXOjw69%252FDAA93254-D84C-41be-B68C-07FD793D3234.png%3Falt%3Dmedia%26token%3D3d9ac360-5768-4477-8209-17508655c4fe&width=768&dpr=3&quality=100&sign=b4574544&sv=2)

#### Non-Linear Slider

To accommodate scenes of different sizes, the Z depth distance slider bar is non-linear, and the following figure gives the approximate distance scale in metres.

The values are for reference only. For actual use, the position of the black-and-white slider scale should be determined according to the preview content of the screen.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F62BsnpUnV4s3E1L01rGU%252FD60B914E-1692-4df5-80FE-3BB01E88860D.png%3Falt%3Dmedia%26token%3D71d7dd18-f365-4dc1-9ea5-9e12b9a8a071&width=768&dpr=3&quality=100&sign=9c9e052a&sv=2)

Specific operations

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FBQ8aakX5MhxMFbPwte4c%252Fimage.png%3Falt%3Dmedia%26token%3Dd12370ea-9b6d-4e05-a948-b85916da1657&width=768&dpr=3&quality=100&sign=148effb1&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Faq2twVxqk6IQukcPOZTN%252FZ%2520Depth.gif%3Falt%3Dmedia%26token%3D5ff259d8-4b61-4772-89cf-150534bb7c85&width=768&dpr=3&quality=100&sign=7b0c7e9a&sv=2)

## Additional Documentation: How to use Z Depth Map in other post-production software?

Here is an example of using Photoshop, a popular compositing software, to show the process of using Z Depth Maps to create depth-of-field effects in post-production.

The scene as shown in the image:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F61YvJtpWKaGHKHgIv83g%252Fimage.png%3Falt%3Dmedia%26token%3D86f2af4c-f2a4-4548-9801-3c3e422da661&width=768&dpr=3&quality=100&sign=bed37d2b&sv=2)

Turn on the "Z Depth" switch in Effect>Style to adjust the distance between the black and white dots to make both the foreground and background objects appear in the preview view:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FigY4rg0C4Dx9WqzHzNYL%252FZ%2520Depth11.gif%3Falt%3Dmedia%26token%3Db3fd00fb-8e2f-4fba-9c31-ff91ff505418&width=768&dpr=3&quality=100&sign=4908b659&sv=2)

Turn off the Z Depth switch and enter the output mode

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fae9CTpmyWeedhAjcZ6hq%252F%25E9%2580%2580%25E5%2587%25BAZ%2520Depth11.gif%3Falt%3Dmedia%26token%3D1f9cdcd1-c9d7-4ab6-b9f0-563e54bde1a9&width=768&dpr=3&quality=100&sign=73872630&sv=2)

In the bottom panel use the scroll wheel, find the channel option, select the Z depth channel and render the image

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FvVMirPYvzqTafsLuI5JI%252Fimage.png%3Falt%3Dmedia%26token%3D9a4a572b-30e3-4794-8ccc-6a4116e03e4c&width=768&dpr=3&quality=100&sign=336351c6&sv=2)

The rendered results are the following two images:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FycSj2HGWFjRRJyty2IRB%252Frender.png%3Falt%3Dmedia%26token%3D65bf1c76-ab8f-444e-82d2-2b4239637369&width=768&dpr=3&quality=100&sign=c7594e39&sv=2)

Just drag the two images into Photoshop and juxtapose them like this:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fqz49Do4sWmyIOyp3bpxS%252Fphotoshop%25E5%25B9%25B6%25E7%25BD%25AE2.gif%3Falt%3Dmedia%26token%3Df1fbf2f9-d4eb-48bf-86e1-344faee1fe3e&width=768&dpr=3&quality=100&sign=45eefb2e&sv=2)

Ctrl+A selects the Z depth map entirely and Ctrl+C copies the Z depth information to the clipboard:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FEFbyj0nLzha5SYqnrkEi%252Fimage.png%3Falt%3Dmedia%26token%3Db21cb303-6904-4664-9475-2bac5b429f64&width=768&dpr=3&quality=100&sign=b4fc0afe&sv=2)

In the result image file, click the "Channels" tab, create a new channel, Ctrl+V, and copy the Z depth information to the new channel "Alpha 1":

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6bipTmAD53gveSR2zgNa%252Fphotoshop%25E5%25A4%258D%25E5%2588%25B6%25E4%25BF%25A1%25E6%2581%25AF.gif%3Falt%3Dmedia%26token%3D5e4c6c89-a835-45b8-b6d6-14c6ba509c56&width=768&dpr=3&quality=100&sign=e82f501&sv=2)

Left-click on the space indicated by the red circle and select the RGB channel.

At this point, the Z Depth information is recorded in the "Alpha 1" channel of the resultant image.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FvpBKiczTtNAqx839NztV%252Fimage.png%3Falt%3Dmedia%26token%3D6ab978d2-0f43-4785-8372-3721dbc9884f&width=768&dpr=3&quality=100&sign=b7e1a65a&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Ftvwyaa3PCHMIA5fJXqV0%252Fimage.png%3Falt%3Dmedia%26token%3Dd8bca6ea-8815-480b-913f-1d58c6b571ae&width=768&dpr=3&quality=100&sign=b3620c6e&sv=2)

Set the Depth Map Source to our pre-written "Alpha 1" channel

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FfUIlEOzXzLoXqak2PUXP%252Fimage.png%3Falt%3Dmedia%26token%3Df615c98d-0197-4a13-a96f-7a8076ad5521&width=768&dpr=3&quality=100&sign=bbadd21c&sv=2)

The value range of the Blur Focus parameter is 0-255, which corresponds to 0-255 of the Z Depth map colour value, and the Blur Focus is set to whatever greyscale, and what Z Depth objects do not produce blurring, and shown to be in sharp focus.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7wDr6oHCzfiHH3eGvhCo%252Fimage.png%3Falt%3Dmedia%26token%3D4eb977c2-6470-4d0f-beb6-c2ab31e76bff&width=768&dpr=3&quality=100&sign=2248e8bd&sv=2)

We can widen the aperture radius to get a more intense depth of field blur effect (consistent with real-life experience):

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FgGaEYAmXDoPm2H1t0kY9%252F%25E8%25B0%2583%25E6%2595%25B4%25E6%25A8%25A1%25E7%25B3%258A%25E5%258D%258A%25E5%25BE%2584.gif%3Falt%3Dmedia%26token%3D08f5ec1c-e7b0-4191-a9eb-4b8b8f774543&width=768&dpr=3&quality=100&sign=837b3933&sv=2)

It is very intuitive and convenient to click on the Set Focal point tool to define the object in focus by clicking directly on it on the screen:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6Z5fYeMgfN0e71beMTnT%252F%25E8%25AE%25BE%25E7%25BD%25AE%25E7%2584%25A6%25E7%2582%25B9.gif%3Falt%3Dmedia%26token%3De13d087a-243a-4b94-9964-383eec242875&width=768&dpr=3&quality=100&sign=a25263c1&sv=2)