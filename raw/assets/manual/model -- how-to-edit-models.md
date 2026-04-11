# How to edit models?

D5 Render primarily supports two methods to move, rotate and scale objects.

### 1. Scene Tools

You can use the "Move & Rotate" Tool to change the coordinates and rotation angle of object such as model or light in the scene by selecting it directly with the mouse in the non-locked state. Use "Scale" to adjust the size of the object.

The default position of the center of the coordinate axis is the center of the bottom of the model.

### 2. Basic Parameter

The "Basic" parameter in the right sidebar also supports adjusting the "Location", "Rotation" and "Size".

## Tools and Parameters

### Move Models

- Drag between any two arrows to move the model in the XY / YZ / ZX plane.
- Click the square in the center of the axis and drag it to move the model freely to any position in the scene.

For multi-selected objects, you can enter values to unify the coordinates. Or hover and drag the mouse over the input box to move the model uniformly to a certain direction.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fsaas.bk-cdn.com%2Ft%2F18217684-957c-4109-9021-5866cc58cc60%2Fu%2Fb2b089df-cb81-4043-b79c-df8b2dc9bba1%2F1675066114049%2F8870a17f-5095-4963-8065-3840e5f1aa0e.gif&width=300&dpr=3&quality=100&sign=9c5b8473&sv=2)

### Rotate Models

You can rotate the model by clicking on the upper semicircle on the coordinate axis.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fsaas.bk-cdn.com%2Ft%2F18217684-957c-4109-9021-5866cc58cc60%2Fu%2Fb2b089df-cb81-4043-b79c-df8b2dc9bba1%2F1675066117833%2F9f93be79-e490-4204-bab8-024117c3d9a2.gif&width=300&dpr=3&quality=100&sign=404f3c32&sv=2)

### Scale Models

> In combination with the locking function of the "Size" parameter, adjustments can be made simultaneously or in one direction only:

- When locked, the model is scaled up and down proportionally.
- When unlocked, the model is scaled in each individual direction.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FuBYYndKrAJhrwotVX5ql%252Fsize.gif%3Falt%3Dmedia%26token%3D3c344d6b-4660-4e31-a227-3b2241d12933&width=300&dpr=3&quality=100&sign=bf0d789e&sv=2)

---

## FAQ

### Q : Why some models have incomplete size parameters or cannot use the scaling tool?

Some models do not support scaling, such as particle models, path models, etc;

Some models only support scaling of flat surfaces, such as surface light models, decal materials, etc.

### Q : Why can't 2D characters rotate?

The 2D character is a plane model material that always faces the currently viewed camera viewport and does not support rotation.