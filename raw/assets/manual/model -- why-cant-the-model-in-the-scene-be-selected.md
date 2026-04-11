# Why can't the model in the scene be selected?

It may be caused by the following reasons:

****1. The object is locked in the "Object" list (as shown below).****

The locked model cannot be directly selected in the scene, but can be selected in the "Object" list. After unlocking, it can be selected in the scene.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FG1ZyEKB3rWwjZhHxAqjE%252Fimage.png%3Falt%3Dmedia%26token%3D859cf23c-b51c-46d5-847e-fa5225e96edb&width=768&dpr=3&quality=100&sign=8a34e71e&sv=2)

****2. The layer where the object is located is locked.****

If the layer where the path is located is locked or hidden, the name of the object in the scene list will be grayed out.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLpCCBMwqAtIs04FSVOpv%252Fimage.png%3Falt%3Dmedia%26token%3D87d6ccaf-ddee-4c25-b672-f027759519f5&width=768&dpr=3&quality=100&sign=434974b9&sv=2)

****3. If the object is far away from the origin point**** , due to precision limitations in calculations, it may be difficult to select the object. You can move the object back to the origin point to select it. Alternatively, you can select the object in the "Object" list and use the shortcut key "Z" to quickly focus on the selected model.

****4. The model is in a group (as shown below).****

When the model is in a group, clicking once will select the entire group where the model is located, while double-clicking on the model will select the elements within the group.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLtQOrnUgjBKNjQzE6ia5%252Fimage.png%3Falt%3Dmedia%26token%3Dc8d275b3-9d77-4692-9802-b49f4afdf619&width=768&dpr=3&quality=100&sign=891d8b55&sv=2)

****5. Category filtering is enabled in the "Object" list.****

When filtering resources of a specific category, only the filtered category can be selected in the scene.

> e.g.
>
> If light sources are filtered in the scene, only the light sources will be displayed in the "Object" list, and only the light sources can be selected in the scene.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FveqX24AQOZsO8hvWwyZX%252Fimage.png%3Falt%3Dmedia%26token%3D77fca529-be29-482e-8cc4-2c15a512e2af&width=768&dpr=3&quality=100&sign=513c0365&sv=2)

Before

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FYPjOU8VRq75jLMd5uvMW%252Fimage.png%3Falt%3Dmedia%26token%3Daf508966-5dbd-47e9-9d1d-f2ec1d723e24&width=768&dpr=3&quality=100&sign=bed910fc&sv=2)

After