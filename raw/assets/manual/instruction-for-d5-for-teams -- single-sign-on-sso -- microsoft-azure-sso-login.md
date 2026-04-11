# Microsoft Azure SSO Login

> ℹ️ > ****SSO**** feature requires a whitelist for activation and is intended for enterprise clients.

> ****Note:****
>
> To activate this feature, please get in touch with the relevant sales representative or customer success manager ([[email protected]](https://docs.d5render.com/cdn-cgi/l/email-protection)), and provide the team owner's account.

## Microsoft Azure SSO (SAML) Setup Guide

### 1. Prerequisites

- The user must have a ****Microsoft Azure account**** for their company
- After logging in, go to the ****“Enterprise Applications”**** page

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FP3iv2oNcrbjgHRl5WysH%252Fimage.png%3Falt%3Dmedia%26token%3D3fa66511-8319-4796-b074-282e48443a86&width=768&dpr=3&quality=100&sign=d3eab27b&sv=2)

---

### 2. Create an Application

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F4N3d44XeoeZQ6A4yB7Rr%252Fimage.png%3Falt%3Dmedia%26token%3Dc7678672-ef23-4119-b2af-d1d681d9bcec&width=768&dpr=3&quality=100&sign=9b0b1d26&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FVaFmaBbpns2B4nt9I294%252Fimage.png%3Falt%3Dmedia%26token%3D4dab0565-dca0-4a44-9698-3908f95ad09e&width=768&dpr=3&quality=100&sign=ac7c1d6e&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FC3wdk1Ht7jb2tRIxkvDf%252Fimage.png%3Falt%3Dmedia%26token%3Db2ecbfcc-4ba4-4faa-ae77-5ef95d7910b0&width=768&dpr=3&quality=100&sign=80ccb5ca&sv=2)

---

### 3. Permission Requirements

- Only ****Team Owners**** or ****Super Team Admins**** have access to the SSO configuration page

---

### 4. SSO Configuration Details

#### ****1. Enable SSO****

- SSO is ****disabled by default****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQjrxO4q7FlhHpvdzEhLG%252Fimage.png%3Falt%3Dmedia%26token%3D04d23d77-fe4f-4498-927d-2264b648cfaf&width=768&dpr=3&quality=100&sign=a821e9a1&sv=2)

#### ****2. Configuration Item Details****

****✅ Identity Provider (IdP)****

- Currently, ****only Microsoft Entra**** is supported

****✅ SSO Protocol****

- Currently, only ****SAML**** is supported

****✅Login Method Options****

There are ****two options**** for how users log in:

Users can log in using either SSO or their account credentials.

Users can only log in via Single Sign-On; password login will be disabled.

****✅Add Domain(s)****

- Enter ****your company email suffixes**** (e.g., `yourcompany.com`)
- ****Multiple domains**** can be added

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FiNnjhX0Xl7hVaNuASDm9%252Fimage.png%3Falt%3Dmedia%26token%3Df075b8a8-d9d0-4e60-9792-1ecd42ffa328&width=768&dpr=3&quality=100&sign=e37b34f3&sv=2)

****✅ Service Provider (SP) Configuration****

- ****Recommended method:****

a. Download the XML file from the D5 Team Management backend

b. In the Azure portal, open the SSO configuration module and go to ****“Set up Single Sign-On”****

c. Click ****“Upload metadata file”**** and import the downloaded XML file

- ****Manual method:****

  a. In Azure’s “Basic SAML Configuration” section, manually fill in the following:

- Copy the ****Identifier (Entity ID)**** from the D5 backend and paste it into the corresponding field

- Copy the ****Assertion Consumer Service URL (ACS URL)**** and paste it accordingly

b. Click “Save” to apply

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FrIigU3QRCCu9lECjlcQn%252Fimage.png%3Falt%3Dmedia%26token%3D81dd6c96-0b6a-4272-bd32-a1959d64a64e&width=768&dpr=3&quality=100&sign=ec5566d7&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fq3LxaJZU7FhvX5OXk8mh%252Fimage.png%3Falt%3Dmedia%26token%3D6b2d0d26-57e6-4d5e-bfda-ecb244a4971e&width=768&dpr=3&quality=100&sign=7d655f6e&sv=2)

****✅ Identity Provider (IdP) Information****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FmF9aApPD483ekUzeJsPW%252Fimage.png%3Falt%3Dmedia%26token%3D3582700d-6ebb-4b92-8c96-b4a88cca937c&width=768&dpr=3&quality=100&sign=1778d5ac&sv=2)

## Microsoft Azure SCIM Configuration Guide

