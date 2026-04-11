# Okta SSO Login

> ℹ️ > ****SSO**** feature requires a whitelist for activation and is intended for enterprise clients.

> ****Note:****
>
> To activate this feature, please get in touch with the relevant sales representative or customer success manager ([[email protected]](https://docs.d5render.com/cdn-cgi/l/email-protection)), and provide the team owner's account.

## Prerequisites

- An account with ****Okta administrator privileges**** is required.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fva054tSzRHUACApLx5zi%252Fimage.png%3Falt%3Dmedia%26token%3Dc6964da7-a3f6-4270-8ed0-1958f8a568e3&width=768&dpr=3&quality=100&sign=db92696c&sv=2)

- In ****Directory**** → ****Groups****, create the following ****three groups**** (names must match exactly):

  - `d5-superAdmin`
  - `d5-admin`
  - `d5-member`

User roles within the team will be assigned based on the group they belong to.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FDzKtVLZ5cZhTJhPlsx3I%252Fimage.png%3Falt%3Dmedia%26token%3D2ef32aa4-4290-4c7e-b959-9579b24cc39d&width=768&dpr=3&quality=100&sign=57350b8b&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSTJQbIbsnvYEa1WTRpKM%252Fimage.png%3Falt%3Dmedia%26token%3Dd2a1a007-89d9-41c0-9674-ed57c621c742&width=768&dpr=3&quality=100&sign=d344586&sv=2)

---

## Configure SAML in Okta

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FUUDPLqHzXCFfqny93dwT%252Fimage.png%3Falt%3Dmedia%26token%3Dddbb0d73-5386-4541-a099-23296a3469d9&width=768&dpr=3&quality=100&sign=963891aa&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7MP5U3vdcFidLdSRRYmA%252Fimage.png%3Falt%3Dmedia%26token%3Da16e798c-0993-455f-99ba-579ae6f67fe7&width=768&dpr=3&quality=100&sign=282c6aad&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FVCTOov8f5TNz4yyiIGyC%252Fimage.png%3Falt%3Dmedia%26token%3D3654b1e3-3935-48ae-bdc8-ca46403abc1f&width=768&dpr=3&quality=100&sign=d41d76cb&sv=2)

- ****Name ID format:**** `EmailAddress`
- ****Application username:**** `Okta username`

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FdEySJkjr3EpN3UZZA0uu%252Fimage.png%3Falt%3Dmedia%26token%3D02b43130-37f5-40fd-9ee6-26ba9f95b4e0&width=768&dpr=3&quality=100&sign=eefb6b55&sv=2)

D5-Myspace-TeamDashboard

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FdetHuLhvpXbqBqvxlIux%252Fimage.png%3Falt%3Dmedia%26token%3D1d2778ba-30be-4c06-9291-9f3e45eab0f0&width=768&dpr=3&quality=100&sign=d9431524&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FfwVvkU48olbtXd1Y3VMo%252Fimage.png%3Falt%3Dmedia%26token%3D5a2a0cf4-5a64-407c-818c-883635da07cb&width=768&dpr=3&quality=100&sign=8c10c6a7&sv=2)

Okta

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F1u46Bhj7L0oJfTpOlb6l%252Fimage.png%3Falt%3Dmedia%26token%3D2479c720-693c-4d8b-9ed1-184be9862a94&width=768&dpr=3&quality=100&sign=eff9738&sv=2)

---

## ****Okta → D5-Myspace Team Management Backend****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F39eQpJbRHVMuRLQjynXw%252Fimage.png%3Falt%3Dmedia%26token%3D9ca17eba-e4c3-4d7b-b725-a5b08dfbdb59&width=768&dpr=3&quality=100&sign=5992df08&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FtytMcvX4GoPGcgWToet7%252Fimage.png%3Falt%3Dmedia%26token%3Df15a6ea7-6f48-4ac3-97a2-e9aa3646137e&width=768&dpr=3&quality=100&sign=83092c01&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7tiQNN6hRczmGTUJKdJT%252Fimage.png%3Falt%3Dmedia%26token%3D7d4a7399-3ffe-46bc-9ef6-98e1910bfd70&width=768&dpr=3&quality=100&sign=924f06cf&sv=2)

