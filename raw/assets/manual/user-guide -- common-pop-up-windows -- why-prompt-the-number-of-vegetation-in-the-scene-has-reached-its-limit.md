# Why prompt 'The number of Vegetation in the scene has reached its limit'?

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FTQ2Og5GK2aJfskOfdMAg%252Fimage.png%3Falt%3Dmedia%26token%3D9e538864-16e3-4f7a-95a5-5854e3a6f203&width=768&dpr=3&quality=100&sign=163de854&sv=2)

Vegetation

D5 has a plant carrying limit currently at 30 million. This number is mainly composed of: brush/scatter/path or drawn plants, plants placed in the scene and terrain grass.

Generally, the capacity of these plants is enough for large scenes; however, if the scene uses terrain grass in a large area, and the density of terrain grass is relatively high, it will be easier to trigger the "plant limit" limit. After triggering this limit, you can delete some brush plants/terrain grasses first.

Therefore, if you only need grass in distant view, you can use grass mapping; if you need to use grass in close view, you can try to use brush to draw some grass, which can alleviate the problem of plant limit.