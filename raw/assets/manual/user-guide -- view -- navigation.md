# How to move the viewpoint freely?

## Navigation Mode

New Navigation Mode: ****Free****
Integrated ****Orbit**** and ****Fly**** into Free mode for flexible and friendly navigation control.

Now, the Navigation mode in the upper right corner is divided into two types: ****Free**** and ****Walk****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F0054NsHZhtXTatPbbd1F%252Fimage.png%3Falt%3Dmedia%26token%3D65b8dfec-880a-45af-ac22-8213c43f9255&width=768&dpr=3&quality=100&sign=2503caf1&sv=2)

### ****Orbit****

The viewpoint moves around the object in the center of the screen, using a combination of the mouse wheel, the right mouse button, and the Shift key.

- In the Orbit mode, when you press the right mouse button or the scroll wheel to click on the model, the intersection point of the mouse and the model will be regarded as the orbit point, and the object will rotate around this point.
- In the Orbit mode, when you press the right mouse button or the scroll wheel to click on the background, the gizmo of the selected object or the object closest to the center of the screen in the current viewport will be regarded as the orbit point.
- Orbit view supports visual icon to help users identify the center point of the current rotation, improving operational feedback and sense of control.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FICzvKM04tudrDYZPcicG%252Fimage.png%3Falt%3Dmedia%26token%3D44a9aea2-7bac-4b24-b17b-8ed421dad871&width=768&dpr=3&quality=100&sign=d65081d5&sv=2)

Orbit point

### ****Fly****

Use the ****right mouse button**** with the ****WASD**** on the keyboard to Use the center of the screen as a moving target.

### Walk

Walk and view the scene in the first person, ****right mouse button**** with ****WASD**** on the keyboard to move around.

> - After switching to Walk Mode by clicking on the upper right corner of the interface, the viewpoint will drop down to the object below according to the set height.
> - When using WASD to walk, always keep the camera height to move, such as encountering a wall will cause collision and can not pass through.

OperationOrbitFlyWalk

Hold the scroll wheel

Free movement according to the center of the screen

Free movement

Free movement

Scroll wheel

Move the camera according to the position of the mouse

Move the camera back and forth to the center of the screen

Move the camera back and forth to the center of the screen

Right mouse button

Camera moves around the center of the screen

Fixed camera position, change the direction of view

Fixed camera position, change the direction of view

Hold down the left and right mouse button

-

Move the camera up and down

Move the camera up and down

WASD

-

Move the camera back and forth and left and right

Move the camera back and forth and left and right

QE

-

Move the camera up and down

Move the camera up and down

Shift + Right mouse button

Panning camera

-

-

## Comparison between old and new navigation modes:

Orbit

Pan

Look around

Move forward/backward/left/right in Fly mode

Up in Fly mode

Down in Fly mode

Custom speed

Accelerate/Decelerate

Dolly in/out

Zoom(FOV only)

Deselect

Box Select

D5 2.11

In Oribt Mode:

Right mouse button or Middle mouse button

In Orbit Mode:

Shift + Right Mouse Button or Middle Mouse Button

In Fly Mode: Hold the right mouse button and drag to look left/right/up/down

Hold down the middle mouse button and drag to look left and right, move forward and backward

WSAD

Q

E

Hold the right mouse button and then scroll wheel.

Value range: 1-200. This action is distinct from single right-click.

In Fly/ Walk mode: Hold Shift to speed up and Space to slow down

Scroll the mouse wheel. In Orbit mode, the dolly distance adjusts proportionally; In Fly mode, it adapts to the movement speed.

Shift + Scroll Wheel

Press the left or right mouse button without moving the cursor, equivalent to pressing Esc.

Hold Ctrl and the left mouse button to drag

D5 3.0

(Temporary default settings)

Left mouse button

Hold the middle mouse button and drag

Right mouse button

WSAD ↑↓←→

Q

E

Hold the right mouse button and then scroll wheel.

Value range: 1-200. This action is distinct from single right-click.

Hold Shift to speed up and Space to slow down