---

## Configure SCIM in Okta

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FhyiSDMhxKDtNwI5K9KzL%252Fimage.png%3Falt%3Dmedia%26token%3Ddd5bbe33-6f4f-499b-9cf6-b1cc57a5a5e9&width=768&dpr=3&quality=100&sign=c8e5847e&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FWDVxRZg6KNZcx7PFCs5X%252Fimage.png%3Falt%3Dmedia%26token%3Decfaf508-b722-4b96-94ac-d727106bfb64&width=768&dpr=3&quality=100&sign=cd54fef4&sv=2)

#### Provisioning Settings

In ****Provisioning**** → ****Edit****, update the following settings and save:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FmCWeTFPluu7h8NXlrxCZ%252Fimage.png%3Falt%3Dmedia%26token%3D5254adec-0c92-4f79-b964-c79c103a2070&width=768&dpr=3&quality=100&sign=dd26b2a6&sv=2)

- ****SCIM connector base URL****
  Copy from:
  `D5-Myspace Team Admin → SSO & Provisioning → Provisioning Management → SCIM Endpoint`

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FnF1pD0Wu146VfIRHHLc5%252Fimage.png%3Falt%3Dmedia%26token%3Df21b1a8b-20c9-481a-afa8-5161b9f9c274&width=768&dpr=3&quality=100&sign=ad340e43&sv=2)

- ****Unique identifier field for users****
  `userName`
- ****Supported provisioning actions****
  Enable the ****first four options****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FiDPFeoBogiti2iUH8FMQ%252Fimage.png%3Falt%3Dmedia%26token%3D2f8df4cb-b5e1-4cd0-90a0-ee3f5718aa2c&width=768&dpr=3&quality=100&sign=98402943&sv=2)

- ****Authentication Mode****
  `HTTP Header`
- ****Authorization****
  Copy the ****Access Token**** from:
  `D5-Myspace Team Admin → SSO & Provisioning → Provisioning Management`
- To App
  Click ****Edit****, enable the ****first three options****, and save.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FzEVuuSWevLAVmtGC14dg%252Fimage.png%3Falt%3Dmedia%26token%3D6a939860-d144-4d54-959b-4d673d7651bb&width=768&dpr=3&quality=100&sign=8a8cd5d8&sv=2)

- ****D5-SSO Attribute Mappings****
  Keep only the required mappings and delete the rest.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFnt3zcabYFXQgCNEfHwG%252Fimage.png%3Falt%3Dmedia%26token%3D4d861c13-2e63-4628-86a8-9d29aaf5b555&width=768&dpr=3&quality=100&sign=41f660d1&sv=2)

#### Push Groups

- Go to Push Groups and add the following three groups:

  - `d5-superAdmin`
  - `d5-admin`
  - `d5-member`

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fl7nVF4tuSaHOirAjh6di%252Fimage.png%3Falt%3Dmedia%26token%3Df91abc1a-7737-4aff-bf01-a1f27602392b&width=768&dpr=3&quality=100&sign=df091a3&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fz6DZTXIbQrxWIOwTcUB5%252Fimage.png%3Falt%3Dmedia%26token%3D4a26967a-670e-4e1b-81d3-7cb1b86cfb7a&width=768&dpr=3&quality=100&sign=da5d9845&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FAc6pH51mZw9kdAO6lOTi%252Fimage.png%3Falt%3Dmedia%26token%3Df6fb81c9-084a-49ec-90de-1f2b2d9d7839&width=768&dpr=3&quality=100&sign=a91c94f4&sv=2)

#### Assignments

