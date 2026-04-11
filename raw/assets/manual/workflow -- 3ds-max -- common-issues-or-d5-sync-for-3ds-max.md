# Common issues | D5 Sync for 3ds Max

## 1. Why does the menu bar in 3ds Max display "D5" and "D5 Render"?

The "D5 Render" displayed in the menu bar is an older version (version 2.98), and "D5" is the current newer version;

If you need to keep only "D5", please select "Customize - Customize User Interface - Menu - D5 Converter - Delete - Save" in the menu bar to keep only "D5".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FNmzecwZExCBtWZ4IZ3Wf%252Fcommon%2520issue-1.png%3Falt%3Dmedia%26token%3D032ee0e0-d059-4b86-bd7f-9e171da6627b&width=768&dpr=3&quality=100&sign=13cae20c&sv=2)

## 2. Why does the D5 converter - 3ds Max export .skp files slowly?

Due to the limitations of export efficiency, exporting larger 3ds Max files (over 1.5G) to .skp is indeed slower.

Suggestion: If you need to import to D5, you can directly use the linked workflow; if you need to export .skp files, you can try to export the overall model in multiple .skp files.

## 3. Why does the transparency map in the material get lost when the 3ds Max model is synchronized to D5?

The transparency map needs to be added to the "Opacity" map slot in the 3ds Max material.

After synchronization or export to D5, it will automatically correspond to the transparency material template.

## 4. What types of 3ds Max lights are supported for import into?

Currently, Vray Light Dome/Vray Light Mesh/Vray Light Environmental Light are not supported.

3ds Max Lights type

3ds Max Lights parameters

D5 Lights

Standard-Target/Free Spotlight

location, attenuation-use-end, light cone-aspect, orientation, light color

Spotlight

Standard-Target/Free Parallel Light

light cone-aspect, light color

Strip light

Standard - Floodlight

colour

Point light

VRay Plane

location, size (light length and width), orientation, temperature/colour

Strip light

VRay Sphere

location, colour

Point light

VRay IES

ies files, rotation

Spotlight

Corona Light

ies file, temperature/colour

Spotlight

Corona Rect

location, size (light length and width), orientation, temperature/colour

Rect light

Corona Disk

location, temperature/colour

Spotlight

Corona Sphere

location, temperature/colour

Point light

Corona Cylinder

location, temperature/colour

Rect light

Corona Sun

location

Strip light

Arnold Light

Point light

Photometric light

Point light

## 5. Why do the materials of the 3ds Max model lose or have effect issues after being synchronized to D5?

Please refer to the instructions for the current material support in D5 Converter-3ds Max:

- Dirt Material: When there are both occluded and non-occluded maps, the non-occluded map is taken.
- The current version only supports basic mapping for procedural maps such as falloff, mix, composite, etc., and will be individually optimized for these nodes in the future.

Suggestions: Directly remove the falloff node, or replace it with a material library material (When the IOR is greater than or equal to 10, the D5 material metalness parameter is 1, it is recommended to manually adjust the IOR to below 10 or lower the metalness parameter in D5).

## 6. How to uninstall D5 Converter-3ds Max?

Method 1: Click on "Windows System-Start Menu-Plugin Uninstaller-Uninstall D5 Converter for 3ds Max".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F5UzI5ZDEwCWrjlNPNQQm%252Fimage.png%3Falt%3Dmedia%26token%3D0dc69fde-f07a-4ea9-a0ef-5f81b9dcf33c&width=768&dpr=3&quality=100&sign=57e84d24&sv=2)

Method 2: Uninstall it through "Computer-Control Panel-Programs-Uninstall a program".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FPlhmniCph3uuAxYmXKU4%252Fimage.png%3Falt%3Dmedia%26token%3D5acefb8a-cb05-4d8b-800c-6235d17c3401&width=768&dpr=3&quality=100&sign=ab7fcf28&sv=2)

## 7. Why does the model deviate when aligning two objects during export or snyc using the D5 Converter-3ds Max plugin?

