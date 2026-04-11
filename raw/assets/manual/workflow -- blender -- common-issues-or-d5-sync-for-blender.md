# Common issues | D5 Sync for Blender

## 1. Why does the blender preferences not show D5 related content after installing the plugin?

Note: Please refer to Workflow | D5 Sync for Blender first to make sure the version of blender you are currently using is the version supported by the D5 plugin.

The current blender plugin exists in two folders:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F85oYWbAsz9tNVYTdWqgP%252Fimage.png%3Falt%3Dmedia%26token%3D917a5c52-5af1-4be9-a14d-89744949e7fd&width=768&dpr=3&quality=100&sign=2a55b723&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FEaXKvlPvsNajZMgyhzRH%252Fimage.png%3Falt%3Dmedia%26token%3D340876ad-f33b-41fb-9c05-31699551097c&width=768&dpr=3&quality=100&sign=5da95f45&sv=2)

Some users can't recognise the plugin after installation because they have changed the first path of the default installation of the blender plugin.

In this case, after installing the plugin, you need to copy the entire d5\_export file from the C:\Users\Administrator\AppData\Roaming\Blender Foundation\Blender\3.5(Blender version)\scripts\addons directory to the path (the actual path modified by the user) that is recognised by Blender. directory, and then open Blender to display it in the preference settings.