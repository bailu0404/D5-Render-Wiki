# How to install D5 Render?

## Download and Installation

The latest version can be downloaded from the [official website](https://d5render.com/), or directly by clicking the link below.

> The default installation directory for the ******D5 Render****** is on the C drive, and user-selected custom installation directories are supported. ******D5 Launcher****** is not supported to change installation directory.

The downloaded file is named ****D5DeployTool****; double-click it to install. D5 Launcher is ticked by default and must be installed; D5 Render can be installed optionally.

- ****D5Launcher-windows-x.x.x.xxxx.exe:**** Used for the unified management of D5 Render, potential future products, and project files.
- ****D5\_Render\_installer-x.xx.xx.xxxx.exe:**** The D5 Render client.
- ****D5DeployTool-windows-x.x.x.xxxx.exe:**** The installation management tool.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FApR7iaDxQROQBfatdJn4%252Faf56f80e5015390a23141be1c5173e9c.png%3Falt%3Dmedia%26token%3D110a9442-d47a-4ee2-b5fd-8227a0b8a88c&width=768&dpr=3&quality=100&sign=289a646a&sv=2)

D5DeployTool---D5 Render&D5 Launcher

> ℹ️ > By default, the software will download assets in the installation path, and after the installation is complete, it supports migrating assets to a custom directory in the Preferences. If you do not want to migrate assets, it is recommended to reserve a larger installation space.

## Hardware Check

After the software is installed and launched for the first time, we will perform a hardware check to ensure that your hardware and system configuration are up to standard for a smooth rendering experience.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkYCL5-EOpM5NPyHBtB%252F-MkYHWDSg4C2h9Zn5Uw4%252FScreenshot%25202021-09-27%2520020639.png%3Falt%3Dmedia%26token%3D32100508-d2c0-4e60-9696-ce705fbd6757&width=768&dpr=3&quality=100&sign=36ce419f&sv=2)