### 1. Setup in D5 Myspace - Team Management Backend

Enable Provisioning

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FaRq9GbbBBhPMUk4AS7ow%252Fimage.png%3Falt%3Dmedia%26token%3Dc5fe788a-69ae-4619-8a86-ac4a7d16c4bc&width=768&dpr=3&quality=100&sign=2ce4bab6&sv=2)

---

### 2. Setup in Microsoft Azure

- Go to ****Enterprise Applications > SSO Control Module > Provisioning****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FI8XHvFmf0eoiBEqh84Gz%252Fimage.png%3Falt%3Dmedia%26token%3Dc19869ba-e804-4e2d-b9c4-24f8473b70d7&width=768&dpr=3&quality=100&sign=fe6e3295&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FnLxXKS0pJSZPVGNyf7U9%252Fimage.png%3Falt%3Dmedia%26token%3D9aa689dc-1d66-4886-86d3-09de36fbbae4&width=768&dpr=3&quality=100&sign=b82a082c&sv=2)

- Click ****Add a new configuration****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FO1tfLhN63YhE4X8SzuTb%252Fimage.png%3Falt%3Dmedia%26token%3D1beb3209-80b2-426c-a6e7-f4601a29190a&width=768&dpr=3&quality=100&sign=6a95523b&sv=2)

- Enter the ****SCIM endpoint and access token**** provided in the D5 Team Management Backend. Click ****Test Connection****, and after the test is successful, click ****Create****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FeR6B7UJ059Q0QoFB1d5n%252Fimage.png%3Falt%3Dmedia%26token%3Db7893f3c-498a-4fb2-ab3b-bfc10a89cce8&width=768&dpr=3&quality=100&sign=65cb23d0&sv=2)

- Click ****Settings****, enable the provisioning switch, and click ****Save****.

> 💡 If the access token changes in the future:
>
> - Navigate to ****Provisioning > Settings > Admin Credentials****
> - Set the ****Provisioning Status**** to ****On****
> - Click ****Save****
> - Finally, ****enable provisioning**** to sync user accounts

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FAJvZoO3LG1COk1gw19vk%252Fimage.png%3Falt%3Dmedia%26token%3Db4e53585-8870-4dde-be73-c2063a3d8fab&width=768&dpr=3&quality=100&sign=902e110&sv=2)

- Click ****Mappings****, then select ****Provision Microsoft Entra ID Users****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FvEDMoIMWEVqbT0jmFHeD%252Fimage.png%3Falt%3Dmedia%26token%3D8e2f9485-f267-4ef2-a175-1443843f1245&width=768&dpr=3&quality=100&sign=8c8819d0&sv=2)

- On the attribute mapping page, click ****Add New Mapping.****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSZ0nZZkIFsjNDlIqjX6t%252Fimage.png%3Falt%3Dmedia%26token%3Deaaeed11-3bb6-461b-ab1b-6313b59f10c9&width=768&dpr=3&quality=100&sign=7ebb6471&sv=2)

- Configure the new mapping with the following steps. After completing the configuration, click ****Save:****

> - Set ****Mapping type**** to ****Expression****
> - Enter the following ****Expression:**** `SingleAppRoleAssignment([appRoleAssignments])`
> - Set ****Target attribute**** to `roles[primary eq "True"].value`
> - Set ****Match objects using this attribute**** to ****Yes****
> - Set ****Matching precedence**** to ****2****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFKVAk3WEhgxwAEyLaCG4%252Fimage.png%3Falt%3Dmedia%26token%3Dd995d0b0-fdf6-4200-a5de-14a75f810990&width=768&dpr=3&quality=100&sign=1ebb3c81&sv=2)

- Return to the attribute mapping page and click ****Save.****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FF9tlmeHboP0PguTtsJ8y%252Fimage.png%3Falt%3Dmedia%26token%3D96216c0c-8512-4ff1-a48e-3b5aab3e48b9&width=768&dpr=3&quality=100&sign=bcd08b3c&sv=2)

- Return to the ****Overview (Preview)**** page to confirm whether provisioning has started. If it hasn't, click ****Start Provisioning.****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FS8JHDBhqOt6WUjVsTfLt%252Fimage.png%3Falt%3Dmedia%26token%3D1786991a-d9a2-4cbd-893b-c592e85f5e65&width=768&dpr=3&quality=100&sign=7a08225&sv=2)

---

### 3. Creating Application Roles

- Go to ****Enterprise Applications > SSO Control Module > Properties****
- Click ****“App Registrations”****
- After entering, go to the ****“App Roles”**** section
- You can ****add new roles**** here as needed

