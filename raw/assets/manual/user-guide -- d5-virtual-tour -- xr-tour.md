# XR Tour

### What's D5 RENDER XR？

D5 RENDER XR is a new way of displaying rendering results that combines 3d rendering technology and 3d guassian splatting technology, allowing users to use renderers to render images of multiple angles of an object (or scene) in batches, and then publish these training data to the cloud,Through the AI training of the 3d guassian splatting training service deployed on the server, a 3d web link (file format is. ply or. splat) that can be shared online is finally obtained.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fmg5UvHaYxS1dv0EMkL7V%252Fimage.png%3Falt%3Dmedia%26token%3Dbf943e28-f946-40b0-bac6-8006c5f2ab22&width=768&dpr=3&quality=100&sign=3d76da03&sv=2)

### What's 3d Guassian Splatting?

Imagine recording a video of a room with your phone. Traditional methods might produce a basic 3D model, but it would lack detail and render slowly. In contrast, 3DGS represents each point in the scene as a "fuzzy ball" defined by its color, position, size, and transparency (using Gaussian functions). These fuzzy balls are then projected onto 2D images for rendering, enabling fast and high-quality 3D reconstruction.

This approach resembles treating each point in the scene as a light spot and reconstructing the entire scene by overlaying these spots. Leveraging the characteristics of Gaussian functions, the rendered images exhibit smooth edges, intricate details, and realistic visual effects.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fc8NKHBHP7QXTrMxiS7Zs%252Fimage.png%3Falt%3Dmedia%26token%3D580acec3-1e9e-4c99-8503-099da0324e12&width=768&dpr=3&quality=100&sign=c4541ac&sv=2)

Display 3d Guassian Splatting information by storing numerous ellipsoid functions in the ply file

****Advantages of 3d Guassian Splatting technology:****

- ****High quality:**** Compared to traditional methods, 3DGS can more realistically reproduce scene details and lighting effects.
- ****Real-time rendering:**** Using GPU acceleration, 3DGS can achieve real-time rendering at over 30 frames per second, making it suitable for applications such as virtual reality (VR) and augmented reality (AR) that require instant feedback.
- ****Low cost:**** Using ordinary photos or videos, without the need for expensive equipment or complex modeling processes, ordinary users can easily generate high-quality 3D content.

### D5 RENDER XR Workflow

#### ****Step1: Create XR Tour projects, use templates to quickly shoot scenes****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F9wAVsE9AYO7qBfpPcGzv%252Fimage.png%3Falt%3Dmedia%26token%3Dec683996-232f-43b0-b67b-0ddd80b3148c&width=768&dpr=3&quality=100&sign=17e521a6&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FoR7CBjNjSSFr54SqqoVV%252Fimage.png%3Falt%3Dmedia%26token%3D88da8b6e-5905-4f30-8a69-27eabb60f648&width=768&dpr=3&quality=100&sign=8724aba5&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FtWLCveeUDwEm1UyYWN0q%252Fxr.gif%3Falt%3Dmedia%26token%3Dc1292f60-f74c-444e-b1b8-856d68376daa&width=768&dpr=3&quality=100&sign=b577226a&sv=2)
> 70MB

[Initialise templates, editing adjustments and previews.mp4](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FT7nW3OuaM7X4uhRzx9ju%2FInitialise%20templates%2C%20editing%20adjustments%20and%20previews.mp4?alt=media&token=359e312f-7a81-4909-b6ba-5f65388ea6db)Download[Open](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FT7nW3OuaM7X4uhRzx9ju%2FInitialise%20templates%2C%20editing%20adjustments%20and%20previews.mp4?alt=media&token=359e312f-7a81-4909-b6ba-5f65388ea6db)
> 92MB

[Multiple camera templates for display.mp4](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FHtMeUeQFgViB6gTNcLo9%2FMultiple%20camera%20templates%20for%20display.mp4?alt=media&token=53363b2f-a75c-4079-aff6-ed54a33a14b6)Download[Open](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FHtMeUeQFgViB6gTNcLo9%2FMultiple%20camera%20templates%20for%20display.mp4?alt=media&token=53363b2f-a75c-4079-aff6-ed54a33a14b6)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6CCP9NlJchVToA9GJ68P%252F5.gif%3Falt%3Dmedia%26token%3D102a7760-a3cd-412a-b8cb-159a4fc96831&width=768&dpr=3&quality=100&sign=627661a9&sv=2)
> 3MB

