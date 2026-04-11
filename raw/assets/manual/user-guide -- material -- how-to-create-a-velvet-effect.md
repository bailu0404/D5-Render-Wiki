# How to create a velvet effect？

Important material parameters related to velvet are:

- Normal: Used to simulate the bumpiness of the velvet fabric itself.
- Specular: Used to simulate the sheen of a velvet surface.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fcw6tWoue7xpDMjkhcfXi%252Fvelvet1.png%3Falt%3Dmedia%26token%3D96a1c121-eb94-42af-849d-8de4a3dfdaf6&width=768&dpr=3&quality=100&sign=e7834dd9&sv=2)

- Attenuation: The use of attenuation simulates the effect of a dense, flat, glossy pile on velvet. The whitening effect is more pronounced where the surface of the material is tangent to the camera's line of sight. The higher the Attenuation parameter, the more pronounced the whitening.
- AO: Ambient Occlusion channel, through the AO map and the base colour mapping positive slicing (multiplication), to enhance the corners and seams of the shadows, to enhance the role of the details of the three-dimensional sense of the role, used to simulate the surface of the velvet unique traces of kneading.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJxNwXkYvwfjPBhSLFoNn%252Fvelvet%2520ao.png%3Falt%3Dmedia%26token%3Dae1b282e-6b50-4287-a25f-9d070531e4d7&width=768&dpr=3&quality=100&sign=936cfffb&sv=2)

The "Velvet 01" and "Velvet 02" in the Material Library - Cloth - Velvet are the new velvet materials using this set of maps. You can combine more velvet materials based on the above principle by replacing the base colorr maps and adjusting the UV parameters according to the current usage scenario.