# How to align models imported separately?

Similar question:

- How to align the axes of a model?

- How to use the align function?

- How to align the coordinates of different models?

## Overview

When the model is large and has lots of faces, using the D5 converter to export d5a may take up a lot of resources, and the process may be less efficient or even fail. You can first split the model according to the scene, and then export it separately. For example, split the building, plot, and environment, and then import them into D5 for alignment.

Similarly, modeling formats that support direct import can also be imported in chunks for alignment.

## Operation

#### Align

If the models are from the same model file, you can multi-select the models and select the "Align Coordinates" in the right sidebar. Then the selected models will be grouped into alignment according to the original modeling axes, keeping the relative position of the coordinates in the modeling software unchanged.

The rule of alignment is that the model selected later will move to the first selected model. That is, the position of the first selected model is fixed and the coordinates of other models will move.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6SsEtwk6esf0BI2EVbcD%252F%25E5%25AF%25B9%25E9%25BD%2590.gif%3Falt%3Dmedia%26token%3Dbea843a7-fd2b-4867-b7ed-78e848b35f5a&width=768&dpr=3&quality=100&sign=b4df8ee5&sv=2)

#### Sync Coordinates

If the models are from different model files or even different modeling softwares, you can use the "Sync Coordinates" feature to restore the model directly to the absolute modeling coordinates. This function is in the resource list menu on the left side.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FIHDlnVOjAhHKs63DyB9w%252Fsync%2520coordinates.jpeg%3Falt%3Dmedia%26token%3Dc2b25204-4cbc-4c60-a5c3-cea49aedec11&width=768&dpr=3&quality=100&sign=88c7fc81&sv=2)

When you click on "Sync Coordinates", the view will move to the model's position at the same time.