[Initiate Multi-Template Rendering.mp4](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FTd3yhrG859k4av1UCqJX%2FInitiate%20Multi-Template%20Rendering.mp4?alt=media&token=c0a98c9a-d2cb-41d5-b282-ebb493336707)Download[Open](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FTd3yhrG859k4av1UCqJX%2FInitiate%20Multi-Template%20Rendering.mp4?alt=media&token=c0a98c9a-d2cb-41d5-b282-ebb493336707)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FHbDoQt4dmKblDC9CGdhD%252F6.gif%3Falt%3Dmedia%26token%3D56b255db-42b5-4337-ab49-f75293b30698&width=768&dpr=3&quality=100&sign=e5e91547&sv=2)
> 55MB

[Local file browsing.mp4](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FEwlMUfHj7njfIYp1BuHM%2FLocal%20file%20browsing.mp4?alt=media&token=608e41ce-af07-4159-9c1b-8103ea002c2e)Download[Open](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FEwlMUfHj7njfIYp1BuHM%2FLocal%20file%20browsing.mp4?alt=media&token=608e41ce-af07-4159-9c1b-8103ea002c2e)

****Template Types and Applicable Scenarios****

Hemisphere templates represent the most widely applicable template type, suitable for rapidly capturing a comprehensive bird's-eye view of an entire building.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FrCb6fIxl6UNL9yD8UDNW%252Fimage.png%3Falt%3Dmedia%26token%3D3b436ca8-171b-4573-8a73-7eefc5e1a8ce&width=768&dpr=3&quality=100&sign=3ad65732&sv=2)

Cube templates comprise six faces and two camera orientations. Users may also choose to exclude models contained within certain faces, thereby enabling enhanced photographic detail for specific angles of the building.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FPEhkJsQBVx2EHVUS2Rk9%252Fimage.png%3Falt%3Dmedia%26token%3D6276c9c5-f534-4868-b570-60ee41f4e8bf&width=768&dpr=3&quality=100&sign=2008c06e&sv=2)

Sphere templates are suitable for 3D objects requiring a 720-degree display of every detail, such as product photography.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F1zhrf1zmSFVEk2kRc9Ri%252Fimage.png%3Falt%3Dmedia%26token%3D5f7c0d3d-cf98-4c0c-b8c8-6e6b9ced0e32&width=768&dpr=3&quality=100&sign=54d06061&sv=2)

#### ****Step2: Publish to the MySpace cloud project and wait for the training to be completed.****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FK18O5Dqcpjcp40cjm56R%252Fimage.png%3Falt%3Dmedia%26token%3D0cbba6d8-266d-49c6-9225-ab1e69e5d4d4&width=768&dpr=3&quality=100&sign=e8ee78a8&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQLPIIVQPyHvobgKU9sNF%252Fimage.png%3Falt%3Dmedia%26token%3D89552d4a-a1dc-4978-bbe5-1af95a2bc906&width=768&dpr=3&quality=100&sign=7b36ab29&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FEeYBpgLbqflkR1y3eGKA%252Fimage.png%3Falt%3Dmedia%26token%3D53c101b9-bcbb-48f5-8c29-e19de7382940&width=768&dpr=3&quality=100&sign=f90330c4&sv=2)

#### ****Step3：Edit & Publish Share in Web Editor****

> 75MB

[Open the Web Editor.mp4](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FmQYXdCDDRvZEesvPzqAl%2FOpen%20the%20Web%20Editor.mp4?alt=media&token=39d5b9f0-a429-405a-9d82-148aad9c7899)Download[Open](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FmQYXdCDDRvZEesvPzqAl%2FOpen%20the%20Web%20Editor.mp4?alt=media&token=39d5b9f0-a429-405a-9d82-148aad9c7899)
> 44MB

