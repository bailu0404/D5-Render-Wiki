# D5 Lab Version (LAB) Installation Guide

This document provides installation instructions for the Lab License, designed for school IT administrators. This is an initial version, and we will promptly address any issues. Thank you for your support!

## 1. Preparation

> ⚠️ > Before proceeding, please verify with our sales team that your D5 Lab subscription is active.

### 1.1 Log in to the Lab Management Console

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F1vzOi75p8S2pRyxe0JST%252Fimage.png%3Falt%3Dmedia%26token%3Daf70075a-8b68-49cf-bd34-4c2fffa8015b&width=768&dpr=3&quality=100&sign=35dd5faf&sv=2)

### 1.2 Set Your Organization Address

> ⚠️ > If you cannot find your city in the list, please contact our sales team.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FN5MXHYRZAEId5ruj5XQo%252Fimage.png%3Falt%3Dmedia%26token%3D958c7e4a-1646-447d-aea2-4c8059cec5ff&width=768&dpr=3&quality=100&sign=880f01e1&sv=2)

### 1.3 Download installation files

Click `D5 Deployment Kit` ****to download the necessary installation files for the D5 Lab version. Please unzip the downloaded file to extract the following three installation packages:****

- ****D5Launcher-windows-x.x.x.xxxx.exe:**** Used for the unified management of D5 Render, potential future products, and project files. (Required)
- ****D5\_Render\_installer-x.xx.xx.xxxx.exe:**** The D5 Render client. (Required)
- ****D5DeployTool-windows-x.x.x.xxxx.exe:**** The installation management tool.

> ⚠️ > If you also need to install DCC LiveSync plugins suited to your workflow, please visit the official website to download the corresponding plugins and follow the instructions in [****Section 2.4****](https://docs.d5render.com/instruction-for-d5-labversion-lab/download-and-installation#id-2.4-example-2-install-d5-launcher-d5-render-and-dcc-livesync-plugins) to install them.

### 1.4 Retrieve the Installation Secret Key

Before installation, please ensure you have your organization's ****Secret Key**** ready.

## 2. Silent Installation

### 2.1 Command Line Arguments

Required Arguments

`--agreeEula=true`

Agrees to the End User License Agreement (EULA).

`--launcherPath="path"`

Replace `path` with the file path of `D5Launcher.exe`

`--renderPath="path"`

Replace `path` with the file path of `D5Render.exe`.

`--installPath="path"`

Replace `path` with the custom installation path for D5 Render. (Note: Custom path is not supported for D5 Launcher).

`--labSecret=string`

Replace `string` with the installation secret key prepared in the previous step.

Optional Arguments

`--pluginPath="path"`

Replace `path` with the file path of the D5 DCC LiveSync plugin installer (see [Section 2.4](https://docs.d5render.com/instruction-for-d5-labversion-lab/download-and-installation#id-2.4-example-2-install-d5-launcher-d5-render-and-dcc-livesync-plugins)).

`--logDirPath="path"`

Replace `path` with the custom output path for installation logs. If not specified, the default is `%TEMP%/D5Deploy/`.

`--isForCurrentUser=true/false`

Specifies whether to install for the current user only. Defaults to `true` if not specified.

`--workspacePath="path"`

Replace `path` with the custom D5 Workspace path.

**(The "Workspace" function supports setting the storage location for all online library assets, local library assets, custom HDR/LUT/IES files, and some temporary files).**

If not specified, a "D5 Workspace" folder will be created by default on the drive with the most available space. During an overwrite installation, the existing workspace path will be used.

`--useCid=true/false`

Specifies whether to use CID. Defaults to `false` if not specified.
**Please note that** `useCid` **is only used for resolving specific problems. If a device is used by multiple users, please set** `useCid=true`**.**

`--configPath="path"`

Replace `path` with the file path of the `.ini` configuration file to execute the installation based on its content (see [Section 2.5](https://docs.d5render.com/instruction-for-d5-labversion-lab/download-and-installation#id-2.5-example-3-install-using-an-.ini-configuration-file)).

### 2.2 Start Installation

> ****Note:**** Replace `X:\...\` with the actual directory path where you downloaded the D5 Deployment Kit in [Section 1.3](https://docs.d5render.com/instruction-for-d5-labversion-lab/download-and-installation#id-1.3-download-installation-files), and replace `D5DeployTool-windows-x.x.x.xxx.exe` with the actual filename of the deployment tool (filenames may vary by version).

### 2.3 Example 1: Install D5 Launcher and D5 Render Only

Enter the following command in the Command Prompt to install D5 Launcher and D5 Render. (Replace the paths, filenames, and secret key with your actual data).

****Install D5 Launcher and D5 Render Only ↓****

### 2.4 Example 2: Install D5 Launcher, D5 Render, and DCC LiveSync Plugins

> ⚠️ > To install DCC LiveSync plugins (such as SketchUp, Revit, or Rhino plugins) simultaneously, please first download the corresponding plugin installers from the ****Workflow**** page on the official [D5 Render website](https://www.d5render.com/).

Enter the following command in the Command Prompt to install D5 Launcher, D5 Render, and the selected plugins. Multiple plugins can be installed at once. **(Replace the paths, filenames, and secret key with your actual data).**

****Install D5 Launcher, D5 Render, and DCC LiveSync Plugins ↓****

### 2.5 Example 3: Install Using an .ini Configuration File

The tool supports `.ini` configuration files, allowing you to store all parameters in a single file for deployment.

****Example of .ini ↓****

Enter the following command in the Command Prompt to install using the configuration file: **(Replace the path and filename with your actual data).**

> ❌ > ****Note:****

In the config.ini file above, you must use two backslashes: ****\\****

****Install Using an .ini Configuration File ↓****

## 3. Batch Installation

You can use your preferred batch deployment tool to execute the mass installation using the commands described above. If you require assistance, please contact our sales team.