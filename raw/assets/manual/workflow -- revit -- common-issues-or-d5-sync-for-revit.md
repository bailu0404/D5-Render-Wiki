# Common issues | D5 Sync for Revit

### 1.Why the relevant parameters in the D5-Revit plugin settings shown in gray?

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FzLfeEpfSh2OEmnF0lO0M%252Fimage.png%3Falt%3Dmedia%26token%3D55b9f63c-f937-4860-8567-b268328ac4c1&width=768&dpr=3&quality=100&sign=b259287&sv=2)

Settings shown in gray

Please check whether you are currently using D5-Revit plugin for linkage operation. Generally, it does not support the modification of relevant parameters during linking, so the display is grayed out. After linking, you can adjust the relevant parameters normally.

### 2.Pop-up prompt after launching D5 Converter "Rendering is currently not supported in the running instance of Revit". Or "Rendering features are currently disabled. You must install the Rendering library to use rendering features".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FR7heSUC0BOKCZUyMkZQK%252Fimage.png%3Falt%3Dmedia%26token%3Df7bbc0b2-75bc-417d-a181-0b61c1dd6a19&width=768&dpr=3&quality=100&sign=f24d447e&sv=2)

After launching the D5 Converter

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FCAl4qnCbNEO17YGrZKFs%252Fimage.png%3Falt%3Dmedia%26token%3D6549b164-1b2c-4f42-9f58-d87e5531d4d8&width=768&dpr=3&quality=100&sign=f8c1e0e5&sv=2)

Prompted after launching Revit

Reason: Material Library is not installed correctly.

Solution: Uninstall and reinstall Autodesk Material Library.

For details, please refer to: <https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Rendering-features-are-currently-disabled-You-must-install-the-Rendering-library-to-use-rendering-features.html>