# Why models with smaller sizes in the distance not shown when previewing or exporting?

For real-time efficiency, models within 1.5 meters in diameter will be optimized for display at a distance during preview or map output, and the models will be culled and displayed in solid color in the viewport.

In the default preview state, the model will be rejected when the distance from the camera is more than 50 meters.

If the distance of the model from the camera is more than 1000 meters, the model will be rejected in the default output state.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FROaQO2avoaehalQC1oJh%252Fimage.png%3Falt%3Dmedia%26token%3D4e3bb4ce-d765-42d1-85ea-ad0d8c2befa3&width=768&dpr=3&quality=100&sign=43feecd6&sv=2)

This culling distance can be customized in "Preference" -> "Rendering" -> "Cull Distance".

****Inside the Viewport Preview Cull Distance:**** Support to set the culling distance in the preview scene, the range is 20~9999 meters. When the distance is large, it will cause the real-time preview to lag.

****Output Cull Distance:**** Support to set the culling distance when rendering out the image, the range is 20~9999 meters. When the distance is larger, it will prolong the time of image out. In order to ensure that the rendered image is consistent with the preview, the rendering culling distance must be greater than or equal to the preview culling distance.

****Outside the Viewport Cull Distance:**** controls the visibility range for content outside the viewport. This setting affects both the viewport and image/video outputs.

- It is possible to set different distances for real-time preview and rendered results respectively.The settings will be recorded in the project files.
- Best Practice: Enable this option to fix the issue where a plant behind the camera disappears from the transparent material reflections.