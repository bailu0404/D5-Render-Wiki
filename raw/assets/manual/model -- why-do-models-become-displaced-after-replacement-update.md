# Why do models become displaced after replacement/update?

> Similar question:
>
> - Why does the brush plant produce an offset after updating/replacing the model?

## Solution:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FkpverTMNRyFxSccfrvx6%252F16C1017C-F9F4-4391-81A5-168973A9A6EF.png%3Falt%3Dmedia%26token%3D5d500df3-edab-4276-9d0f-011a796683aa&width=768&dpr=3&quality=100&sign=e033f1d6&sv=2)

## The reason for the issue:

The coordinates of the model that is imported directly into D5 is set to the default point A at the bottom center of the model.

If the overall range(bounding box) of the model is changed after replacement, the position of the coordinate axis will be recalculated and changed to point B, which can cause displacement issues.

By clicking the "Sync Coordinates" after selecting the model, the model will be restored to its absolute modeling coordinate position.

> ℹ️ > ****Note:****

****If the imported model is a .d5a file with group structures****, please perform the ‘Sync Coordinates’ after the first import and after replacing the model, respectively.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FeroV2ZmCLghvmncs1KM4%252Fsync2_compressed.gif%3Falt%3Dmedia%26token%3Dc86917a6-4299-42a8-9f5a-160e19cb13f1&width=300&dpr=3&quality=100&sign=e90b6a6b&sv=2)

---

****e.g.****

(As shown in the figure below) if you have three models, a square, a circle, and a rectangle, and the coordinate origin of the models is at point A (D5's coordinate axis is set to the bottom center of the model by default).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8ZD0JQ5JwcflCDXFAlM0%252Fimage.png%3Falt%3Dmedia%26token%3D3d58f1cd-36ed-4fe6-8dcb-49b667d49619&width=768&dpr=3&quality=100&sign=f8c2eaf0&sv=2)

If we delete the rectangle, the coordinate origin of the model will change from point A to point B.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F0eazxzTrsN8JCfAyMtwM%252Fimage.png%3Falt%3Dmedia%26token%3D80d93b1d-e158-411d-b83b-f7b5de5e7104&width=768&dpr=3&quality=100&sign=6a099abf&sv=2)

If we align the coordinate axis at this time, the models will move.

---

This is why the model stays in place even if the bounding box changes.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fywp4YBQTZkYo45xduqKE%252Fimage2.png%3Falt%3Dmedia%26token%3D672acd77-8a0d-4005-b3e6-5a77ed8fa7dc&width=768&dpr=3&quality=100&sign=f4245b41&sv=2)

By using the "Sync Coordinates", the model will be moved to the position of the coordinates in the modeling software.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FBtZfo8DbSAfy1y0jkeCZ%252Fimage3.png%3Falt%3Dmedia%26token%3Db8fd85c6-bcd3-4922-9c52-328a33753e48&width=768&dpr=3&quality=100&sign=29b2f24&sv=2)

If you make changes to the model at this time (with the little tiger as the reference object), the position of the model will not be displaced anymore!