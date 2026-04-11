# Vegetation Path

## Draw Path

Select "Draw Vegetation" -> "Paths" from the navigation bar, and then click on it to select a model from the asset library. You can add up to 6 models to the vegetation path.

Please refer to👇

[Draw Path](https://docs.d5render.com/user-guide/animation-path/draw-path)

## Basic Editing

Paths support basic "Duplicate" and "Focus on" functions.

Click the "Edit" button to enter the path control point editing mode. In this state, you can only add, move and delete control points of the path. After editing, click the right mouse button or click "Done" button to exit the drawing.

The basic parameters include location and rotation, which can also be adjusted with the scene tool. Paths do not support rescaling.

## Parameter Adjustment

Used to adjust the distribution of vegetation models on the path.

### Number of items

The "Number of items" controls the total number of models on the currently selected path. The minimum number of models is 2, distributed at the two endpoints of the path; the maximum number is 100.

### Direction and Random Direction

The "Direction" parameter controls the direction of the model rotation, which is the uniform direction of all models on the path.

The "Random Direction" is based on the existing Direction, and then rotate each model randomly.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkZG1i9uIVX9ilgfI8i%252F-MkZIaehO9KqO9PrhXpf%252F%25E6%25A4%258D%25E7%2589%25A9%25E8%25B7%25AF%25E5%25BE%2584%2520%25E6%2597%258B%25E8%25BD%25AC.gif%3Falt%3Dmedia%26token%3D0a90fe7b-b282-4b00-a520-94c8dfb3ffeb&width=768&dpr=3&quality=100&sign=5186a5fd&sv=2)

### Random Spacing and Random Offset

By default, models are equally spaced along the centerline of the path. Adjust the position with the "Random Spacing" and "Random Offset" parameters to randomize the models within a certain range.

"Random Spacing" means that the model moves a certain distance along the centerline of the path, increasing or decreasing the distance between the two modes directly.

"Random Offset" is when the model moves perpendicular to the centerline of the path, randomly increasing the distance from the centerline and increasing the width of the path.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkZIdP0D3PJ2i75Tx26%252F-MkZJSHskbMX089OVZtp%252F%25E8%25B7%25AF%25E5%25BE%2584%2520%25E5%2581%258F%25E7%25A7%25BB.gif%3Falt%3Dmedia%26token%3D2814fd22-5e9e-4fe0-8cb7-54840ff15070&width=768&dpr=3&quality=100&sign=e3c7f41a&sv=2)

### Size and Rrandom Size

The "Size" parameter controls the uniform size of all models on the path. The default standard size of the model is "1", and the size can be adjusted in multiples of "0.1 to 2".

The "Random Size" allows you to set the size of the model randomly based on the existing size of the model.

### On the Ground

When the model surface is curved and uneven, the path does not fit the model surface completely, and the model on the path will float in mid-air. When you use the "On the Ground" function, the model will be automatically attached to the nearest model surface.