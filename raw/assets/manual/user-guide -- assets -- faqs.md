# FAQs

## Why is the button for the Assets grey and unclickable?

It is not supported to add models to the scene in render (image/video) mode. Just exit the rendering mode.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F0ipASjBGKDCNVTVJY5IJ%252F%25E7%25B4%25A0%25E6%259D%2590%25E5%25BA%2593%25E6%258C%2589%25E9%2592%25AE%25E7%2581%25B0%25E8%2589%25B2.jpg%3Falt%3Dmedia%26token%3Dd4ca052d-2864-44b0-94b9-f475d31fca50&width=768&dpr=3&quality=100&sign=9924d9d3&sv=2)

## Why are there watermarks/does it display D5 PRO ONLY on assets in the scene?

The watermarked assets are for D5 Pro version only.

Just log in to your Pro/Edu/Teams account to hide the watermarks on assets.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FdSlyakqI7vI4fvUMUwK0%252Fscreenshot_2024-12-05_15-50-02.png%3Falt%3Dmedia%26token%3D56fe0047-0aa5-4242-bc9b-ba201ffcb971&width=768&dpr=3&quality=100&sign=83ca7143&sv=2)

## How to edit the material of a model in Assets Library? How to modify the color of a plant in Assets Library?

> Models from Assets Library are unlocked by default when placed in the scene.

- When the model is unlocked, the selected model will be defaulted to editing status.
- If you need to adjust the material, you need to lock the model, or use the Material Picker (default shortcut is i) to pick up the material directly.

> Specifically, please refer to: [How to select material in the scene?](https://docs.d5render.com/user-guide/material/how-to-select-material-in-the-scene)

## Why doesn't the plant in the scene move with the wind?

#### 1. Use plants not supporting wind movement

All dynamic models in the assets library will have an individual icon on their thumbnails.

- This icon in the plant categories means that it supports wind movement or you can also filter the dynamic models in the assets library.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FzxL3YbB5xg2XD6IlUM90%252Fimage.png%3Falt%3Dmedia%26token%3Df8062b4b-a826-4a3f-9a5e-1ee37ee296f3&width=768&dpr=3&quality=100&sign=522da39c&sv=2)

2. The dynamic mode may not be enabled.

3. The wind option may not be enabled.

## Why doesn't the particle effect move?

#### The dynamic switch in the Display-Mode is not turned on.

The "Dynamic" button is mainly used to control whether or not to preview the movement of dynamic elements in the scene. For example: cloud movement, plant wind movement, character animation, etc. To preview the wind effect, this switch needs to be turned on.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Frqy0mpGRG9T1IgW68V2c%252F%25E5%25AE%259E%25E6%2597%25B6%25E9%259D%259E%25E5%25AE%259E%25E6%2597%25B6%25E7%258A%25B6%25E6%2580%2581.png%3Falt%3Dmedia%26token%3D719ca12e-42ec-49a3-94d3-a9027dd8c955&width=768&dpr=3&quality=100&sign=3a1ac202&sv=2)

## Why is the dynamic character static in the output animation?

It is needed to add keyframes to the ****dynamic characters**** before outputting them in animation mode.

You can refer to the keyframe tutorial:

## Why does the plant gradually revert to its original value after adjusting the base color or base color map, as the distance between the plant and the camera increases?

This is within expectation if the plants showing this effect are low poly plants.

Due to the LOD (Level of Detail) processing of the asset, when the camera is farther away from the plant model, it will use a lower complexity model (i.e., fewer polygons and details), which reduces the rendering burden and improves the rendering efficiency.

Suggestion: Users can turn off LOD in Preference to get normal output (but the preview will still restore the original value).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FYmEl5rvmLj0pQOfVB38f%252F%25E4%25BD%258E%25E6%25A8%25A1%25E6%25A4%258D%25E7%2589%25A9%25E6%2594%25B9%25E5%258F%2598%25E5%259F%25BA%25E7%25A1%2580%25E8%2589%25B2%2520%281%29.gif%3Falt%3Dmedia%26token%3Dc544f712-f123-4915-b0fb-84ea03c93e90&width=768&dpr=3&quality=100&sign=c534414a&sv=2)