- Go to ****Assignments**** and add the users who will log in via SSO.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F0dgZj8ZPzpP6MLU6i6id%252Fimage.png%3Falt%3Dmedia%26token%3Dea8d61dc-3d75-40ef-aca0-572ca12763de&width=768&dpr=3&quality=100&sign=decaca16&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FWmjR6gBadyO0rIi49WA3%252Fimage.png%3Falt%3Dmedia%26token%3Dc78bd8ed-7a69-4feb-a9e7-68bf62bb305e&width=768&dpr=3&quality=100&sign=48ebc624&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fr2nLVbSeQvGC97g295Zr%252Fimage.png%3Falt%3Dmedia%26token%3De59674dc-a1b5-4585-96f6-78064bf3cd70&width=768&dpr=3&quality=100&sign=97d986f5&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FEx0jRdB4i8kNyj4QGnrn%252Fimage.png%3Falt%3Dmedia%26token%3Dabf924e2-20eb-498e-8410-024c2f704e3a&width=768&dpr=3&quality=100&sign=da16546e&sv=2)

---

## D5-Myspace SSO Configuration

#### Access Control

- The configuration page is visible ****only if****:

  - The team is on the ****whitelist****, and
  - The logged-in user is the ****team owner**** or a ****super admin****
  - SSO is ****disabled by default****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FyfzkTnaNIg8KgjMTBgga%252Fimage.png%3Falt%3Dmedia%26token%3D842b232c-60aa-40a0-b5c9-1086f707325b&width=768&dpr=3&quality=100&sign=de03f1a8&sv=2)

#### Whitelist Behavior

- If ****SSO & SCIM**** are enabled and the team is removed from the whitelist:

  - All SSO & SCIM settings are automatically disabled.
- After re-adding the team to the whitelist:

  - Users must ****manually re-enable SSO & SCIM****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FfQnPT0KKMFvh6YJNJw14%252Fimage.png%3Falt%3Dmedia%26token%3D324cafc8-2f84-4d22-b9ba-3fb7340b6b27&width=768&dpr=3&quality=100&sign=4971d9a3&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKm6Qz2v75dMgaVcZEKhM%252Fimage.png%3Falt%3Dmedia%26token%3D3e2dab87-d05d-4534-8e77-69495978f68a&width=768&dpr=3&quality=100&sign=6370ff6&sv=2)

#### Configuration Options Explained

- ****Identity Provider****

  - `Microsoft Entra` (default)
  - `Okta`
- ****SSO Protocol****

  - Currently supports ****SAML only****
- ****Login Method****

  - `SSO + Username/Password` (default)
  - `SSO Only`
- ****Domain****

  - Required
  - Leading/trailing spaces are trimmed
  - Domain format validation enabled
  - Max length: 128 characters
  - Domain is saved immediately; domain list may be empty

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F3dUxeALVcgZaP3Yb45yd%252Fimage.png%3Falt%3Dmedia%26token%3D86eb6c68-4a00-422f-a308-a10e0f8bfa10&width=768&dpr=3&quality=100&sign=798f278b&sv=2)

#### Service Provider (SP) Information

- These values are ****fixed****
- Users must manually copy them into the corresponding fields in Okta

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8e7eNZTzq3LyKdT2wx5F%252Fimage.png%3Falt%3Dmedia%26token%3D89629e28-1310-46ed-8130-4476e0a5d1f2&width=768&dpr=3&quality=100&sign=a70986bd&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FkOIQkZY3210xk8cGgUJV%252Fimage.png%3Falt%3Dmedia%26token%3D4fd112db-2016-4807-a3c4-06bdbf5de3dc&width=768&dpr=3&quality=100&sign=e431eef4&sv=2)

#### Identity Provider (IdP) Information

- Upload the `metadata.xml` exported from Okta
- The system will parse it and automatically extract the ****IdP Login URL****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FoV9rXhgWzUVqdzSTajP0%252Fimage.png%3Falt%3Dmedia%26token%3D64f9fced-34c2-43e0-b01e-6b9a33eae0f4&width=768&dpr=3&quality=100&sign=b8644798&sv=2)

