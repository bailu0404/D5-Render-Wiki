# How to render a video clip?

The D5 2.6 version has added a camera path editing feature. Clip, shot and view are the three core elements that make up a great animation. Each clip can contain multiple shots, and all the shots within the same clip are compiled into a single video file, saving time on post-production editing.

## 1. Create shots:

There two ways to create shots in a clip:

> Tips:
>
> - The order of shot and view can be switched by dragging and dropping.
> - The environment and post parameters in shot and view can be duplicated and pasted by right click. Right-click on the shot to "update all parameters", and batch update the environment and post parameters of all views in the shot.

## 2. Parameter adjustment

> ℹ️ > Note: The default aspect ratio for new clips is 16:9.

- After selecting clip/shot/view, select the "Edit Path" button from the right sidebar "Parameters" to enter this mode. The mirror track is visible in the 3D scene. The path contains 3 objects that can be operated and specific operations, they are:

-Camera Carrier, click “Edit Path” and the three axes will appear, for the overall movement and rotation of the camera path.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQ1B04T75XTqOvhuhEGbl%252Fb74c39fee02a7c5ec9d7320087ec22409118a040_2_690x373.png%3Falt%3Dmedia%26token%3D872c75e3-8275-4b35-b148-ee4d87926e18&width=768&dpr=3&quality=100&sign=a4d4a897&sv=2)

Camera carrier

-View Carrier, which corresponds to the view in the current shot. Select to adjust through gizmo.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FxhwEZMzM9swagi6gkFtX%252F5b6ab01acf65f10b36e880ed7821fca59fb8019f.png%3Falt%3Dmedia%26token%3Dfd1cbbb0-e660-4fd6-9b8a-c8d03480f7c0&width=768&dpr=3&quality=100&sign=7d45c234&sv=2)

View carrier

-Spline Tool, corresponding to the two control points for bending the lines. Select to adjust the path through gizmo.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLoz4lpkeaRMKghg0rQGQ%252F8f5d46359e7f74c4129c0722a2ecba529c01714c.png%3Falt%3Dmedia%26token%3D179e9039-8869-43d4-93ae-cdaef6cd20e6&width=768&dpr=3&quality=100&sign=cd1c4e9&sv=2)

Spline Tool

Enter Video Mode - Shot - Edit Path - ''Camera Target'' feature in the right sidebar.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7mQpwnrIBAELOMNWyYA6%252Fimage.png%3Falt%3Dmedia%26token%3Da23260bb-cb6e-4fbc-8060-12a3ebb4d2ed&width=768&dpr=3&quality=100&sign=78a3c591&sv=2)

With Camera Target enabled, users can specify a target object by clicking on the "Focus" button. Once a target is selected, the camera will automatically lock onto and focus on that object as it moves.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F5mxIz0QEHNCZCU0N352X%252Fimage.png%3Falt%3Dmedia%26token%3Df8ec03db-5305-447c-ae2e-a9bd92297f8a&width=768&dpr=3&quality=100&sign=74050497&sv=2)

Refresh Shot

This feature is ideal for complex camera movements, including surround, semi-surround, and curved lens paths. It eliminates the need for manual lens orientation adjustments, significantly simplifying the camera control process.

- When you select shot, the "Auto View Interval" option in the right sidebar parameter is not ticked by default. After ticking this option, if you change a certain time in the shot, the time interval of each view in the shot will be recalculated automatically, so that the speed is always the same between different views.

- ****Movement controls the way the path is segmented between two points in the track.**** It supports adjusting the movement of view move and rotate separately, which affects the movement rate of the camera path, e.g.: fast then slow.
- ****The movement support 5 basic option: Linear, Ease in, Ease out, Ease in out, Speed in out.**** Support for customising settings via 2D view or by entering values. The movement parameters are applied from the first view to the next view. Adjustment will batch change view settings when clip, shot is selected.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FimLFkuCavGpksych1FyL%252Fhelp%2520center%25201.gif%3Falt%3Dmedia%26token%3D7d757c7f-3594-43e1-9f61-4dc1c370e206&width=768&dpr=3&quality=100&sign=fa707b20&sv=2)

## 3. Add keyframe

Select an object in the object list and click the Add Keyframe button (or use the shortcut K) to quickly create a keyframe.

