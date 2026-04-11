# Action

When an unlocked model is selected, the relevant parameters are displayed on the right for adjustment.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F5IPyckDsa7oQVANv3M8p%252Fmodel.png%3Falt%3Dmedia%26token%3D2fb5263a-adcc-4d4d-82c8-60162cc00df4&width=768&dpr=3&quality=100&sign=87051af&sv=2)

## Duplicate

When you click "Duplicate", an identical model will be created at the cursor and will follow the mouse movement.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-Mkeb22qhypbCw78jZf6%252F-MkebjxW84jJoJq7Op5H%252Fdup.gif%3Falt%3Dmedia%26token%3D88c0143c-4baf-494a-b807-b0395643d206&width=768&dpr=3&quality=100&sign=fda22253&sv=2)

When using the shortcut `Ctrl+D` to duplicate, materials are associated with each other by default. That is, if you adjust the material on any model, the other model will follow the change. If you want to duplicate without association, you can use `Alt+D` to duplicate.

## Make Unique

If you need to unassociate a material from a model that was created by a duplicate operation, click on "Make Unique" to unassociate it.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkebopxW69NwlWpRhlV%252F-Mked5wV_G2m5sAwjfFT%252FU.gif%3Falt%3Dmedia%26token%3Dded2438c-9d1d-4627-8e07-2524b4ac5d63&width=768&dpr=3&quality=100&sign=ee9bb31d&sv=2)

## Flip

The "Flip" function mirrors the model along the red axis (X axis).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkebopxW69NwlWpRhlV%252F-MkedCXkAMY34uIL_mI9%252Fflip.gif%3Falt%3Dmedia%26token%3D320bd686-9f59-4106-917b-85008633444c&width=768&dpr=3&quality=100&sign=96b80509&sv=2)

## Focus on

Select the object and move the camera to the front of the object so that the object is fully displayed in the main view.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkebopxW69NwlWpRhlV%252F-MkedxMlDYNKVdbU7aNo%252Ffocus.gif%3Falt%3Dmedia%26token%3D16c7e87a-9dd3-4bce-ab3a-ee77cf4318b3&width=768&dpr=3&quality=100&sign=69827ef4&sv=2)

## Align

For model files imported in parts, after multi-selecting models (hold `Ctrl` to multi-select), using the "Align" function, the selected models will be aligned according to the original modeling axes, keeping the relative position of the coordinates in the modeling software unchanged.

When aligning, the first selected model is used as the reference and its position remains unchanged, and the other models are aligned to the first model.

> ✅ > For example, if there are three models A, B and C, and the selected order is B, C and A, then B remains in the same position when aligning, and C and A models are aligned to B with the original modeling coordinates.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkebopxW69NwlWpRhlV%252F-Mkedsf_1sYEi9-Gz32s%252F28dd1bbf-6cb0-4264-ab5e-d3395647174c.gif%3Falt%3Dmedia%26token%3D56502d3d-4b07-4a6f-9f7c-7a3fc24af619&width=768&dpr=3&quality=100&sign=9931cc2&sv=2)

## ****Sync coordinates****

For imported models, when clicked "Sync Coordinates", the model will move to the location of the coordinates from modeling software. The Align button is to multi-select models then align them according to their relative position, while the "Sync Coordinates" function is to recover their absolute positions( X, Y, Z).

After clicking the "Replace from Assets" button, select a model from the Asset library to replace the selected model in the current scene.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLf4FSUJHr0b6NZAaefdt%252FSync%2520coordinates.png%3Falt%3Dmedia%26token%3D24b6b7c5-22bd-47dc-896b-4692626bc277&width=768&dpr=3&quality=100&sign=20fa29f1&sv=2)

## Replace from Local Folder

After clicking the "Replace from Local Folder" button, select a model file from the local folder to replace the model in the current scene.

## Reload

After the model source file is modified and saved, click Reload and D5 will automatically synchronize the model to the latest, consistent with the source file.

You can continue to operate in the scene while the model is reloading. The progress of the update is displayed in the resource list on the left; when reload is complete, a finish mark will displayed in the list.

## Export and Add to local

For models that have been imported into D5, click "Add to Local" to save the adjusted model to "Assets" -> "Local" for easy reuse in other projects. You can also choose to export the model as .d5a format and save it locally.

Export and Add to Local functions are also supported for grouped models.