# What is the Scene List?

## Scene shot setup

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FGT5sdrL9ODt5eovbQ1gZ%252Fimage.png%3Falt%3Dmedia%26token%3D09b377f9-8ab7-4714-b374-31e9608e4927&width=768&dpr=3&quality=100&sign=b91d16f9&sv=2)

When you have saved multiple camera views in the scene list, you can click on one of them to switch the shot. You can also click the "Rename", "Update Scene" and "Delete" buttons after the shot name to adjust the current saved shot view.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FUtYI93IIVnPWrQS5jjKS%252Fimage.png%3Falt%3Dmedia%26token%3D2b902e57-f0ea-4a4f-ba5f-fd0ab906a2e9&width=768&dpr=3&quality=100&sign=f6f1b23f&sv=2)

- Transition Animation is used to set whether or not to display the transition animation at the same time as the shot switch.
- Environment & Effect

-Apply to all: apply the last adjusted outdoor and post parameters when switching between cameras. It reads the scene's camera position information and the current outdoor and post parameters when switching between cameras.

-Save separately: when switching between cameras, read the current scene's camera position information and environment post parameters.

> ℹ️ > ****Note:****

If the scene parameters are not saved after switching shots, it is possible that "Apply to all" is turned on in the settings of the scene list.

- Copy/Paste feature: Copy and click Paste to immediately apply the environment and effect parameters saved in the scene to a different scene.
- Create Preset: Store the Environment & Effect parameters of the current scene as a preset in Studio.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fi7KMybR1WV0m5QoUJ9TC%252Fimage.png%3Falt%3Dmedia%26token%3D86abe322-ae54-480d-8ca8-e20aa86dbe57&width=768&dpr=3&quality=100&sign=cd40f970&sv=2)

## Create New Scene

In the scene list, click the "Add Scene" button to save the current view. When creating a scene, it will record the ambient lighting information of the current scene and the color and special effect information in the post-processing stage. Each scene can correspond to different parameters.

When you add a scene, a camera for the current viewpoint will be created by default. Click "Scene" to activate the camera. The camera in the upper right corner of the interface will indicate the currently activated camera. Click on the camera icon to exit the activated state of the camera in the right sidebar, and set the projection mode, frame ratio, depth of field, and other parameters. The camera parameters adjusted in the right sidebar will be updated instantly without clicking. The camera parameters adjusted in the right sidebar will take effect instantly without clicking "Update."

When you move the viewpoint only when the scene is selected, the camera corresponding to the scene will be exited immediately, and return to the default "God's view" state. When both the scene and the camera are selected, you can keep the mobile operation in an active state.

> ℹ️ > ****Note:****

If the screen returns to the default "God's view" when the viewpoint is moved, it is because the scene and its corresponding camera are not selected at the same time.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FbJWtUewVx1KC9wfq0bm8%252Fimage.png%3Falt%3Dmedia%26token%3D53a06071-58b2-4916-8ef6-5ec6fa1d742d&width=768&dpr=3&quality=100&sign=c8d87402&sv=2)

## Update scene shots

Scene shots will record the environment, post, and the current object's hidden state information when created. When the environment and post parameters are modified, the parameters need to be updated.

A purple dot indicates that it has been successfully updated.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQLEgxvvP4RfbYA0GHRaV%252Fimage.png%3Falt%3Dmedia%26token%3D7db93c59-745e-40c5-9244-846912513873&width=768&dpr=3&quality=100&sign=6852fc46&sv=2)

## Scene List supports group management

****Scene Group Creation and Management****

****Create Group:**** Right click Scene Group → Select ''Group'' or use shortcut `Ctrl + G`

****Ungroup:**** Right click the Scene Group → Select ''Ungroup'' or use shortcut `Ctrl + Shift + G`

****Rename:**** Right click the Scene Group → Select ''Rename'' or double click group name

****Paste Parameter to Groups:**** After copying the parameter, right click the Scene Group → Select ''Paste Parameter'' → The Environment/Post-processing parameters will be pasted to all the Scenes in the Group.

****Delete:**** Right-click on the Scene group → Delect ''Delete'' → Current group and the Scenes in the group will be deleted (this operation supports Ctrl + Z to undo)

****Drag & Drop:**** Drag and Drop Scene groups to change their order, and Drag and Drop individual Scenes to move them into or out of a group.

****Scene list operations support Undo****

Undo operations for both Scenes and Groups are supported by pressing `Ctrl + Z`

- Scene: Add/Delete/Update
- Group: Group/ Ungroup/ Delete

****Add all the scenes in Group to the Render Queue****

Enter Render Mode → select the group → and click "Add to Render Queue" at the bottom right corner of the window, and the scenes in the group will be added to the queue in order.