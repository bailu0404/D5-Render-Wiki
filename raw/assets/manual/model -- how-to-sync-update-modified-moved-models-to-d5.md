# How to sync/update modified/moved models to D5?

## Directly Import from Workflow

If the model is directly imported into D5, after the model file is modified, you can right-click on the original model in the scene resource list, and select ****"Reload"**** or ****"Replace from Local"**** from the menu bar.

> - If the model's file name or location changes, it can cause the update to fail. You can try re-importing or replacing the model.
> - The updated or replaced model cannot be restored, so please confirm before proceeding with the operation.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FDVGKFhnTRLqWVUpdx61w%252Fimage.png%3Falt%3Dmedia%26token%3D2910ba1a-1e41-42fd-86cf-84fa6c070213&width=768&dpr=3&quality=100&sign=687bab7d&sv=2)

## Sync

To sync the model to D5 using the D5 converter, during synchronization, after modifying the model file, you can ****click the "Update" button in the D5 converter**** to synchronize the modified model to the D5 Render and retain any adjusted materials in D5.

### Modified the model after stop syncing and the file path remained unchanged

Modifications were made on the original model and saved without changing the file name and path of both the model file and D5 scene file.

Solution: You can directly open the modified model file by clicking the "Launch D5 Render" button in the modeling software using the D5 converter. This will allow you to continue with the linkage, and D5 will automatically update to the modified model while retaining the adjusted materials in D5.

### Modified the model after stop syncing and the file path unchanged

A new file was saved, or the file name or file path of the model file/D5 scene file was changed due to moving the file location.

Solution: First, open the model file and D5 scene file separately, click the launch button in the D5 converter, and when the D5 popup appears, click "Select File":

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKEs5xBAWVA6EgUfJACtl%252Fimage.png%3Falt%3Dmedia%26token%3D0a7a5190-e438-40b1-9357-09722c3d4246&width=768&dpr=3&quality=100&sign=f3077e39&sv=2)

After selecting the corresponding model, click "Replace" to continue with the linkage:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F4CLjdvGriDC8j4WqjGDE%252Fimage.png%3Falt%3Dmedia%26token%3Dc5ca54d8-ed56-4bce-9e67-0d621bfddea0&width=768&dpr=3&quality=100&sign=3c92fa5f&sv=2)

## Other FAQs

### Q : Why is the "Reload" button grayed out?

There are two reasons:

1. The model is from the asset library. As there is no source file, the model can't be updated.

2. The current model was sync to D5 using the converter. If you need to update the model, you can use the update model feature in the D5 converter.

> Note:
>
> Do not mix up the workflow of sync and direct import! The models/lights may overlap each other!

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FgiwscGaWwG8OcLa2W2MO%252Fimage.png%3Falt%3Dmedia%26token%3D1a3fd8a0-5c21-4bed-8a6e-adee7d1a3af5&width=768&dpr=3&quality=100&sign=9fe07043&sv=2)

### Q : What is the difference between "Reload" and "Replace from Assets"?

****1."Reload"**** is applicable when the file name and file path of the model have not changed, and all model updates are based on the original model file. Clicking "Reload" will update the model file to the latest version, and adjustments made to the same named materials in D5 will be preserved.

Otherwise, the update will fail, and you will need to manually select the location of the model file.

****2."Replace from Assets"**** follows the same strategy as "Reload", which updates the model file to the latest version and preserves adjustments made to same named materials in D5. Compared to "Reload", there is an additional step where you need to manually select the file path.