# What materials are the Water templates suitable for? What are the special parameters?

The Water material template has animated effects and is used to create flowing water.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkejL9M9mZrDG476XmI%252F-MkekNbWDwVEw4GJp3pN%252Fwater.gif%3Falt%3Dmedia%26token%3Db0ab6eae-2407-4665-b0c6-3aad5f37a815&width=768&dpr=3&quality=100&sign=a6e63acd&sv=2)

- ****Base color/Base Color Map:**** Used to control the color of the water.
- ****Normal:**** Controls the size of the wave.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkejL9M9mZrDG476XmI%252F-MkeknNouH9HihumqXlo%252FwaterN.gif%3Falt%3Dmedia%26token%3D374584f6-d3f8-48cf-bcdc-950879b4a44a&width=768&dpr=3&quality=100&sign=ea019242&sv=2)

- ****Specular:**** Control the Reflectance of the water surface, the specular value of water is 0.25.
- ****Refraction:**** Control the IOR of the water surface. The IOR of water is 1.33.
- ****Flow Velocity:**** Adjust the rate of the water animation, turn on "Realtime" to preview the water animation in "Display" option.
- ****Depth:**** Control the absorption of the water to the incident light, make clear shallow water or more turbid and deep water, need to model the part below the water surface to see the effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkejL9M9mZrDG476XmI%252F-Mkel9soNT2NzsuWxUD5%252FwaterD.gif%3Falt%3Dmedia%26token%3D3586c816-bcd8-4c47-bbaa-d28cf6a2a5cb&width=768&dpr=3&quality=100&sign=a3c31f86&sv=2)

## FAQ

### Q1: How to achieve the correct water effect?

To be able to fully display the effect of water, the following should be taken into consideration:

- When modeling, ****the water material itself is a single-sided model****.
- When modeling, ****there should be a plane below the water material model**** (i.e., the bottom of the water) .
- When rendering a video, appropriately adjusting the "****Flow Velocity****" can better depict the fluctuation of the water surface.
- Control the ripple of water by ****adjusting the normal intensity and custom normal maps****.
- The color of the water can be accurately controlled by the ****"Base Color-Hue, Saturation, Luminance"& "Depth"**** parameter of the Water Material Template in the Material panel.

The depth parameters in D5 make the water material more realistic, closely resembling physical phenomena in real life, and this is related to the depth of the container.

> As can be clearly seen from the diagram, under the same material parameters, the effect of container depth on the water material representation:

The color of water also changes with the depth of the container, equivalent to automatically attenuating the intensity of light below the surface according to depth.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F1KODNjjKQ5jxGt55TwEM%252F339a5859-6cbb-4397-a53c-448e51df5ce0.png%3Falt%3Dmedia%26token%3D21947df0-6773-41d5-8575-4e3d4101afbf&width=768&dpr=3&quality=100&sign=79ebf8ea&sv=2)

under the same material parameters, the effect of container depth on the water material representation