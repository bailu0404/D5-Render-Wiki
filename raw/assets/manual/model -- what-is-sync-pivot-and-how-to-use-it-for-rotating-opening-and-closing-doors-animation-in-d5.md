# What is "Sync Pivot" and how to use it for rotating/opening and closing doors animation in D5?

> Similar question:
>
> - How to modify the axis position/pivoting point of a model?

## Overview

In D5 render, the axis of the model will be placed at the bottom center of the model by default.

You can't modify the axis position directly, but you can combine the ****"Sync Pivot"**** and keyframe function to create the door opening/closing animation.

Please refer to the following method:

## FAQ

### What is the difference between Sync Pivot and Sync Coordinates?

- ****Sync Pivot**** is to synchronize axes, the axes' position will change, not the model.
- ****Sync Coordinates**** is to synchronize model position, the coordinate axis will remain at the bottom center of the model.