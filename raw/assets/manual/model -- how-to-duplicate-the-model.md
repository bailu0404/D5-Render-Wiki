# How to duplicate the model?

## Function overview

D5 Render provides multiple ways to duplicate the scene resources：

> - Shortcut keys support custom modification.
>
> Please refer to: [How to view and change the default shortcuts?](https://docs.d5render.com/user-guide/preference/how-to-view-and-change-the-default-shortcuts)
>
> - Please note: the duplicate operation supports not only models, but also path tools and other assets.

Function

Shortcut key \*

Usage

****Associative duplicate****

****Ctrl + D****

After duplicating the model, the material of the same part is associated with each other. Adjust the material on one model, and the other model will follow the changes.

****Independent duplicate****

****Alt + D****

The duplicated models are independent of each other, and the materials are not associated. When adjusting the material, the models do not affect each other.

****Drag associative duplicate****

****Shift + Drag the axis****

Copy along an axis in a certain direction. After duplicating the model, the materials are associated with each other.

## Operation

### Associative duplicate

Use the shortcut key "Ctrl + D" to duplicate, and the materials are associated with each other by default. Arbitrarily adjust the material on one model, and the other model will follow the changes. Click the "Duplicate" function in the menu or the right sidebar.

### Independent duplicate

Use the shortcut key "Alt + D" to duplicate the model to avoid material association.

### Drag associative duplicate

Press the "Shift" first, and click the axis in any direction to duplicate the model along the specified direction.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FroAcXN3sPeP7Ho70xmNi%252F%25E5%25A4%258D%25E5%2588%25B6-2.gif%3Falt%3Dmedia%26token%3D401006c0-653b-4d66-9211-ae4dff308c74&width=768&dpr=3&quality=100&sign=83cfddb7&sv=2)

---

## FAQ

### Q: How to cancel the associate material from a model?

Unassociate a material from a model by "Make unique".

> Reference: [What is "Make Unique"?](https://docs.d5render.com/model/what-is-make-unique)

### Q: How to duplicate the model in situ (the position of the duplicated model remains unchanged)?

After duplicating, click the mouse in the scene (without moving the mouse) to duplicate the model in situ.

### Q: Do lights support parameter association?

Duplication of lights does not support parameter association. After multiple selections or grouping of the same type of lights, the parameters of the lights can be edited uniformly.