[Add hotspots.mp4](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FLf4gxOMvIbxHPdrm1fUV%2FAdd%20hotspots.mp4?alt=media&token=8ca69ae1-624d-4034-86f4-23e37350f7a6)Download[Open](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FLf4gxOMvIbxHPdrm1fUV%2FAdd%20hotspots.mp4?alt=media&token=8ca69ae1-624d-4034-86f4-23e37350f7a6)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJuQmb4ra78Kok7xHdKa8%252Fimage.png%3Falt%3Dmedia%26token%3De1a543d8-94cf-42d7-b9d4-1fc5545b5377&width=768&dpr=3&quality=100&sign=765f1a01&sv=2)

****Media Hotspot****

Video: Require an iframe link for the video to be added

Images: Up to 20 photos may be added, each with a maximum size of 100MB. Supported formats: JPG, JPEG, GIF, PNG, WebP, BMP

Hyperlinks: Supports valid URLs beginning with http/https

Text: Supports free input of plain text (Chinese/English characters, numbers, symbols, etc.), including pasted text. Maximum text length: 1000 characters.

Supports adding URLs and iframe links. Click the preview button in the bottom-right corner of the editor to open a pop-up window. Clicking the icon within the scene will open the corresponding webpage pop-up.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FppnlZ51YkaCo3ng10R8N%252Fimage.png%3Falt%3Dmedia%26token%3D7c12042b-8a77-4806-bd98-90176132ce68&width=768&dpr=3&quality=100&sign=dccc16cc&sv=2)

****Web Hotspot****

Hotspot Style

Hotspot Colour: Select colour from the colour picker

Hotspot Size: Adjust dimensions by dragging the slider

Display Hotspot Name: Enable/disable hotspot name display in the scene

Hotspot Name: Customisable text input

Hotspot Name Position: Position relative to the icon

Text Size: Adjust hotspot name size by dragging the slider

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Frfpohajavpp0H5ZtOPVW%252Fimage.png%3Falt%3Dmedia%26token%3D9ca63c0d-10ca-42fa-91c2-589df108d879&width=768&dpr=3&quality=100&sign=d940f32f&sv=2)

3. Upon completing all edits, click ‘Share’ to generate a shareable link for online display of your 3D project. You may communicate with team members or external collaborators via comments.

> 20MB

[Share videos.mp4](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2F8G44ogKSCcdMSeh1tvHB%2FShare%20videos.mp4?alt=media&token=c7439438-0de1-495f-99da-1b9809d9896a)Download[Open](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2F8G44ogKSCcdMSeh1tvHB%2FShare%20videos.mp4?alt=media&token=c7439438-0de1-495f-99da-1b9809d9896a)

### External Export & Workflow with Other Software

The D5's built-in online XR tour browsing service facilitates project sharing and collaborative communication. Beyond this, it offers more extensive scenarios for integration with other software. Within the user project list↓, users can download .ply source files for import into other software applications.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FxIT8N0bn90NrqEHw77IL%252Fimage.png%3Falt%3Dmedia%26token%3D854c29c3-fa34-4eb0-9bde-9d58a816260e&width=768&dpr=3&quality=100&sign=3a888725&sv=2)

### Import [CESIUM](https://cesium.com/) to make 3d project presentation PPT

After downloading the PLY file locally, upload it to Cesium to create an interactive 3D presentation for the proposal.

> 61MB

[cesium creates ppt.mp4](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FlgdiQGsbzuEOhZeN2l5G%2Fcesium%20creates%20ppt.mp4?alt=media&token=bd941f3c-1611-46e8-a081-a27d6aad3853)Download[Open](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FlgdiQGsbzuEOhZeN2l5G%2Fcesium%20creates%20ppt.mp4?alt=media&token=bd941f3c-1611-46e8-a081-a27d6aad3853)

### Import [Spline](https://app.spline.design/) for Website Development

After downloading ply locally, utilise Spline's APK export service to develop your own 3D app or web application.

> 12MB

