# Syncing Objects and Properties

This plugin supports synchronisation of objects and attributes between Sketchup and D5 Render for collaborative work across software. Below is a description of syncing objects and attributes:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FG8QIcgBhIG31ybmMA7t0%252Fimage.png%3Falt%3Dmedia%26token%3Db493591e-6309-4c39-a8bf-a3c83ecafb26&width=768&dpr=3&quality=100&sign=ff6d01cd&sv=2)

## Details of Syncing Objects and Properties

### Syncing Model

#### Supported properties:

- 3D Transformations (Pan/Rotate/Scale)
- Component
- Material Assignment
- Outliner (show/hide)
- Tag (show/hide)

#### Not supported yet:

- Tag/Layer

#### Notes:

- SU has double-sided materials, while D5 only supports single-sided materials (front materials). If there are double-sided materials in the scene, it may lead to rendering errors.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FpmssJxoe4zuAH444UcWk%252Fimage.png%3Falt%3Dmedia%26token%3D0a527190-7141-41e9-b12b-c751e658e35d&width=768&dpr=3&quality=100&sign=72b6eee2&sv=2)

Double-sided material in SU

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FrEXRMVCSoVMmI9sjwlOE%252Fimage.png%3Falt%3Dmedia%26token%3D579c1fd8-5232-4437-a113-9e5ab1ff8023&width=768&dpr=3&quality=100&sign=fe810dc4&sv=2)

Abnormal scatter plants

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F4yEeTifIgYCun3cw3YFB%252Fimage.png%3Falt%3Dmedia%26token%3D3bf38501-3acb-498b-a0ec-69122db8b1e0&width=768&dpr=3&quality=100&sign=689778cd&sv=2)

Subsurface scattering(SSS) material

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSK5l9h9gf00GuYVNo6VN%252Fimage.png%3Falt%3Dmedia%26token%3Df2fd0f31-b532-4429-9ca6-d341196db2ef&width=768&dpr=3&quality=100&sign=bf6f6dc9&sv=2)

Abnormal terrain grass

### Syncing Material

#### Version Compatibility:

- SU version 2024 and earlier: Supports Basic Color / Opacity / Texture / UV.
- SU version 2025: Added PBR material support.

#### Syncing Rule:

- Material priority：Front Material > Parent Component Material > Reversed Material
- How to revert back to material in SU after modification within D5:

  - Method 1: Modifying material names in Sketchup to trigger synchronisation
  - Method 2: After clicking ‘Reset’ parameters in D5, then re-adjust parameters in SU.

### Syncing Light

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FXPSa5xQEETk9JOjtO9ny%252Fimage.png%3Falt%3Dmedia%26token%3D9737b961-67af-4629-97cc-23c37d243edd&width=768&dpr=3&quality=100&sign=78beb07b&sv=2)

D5 Light

#### Supported types:

- Point Light / Spot Light / Strip Light/ Rect Light/ Disc Light
- 3D transformation properties
- Outliner (show/hide)

#### Note:

- Light intensity to be calibrated at SU en

### Scene and Viewpoint

#### Supported:

- 3D transformation properties
- Perspective/Two-Point Perspective

### Geo and Sky

#### Supported:

- 'North Angle' parameter
- Sync 'time/date' parameters from 'Shade' panel in SU automatically

#### Not supported yet:

- HDRI Sky

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fdh2amUwad1XNoxweVN8Z%252Fimage.png%3Falt%3Dmedia%26token%3D08b8f5a2-bee6-442a-ba8c-fad0f14d65a0&width=768&dpr=3&quality=100&sign=bed8c2e&sv=2)

North Angle