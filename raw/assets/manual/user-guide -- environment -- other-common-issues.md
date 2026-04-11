# Other common issues

## 1. Why is the imported HDRI blurry?

High-definition HDRI takes up more resources when previewing, so the HDRI is compressed to 2k by the D5 when previewing to ensure that accurate lighting is provided.

- The image output is based on the actual size of the imported HDRI.
- The HDRI is also compressed to 2K/4K/8K for video.

## 2. Why does it prompt " Failed to load HDRI"?

Custom HDRIs imported into the D5 renderer need to be standard size files.

Common sizes:

1k2k4k8k

1024×512

2048 × 1024

4096 × 2048

8192 × 4096


## 3. Why are there two angles of shadow in the scene?

In some HDRIs the sun is visible and already produces clear shadows. If ****"Sun-Direction-Custom" is ticked****, it is possible to have this "heavy shadow" problem in certain cases, because there is already a sun in the original HDRI.

The following is recommended for adjusting the sky:

## 4. How to adjust the Tyndall effect/volume light?

In the second item of the "Environment" panel on the right sidebar, find ****"Weather" > select "Fog" > enable the "Volume Light" button****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F1tQaoOGXVJGzvH1VHkZS%252Fimage.png%3Falt%3Dmedia%26token%3D3ce24232-141a-4464-8cbf-a9e8fb591517&width=768&dpr=3&quality=100&sign=dae94e7f&sv=2)

- Volume Light: The Tyndall effect is a phenomenon in which light is scattered by particles in the air, allowing pathways of light to be seen.
- Scattering: Controls the scattering distribution of the Volume Light scattering effect. The default value is 0 for a uniformly light fog, adjusting it to 1 will make the fog brighter from the direction of the light source.

> Note: The issue of "preview is normal but output has no Tyndall effect" has been fixed in 2.9 version, please output with 2.9 version.

> ℹ️ > ****Note:****

If you get ‘stripes of light’ when creating the Tyndall effect/Volume Light, this is a known issue with the current 2.9 version. Please try giving the one-sided wall a certain thickness (or placing a plane outside the wall).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FfJXhTboOC8hD8hoxHLtW%252F%25E6%259C%25AA%25E6%25A0%2587%25E9%25A2%2598-1.png%3Falt%3Dmedia%26token%3Da51f8f9c-aff5-4d84-b24a-45acfb6d193b&width=768&dpr=3&quality=100&sign=6919c573&sv=2)

stripes of ligh & placing a plane outside the wall

## 5. How do I achieve the effect of no precipitation but having standing water/snow?

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FtfbSb9QzhWVsMg8JXXZZ%252Fimage.png%3Falt%3Dmedia%26token%3D565b7477-1fd8-41aa-933c-3f25d4f8590f&width=768&dpr=3&quality=100&sign=3bc9dc10&sv=2)

adjust the Precipitation strength to 0, and increase the Puddle

## 6. Why is the custom HDRI/LUT file import not working?

This will occur if the file path of the custom HDRI/LUT file contains special characters.

It is recommended that the HDRI/LUT file be placed under an English path.

## 7. Why do scenes lose HDRI thumbnails?

There are two cases that can occur in the current version:

- Load an old archive and that archive uses the D5 inbuilt HDRI - Pure White;
- Download the HDRI from the D5 Assets Library - HDRI and import its local cache.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fg5GSdoOGVq50IAQCg6uH%252Fimage.png%3Falt%3Dmedia%26token%3Dc847fa14-e638-4676-a857-34e957b6d479&width=768&dpr=3&quality=100&sign=1a9cf73e&sv=2)

## 8. When keyframing the environment (Geo and Sky/HDRI), why does the scene flicker/have white spots?

It's a current KNOWN ISSUE.

It is relatively difficult to downsample in this case (when the scene environment changes), thus white spots/scene flickering may occur during preview or output.

Suggestion: When keyframing the environment in animations, if white spots/flickering occurs, it is recommended to output in two separate times and merge them in the post-production software.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FN4LdRPxofJFvQFNXPBbz%252F0814%2520%281%29.gif%3Falt%3Dmedia%26token%3Ded5c9a39-93c1-44dd-81dc-a5fd4760e3ef&width=768&dpr=3&quality=100&sign=4741f65d&sv=2)

## 9. Why do scenes created in version 3.0 appear different when opened in previous versions?

When opening files saved in version 3.0 using previous D5 versions, ****the manual exposure**** and ****fog effects**** may alter, requiring manual adjustment of the parameters.