When using D5 2.4 version, align the group structure objects （export or snyc）with non-group structure objects, the model will deviate by 90°.

Suggestion: Keep all objects in the D5 scene as either group structure objects or non-group structure objects for correct alignment.

## 8. Why does the exported .d5a file deviate after using the sync coordinate?

After importing and saving the .d5a file in D5 version 2.3, the scene is opened in D5 version 2.4, and the .d5a file is imported again - the coordinate is synchronized, the model deviates by 90°.

Suggestion: Swap the x/y values of the model's position in D5, and then add a "-" sign to the swapped y value, which can align with the .d5a file imported in version 2.3.

For example: The position of the imported .d5a in the figure below 2.3 is (-8,15,0); after the .d5a file imported in 2.4 is synchronized with the coordinate, the position is (-15,-8,0), swap its x/y values and add a "-" sign to the swapped y value, then it becomes (-8,15,0).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FDmtHUiAdfRnvZgWMBbPe%252Fcommon%2520issue-2.png%3Falt%3Dmedia%26token%3D3141dd3e-82f2-4ece-8b6b-a6b3848f12e6&width=768&dpr=3&quality=100&sign=5a1a7d8d&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F2N9bQAsFm8bgf88FLzfX%252Fcommon%2520issue-3.png%3Falt%3Dmedia%26token%3D903f813b-64d3-4acb-b684-39edf7e1cf21&width=768&dpr=3&quality=100&sign=765dfc05&sv=2)

## 9. Why are objects hidden in 3ds Max displayed after being synchronized to D5?

The sync and export .d5a function currently does not support layer hiding or category hiding.

Suggestion: If you need to export, you can use the group export function, group the parts you need to hide before exporting, in order to achieve the model hiding effect in D5.

## 10. Why ungrouped objects in 3ds Max group together after being synchronized to D5?

Currently, only group exports to .d5a files are supported, and the sync feature does not yet support preserving group structures in D5.

## 11.D5-3ds Max converter installation error, indacates "Create File failed; code 5.Access is denied."

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FZSyNSfZMkZuIgrKAxwmJ%252Fcommon%2520issue-4.png%3Falt%3Dmedia%26token%3D012087af-82bf-4de3-bdc1-c9dd976e01a6&width=768&dpr=3&quality=100&sign=afc61f83&sv=2)

This error is due to permission issues；

Suggestion: Uninstall the D5-3ds Max converter from the Windows start menu, and then reinstall the new version of the plugin.

Specific uninstallation steps can refer to: [How to uninstall D5 Converter-3ds Max?](https://docs.d5render.com/workflow/3ds-max/common-issues-or-d5-sync-for-3ds-max#id-6.-how-to-uninstall-d5-converter-3ds-max)

## 12. "Exception catched in D5ExportD5A/D5ExportSKP." when exporting.

Mothod 1: Uninstall the D5-3ds Max Converter in the Windows start menu in either way, and reinstall the new version of the plugin.

Mothoed 2: If after uninstalling and reinstalling, the error message still occurs. Delete the MaxToD5a.toml file or MaxToSkp.toml file under the corresponding path. For example, if you get an error when trying to export a .d5a file from 3ds max2022, delete the MaxToD5a.toml file under 3ds max2022, file path: C:\Users\Administrator\AppData\Local\Autodesk\3dsMax\2022 - 64bit. CHS\plugcfg\_ln\MaxToD5a.toml

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FqkXghADwty85Egiq2pB6%252Fimage.png%3Falt%3Dmedia%26token%3D6ee61cb3-3966-4f90-9efd-4cf2a00e0170&width=768&dpr=3&quality=100&sign=6f84c850&sv=2)

## 13. Why is the plugin UI not displayed after installing the 3ds Max-D5 Sync plugin?

## 14. Why are some models not displayed or misplaced when using the plugin to sync/export .d5a models?

Due to data efficiency reasons, some models will have the above situation. Solution: Collapse/reset the abnormal part of the model in 3ds Max to transform it a bit, it will improve.