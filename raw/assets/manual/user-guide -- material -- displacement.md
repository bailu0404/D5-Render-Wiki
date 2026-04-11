# What materials are the Displacement templates suitable for? What are the special parameters?

Displacement is a feature used to represent the true bump detail of a material. Previously, only parallax replacement was supported. The new version adds a true replacement option to achieve a more realistic surface effect by modifying the geometric structure of the model.

### ****Opacity Map****

Added Opacity Map to Displacement Material Template to enable precise control over the cutting of materials. It achieves uneven and hollow effects on hedges, fences, bamboo weaving surfaces, and other materials.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F5myOAP6carUe0nIoKekG%252Fimage.png%3Falt%3Dmedia%26token%3D50758ccd-e822-47d8-a958-ccb5fa84da1b&width=768&dpr=3&quality=100&sign=8771f7ef&sv=2)

### ****Height****

The only special parameter of the Displacement material template is the Height, which is usually defined by a height map that defines the bumpiness of the model.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkX6K9RJdG78HZkUlO3%252F-MkX6xoZzaiFm2uJYWIH%252F14d0a779-dc88-487a-a900-167c8e4109b7.png%3Falt%3Dmedia%26token%3Dba8c922d-defa-451b-ba73-30858c12c274&width=768&dpr=3&quality=100&sign=71ee6eab&sv=2)

example

The white color is the convex part and the black color is the concave part.

In the case of the figure below, the height map is pre-imported and used to define the terrain.

#### ****True Displacement****

Expand and enable the true displacement switch in [More Settings].

> ******Tip:****** **If no mapping is added to the height channel, the "More" button does not appear in the interface.**

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FYjqR1GVptrs6DIHvKMo4%252Fimage.png%3Falt%3Dmedia%26token%3Def12338d-a23b-49b6-89c6-647446c819e9&width=300&dpr=3&quality=100&sign=94867558&sv=2)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FvmjyKlQveFQs68kzbzat%252Fimage.png%3Falt%3Dmedia%26token%3D9a363611-4614-48c3-8395-0e9bab2e4c4a&width=300&dpr=3&quality=100&sign=68ececdb&sv=2)

****True displacement parameters:****

- ****Subdivision Level:**** Controls the number of mesh subdivisions.

> ******Tip:****** **A higher subdivision level value can achieve a finer replacement effect, but it will increase the number of model faces, memory usage and rendering time. Excessive use may lead to unexpected flashback. Please set it reasonably according to the hardware performance.**

- ****Vertical Offset:**** The current displacement algorithm does not move at the current model position and rises along the positive normal direction. If the model is on the ground, it will appear raised. To avoid this problem, the vertical offset parameter can be used to compensate for the model's overall position, and the model can be remain in contact with the original ground by adjusting the offset value, without suspension or interpenetration.
- ****Maintain Continuity:**** Ensure that the model's solid structure is closed and complete, avoiding cracks or voids.
- ****Remesh:**** For models with poor original topology (e.g., triangle sizes and topological confusion), mesh reconstruction can be performed first to improve the replacement quality.

  - Off: The tessellation is based on the original topology.
  - On: Tessellation is based on the reconstructed mesh.

> ℹ️ > ****Note:****Mesh reconstruction aims to fix the defects of the original mesh without modifying the structure of the model itself. Please try to ensure the simplicity and accuracy of modeling.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FZglg3UNZYHBaLzgauVwV%252F9c2b180578e556010825584590303cf2.gif%3Falt%3Dmedia%26token%3Dbea8b634-de66-446d-b200-c624763387b5&width=768&dpr=3&quality=100&sign=27f7482e&sv=2)

True displacement

> ⚠️ > ****Note:****

- The ****LiveSync model**** does not support true replacement (the UI interface switch is disabled).
- If you want to use real replacement, you can convert the model to a non-real-time synchronization model (scene resource list-selected model-right-click to convert to a non-real-time synchronization model).