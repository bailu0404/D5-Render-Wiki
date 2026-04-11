# How to restore the imported model's built-in materials?

### Solution:

1. Change the material name in the modeling software.

2. If it's during the sync process, click the "Update" button in the D5 Converter.

If it is a directly imported model, right-click on the model in the resource list and select "Reload" from the menu bar.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FbDtOf5rE86fdVitls0wP%252Fimage.png%3Falt%3Dmedia%26token%3D8fc5d036-1577-42fc-8761-294d1635e210&width=768&dpr=3&quality=100&sign=862b43fc&sv=2)

### The logic of sync materials

Currently, the logic of sync materials through the converter are as follows:

1. If the material parameters have not been changed in D5, always sync the plugin parameters.

2. If a parameter has been changed in D5, the D5 parameter will take precedence, and the corresponding material parameter in the modeling software will no longer override the D5 parameter.

3. If a material template has been switched in D5, all parameters in the current material template will still follow the rules of [2].

4. If a material's name has been changed, it will be treated as a new material and resynchronized.

5. If you use a material from the asset library, it is equivalent to completely replacing a new material, and cannot be reset.

The logic of sync materials through directly importing and reloading models are as follows:

6. Once imported, the material parameters in the modeling software will no longer affect the material parameters in D5.

7. Only renamed materials will be treated as new materials and resynchronized.

The most effective way to restore the material to the one in the modeling software is to rename the material in the modeling software and then update the model/resynchronize.