- View [System Requirement](https://docs.d5render.com/getting-started/quick-start#system-requirement)

## Silent Installation (CMD Installation)

### ****1. Download**** installation files****:****

Download all files required for silent installation and place them in the same folder.

- ****Download link:****

Option 1: Download files together- [****D5 Deployment Kit****](https://usa.api.d5render.com/d5-admin/sl/Ht9KVeQ4) (A zip file containing D5 Launcher, D5 Render and D5DeployTool)

Option 2: Download them separately- [****D5 Launcher****](https://usa.api.d5render.com/d5-admin/sl/LsY4vDq8)****,**** [****D5 Render****](https://usa.api.d5render.com/d5-admin/sl/TO81V9bi)and[****D5DeployTool****](https://usa.api.d5render.com/d5-admin/sl/Qp7bLmA2)

- ****What are they for?****

  - ****D5Launcher-windows-x.x.x.xxxx.exe:**** Used for the unified management of D5 Render, potential future products, and project files. ****(Required)****
  - ****D5\_Render\_installer-x.xx.xx.xxxx.exe:**** The D5 Render client. ****(Required)****
  - ****D5DeployTool-windows-x.x.x.xxxx.exe:**** The installation management tool.

> ⚠️ > ****Note:****

If you also need to install DCC LiveSync plugins suited to your workflow, please visit the official website to download the corresponding plugins and follow the instructions in [****Section 2.4****](https://docs.d5render.com/d5-account-and-purchase/download-and-installation/how-to-install-d5-render#id-2.4-example-2-install-d5-launcher-d5-render-and-dcc-livesync-plugins) to install them.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F2y0MN16UTSO7XPhrzOBs%252Fimage.png%3Falt%3Dmedia%26token%3D298e53a1-1954-4a25-af30-57aba54a3c9d&width=768&dpr=3&quality=100&sign=aadf29e9&sv=2)

Example

### 2. ****Silent Installation****:

#### ****2.1 Command Line Arguments****

Required Arguments

`--agreeEula=true`

Agrees to the End User License Agreement (EULA).

`--launcherPath="path"`

Replace `path` with the file path of `D5Launcher.exe`

`--renderPath="path"`

Replace `path` with the file path of `D5Render.exe`.

`--installPath="path"`

Replace `path` with the custom installation path for D5 Render. (Note: Custom path is not supported for D5 Launcher).

Optional Arguments

`--pluginPath="path"`

Replace `path` with the file path of the D5 DCC LiveSync plugin installer (see [Section 2.4](https://docs.d5render.com/d5-account-and-purchase/download-and-installation/how-to-install-d5-render#id-2.4-example-2-install-d5-launcher-d5-render-and-dcc-livesync-plugins)).

`--logDirPath="path"`

Replace `path` with the custom output path for installation logs. If not specified, the default is `%TEMP%/D5Deploy/`.

`--isForCurrentUser=true/false`

Specifies whether to install for the current user only. Defaults to `true` if not specified.

`--workspacePath="path"`

Replace `path` with the custom D5 Workspace path.

**(The "Workspace" function supports setting the storage location for all online library assets, local library assets, custom HDR/LUT/IES files, and some temporary files).**

If not specified, a "D5 Workspace" folder will be created by default on the drive with the most available space. During an overwrite installation, the existing workspace path will be used.

`--configPath="path"`

Replace `path` with the file path of the `.ini` configuration file to execute the installation based on its content (see [Section 2.5](https://docs.d5render.com/d5-account-and-purchase/download-and-installation/how-to-install-d5-render#id-2.5-example-3-install-using-an-.ini-configuration-file)).

#### ****2.2 Start Installation****

> ****Note:**** Replace `X:\...\` with the actual directory path where you downloaded ****the D5 DeploymentTool**** in [Section 1,](https://docs.d5render.com/d5-account-and-purchase/download-and-installation/how-to-install-d5-render#id-1.-download-installation-files) and replace `D5DeployTool-windows-x.x.x.xxx.exe` with the actual filename of the deployment tool (filenames may vary by version).

#### ****2.3 Example 1: Install D5 Launcher and D5 Render Only****

Enter the following command in the Command Prompt to install D5 Launcher and D5 Render. (Replace the paths, filenames, and secret key with your actual data).

****Install D5 Launcher and D5 Render Only ↓****

#### ****2.4 Example 2: Install D5 Launcher, D5 Render, and DCC LiveSync Plugins****

> ⚠️ > To install DCC LiveSync plugins (such as SketchUp, Revit, or Rhino plugins) simultaneously, please first download the corresponding plugin installers from the ****Workflow**** page on the official [D5 Render website](https://www.d5render.com/).

Enter the following command in the Command Prompt to install D5 Launcher, D5 Render, and the selected plugins. Multiple plugins can be installed at once. **(Replace the paths, filenames, and secret key with your actual data).**

****Install D5 Launcher, D5 Render, and DCC LiveSync Plugins ↓****

#### ****2.5 Example 3: Install Using an .ini Configuration File****

The tool supports `.ini` configuration files, allowing you to store all parameters in a single file for deployment.

****Example of .ini ↓****

Enter the following command in the Command Prompt to install using the configuration file: **(Replace the path and filename with your actual data).**

> ❌ > ****Note:****

In the ****config.ini**** file above, you must use two backslashes: ****\\****

****Install Using an .ini Configuration File ↓****

#### ****3. Batch Installation****

You can use your preferred batch deployment tool to execute the mass installation using the commands described above. If you require assistance, please contact our sales team.

---

## ****Silent Update****

To upgrade, simply download the newer installer and run the silent installation command using the same installation directory as before, but omit the **-workspacePath** parameter. This will perform an in-place upgrade. Example:

> ℹ️ > ****Note:****

Please replace D5\_Render\_installer-2.x.x.xxxx.exe with the name of the software programme which corresponds to the update downloaded.

---

## ****Silent Uninstallation****

To uninstall D5 Render silently, use the following command:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7TXgz9mi6KQrva4hepdj%252Fimage.png%3Falt%3Dmedia%26token%3D60b0eb29-fd2d-4744-9f45-0febc20615e8&width=768&dpr=3&quality=100&sign=ccc9ef75&sv=2)

## Note:

(1) Ensure that you have downloaded the appropriate version of D5 Render (e.g., v2.9.5 or higher).

(2) Note: On Windows, backslashes \ in command-line arguments are treated as escape characters. Handle this by enclosing file paths in double quotes and using / instead of \ . For example, "C:/Program Files/D5 Render".

(3) If using the parameter "**-isForCurrentUser=false**" to install for all users, you must run the script or command as an administrator; otherwise, the installation may fail.

(4) Before actual deployment, run a silent installation in a test environment to ensure it executes correctly.

(5) Remember to back up user configurations and settings to avoid data loss during installation or uninstallation.