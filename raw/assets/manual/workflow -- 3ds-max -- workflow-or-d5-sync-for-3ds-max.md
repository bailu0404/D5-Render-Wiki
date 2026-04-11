# Workflow | D5 Sync for 3ds Max

D5 Converter-3Ds MAX helps you to link 3Ds MAX smoothly.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FwAFONwrduLc47aexsgPd%252Fsync%2520plugin.png%3Falt%3Dmedia%26token%3Dcf1d4a5c-5581-471e-a91d-38d67f242e48&width=768&dpr=3&quality=100&sign=826321d6&sv=2)

<https://www.youtube.com/watch?v=xrXakSqLt0Y>

## Installation environment and version support

- 3ds Max 2014-2016, 2018-2026
- VRay 3.6 and above, Corona 6.0~13.0
- D5 Render 2.6 and later versions

## Download and Installation

[![Logo](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fcdn.prod.website-files.com%2F62cc341ca212fe5f03df86e6%2F6967849201a18d8021a5b371_D5%2520LOGO%2520ROUND%25202.png&width=20&dpr=3&quality=100&sign=c036291d&sv=2)3ds Max Rendering with Real-time Raytracingwww.d5render.com](https://www.d5render.com/workflow/3ds-max)

After downloading, unzip the file, double click on the .exe file, and follow the prompts to install the D5-3ds Max converter.

## Feature Introduction

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FX0SktrSlwjYPGIG41JxU%252F3dmax%2520feature.png%3Falt%3Dmedia%26token%3De06420ee-1194-4544-886b-b5342c42ae45&width=768&dpr=3&quality=100&sign=1ba8e05e&sv=2)

### Start Sync

- Launch the D5 render with one click inside 3ds Max and sync the viewport inside 3ds Max to D5.

You need to save the max file before you can perform the "launch sync" operation.

### Data Sync

- After adding, deleting, changing the structure of a model or modifying the name of a material in 3ds Max, click Data sync can quickly synchronise the changed model and materials to the D5 Render, while retaining other parameters such as materials and scenes that have already been adjusted in the D5 Render.

### View Sync

- Keep the viewport of 3ds Max and D5 render consistent from any perspective, achieving real-time sync between the D5 perspective and 3Ds Max.

### Scene Sync

- Supports one-click sync of the Standard/Vray/Arnold cameras in 3ds Max to the scene list of the D5 render.

### Lights Sync

- Click the Lights Sync button to sync the type and position of the current Standard / Corona / Vray / Arnold lights in 3ds Max to the D5 render.

The specific parameters of the lights need to be adjusted in the D5 render.

3ds Max Lights type

3ds Max Lights parameters

D5 Lights

Standard-Target/Free Spotlight

location, attenuation-use-end, light cone-aspect, orientation, light color

Spotlight

Standard-Target/Free Parallel Light

light cone-aspect, light color

Strip light

Standard - Floodlight

colour

Point light

VRay Plane

location, size (light length and width), orientation, temperature/colour

Strip light

VRay Sphere

location, colour

Point light

VRay IES

ies files, rotation

Spotlight

Corona Light

ies file, temperature/colour

Spotlight

Corona Rect

location, size (light length and width), orientation, temperature/colour

Rect light

Corona Disk

location, temperature/colour

Spotlight

Corona Sphere

location, temperature/colour

Point light

Corona Cylinder

location, temperature/colour

Rect light

Corona Sun

location

Strip light

Arnold Light

Point light

Photometric light

Point light

### Export .d5a files

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FZgQo97CT5qjhbzunXI8f%252FExport%2520d5a%2520sync.png%3Falt%3Dmedia%26token%3Db625ab6d-8951-49eb-ae02-2428250ea69c&width=768&dpr=3&quality=100&sign=e8e9055e&sv=2)

- Export 3ds Max models in .d5a format to directly open them in D5 Render.
- Export .d5a files without compressing texture resolution.
- Export the whole project or selected part only.
- The Auto Collapse feature is added and the last setting will be saved (to solve most problems of model dislocation, normal UV and closed line export).
- Select keep group hierarchy and import the exported .d5a file into D5, which will be displayed as a group structure.

### Export .skp files

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FkYR6OuLrC7besooug1Yz%252FExport%2520skp%2520sync.png%3Falt%3Dmedia%26token%3D0e564a9c-1e74-4016-89c4-db6d9fa7bd80&width=768&dpr=3&quality=100&sign=122529ec&sv=2)

- Support model export in .skp format to import into SketchUp and D5 Render
- Resize Bitmap: 512 \* 512, 1024 \* 1024
- In addition, some other features are added: hide all edges, origin to center, merge coplanar faces, and more.

### Setting

- Check the version number, global settings and current sync solution
- “Automatically save scenes after sync” and “Choose Sync Solution” options are provided, and the last setting will be saved.
- Automatically save scenes after sync: when there are materials with the same name in the 3ds max file, after synchronization of first time, the converter will automatically change the material name to a unique one to prevent the material assigned in D5 from getting overwritten next time.
- Sync Method

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FZW8ARD4hgZn6ec2uylI6%252Fsync%2520method.png%3Falt%3Dmedia%26token%3Daa18b26c-2b7b-44e2-a2d2-60176e32b307&width=768&dpr=3&quality=100&sign=83773c01&sv=2)

New method (recommended): It is for all new projects that did not use previous versions of 3ds Max plugin (2.98 and older), which can synchronize the model coordinates and align them automatically.

Compatible method: It is only for projects that once have been linked to D5 scene files through old versions of 3ds Max plugin (2.98 and older).

### Quick ProOptimize

Features can be found in the menu bar

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fuf8BVuzuE6EilzwKwfWT%252Fimage.png%3Falt%3Dmedia%26token%3Dc58af940-0c28-46bb-bfe6-c57ed371bd3c&width=768&dpr=3&quality=100&sign=9f24dccd&sv=2)

### Uninstall

Method 1: Click "window System Start Menu - Plugin Uninstaller - Uninstall D5 Converter for 3ds Max".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FAgoPuZAPjO3PcCFDZhYZ%252Funstall.png%3Falt%3Dmedia%26token%3De13aacfc-dfa5-45e6-9a24-ab631b50b5a7&width=768&dpr=3&quality=100&sign=5eece9cc&sv=2)

Method 2: Uninstall in "Computer Control Panel - Programs - Uninstall a programme".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8lS9EAUGpi9D2iWBumTI%252Funstall-2.jpg%3Falt%3Dmedia%26token%3D8cd5c3b3-dbcd-4724-a7b5-24f3d1e9b39a&width=768&dpr=3&quality=100&sign=ebf3ffd7&sv=2)