- ****Visibility****: In the video mode, users can select models or layers and combine the "Visibility" option from the right sidebar panel to create animations that display/hide keyframes.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FCpocYtzr4lR7e8UffJEG%252Fhelp-center-2.gif%3Falt%3Dmedia%26token%3D96c51114-f1a3-4921-8d2a-c65cf0093c0a&width=768&dpr=3&quality=100&sign=e4834b84&sv=2)

Model and layer show/hide keyframes

## 4. Switch clip view

Click the button in the upper right corner of the video editor to switch between "shot view" and "timeline view". Hold down Alt+mouse wheel to zoom in and out. Playback control adds view/keyframe switching, forward/backward time progress control, start/end position jumping. These can be used separately with shortcut keys.

## 5. Use Template

### ****Camera Movement****

The [Camera Movement] section provides some basic templates (e.g., pan cameras, etc.) for daily use.

> The adjustment of “Movement” parameters is ****not supported for shots created using “Template-Camera Movement”.****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FNM07DSPf9qLxeDgvGuuc%252Fimage.png%3Falt%3Dmedia%26token%3D04808edd-4fd2-4561-83aa-e6ae591e9ab1&width=768&dpr=3&quality=100&sign=d2f8b2bf&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FrVRnuiX3Y2CYXeF4BCJt%252FDingtalk_20241120120656.jpg%3Falt%3Dmedia%26token%3Dad5723df-e5c3-40aa-985c-b0487fbd121e&width=768&dpr=3&quality=100&sign=91eb8f73&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJNtK4WA0kulfp3bOcrXW%252FDingtalk_20241120120821.jpg%3Falt%3Dmedia%26token%3D2e0de607-0ef3-4138-b8ad-918acd7050eb&width=768&dpr=3&quality=100&sign=ffa065d2&sv=2)

### ****Animation Template****

[Phasing Animation Template] in the Video mode allows for a simple and rapid visualization of the step-by-step building process, avoiding the need for complex keyframe settings. This tool can be applied to create animations for building structure growth, architectural analysis, component installation demonstration, product animation, and landscape vegetation growth.

> **Prior to using this feature, you need to import the models for phasing animation into D5.**
>
> - **It is recommended to use the group export feature of D5 Sync plugins (e.g., SketchUp, 3ds Max, Rhino, Revit) to export .d5a files with their group structure, facilitating the creation of phasing animation.**

#### 1. Check and select required animation templates in the Video mode

In the Video mode, all new animation templates can be accessed in the right sidebar under 'Template', including Drop/Rise, Ascend/Descend, etc. You can preview the effect throught the dynamic thumbnail.

Click on the required animation template to access the object selection state.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FN7npD6S3WBnZyjU7qOFR%252F6.jpg%3Falt%3Dmedia%26token%3D4e850c94-2369-45b0-8fd1-7a16fa7d2d0a&width=768&dpr=3&quality=100&sign=2f3fc1cc&sv=2)

#### 2. Select the required models for phase animation

Click on any template to enter the Edit Objects mode where you can add models you want to create a phasing animation for. Select models by clicking on the corresponding objects from the viewport or the object list. You can hold down the Shift key for multi-selection. You can also put all the desired objects into one layer and simply select the layer to add all the objects within it. (The added models will appear in the right sidebar. )

Their order follows the sequence in which they were clicked and this sequence will be the default for the phasing animation.

- You can adjust the order of the list by dragging the models upward/downward and delete the models from the list when you don't want them any more.

> TIPS:
>
> a) Supports multi-selection (shortcut key Shift)
>
> b) When there are many objects to be selected, you can ****put all the objects to be selected in a separate layer, and just click on the layer to select them all during selection.****
>
> c) Please note that D5 ****adds single objects by default.**** Therefore, even when you select a group, D5 will individually add all the objects within the group.
>
> To add a group as a whole, you can press the shortcut key 'G' to switch to ****'adding groups'**** selection mode. In this mode, the selected group will appear as a single unit in the phasing animation.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FwELAuSXqlzGzifbSZtff%252F7.png%3Falt%3Dmedia%26token%3D52a15d3e-52b6-4170-86e6-d30d06345df0&width=768&dpr=3&quality=100&sign=ae312e9e&sv=2)

#### 3. Create Phase Animation