[Import Spline for Website Development.mp4](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FMyCc8CvXzgZq6eCfm0V4%2FImport%20Spline%20for%20Website%20Development.mp4?alt=media&token=aa2311ef-22ac-4463-b7d9-f5e7ad0117a3)Download[Open](https://3611830798-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MjbN1iGmN_HBnj_fyU9%2Fuploads%2FMyCc8CvXzgZq6eCfm0V4%2FImport%20Spline%20for%20Website%20Development.mp4?alt=media&token=aa2311ef-22ac-4463-b7d9-f5e7ad0117a3)

### D5 RENDER XR Best Practices

Below, a typical villa residential design project (see the figure below) is used as an example to illustrate how to select appropriate camera templates and configure shooting parameters.

First, we analyze the composition of the project. There is a single main building at the center, with three areas of “negative space” between the building and the background (surrounding trees). Based on this composition, five camera templates are created for the project: two hemisphere templates to cover the main structure, and three cube templates to capture details within the surrounding development spaces.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKN5XAgsNPysWFWQqCwS4%252Fimage.png%3Falt%3Dmedia%26token%3Dc28c94cc-2f22-4579-ae4c-e49b28d0ade6&width=768&dpr=3&quality=100&sign=287f96e5&sv=2)

Using the sandwich technique to capture the building's main structure:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FRk7IXvf3IpaMg9QY0soy%252Fimage.png%3Falt%3Dmedia%26token%3D9b48f90a-b27c-4678-aa60-16c47c2f8f64&width=768&dpr=3&quality=100&sign=a360146&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLgNy2NJmnD9ANDnCoICX%252Fimage.png%3Falt%3Dmedia%26token%3Dd4986bd8-d5df-44a4-8f44-5c01dfc058be&width=768&dpr=3&quality=100&sign=5b667c4a&sv=2)

Use the cube template to add details to the scene:

For the three void spaces at the front elevation, rear courtyard, and garage of the main building structure, create three cube templates respectively.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKIMnkvvADEcSsn4XyfHR%252Fimage.png%3Falt%3Dmedia%26token%3Db5b8f0fb-03ae-4816-b7d1-b24dd193764d&width=768&dpr=3&quality=100&sign=281e3929&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8o29LJhXI3jVlVkvXqNt%252Fimage.png%3Falt%3Dmedia%26token%3D45fb0a92-1b50-4823-962a-ecf0abb0e4b4&width=768&dpr=3&quality=100&sign=7ce4aacc&sv=2)

When capturing the building’s principal elevation, retain only four faces of the cube template. This allows the cube template to be positioned more flexibly within the interstitial spaces between buildings.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8G5Ack09HK45R8KpBfb8%252Fimage.png%3Falt%3Dmedia%26token%3D3e4c82be-017c-4d45-a35a-05b5d63740dc&width=768&dpr=3&quality=100&sign=12006b7a&sv=2)

Upon completion of the final capture and rendering, the results of the trained model published on the webpage are as follows:

<https://share.d5render.cn/team-api/shortLink/BHNNP8>

### Notes

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FtZMmqHVEFN5mY8jLZh8b%252Fimage.png%3Falt%3Dmedia%26token%3D58ed2103-f3cf-415f-ac2e-e91815a660ec&width=768&dpr=3&quality=100&sign=87ccc386&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FU8WAYans7GHvBeq8FvCu%252Fimage.png%3Falt%3Dmedia%26token%3D9385b6e4-20b2-4b29-a856-b2c2bcb865f3&width=768&dpr=3&quality=100&sign=35380a81&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FcEbXuQK8vway2suRQgkS%252Fimage.png%3Falt%3Dmedia%26token%3D1dee20fc-f17a-4675-bd03-b48b43cf0756&width=768&dpr=3&quality=100&sign=20dd39f8&sv=2)

### XR Tour comment function

You can add or view comments on the XR tour's viewing page.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FgyO6n9zoky7AR3tx3eWN%252Fimage.png%3Falt%3Dmedia%26token%3D6711b386-c4ad-4d33-8b3b-be4ea4eda2be&width=768&dpr=3&quality=100&sign=95d3ca72&sv=2)

The comment function is enabled by default and can be disabled in the list on the right in the editor. Users must log in to the D5 account to comment, and anonymous comments from tourists are not supported.

Comments support adding the following type information:

- Text: Up to 500 characters, supports @ team members (only for use between team members)
- Image: up to 20MB. Support screenshot paste
- Camera angle of view: Comments can be added for each camera angle. Clicking a comment will automatically switch the view to the corresponding camera angle.