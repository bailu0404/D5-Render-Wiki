# How to create a NAS shared folder?

\*For illustration purposes, only Synology NAS is used as an example.

## Step 1: Enable SMB services

Log in to the NAS device, open the control panel, and enable SMB services.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FrDaJBMLU64PNVu3qcP7w%252Fimage.png%3Falt%3Dmedia%26token%3Dc788d368-687c-433a-9551-ff0b3c4a6202&width=768&dpr=3&quality=100&sign=6d94c688&sv=2)

## Step 2: Setup Shared Folder

Click on "Shared Folder", create a folder and name it (for example, name it "D5LibTest"), then click "Next" to proceed to encryption settings.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FmzZutuLN2QPnaz8CV1Ig%252Fimage.png%3Falt%3Dmedia%26token%3D5c4722fe-f838-4845-8d2b-ff1d2bd41736&width=768&dpr=3&quality=100&sign=6b76281f&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FpkUp0l5KFJ76iZooI1b6%252Fimage.png%3Falt%3Dmedia%26token%3D8f1e282b-7d13-408a-906a-38b957175dc4&width=768&dpr=3&quality=100&sign=73162c26&sv=2)

When creating a shared folder for the team asset library, you can choose to encrypt it as needed (not recommended).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FywqmDn1bBxeESam5nOP4%252Fimage.png%3Falt%3Dmedia%26token%3D9c4a6a01-0d96-4336-920f-97631fcd491d&width=768&dpr=3&quality=100&sign=7e6dc3b8&sv=2)

Select the users who can share this folder and set the permission to "Read/Write".

## Step 3: Get the address of the shared folder

Click on the PC (Windows Explorer) address in "File Services".

For example, \\D5NAS Add the name of the shared folder that was just created to get \D5NAS\D5LibTest, which is the address of the team library shared folder.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F2CRdQQsIsfynm1IS515i%252Fimage.png%3Falt%3Dmedia%26token%3D5fd48f74-7a98-4adc-9a1c-8a1675322675&width=768&dpr=3&quality=100&sign=beccd6c3&sv=2)

Notes:

If the shared account password is correct but the team library cannot be connected, you can make the following settings in the NAS: File Services >> SMB >> Advanced Settings >> Others >> Check "Enable NTLMv1 authentication".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJMTGFbVSRUHUoKbq7mkk%252Fimage.png%3Falt%3Dmedia%26token%3D650c7583-5dff-4dba-ac2c-289c1f284dab&width=768&dpr=3&quality=100&sign=9ec87b6e&sv=2)