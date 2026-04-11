# What is the object list? How to manage the resources in a scene?

Resources added to the project will be displayed here in a list.

Models, lights, particles, and other resources placed in the scene will be displayed in the list and support for shortcuts.

Resource information entries in the list can be set using the right-click menu options.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FBCjxoY464n5QGr2LDiPq%252Fimage.png%3Falt%3Dmedia%26token%3D05c91bff-a1ad-4ecf-8767-2b20f3baa4cb&width=768&dpr=3&quality=100&sign=3e2d47f7&sv=2)

## Lock and Unlock

Locked and unlocked are the two most commonly used states in the list. For models, it is not possible to directly select the model in the scene, but the functions of the list menu and the parameters in the right sidebar remain available and disconnect from the "Locked" behaviour.

When the model is locked, you can select the material with the mouse to edit it, instead of using the "Select Material Tool".

Once the model is unlocked, you can make adjustments to the model in the scene. If you want to select the material of the model, you can use the "Select Material Tool".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fg74U8MtNN6vPYznTXn5R%252Fimage.png%3Falt%3Dmedia%26token%3D9360da39-75d6-4450-9c81-4e0be07d2606&width=768&dpr=3&quality=100&sign=c09c80c0&sv=2)

## Sync pivot

After selecting the model in the scene and clicking the "Sync pivot" button on the right menu bar, it supports to synchronize the modelling coordinates to be displayed in D5. It is convenient to create door opening and closing animation.

> In video mode, models that have had keyframes added will be cleared of keyframe data after switching axis positions.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fkmfk9moGBibDGyYDjUtM%252Fimage.png%3Falt%3Dmedia%26token%3D05c4e2ae-8e5a-4a1d-a475-a4d67e3aab16&width=768&dpr=3&quality=100&sign=4c9ecb9b&sv=2)

## Multi-select and Group

> In the list, use the ****Ctrl**** or ****Shift**** keys to multi-select entries.
>
> When performing a multi-select operation, the independence of each object is preserved and the operation after multi-selection is considered as a batch operation.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKoDYDSIO1rTUsKnE0ZLN%252Fimage.png%3Falt%3Dmedia%26token%3Dff6e8d12-bd3e-42ee-b99c-15db05cd9d93&width=768&dpr=3&quality=100&sign=789956f1&sv=2)
> The difference between the behaviour of multi-selection and grouping is that, e.g., for rotational behaviour, the group rotates as a whole when rotating, revolving around the group's axis point; for multi-selection, each object rotates along its own axis.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fd5KkjFg7bJ3WtvPpPwiP%252F%25E5%25A4%259A%25E9%2580%2589%25E5%2592%258C%25E7%25BB%2584.png%3Falt%3Dmedia%26token%3D9392fbb2-5f98-4e62-ae4d-2700d8ce7d88&width=768&dpr=3&quality=100&sign=e2bea8ea&sv=2)

## Filter and Search

By using the filter function below the list, models of different categories in the scene, such as plants, people, vehicles or imported models are displayed by categories. After filtering, only the filtered categories can be selected in the main scene, other categories of models cannot be selected.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FNVxQwCh0zbOblOA0moTr%252Fimage.png%3Falt%3Dmedia%26token%3D4354c314-f5f8-4c9f-b2ed-97bdc818d283&width=768&dpr=3&quality=100&sign=ccda9bca&sv=2)

The entries in the list are searched based on keywords, and the search results are highlighted.

## Object list sorting

When objects are added or grouped, the entries will be arranged below the selected entries. When ungrouping, the top element in the list will be the top element, and the elements in the group will be sorted downwards accordingly.

## FAQ

### Q : Why does hiding or showing a model in the object list not show up in the preview interface?

The model is hidden in the layer settings, thus hiding or showing the model in the object list will always not be shown in the preview interface.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQkSxxNV4rl9LsJtsWouQ%252Fimage.png%3Falt%3Dmedia%26token%3D16e23d96-6e1b-4652-94f7-e5b76f0b5d72&width=768&dpr=3&quality=100&sign=94d76436&sv=2)

### Q : Why doesn't the model show up when imported directly into D5?

There may be the following reasons and solutions:

- Imported models will exist in the Resource list - Imported list. You need to manually click the models to place them in the scene.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSkqgqqXjP6NDjPgYAW4u%252Fimport.jpg%3Falt%3Dmedia%26token%3Dd924f87c-0f72-43f4-802a-5b8f828d6724&width=768&dpr=3&quality=100&sign=58d923b3&sv=2)

- Please check if the device you are using has installed encryption software. D5 may not be able to read models, or model material data, due to encryption software. It is recommended to add the D5 renderer to the whitelist of the encryption software, or decrypt the file before importing it into D5.