Click ‘Done’ to exit the 'Edit Objects' mode when you complete model selection. The corresponding control panel for the animation template will appear in the right sidebar. A new phasing animation track will be added into the timeline right above the shot track.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FHHDezpvOrSRTwSAYOQ1q%252F8.gif%3Falt%3Dmedia%26token%3Daab7d3a3-b5b6-44cb-93b1-3d087f19ead3&width=768&dpr=3&quality=100&sign=7effa11b&sv=2)

#### 4. Confirm the phase animation effect and adjust its parameters in the right sidebar.

After selecting objects and clicking the ‘Done’ button above, the corresponding template can be seen in the ‘Bottom Sidebar - Animation Edit Bar’. Click "Play" to preview the current phasing animation. Click the template to adjust corresponding parameters in the right sidebar:

- Animation Controller: The independent animation controller at the top supports various motion settings such as Linear and Ease In. Click "Play" to preview the current phasing animation. During playback, the viewing angle can be freely adjusted to observe the animation from different perspectives.
- Property:

  - ****Objects: Set the order of animating objects.****

  a) Sort by the object list: Animate objects in the order according to the order of the object list.

  b) Sort by the world coordinate: Animate objects in the order according to their coordinates on the three axes to achieve natural phasing animation.

  > E.g.
  >
  > If model A has a positive X-value while model B has a negative X-value, model B will move first when ‘Sort by world coordinate’ is selected.
  >
  > If both AB models have the same X-value, the model with smaller Y-value will move first when ‘Sort by world coordinate’ is selected.

  - ****Time interval: Control the playback interval between individual object animations within the overall animation.****

  a) Simultaneous: All the objects appear simultaneously.

  b) Cascading: Objects appear in an overlapping manner, creating a flowing visual sequence.

  c) Sequential: Objects appear one by one.

  - ****Distance: Control the distance by which each object moves during the animation.****

  （supports only for 'Drop/Rise', 'Ascend/Descend', 'Fly in/Fly out', and ‘Explode/Implode’.）

  - ****Target direction: Control the direction in which objects fly in/out.****

  (supports only for 'Fly in/Fly out')

  - ****Visibility: Control the visibility of objects before and after the animation.****
- Effect: Overlay another animation effect (Not all templates are available).

  - ****Rotate****: Achieve the effect in which objects rotate while moving/scaling.
  - ****Bounce****: Achieve the effect in which objects bounce back after falling to the ground.
  - ****Scale bounce****: Achieve the effect in which objects scale up and down in size quickly.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FK3PHQ8ykWOldT1xSUhdF%252F9.png%3Falt%3Dmedia%26token%3D07a9bab3-c0d5-42f3-a487-1a97d0a064fb&width=768&dpr=3&quality=100&sign=deeb604d&sv=2)

Animation/Property/Effect overlay

#### 5. Adjust parameters in the ‘Bottom Sidebar - Animation Edit Bar’

‘Video Mode - Bottom Sidebar - Animation Edit Bar, is used to host, edit animation templates.

- Supports free dragging of the animation bar between rows, along with auto snapping.
- Supports adjustments to the animation duration by dragging both sides of the animation bar or by entering values.
- The name of the animation bar defaults to the corresponding animation template name. Double-click on the animation bar to customize the name.
- Right-click on the animation bar to access options including "cut (modify the duration)", "duplicate", "copy", "paste", and "delete".
- Free Camera Playback: By default, you can only preview the animations within a shot if one exists. Enable ****"Free Camera Playback"**** to preview all animations, even those exceeding the shots.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FITxILweTiBkPawegW0uW%252F10.png%3Falt%3Dmedia%26token%3D42a8ca25-466a-4bf7-922f-15bea6e8dd33&width=768&dpr=3&quality=100&sign=612b7c73&sv=2)

## 6. Render video

---

## FAQs

### 1. How to import video clips into the render queue with one click?

There are two ways to achieve this:

### 2. How to creat shots in a clip?

There are two ways to achieve this:

### 3. What is the maximum video resolution supported for output?

Video output resolution depends on your account type, with different account identities having different maximum resolution limits. ****Individual identity**** accounts support video output at resolutions ****up to 4K****; ****Team identity**** accounts support video output at resolutions ****up to 8K****.