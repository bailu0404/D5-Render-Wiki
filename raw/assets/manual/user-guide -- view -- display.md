# What are the different display modes for?

## Mode

The Display Modes are divided into Lit, Wireframe and Clay Model.

- ****Lit :**** default mode, with a real-time preview of all materials and lights.
- ****Wireframe :**** shows only edge lines in the scene, and this mode does ****not support rendering****.
- ****Clay Model :**** overrides the material with white material, which makes it easier to emphasize the volume of the model and observe the lighting.
- ****Still/Dynamic :**** controls whether to preview the motion of dynamic elements in the scene.

  e.g. cloud movement, vegetation wind movement, character animation, etc.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFU9yBlnSVGqGt06FNj2E%252FDingtalk_20241021171618.jpg%3Falt%3Dmedia%26token%3D22125cab-5ccc-41e6-aba1-cced1ace9060&width=768&dpr=3&quality=100&sign=5dc08c91&sv=2)

****Lit****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkeVNwZJ9GwamTTKq4k%252F-MkeW4P3HzUnxQc8vvhW%252Ff5c06cef-68b6-4e37-805e-3f76128c387f.png%3Falt%3Dmedia%26token%3D77c6ad16-c143-4511-87da-8ae05662a96c&width=768&dpr=3&quality=100&sign=b3240e0d&sv=2)

****Wireframe****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FCrf87p28PUm3T8Z2bbgB%252FDingtalk_20241021171642.jpg%3Falt%3Dmedia%26token%3D0e0f02e7-57af-49c7-aa1e-044a20da8687&width=768&dpr=3&quality=100&sign=f904c665&sv=2)

****Clay Model****

## Preview Quality

The Preview Quality is the quality of the preview image in the current window. The different preview qualities only represent the results of the current temporary rendering, not the quality of the final rendering. The final rendering quality is always the best result, independent of the quality of this preview.

- When the preview quality is "****Precise****", the real-time preview is automatically enabled.
- When the preview quality is "****Smooth****" , clicking "Render Preview" or pressing F12 will temporarily render the current image to get close to the final rendering quality.

> ✅ > For computers with RTX graphics cards, you can select "Precise" for a better experience.

Preview Quality

Preview Results

Precise

All ray tracing features are turned on in real time, and after a short automatic convergence, physically realistic results are obtained.(Shortcut key F1)

Smooth

Turn off reflections, shadows and other ray tracing features, and click on the Render Preview button to get physically realistic results.(Shortcut key F2)