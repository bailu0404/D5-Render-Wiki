# How to import model files into D5 Render?

## Overview

D5 Render primarily supports two methods for importing external model data files:

In addition, D5 Assets Library contains various high-quality models such as vegetation, characters, indoor furniture, and commercial backgrounds that can be directly used in projects.

****Direct import****

****D5 Converter****

****SketchUp（.skp）****

✅

✅

****Autodesk FBX （.fbx）****

✅

****D5 model（.d5a）****

✅

****Rhino（.3dm）****

✅

✅

****Alembic animated file（.abc）****

✅

****Wavefront OBJ (.obj)****

✅

****Collada (.dae)****

✅

****3D Studio (.3ds)****

✅

****Aseprite/3ds Max ASE (.ase)****

✅

****Assimp Binary (.assbin)****

✅

****AutoCAD DXF (.dxf)****

✅

****Stereolithography (.stl)****

✅

****gITF (.gltf/.glb)****

✅

****MikuMikuDance (.pmx)****

✅

****Revit****

✅

****3ds Max****

✅

****Cinema 4D****

✅

****Blender****

✅

****Archicad****

✅

****Vectorworks****

✅

## Import models

### 1. Open files from D5 Launcher to start a new scene

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fj9TUwLqYlPaZGw2lBqaL%252Fimage.png%3Falt%3Dmedia%26token%3Dbadc3625-3be2-4121-b6ab-d272a7f803f2&width=300&dpr=3&quality=100&sign=f26310a7&sv=2)

From D5 Launcher, you can select "Open" to select a model file directly to create a D5 scene file. If the model contains cameras or scene data, they will be imported into D5's scene list as well.

Models imported in this way default to coordinates of 0,0,0 and are locked by default after import.

### 2. Use the Import button when editing scenes

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FGBerUMCEISwD2pdp4xAi%252Fimage.png%3Falt%3Dmedia%26token%3Dace0c3c7-6870-4323-acbf-0ee169e4f283&width=768&dpr=3&quality=100&sign=3746b9df&sv=2)

When editing scene files, we can also use the Import button at the top left corner then select files needed to be imported.

Through this method, the imported models will be displayed in the Imported list on left sidebar. Click on the file name, load it, and the model will be placed in the scene. The model is unlocked by default.

This method supports importing multiple model files at once.

### 3. Add models from D5 Assets Library

Go to D5 Assets Library (online) > Model to select models for downloading. After the download is complete (only necessary for the first time use), you can place the model in the scene, and the model will be unlocked by default.

### 4. Use D5 Converters to sync models or export .d5a files

After installing D5 Converter add-on for modeling software, we can start live sync to send models to D5 or export the model files in .d5a format.

Currently supported workflow for D5 Converters :

## FAQ

### Q: Why imported .fbx models do not animate, move, or have materials?

### Q: Why imported .abc models do not have materials?

Currently, import of .abc files with textures is not supported in D5. You will need to separate the textures in modeling software and then re-apply them in D5. We will consider adding support for this in future iterations.

### Q: Why I can not select materials of imported models by clicking?

Models opened from the welcome page are in a locked state by default in the scene, and you can directly click to select the material.

Models imported when editing scenes are unlocked by default, and clicking on them will select the models instead of materials. We can use the material selection tool at the top left corner (material picker) to select the materials. Alternatively, we can lock the model and then click to select the material.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FvtKGiHmuvHOZC5zu0Xov%252Fimage.png%3Falt%3Dmedia%26token%3Dbbfc873f-8d2c-476e-a014-f2f78cffc68c&width=768&dpr=3&quality=100&sign=3585d444&sv=2)