# Team Library Deployment

After setting the address, username and password for the shared folder in D5 Render, your team members can freely access resources in the folder on the LAN after logging in to their D5 accounts.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FX0KDDSqy5pGgPzAOsKPJ%252F1100.jpeg%3Falt%3Dmedia%26token%3D2d2e4f23-27c9-4917-bfab-d2e6ee9f203e&width=768&dpr=3&quality=100&sign=926f40da&sv=2)

### Step 1: Create a Shared Drive

Currently, D5 can connect to shared drives using the Samba protocol. By configuring the corresponding shared drive address, access account, and password in the D5 client, you can use the team library on the LAN.

[How to set up Windows shared drive?](https://docs.d5render.com/instruction-for-d5-for-teams/how-to-deploy-team-library-and-manage-team-assets/how-to-set-up-windows-shared-drive)

Use a portion of your local storage as a network storage location.

Advantages: No additional cost. Easy and convenient setup.

Disadvantages: This tends to cause a shortage of local storage space, and shared host needs to remain powered on. There is a maximum limit on the number of users who can access it.

[How to create a NAS shared folder?](https://docs.d5render.com/instruction-for-d5-for-teams/how-to-deploy-team-library-and-manage-team-assets/how-to-create-a-nas-shared-folder)

NAS - Professional Network Storage Device

Advantages: Large storage space, does not occupy local storage space, secure and stable, suitable for multi-person team sharing.

Disadvantages: Relatively high cost

### Step 2: Configuring the Team Library Address in D5 Render

****Configuration entrance****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQEyp8Mrqfyu0eNU0dPdu%252FF42B8F66-CA6E-4f63-A092-F49E506538DF.png%3Falt%3Dmedia%26token%3Dd13942e3-d0d9-4efa-8f49-26b52676b8a3&width=300&dpr=3&quality=100&sign=b379a151&sv=2)

Go to D5 Launcher: Setting - Team Library Deployment (visible only to administrators).

Copy the shared drive information you set up to the corresponding input box and click Save.

****Modification and permission management****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F13hnmMhuzmtgMbWRHUOO%252FA29A4366-3447-43e7-9C11-24C5E3D8CE84.png%3Falt%3Dmedia%26token%3Db3f18fda-7d5a-404f-84bc-6d27467ef9e8&width=300&dpr=3&quality=100&sign=8dbcf32&sv=2)

● If you need to modify a saved shared drive address, you must first remove the original address.

● It is recommended to set the shared drive to the highest permission level to allow for deletion, modification, upload, and download.

### Team Assets Management

****Access Team Assets****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FeyvYQh2ALFjnlWOVpgCk%252F116.jpeg%3Falt%3Dmedia%26token%3Dc3d9042d-7907-43af-817f-c557263ae242&width=300&dpr=3&quality=100&sign=4d8c4131&sv=2)

Open the D5 Asset Library and go to "Team", all the d5a(asset) and d5m(material) files under the access address directory of the shared drive will be displayed.

Note:

If the folder structure exceeds 4 levels, after opening it, assets will take longer to load.

****Migrate Team Assets****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F3SNDxDt1FVRO2OlJdZbw%252F117.jpeg%3Falt%3Dmedia%26token%3D1a071d86-afd8-4b5b-ac50-641a6f0e1c17&width=300&dpr=3&quality=100&sign=17961501&sv=2)

Team administrators can directly copy the accumulated D5a & D5m file assets to the corresponding folder in the team asset library.

Note:

Currently only team administrators can perform this operation.

****Generate Asset Thumbnails****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FkfqNyLHeYFnDtVQ16IWQ%252F118.jpeg%3Falt%3Dmedia%26token%3D68ae8eb0-8019-4326-86ea-088d939f577f&width=300&dpr=3&quality=100&sign=4402156a&sv=2)

Team administrators can upload assets to the asset library and then click the "Refresh" button in the upper-right corner to automatically generate preview images for the assets in the team asset library.

Note:

Setting preview images can speed up the loading of the asset library.

****Upload File Permission****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7b3gmntv76piwgYkGn7q%252F5DAAC46B-7A20-4415-AA60-65B07BF142A5.png%3Falt%3Dmedia%26token%3D0644e336-168a-4045-9973-5ac22103c94e&width=300&dpr=3&quality=100&sign=5b97a3ab&sv=2)