Scroll the mouse wheel to move proportionally, which follows the dolly logic of the Orbit mode.

Alt + Scroll Wheel

Press the left mouse button without moving the cursor, equivalent to pressing Esc.

Hold Ctrl and the left mouse button to drag

## Navigation Presets:

- Added navigation presets matching SketchUp, Rhino, 3ds Max, and Revit, along with default D5 presets, under Navigation > Settings. Changes take effect immediately upon switching presets.
- Compatibility with old navigation modes:

  - D5 Preset 1 (Default) for Fly mode
  - D5 Preset 2 for Orbit mode

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FdFAFEnHampsXa9MRyPTw%252Fimage.png%3Falt%3Dmedia%26token%3D98b0b8ca-b1b6-42cd-949d-c1430c0018ab&width=768&dpr=3&quality=100&sign=64d2ef01&sv=2)

- Customizable Shortcuts

  - Supports setting custom shortcuts for navigation presets.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FWE4MSs1qWyOJh8Lpo6hO%252Fimage.png%3Falt%3Dmedia%26token%3D41d263d7-bcea-492f-bfb1-53bc14526589&width=300&dpr=3&quality=100&sign=ad86addb&sv=2)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FbvAKUekpSYSMEb2ziLBR%252Fimage.png%3Falt%3Dmedia%26token%3D22e2ce14-f4f7-4477-9a88-5bb35273a4d0&width=300&dpr=3&quality=100&sign=b736a24c&sv=2)

## Parameter Adjustment

### ****1. Movement speed:****

- Orbit Mode

****In 'Orbit'Mode ,The speed is not adjustable.****

The movement speed is related to the distance of the lens from the objects in the scene, moving slower when the distance is close and faster when the distance is farther away.

- Fly and Walk Mode

  - In 'Fly' and 'Walk' modes, when pressing the ****Shift key****, the speed will become 4 times faster than the original speed. Press the ****Space key**** to decelerate the speed. Press the ****Shift+Space keys**** to accelerate by 2 times. When the speed is set at 1, pressing the ****Space key**** will lower the speed to 0.2 for tweaks.
  - You can press the right mouse button and scroll the wheel in Fly Mode and Walk Mode to modify the movement speed, scrolling the wheel fast to change the speed quickly, scrolling slow to fine-tune the speed.

### ****2. Eye level:****

Adjust the vertical height of the actual viewpoint of the lens from the horizontal plane of the scene origin coordinates, the range of the slider value of the lens height in the Walk mode is 0.8m-2.5m, and it ****does not support manually inputting a larger value****.

### ****3. Altitude****

Adjust the vertical height of the actual point of view of the lens from the horizontal plane of the scene origin coordinates, the range of the slider value of the flight height in the Fly mode is 0m-50m, and it ****supports manually inputting a larger value****.

### ****4. Roll****

Control the rotation angle of the camera in the horizontal direction.

### ****5. Mouse Speed****

Adjust freely the speed at which the camera rotates around the object in Orbit mode, and the speed at which the camera turns its head up, down, left, right, and center in both Fly & Walk modes.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FBce3h7o3HxGvkbn4k6TX%252Fimage.png%3Falt%3Dmedia%26token%3D941b403c-e658-47c5-88ab-804279297c74&width=768&dpr=3&quality=100&sign=43990d5f&sv=2)

---

## FAQs

### Q: Why does moving the viewpoint with WASD not work?

A: ****WASD shortcuts only work when the movement mode is fly and walk.****

- In orbit mode, you need to use the mouse and scroll wheel to adjust.

### Q: Why can't I use walk mode?

A: If ****the landing site is not captured in the current view****, it will automatically switch from walk mode to fly mode or fail to switch to walk mode and display the ↓ prompt.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FWcxxHQ2n4OUYRimpGzrr%252Fimage.png%3Falt%3Dmedia%26token%3D1960aa0c-2b2c-40c2-908c-7d25b5e7d4d6&width=768&dpr=3&quality=100&sign=ca6a954d&sv=2)