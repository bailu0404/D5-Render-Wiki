# Why does adjusting the parameters of the Effect panel not have any effect?

If the main model in the scene is too far away from the origin of the world coordinates, it may lead to an error in the precision calculation of the parameters in the later stage, just select all the models in the scene and zero the coordinates.

It is recommended to move the coordinates of the model to (0,0,0) automatically first when importing the model into D5 for the first time.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKcXNZl8ksnpW8KufS0cZ%252Fimage.png%3Falt%3Dmedia%26token%3De7c32203-3b4b-4675-b0bf-19ef90057b34&width=768&dpr=3&quality=100&sign=9dd12456&sv=2)

The model is located at the origin (0, 0, 0)