For easy management of team library by administrators, the default LAN library permits only [team administrators] to upload files via the client.

If you want all team members able to upload files to the LAN library, owner or administrators can enable the ‘Enable members to upload files’ custom switch.

### Team Project Management

****Access and manage project libraries****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FbIeyVPHvyO8RgC9hkcYx%252F96F46FD6-D4D7-451e-9C5F-E2D17292D350.png%3Falt%3Dmedia%26token%3Dbd3628b3-29ac-4204-9b5d-f58194fd81fb&width=300&dpr=3&quality=100&sign=75f13f2d&sv=2)

After successfully configuring the project library address, D5 Launcher will display a "Team Projects" entry.

After opening the project library, you will see all the D5 projects under the root directory.

****In the project library, the same project can only be edited by one user at a time when the project is not a Workset****.

**If multiple users edited the same project in a shared NAS, it may cause local archives to overwrite each other, resulting in the risk of data corruption.**

When multiple members need to edit a project simultaneously, you can ****convert it into a Workset**** and set which parts each member can edit and save to local. [How to use Multi-editing?](https://docs.d5render.com/instruction-for-d5-for-teams/how-to-use-multi-editing)

****Forced quit of editing status****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJd4XbeRYRzrgkaNHv2fu%252F1105.png%3Falt%3Dmedia%26token%3D24125d4f-a762-4c29-b3ad-34e9ad54c00a&width=300&dpr=3&quality=100&sign=4167a801&sv=2)

If a project is not closed properly, such as due to software crashes or computer shutdowns, the project will remain in an editing state. You can remove the editing state in two ways:

1. If you are the editor of the project, please reopen the project and close it properly.

2. Team administrators can use the "Forced quit of editing status" feature to remove the editing state of the project. Please make sure that the project is not being edited at the moment, otherwise archive errors may occur.

****Create a Template****

You can save a project as Template.

### Notes

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FwvE1XSp2jEpvv3gYEke7%252F1101.jpeg%3Falt%3Dmedia%26token%3D5b445ce8-a4c8-4623-96da-ff4aa3342e57&width=768&dpr=3&quality=100&sign=8bac532b&sv=2)

1. After the administrator updates the assets in the shared folder, they need to click the "Refresh" button in D5 Render team library to load the cache. If the asset library has been updated without refreshing in time, the preview images could get slow to load.

**Please do not add or delete folders after opening D5 Render, as the folder acquisition is not real-time. If the folder directory is not updated in time, please close D5 Render and reopen it.**

2. The D5 Render team library is based on the LAN protocol. If team members cannot access the team asset library, please check if the network of their computer is consistent with the network used by the shared drive address.

**If you find that the download speed of assets (or projects) in the team library is slow, you can check if the NAS that stores the team library has set traffic restrictions.**

3. If you need to use the team asset library in a WAN environment, there are three ways to achieve it:

a. Use the VPN provided by the company's IT department to access the internal network.

b. Apply for a public IP address from the ISP.

c. Use a network proxy provider, such as Synology NAS Quick Connect.

Usage recommendations

1. Manage asset library and project library separately using different addresses.

2. Name and classify folders according to asset category or by project.

3. Do not place too many projects in the project library. Completed projects can be moved out of the project library and backed up.

### Common Issues and Troubleshooting

When deploying D5 Team Library, if the connection fails, the Windows system will return several corresponding error codes, and the corresponding feedback in the D5 Render is as follows: ↓

Error codes returned by Windows

Prompt in D5

Note

ERROR\_ACCESS\_DENIED

The current account does not have permission to access the address

Possible causes: 1. Improper permissions set for the shared drive; 2. The host where the shared drive is located has been shut down.

ERROR\_BAD\_NET\_NAME

The target folder location is invalid

ERROR\_BAD\_USERNAME

The user name is invalid

ERROR\_INVALID\_PASSWORD

The password is invalid

Possible cause: 1. The computer where the shared folder is located has the same account name (i.e. login name) as the other members' computers, making it impossible to share.

ERROR\_NO\_NETWORK

The network is not available, please check if you are on the same LAN

ERROR\_LOGON\_FAILURE

The account or password is invalid