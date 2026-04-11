# How to render channel maps? Which channel maps are supported?

Check the Channel option, and check the desired channel map for rendering in the right setting column of it, then the channel maps will be exported when exporting the pictures, which can be used for post-processing.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FOGzUrzhpWoOIvra0RaG2%252Fimage.png%3Falt%3Dmedia%26token%3D13bf1e7c-da35-4188-a68d-c62dc0c97cc4&width=768&dpr=3&quality=100&sign=9a88a42a&sv=2)

Currently D5 supports rendering the following types of channel maps:

- SkyMask
- AO
- MaterialID
- Reflection
- Transparent
- ZDepth
- AI Post Channel (AI\_Albedo、AI\_Normal、AI\_Material)

> Note:
>
> AI Post Channel is checked by default when outputting images; not available when outputting sequence frames.

## FAQS

****1.Why aren't transparent materials displayed in the channel map?****

A: For ease of post-processing, D5 provides an exclusive colored channel map called 'Transparent' for rendered transparent materials.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FXpxhayTVGzMzMNOs2Z7y%252F4553c892bd478c15a7ddf7198d28da5ae9d10305.gif%3Falt%3Dmedia%26token%3D3bbf56a1-3237-4ffd-a537-ddb62142c186&width=768&dpr=3&quality=100&sign=e61e9003&sv=2)