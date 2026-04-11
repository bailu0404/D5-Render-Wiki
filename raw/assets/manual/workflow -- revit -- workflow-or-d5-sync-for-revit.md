# Workflow | D5 Sync for Revit

Sync Revit with D5

[**Download the demo scene for free**](https://forum.d5render.com/t/scene-express-vol-141-revit-d5-workflow-tutorial-demo-scene/12005)

## Download & Installation

Double click on the .exe file after the download, and follow the notifications to install [D5 Sync for Revit](https://d5converter.d5cdn.com/installer/revit/latest/D5_Sync_Revit_usa_latest.exe)

Learn more about [D5 Render for Revit](https://www.d5render.com/post/d5-render-for-revit-best-real-time-3d-rendering-workflow-for-bim-professionals)

Download [D5 Render](https://www.d5render.com/download)

#### Supported versions

Revit 2018.3 - Revit 2026

## Functional Description

#### One-click to Launch D5 Render in Revit

- Import the new models into D5 Render to start real-time rendering.
- When a model file needs to be modified during rendering, start Sync to create a connection with the original model or replace it with the new model.
- Import Revit models into D5 Render by Sync feature without exporting d5a.

#### Model/Material/Scene/Light Sync

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fz4iLTQ6kWeSoIg3vTbPV%252Fimage.png%3Falt%3Dmedia%26token%3Ddeb14f8f-54fb-4273-8811-c072c334010f&width=768&dpr=3&quality=100&sign=7f21326b&sv=2)

Model/Material/Scene/Light Sync

- After being modified in Revit, use the Sync button to quickly synchronize the modified model and materials to D5 Render, and keep the materials, scenes and other parameters that have already been adjusted in D5 Render.
- Support one-click synchronization of Revit scenes to the D5 Render scene list.
- Support to exclude the categories that don't need to be synchronized by categories. You can also think of separating categories such as Furniture, Furniture System, and Generic Models through the settings menu, that will make it also easier for you to control the visibility of those categories when you are rendering exteriors or interiors.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F9ijDf5ntcdDAi11xT6YB%252Fimage.png%3Falt%3Dmedia%26token%3D746f216f-a42a-4073-a0e9-6533228e2e2e&width=768&dpr=3&quality=100&sign=ff52946a&sv=2)

Categories setting

- Support Sync family lights to D5 light.

****Sync Linked Model****

- Synchronizing linked models in Revit to D5.
- In huge projects with many links, each link is automatically separated in D5, making it easy to control what’s visible or what’s not, it also gives flexibility to move around the model while turning off some unneeded links.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FdIdtlIVtUS5XAN0ij36J%252Fimage.png%3Falt%3Dmedia%26token%3D9ac9784c-464e-4250-aa04-4b255cb4de3b&width=768&dpr=3&quality=100&sign=2c14375b&sv=2)

****Sync Linked Model****

#### ****View Sync****

- Keep Revit horizontally aligned with the view of the D5.
- Support one click to turn view sync on or off.

#### ****Use Survey Point****

- The exported model will use Survey Point as Origin (0,0,0) instead of Project Base Point

> Tip: Useful for aligning multiple Revit models with same shared coordinates

#### ****Use Consistent Colors****

The material is exported with Revit mapping before it is turned on, and it is colored after it is turned on.

- Use materials’ RGB graphics colors instead of asset texture and/or color.

> Tip: Useful to start creating your scenes from colored materials only.

#### ****Group Materials by Assets****

- Use asset names as a way to separate elements in D5, instead of material names.

> Tip: Useful for handling professionally organized materials in Revit projects, or with Dynamo scripts that overrides material assets

#### ****Export Smoothness****

- Change model smoothness in D5.

> Tip: Default value is good enough

#### ****Select Categories to Be Separated****

- Synchronized by detached categories, it helps to directly control the visibility of Revit categories inside D5 and control whether these categories are hidden separately in D5.

> Tip: Useful for more control over Revit categories visibility inside D5 directly.

#### ****Export .d5a file****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FgPrf1OQXACl7PeSqEZdf%252Fimage.png%3Falt%3Dmedia%26token%3D398dae65-5b62-4224-9503-a8aa6db854b4&width=768&dpr=3&quality=100&sign=308d3790&sv=2)

Export

- D5 cannot read .rvt files directly, you can use D5 Converter-Revit to convert ****.****d5a files, and then the files can be imported directly into D5.
- Support export of family lights, automatically synchronized to D5 light sources.

#### Group export

- Export the selected instance
- Export the selected family type
- Export the selected category