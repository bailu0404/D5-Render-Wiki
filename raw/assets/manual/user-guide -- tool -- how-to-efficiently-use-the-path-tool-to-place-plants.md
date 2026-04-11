# How to efficiently use the path tool to place plants?

## Custom paths

Supports adding models to the Path from:

- Models from the online Asset Library: including ''All Model'', ''Recent'', and ''Favorite''.
- Models from the Local library.
- Models from the Team library.

****Supports saving path combinations:**** Users can save the whole path + model combination to the Local library or Team library, and enable as the preset in Studio to improve reuse efficiency.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FmoBosHCf7386nl11sK6A%252Fimage.png%3Falt%3Dmedia%26token%3D5d845f35-2ce5-42b6-a7fd-20dc1b6aa96c&width=768&dpr=3&quality=100&sign=169030bd&sv=2)

****Types which are unsupported:****

Procedurally-generated Vine, Decal, Scattered Object, HDRI, Terrain (including height and material assets), City (OSM), GIS sub-level content, Section Plane& Cube, Camera, Material, Light.

> ****Note:**** ''Top Navigation Bar'' is the only portal for creating paths. The Path tool icon that was located in the bottom left corner of '' Asset Library - Online - Models'' has been hidden. To restore it, please go to Menu Bar > Preference > Shortcuts > Compatibility , and enable ''Path tool available in Asset Library''.

## Edit path

Select the "Tools" -> "Paths" function from the navigation bar, click on it and select a model from the library.

- In [Linear] mode, users can adjust the smoothness of polyline corners when drawing control points.
- In [Curve] mode, users can adjust the handle length of polyline corners when drawing control points. As in previous versions, Bézier curves are utilized.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8Mms4UEqMNWfphJmjj0p%252Fimage.png%3Falt%3Dmedia%26token%3D7b28b0b6-8d73-4850-ac16-5274b2ed68f6&width=300&dpr=3&quality=100&sign=7099de3d&sv=2)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQKVUimBvVyDAZfgRHXxu%252Fimage.png%3Falt%3Dmedia%26token%3Dc0a9f948-7a1a-478c-81ee-147beab9818d&width=300&dpr=3&quality=100&sign=c32f3ad0&sv=2)

## Basic edit

- In this mode, you can only add, move and delete the control points of the path.
- After editing, right click on the mouse or click "Finish" to exit the editing.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FpgdkalWMc8lMXqpSg7fQ%252Fbasic.jpg%3Falt%3Dmedia%26token%3De59f7e41-4033-43e3-9254-bf8b88927703&width=768&dpr=3&quality=100&sign=a402de00&sv=2)

## Parameter adjustment

Used to adjust the distribution of plant models on the path.

### Model

- Once a model is selected and the drawing is complete, the models along the path appear as a list in the right-hand sidebar. Users can add, delete, or replace items, allowing design changes at any stage.
- Scale, rotation, and zoom parameters for these objects can be adjusted independently, providing precise control over each element in the path.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fo6XxeBH2dAjaOyjMiOFu%252Fimage.png%3Falt%3Dmedia%26token%3D9cf41d13-d741-4516-983e-406f9d9fa9fd&width=768&dpr=3&quality=100&sign=efa32c66&sv=2)

Adjust models independently

### Alignment

Support selecting [Auto] or [Fixed] mode to choose different plant path arrangement.

The minimum number is 2, distributed at both ends of the path.

The maximum number is 100. Depending on the number, the models are distributed in equal order along the path.

In this case, a corresponding number of models will be generated within the path length, based on a fixed spacing between the two plant models. The maximum value of the spacing will not exceed the path length in metres (m).

### Direction and Random direction

****The " Direction " parameter**** controls the direction of the model's planar rotation, which is a uniform direction for all models on the path.

****The "Random Direction"**** is based on the existing rotational position, and then the rotational direction of each model is randomly varied.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJGzvGiVWLYCIKxKuwQxC%252Fb55911b7-2d23-4ba2-9d49-482a76b49f89.gif%3Falt%3Dmedia%26token%3D05ffc0d2-cae9-4d78-8908-a4a6158e3f07&width=768&dpr=3&quality=100&sign=d7c3fd04&sv=2)

### Random spacing and Random Offsets

"Random Offset" is where the models move perpendicular to the centreline of the path, randomly increasing the distance from the centreline and increasing the width of the path at the same time.

The offset distance is the actual offset value, known as the "random maximum offset", in metres (m), and the maximum value must not exceed the path length.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FlQk00CrSkT9YC0mk0wKp%252F2fb407ba-fe80-4cf6-ba70-72944177804a.png%3Falt%3Dmedia%26token%3D453ef96b-347b-4d05-b235-7dfa3fe31b1b&width=768&dpr=3&quality=100&sign=244e1bb3&sv=2)

### Size and random size

The "Size" parameter controls the uniform size of all models on the path. The default standard size of the model is "1" and can be adjusted by a factor of "0.1 to 2".

"Random Size" sets the size of the models randomly based on the existing size of the models.

### Random Seed

- The random seed controls the randomisation effect applied to objects on the path.
- When any of the random spacing, random rotation, or random scaling parameters are set to a value other than zero, adjusting the random seed generates different object distribution patterns, resulting in more natural and varied path effects.

### Drop

When the surface of a model is curved and uneven, the path does not fit the surface of the model perfectly, and the model on the path floats in mid-air. After using the "Drop" feature, the model will be automatically attached to the surface of the model closest to it.

## FAQs

This is the current effect in expectation.

Due to the use of the path tool, the scene is regenerated every time you open it, and it is not currently supported to save relevant parameters ( to make subsequent openings of the scene show the exact same effect as in the previous archive).