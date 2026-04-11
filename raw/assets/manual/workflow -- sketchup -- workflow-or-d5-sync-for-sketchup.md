# Workflow | D5 Sync for SketchUp

Currently, the D5 renderer supports direct reading of .skp format model files. The D5 Converter - SketchUp can help you seamlessly link SketchUp.

Download Demo Case：<https://forum.d5render.com/t/scene-express-vol-110-sketchup-d5-workflow-tutorial-demo-scene-living-room-by-qu-c-vi-phan/11025>

## Download and Install

### Installation environment and version support

SketchUp 2017 - SketchUp 2023.

### Download exe

[![Logo](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fcdn.prod.website-files.com%2F62cc341ca212fe5f03df86e6%2F6967849201a18d8021a5b371_D5%2520LOGO%2520ROUND%25202.png&width=20&dpr=3&quality=100&sign=c036291d&sv=2)D5 for SketchUp Real-time Rendering Workflowwww.d5render.com](https://www.d5render.com/workflow/sketchup)

After the download is complete, double-click the .exe file and follow the prompts to install D5 Converter-SketchUp.

### Download rbz

[![Logo](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fusa-forum.d5cdn.com%2Foptimized%2F3X%2Fa%2F3%2Fa37590e739387237e65f44599ba633d478e6885d_2_32x32.png&width=20&dpr=3&quality=100&sign=f5767c89&sv=2)Light group changes and different versions for downloading | D5 Converter for 3ds Max and SketchUpD5 RENDER FORUM](https://forum.d5render.com/t/light-group-changes-and-different-versions-for-downloading-d5-converter-for-3ds-max-and-sketchup/15616)

### The difference between version 0.8.5.0001 and 0.8.4.0004

The two versions refer to different ways of grouping lights. For details, please refer to this post: <https://forum.d5render.com/t/light-group-changes-and-different-versions-for-downloading-d5-converter-for-3ds-max-and-sketchup/15616>

## Feature Introduction

### Launch D5 render with one-click in SketchUp

- Import the currently edited new model into the D5 render, and start real-time rendering work.
- Please sync in perspective view for the best viewpoint sync experience.
- When the model file of the ongoing rendering project needs to be modified, you can start a linkage to establish a connection with the original model or replace it with a new model.

### Model/Material/Scene Sync

- After making changes to the current model in SketchUp, use the Sync button to quickly sync the changed model and materials to D5, while preserving other parameters such as materials and scene that have already been adjusted in the D5 render.
- Supports one-click synchronization of the scene list in SketchUp to the D5 render.

### Viewpoint Switch

- Keep the viewpoint consistent in the horizontal direction between SketchUp and D5 renderer.
- Supports one-click to turn on or off viewpoint linkage.

### Light Sync

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F57INbkA9GYMllobxwrpV%252Flight%2520sync.png%3Falt%3Dmedia%26token%3Dbbf535a0-f1a2-48e9-a1d7-bb1cc8d33f3f&width=768&dpr=3&quality=100&sign=9acdf6e7&sv=2)

- Click the "Add Light Source" button, you can select the D5 light source (point light, spotlight, strip light, rect light) in a new window and add it to the scene.
- The position and related parameters of the added light source will be synchronized to the D5 render in real time.

### Uninstall

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FRjwSYmvXxTxlMl5jKap5%252Funstall.png%3Falt%3Dmedia%26token%3Dda1d5386-2a3c-4fdb-ada5-0488da6b186c&width=768&dpr=3&quality=100&sign=86a80182&sv=2)

- Select "Extensions Manager" in the SketchUp menu bar, select "su\_to\_d5render" and choose Uninstall.
- Find the file "su\_to\_d5render.rb" in the directory C:\Users\Administrator\AppData\Roaming\SketchUp\current SketchUp version\SketchUp\Plugins, and delete it.