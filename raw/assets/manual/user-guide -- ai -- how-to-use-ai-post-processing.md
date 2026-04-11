# How to use AI Post-Processing?

To enhance details of rendered images (lighting, materials, characters, vehicles, vegetation, etc.).

> ℹ️ > ****Note****

> Note:

- Click the 'AI Post-Processing' feature from the navigation bar.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FUY6UVTv7pIep0spK69d8%252FB4D46ED0-EA9F-4617-A88D-C18B8C7F569F.png%3Falt%3Dmedia%26token%3D4de99fb7-a7bd-4108-987a-e0f3e7dcd00f&width=768&dpr=3&quality=100&sign=8689ee1a&sv=2)

## AI Enhancer

Enhance the details of lighting, materials, characters, vehicles, and plants in rendered images.

### 1. Enhance Content

Supports selecting specific regions of an image to be enhanced, keeping the remaining unselected parts unchanged. By default, the entire image is enhanced if no specific region is selected.

### 2. Enhancement Weight

Users can drag the slider bar according to their needs to select different processing effects.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FnOwoDG9QCyhK5OmfTZov%252Fimage.png%3Falt%3Dmedia%26token%3Da132db90-9338-4323-bccd-6cb1e4f0c63a&width=768&dpr=3&quality=100&sign=6c4de9da&sv=2)

Enhancement Weight

### 3. Texture Strength

Users can freely adjust the enhancement strength of the texture according to their creative needs.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FnmxDefUdhg9UXnB9veN7%252Fimage.png%3Falt%3Dmedia%26token%3Ddddde606-4e12-4f29-9918-005ee476de83&width=768&dpr=3&quality=100&sign=433f2dbc&sv=2)

Texture Strength

### 4. Adjust Content

Choose 'Enhance Content', adjust the relevant parameters, and click to save the partition. This allows you to assign different weights to various areas, addressing the enhancement needs of different materials simultaneously.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FMxA67zFHAj26kOCrZJxj%252FAI%25E5%25A2%259E%25E5%25BC%25BA%25E5%258F%2582%25E6%2595%25B0.gif%3Falt%3Dmedia%26token%3D3c0ae955-28ba-4b41-a147-d6f88fadc76c&width=768&dpr=3&quality=100&sign=957e6ed1&sv=2)

---

## AI Style Transfer

Select the desired post style, adjust the AI settings, and click the AI Style Transfer button to complete the style transfer.

- ****Stylized:**** Supports one-click transfer to watercolor/cartoon/scale model/pen sketch/pencil sketch/voxel styles without material or model adjustments.
- ****Realistic:**** Supports rapid transfer to photorealistic sunset/night/spring/summer/autumn/winter styles. Supports adapting to reference image styles.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FjiCAzxBmquyalOwxcRtF%252FAI%25E9%25A3%258E%25E6%25A0%25BC.gif%3Falt%3Dmedia%26token%3Dad514000-9d33-4caf-87f9-08ccabc861bc&width=768&dpr=3&quality=100&sign=c1e91c75&sv=2)

---

## Inpainting

Added new local inpainting feature to automatically recognize and inpaint sky, water, or vegetation for images rendered with AI Post channel.

- ****Best practice:**** Leave specific areas, such as a flower garden, empty without the need for manual layout; AI will automatically populate them to enhance the visual appeal.
- ****Inpaint the original image:**** Allows AI to intelligently inpaint based on the original image structure to align with the creative intention.

> ****Note:****
>
> D5 supports auto recognition for the ****Sky**** area. ****Other categories**** (Water and Vegetation) require manual selection.
>
> ****Seed:**** A seed is an integer between 1 and 2147483648. When you use the same prompt and seed, you will get the same result.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FR4cMwI0AnOcyTw8n1T7J%252Fimage.png%3Falt%3Dmedia%26token%3D41002ce5-a8b4-4d86-9563-dc96c3d09dc3&width=768&dpr=3&quality=100&sign=82e9ae&sv=2)

---

## Effect

### Post-production

Select the area to be adjusted, then adjust the ****sharpening, denoising and transparency**** parameters, and click the Save button to save the effect.

- ****Sharpening:**** Improves image clarity by amplifying high-frequency details, enhancing edges and contours to highlight critical features and details.
- ****Denoising****: Reduces noise in the generated image to improve overall quality while maintaining the integrity of the original image’s key characteristics.
- ****Transparency:**** Controls the opacity of the AI-enhanced image, determining the visual blending ratio between the enhanced elements and the original content.

> Note:

### Motion Blur

Supports adding Motion Blur to characters and vehicles with one click.

- Supports customization of angle and intensity.
- Supports setting taillights for vehicles.

> ⚠️ > Note:

'Tail Light' option appears only if the following conditions are met:

- The image contains the Car (must be from D5 Assets Library).
- The current image needs to have been rendered with 'AI Post Channel'.
- Clicked to select regions for processing

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FEaNhUDtas0W4z2Uaxdhz%252Fimage.png%3Falt%3Dmedia%26token%3Db270e96a-7d76-4620-86a9-ffca3f632a50&width=768&dpr=3&quality=100&sign=cfe28ab6&sv=2)

---

## AI Post Channel

The ****AI Post Channel**** in the channels improves the accuracy of region selection during AI Enhancer.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FHThvpw4ZD94M1agM1pSv%252F12.png%3Falt%3Dmedia%26token%3D78243dc1-a4a5-4f8e-a330-d68306f05e91&width=768&dpr=3&quality=100&sign=12f826cf&sv=2)
> ℹ️ > Note:

AI Enhancer & AI Enhancer Channel only support ****rendered images within 6K resolution (no more than 6200 pixels on any side)**** in saved archives.

**Over-sized images can't be ticked with “AI Post Channel” and won't show the 'AI Post-Processing' entrance after rendering.**

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FBnEyGb3VS4vca6yK4mGj%252F6b8e5d8ecfcc47e2498bfc7c75914da2.png%3Falt%3Dmedia%26token%3D85be6af0-dfda-4722-9a6c-b3d30a29b37b&width=300&dpr=3&quality=100&sign=a301edfb&sv=2) ![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8OmCHwIp5rN1VqUiWRCC%252Fc7039b53bec8b649530ff4f4771c157a.png%3Falt%3Dmedia%26token%3Dd287ae76-80da-4d2d-848c-97667e91e6f9&width=300&dpr=3&quality=100&sign=7347d707&sv=2)