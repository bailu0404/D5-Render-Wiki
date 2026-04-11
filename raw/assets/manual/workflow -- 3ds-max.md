# 3ds Max

## Download and Installation

Supported Versions: 3ds Max 2014 - 3ds Max 2026 versions (2020 and above versions are highly recommended)

V-Ray 3.6 for 3ds Max or higher must be installed.

You can download the latest version on the official website, or download from the Welcome Page > Workflow.

After the download is complete double-click the .exe file and follow the steps to install D5 Converter - 3ds Max

## Start D5 Render

Launch the D5 renderer with a single click of ![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkYOKi_31UhwPIBIJLH%252F-MkYRSrPIkTgciLY51cP%252Fimage%2520%281%29.png%3Falt%3Dmedia%26token%3D52b5d3ce-53f8-47be-8942-e5e505c602cd&width=40&dpr=3&quality=100&sign=5159ee8d&sv=2) button and establish a connection with the current model in 3ds Max.

Use![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkYOKi_31UhwPIBIJLH%252F-MkYRwsw3sj31PMpBolk%252Fimage%2520%282%29.png%3Falt%3Dmedia%26token%3D66d84fa5-ce72-4184-95ff-9b381918638e&width=40&dpr=3&quality=100&sign=a40c9fe&sv=2) button to turn off sync and disconnect D5 Render from the current model.

- ****OK:**** Create a new empty .drs scene and import the current .max file to establish a connection with D5 Render.
- ****Select file:**** associate the current .max file in 3ds Max with the model file in the existing .drs scene.

When a model file already exists in D5 Render, the first time you synchronize it, you need to connect the synchronized model to an existing model in the resource list or create a new model.

## Sync

Use ![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkYOKi_31UhwPIBIJLH%252F-MkYT1emzDsDMVcxxVaV%252Fimage%2520%283%29.png%3Falt%3Dmedia%26token%3D320a36ce-28a1-44ac-a577-0ca7ababe0b8&width=40&dpr=3&quality=100&sign=7798961c&sv=2) button to Sync. Laod model files faster by syncing the current model and corresponding materials with incremental updates. Suitable for changing materials and models with the synchronization function when adjusting details.

### Viewport Sync

Use ![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkYOKi_31UhwPIBIJLH%252F-MkYTsdr8HTi0icyuKQ7%252Fimage%2520%284%29.png%3Falt%3Dmedia%26token%3D8a1b8249-55a5-438a-8f56-f2c0b7815f98&width=40&dpr=3&quality=100&sign=dbf22f01&sv=2) to turn on viewport sync to synchronize the current viewport of 3ds Max with the view of D5 Render

Use ![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkYOKi_31UhwPIBIJLH%252F-MkYV9uzrzwHIK9X90DO%252Fimage%2520%285%29.png%3Falt%3Dmedia%26token%3De3b18762-f4d2-4131-86f2-46c52b4d3788&width=40&dpr=3&quality=100&sign=667fab63&sv=2) to turn off viewport sync and disconnect viewpoint sync between 3ds Max and D5 Render.

### Camera Sync

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkYVC4jCzSnE6-LITmo%252F-MkYVQUG_mUxWmcIjnk2%252Fimage%2520%286%29.png%3Falt%3Dmedia%26token%3D69a2f8d2-8cb7-4964-87a5-0e69e89c9ede&width=40&dpr=3&quality=100&sign=535a668a&sv=2) One-click synchronization of 3ds Max standard camera and V-Ray camera to D5 Render scene list.

### Light Sync

Click the Sync Light ![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkYVVAH-TJcBc4yxBT2%252F-MkYVomZfEy7Y3svtOAu%252Fimage%2520%287%29.png%3Falt%3Dmedia%26token%3D2ef12e3a-8dfb-4cc1-9a21-d2eca4c04278&width=40&dpr=3&quality=100&sign=ac86121c&sv=2) button to sync the light type (point, spot, strip, area), light position, and area/strip size parameters of the current V-Ray or Corona lights in 3ds Max to D5 Render.

****D5 Lights****

****V-Ray Lights****

****Corona Lights****

Point Light

V-Ray Sphere light

Sphere

Spotlight

V-Ray IES

Disk

Rectangular Light

V-Ray Plane light

Rectangle

## Exporting d5a/skp files

- D5 Render can not directly load the .max file. You can use the D5 converter - 3ds Max to convert max file into .d5a file which can be directly imported into D5 Render.
- Support exporting model files in .skp format for importing into SketchUp and D5 Render.
- Support fast optimization of surface

## Mapping resolution settings

Support setting mapping resolution up to 4K when syncing and exporting d5a format files.