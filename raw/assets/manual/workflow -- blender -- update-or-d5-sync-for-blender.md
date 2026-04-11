# Update | D5 Sync for Blender

## Ver. 0.10.0.0021

`Release date: 20260112`

## New

- Support for ****Blender 5.0****
- Compatibility with ****D5 Render 3.0****

---

## Ver. 0.9.2.0029

`Release date: 20250807`

## New

- Supports Blender 4.3/4.4/4.5.
- Supports syncing IES for all light types (requires D5 Render 2.11 or above).
- Supports syncing Disk and Ellipse lights to Disc Light (requires D5 Render 2.11 or above).
- Supports syncing HDRI (requires D5 Render 2.11 or above).
- Supports syncing parallel projection (requires D5 Render 2.11 or above).

## Fixes

---

## Ver. 0.9.1.0051

`Release date: 20241024`

### New

### Optimization

### Fixes

### Known Issues

---

## Ver. 0.9.0.0102

`Release date: 20240709`

### New

- Compatible with Blender 4.1
- Supports more Geometry Nodes from Blender 3.4 to 4.1
- Supports more Modifier operations from Blender 3.4 to 4.1

### Optimization

- Increased sync speed
- Increased sync speed for Geometry Nodes
- Increased speed for single texture baking

### Fixes

- Fixed synchronization and material issues for models duplicated using Alt+D

### Known Issues

- Operational delays in Blender when view synchronization is enabled
- In linked mode, the operation of un-hiding objects cannot be synchronized to D5 Render. To ensure proper synchronization, it is recommended to move the object after unhiding it before syncing
- Currently not supports Geometry Nodes with initial data types set to curves, including curve to mesh
- Materials of certain geometry nodes are temporarily unsupported for synchronization and baking

---

## Ver. 0.8.0.0096

Release date: 20240125

### New

- Compatible with Blender 4.0
- Exported .d5a files support thumbnails

### Optimisation

- Increased sync speed
- Improved launch speed for non-first-time Blender starts after installation

### Fixes

- Fixed normal issue that some models synced into D5 being blackened or greyed in colour
- Fixed the issue of texture anomaly when exporting .d5a to D5 after baking the same material for the same object with different resolutions.
- Fixed the size issue of Blender 3.5 models synced to D5.
- Fixed the issue that models were not synced to D5 after the end of sync in some scenes.

### Known issues

- Curve to Mesh node sync is not supported yet.
- Hiding objects does not trigger incremental sync, it is recommended to use full sync.
- If the sync is abnormal after using a modifier, it is recommended to apply the modifier before syncing.
- When you use Alt+D or other methods to associate copied objects with sync errors, it is recommended that you select the model first, click blender Object-Relations-Make Single User-Object&Data&Materials, and then sync.

---

## Ver. 0.8.0.0039

Release date: 20230731

### New

- Support Blender 3.6

### Fixes

- Fixed the issue where some scenes could not be synchronized to D5

### Known Issues

- When using Blender 3.6, the synchronization speed of the D5 plugin is about 3 times slower than other versions.

---

## Ver.0.7.0.0134

Release date: 20230221

### New

### Fixes

---

## Ver.0.7.0.0007

Release date: 20221108

### New

### Currently unsupported:

### Known issue