---

## D5-Myspace SCIM Configuration

After SAML is successfully configured:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7J2iLY45xXpGsR3WxHcB%252Fimage.png%3Falt%3Dmedia%26token%3Dc6374fad-983b-4edd-8610-600aa01ef3ef&width=768&dpr=3&quality=100&sign=837bf067&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FTuiLB2lSUYy1VTSH3r28%252Fimage.png%3Falt%3Dmedia%26token%3D2d565fdc-5a2f-45d6-8bbf-7792e724a34f&width=768&dpr=3&quality=100&sign=f9444c90&sv=2)

---

## SSO Login Logic & Role Assignment

#### Account Creation

- If the user does ****not exist**** in D5:

  - Create the account and add it to the team
- If the user ****already exists****:

  - Add directly to the team

#### Role Mapping Rules

- No Okta group assigned → role = ****Member****
- Assigned to `d5-superAdmin`

  - If no super admin exists → role = ****Super Admin****
  - If one already exists → role = ****Member****
- Assigned to `d5-admin` → role = ****Admin****
- Assigned to `d5-member` → role = ****Member****
- Assigned to multiple groups → role = ****Member****
- Owner’s role never changes, regardless of group
- Removing a user in Okta → SSO login fails; D5 data unchanged
- Changing Okta group → role does ****not**** change on SSO login
- Seat limit reached → SSO login fails until seats are increased

### Web Login

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLymN0jpOtVPkqrano0bt%252Fimage.png%3Falt%3Dmedia%26token%3D02b12791-0a31-4a72-9839-848c52a1bef5&width=768&dpr=3&quality=100&sign=4b3f971b&sv=2)

#### Enabled SSO

- MySpace validates:

  - Email format
  - Email domain
- Email validity is handled by Okta

  Login methods:

  `SSO + Username/Password`

  - Password, phone, WeChat, Gmail logins still work

  `SSO Only`

  - Personal login still works
  - Switching to ****Team identity**** shows an error
  - Owner is ****not affected****

  `Disabled SSO`

  - Login fails with error: ****“SSO-SAML is disabled”****

### Client Login (D5 Render)

Edge cases:

- Empty input → ****Next**** button disabled
- Unconfigured domain → “SSO login is not configured for this account”
- “Management only” accounts:

  - SSO succeeds
  - User cannot access Showreel features
  - Token is cleared → appears logged out in client

### SCIM Synchronization

- Triggered by events
- Sync completes within ****~5 minutes****

#### SCIM Scenarios

****Assignments changes****

- Removing a user in Okta → user removed from D5 team (except owner)
- Assigning user:

  - No group → Member
  - With group → role based on group
  - Existing admin → role unchanged unless overridden by group

****Group changes****

- Removed from all groups → role becomes Member
- Changed to `d5-superAdmin`

  - If no super admin exists → Super Admin
  - Otherwise → role unchanged
- Multiple groups → role determined by ****last added group****
- Owner role never changes

#### SCIM Restrictions

When SCIM is enabled:

- Disable in D5 backend:

  - Manual role changes
  - Account attribute changes
  - Invite to team
  - Remove from team
- ****Same restrictions apply in Group Management****

#### Seat Limit

- If seats are full:

  - SCIM sync fails in Okta

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLTPNdMLRHtI7jxaphwfD%252Fimage.png%3Falt%3Dmedia%26token%3D9025d5c6-ea2f-44c1-a4e5-f6ffe1df74c0&width=768&dpr=3&quality=100&sign=e0d91168&sv=2)

- After adding seats:

  - Admin must remove failed users from ****Assignments****
  - Re-add them to trigger sync again

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FRSNKJFSZp0HM1HNkYNKC%252Fimage.png%3Falt%3Dmedia%26token%3Dd5a7d55f-942b-42a2-b551-588312f005c0&width=768&dpr=3&quality=100&sign=93a2073e&sv=2)