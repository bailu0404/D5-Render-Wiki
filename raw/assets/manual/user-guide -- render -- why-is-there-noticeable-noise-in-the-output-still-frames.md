# Why is there noticeable noise in the output still frames?

The following reasons can result in this effect:

It is recommended to update the driver to a later version: [How to view and upgrade graphics card driver?](https://docs.d5render.com/user-guide/hardware/how-to-view-and-upgrade-graphics-card-driver)

You can check the parameters of the abnormal material, if the normal/roughness/specular parameter is very high, or if there is a light source near the current material or the ambient light is relatively strong, noise may appear; it is recommended to reduce the normal/roughness/specular parameter a little.

This is more likely to occur in indoor scenes, especially in models with small windows/rooms with large depths. Using the default sky parameters may result in noise due to insufficient light to illuminate the scene; it is recommended to switch off the dynamic option or reduce the exposure and add other light sources to bring light into the scene.