> ⚠️ If no roles are configured, synced users will default to ****Team Member**** role

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSlhLZSTBXaR3c3imrm3a%252Fimage.png%3Falt%3Dmedia%26token%3D6cc3ca59-61ed-435b-b5b2-d55bff02c4e2&width=768&dpr=3&quality=100&sign=11ed41bf&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FjXVLVmJgPhebfb1Z97QW%252Fimage.png%3Falt%3Dmedia%26token%3D0b04ef38-4828-473b-aa9c-30493f078676&width=768&dpr=3&quality=100&sign=5f6f4a41&sv=2)

---

### 4. Start provisioning

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FXe3DPYsmPC8otuwzSeAo%252Fimage.png%3Falt%3Dmedia%26token%3Dbaa7d3b9-536b-48de-aa10-43b7768101a6&width=768&dpr=3&quality=100&sign=5a6a9ca0&sv=2)

### 5. SCIM Sync Behavior

- When ****SCIM is enabled,**** the following features will be ****disabled**** in the D5 Team Management Backend:

  - Manually ****editing team member roles****
  - ****Modifying member account attributes****
  - ****Inviting users to the team****
  - ****Removing members from the team****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FVvazWYc1OpA8dIYZl3eD%252Fimage.png%3Falt%3Dmedia%26token%3D7ddcac59-6860-438e-95a9-832cd86040ea&width=768&dpr=3&quality=100&sign=edb3f1bd&sv=2)

- In ****Group Management****, the following options will also be hidden:

  - ****Invite to Team****
  - ****Remove from Team****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8PCl09RMVgllLFc0Jokx%252Fimage.png%3Falt%3Dmedia%26token%3Df4d78b95-8672-4d1a-9a1e-55e971216651&width=768&dpr=3&quality=100&sign=8f5dad12&sv=2)

- Sync Status and Frequency

  - ****Sync Frequency:**** Once every ****40 minutes****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FcnYr6tT1kyiNaenNuzxP%252Fimage.png%3Falt%3Dmedia%26token%3D2cc84522-8d0f-4cda-8c60-1fbfb7482f6a&width=768&dpr=3&quality=100&sign=78c9d4&sv=2)

- ****View Sync Results:****

  - In the Azure backend, click on sync logs
  - You can see ****each step of the sync**** and any ****failure reasons****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJA32YpviiN4JOmUXQWCf%252Fimage.png%3Falt%3Dmedia%26token%3D5a6fb86a-af3b-4e67-8131-c49ca3f62aff&width=768&dpr=3&quality=100&sign=df149199&sv=2)

Example Case

- A new user is added in the IdP (who has ****never registered**** in D5)
- After waiting for the sync cycle, the user will automatically appear in the team

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFnuuft3EXlRw4SNmCidQ%252Fimage.png%3Falt%3Dmedia%26token%3D94db4277-d84b-4506-9c76-c964d0f37c40&width=768&dpr=3&quality=100&sign=68277334&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fg21RqS7zzaASaSP66xbY%252Fimage.png%3Falt%3Dmedia%26token%3D06ddcdb6-ef9c-491d-b667-b19212897bd6&width=768&dpr=3&quality=100&sign=e092321&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FPYc8RZ4yg28AIrtUSHiQ%252Fimage.png%3Falt%3Dmedia%26token%3D51dd4488-00b9-4203-9412-eb598522c663&width=768&dpr=3&quality=100&sign=79a5b774&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FvjRfbR0nWrq1WPJJ2IAV%252Fimage.png%3Falt%3Dmedia%26token%3Dc8cf96cc-377a-4b21-99cd-a7cb4dce4f09&width=768&dpr=3&quality=100&sign=77efe853&sv=2)

---

### 6. Sync Failure Scenarios

- ****Team Seat Limit Reached****

If an existing D5 account is being synced while the team's seat quota is full, the sync will fail, and the account will ****not be added to the team.****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fh6IFNBUKnPOlVRv07fVr%252Fimage.png%3Falt%3Dmedia%26token%3D6c2c22f8-cd08-4a4d-806d-10f269c0fd6b&width=768&dpr=3&quality=100&sign=1381509a&sv=2)

- ****Backend Deployment in Progress****

If the D5 backend is undergoing a release during the sync process,the sync will fail.

The account will ****not be created nor added to the team.****

It will be retried in the ****next scheduled sync.****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fqp7kKRqS6a6D48wps3BB%252Fimage.png%3Falt%3Dmedia%26token%3D9e63b296-7be2-4d0a-87b1-26a40b42761b&width=768&dpr=3&quality=100&sign=731e638&sv=2)