# How to fill hedge leaves with one click?

In the production of outdoor scenes, for the regular hedge scene, it is recommended to use the plant path tool in D5 to quickly generate. And for the scene with rich shapes of the model, you can quickly generate the hedge leaves by one-click filling.

## Where is the one-click fill hedge blade feature turned on for the D5?

### Scater by brush

By selecting the model and choosing the Brush tool, you can use the currently selected hedge leaf material to paint in the scene.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FZ4kTeoULeRD3htXS2Rod%252Fhedge.jpg%3Falt%3Dmedia%26token%3D1d72ef63-6cde-48c5-b64c-3dc24bb450e6&width=768&dpr=3&quality=100&sign=a625138d&sv=2)

A variety of new leaf materials have been added to the "Library" -> "Nature" -> "Hedges" category in the online library, and those with "single" in their names are suitable for use with the Scatter feature to achieve the hedging effect.

- ****Radius****: Set the Radius parameter to maximum, enable the Fill tool and fill the selected model face with hedge leaves.
- ****Density****: Set the density parameter to maximum to obtain a uniform filling effect.
- Select '****Align to Terrain****'.
- ****Random Size****: When the parameter is set to 0, the filling effect of hedge leaves is the most regular and orderly, and the adjustment of the parameter value can control the degree of random changes in the size of the leaves.

> ****Dynamic plants**** do not support the 'Align to Terrain' feature at this time.

- Set the radius to the maximum value to clear the current scattered leaves.
- When selecting the radius between 0.01 and 1, you can make local detail deletion and adjustments in the hedge bush.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FC7AlzbR4nDgaaPM7xeou%252Fhedge-fill.gif%3Falt%3Dmedia%26token%3Dca563dcc-d8d7-4267-8dca-115760aa31cb&width=768&dpr=3&quality=100&sign=255783ff&sv=2)

- ****If the model does not produce uniform blades locally****, you can use secondary scatter to second fill locally on the current base.

> If this operation does not produce results, ****check in the modeling software that the model is all frontal****.

- ****The height of the material is about 15-20cm when the size is 1.**** For scenes that require strict dimension, it is recommended to leave a certain amount of height space in the modeling process or reduce the size to get a suitable effect.
- ****For efficiency issues, it is recommended that the single fill area should not be too large.**** Otherwise, it will result in long scatter generation time or lag in real-time preview.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FhvV9ecWdXM9HzXMbtg1V%252F111.png%3Falt%3Dmedia%26token%3De634dba9-fd6d-44c4-893e-41543fe6d3e7&width=768&dpr=3&quality=100&sign=7c7978a8&sv=2)

Effect before & after one-click filli