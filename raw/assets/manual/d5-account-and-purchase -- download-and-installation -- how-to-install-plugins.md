# How to install plugins?

> It is currently supported for users to install the online version of ****D5 LiveSync plugins**** using silent installation mode through the command line.

## Method 1: Install using installation packages

### 1. Download the plugin

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fdl6VsXi7tCEZb3ElYwPq%252Fimage.png%3Falt%3Dmedia%26token%3D153a2174-2b23-416d-967d-07bc33c4e201&width=768&dpr=3&quality=100&sign=c559f691&sv=2)

### 2. Launch the file

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FegZGTaKT1tJ1rxnXQNVa%252Fimage.png%3Falt%3Dmedia%26token%3Dc646f1e7-0409-4e09-b188-55eccd1ef369&width=768&dpr=3&quality=100&sign=3dd03946&sv=2)

### 3. Tick the corresponding DCC version

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FWn0LzZmLwSDqq8WXZKEH%252Fimage.png%3Falt%3Dmedia%26token%3De732d6ba-f254-457f-89ba-a9903eccd1a8&width=768&dpr=3&quality=100&sign=f94b1eb&sv=2)

### 4. Start the installation

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FK3kEr1ByutPI8kh56ZMP%252Fimage.png%3Falt%3Dmedia%26token%3Daecce3bd-a691-43dc-aabf-8e03fd4b0ca0&width=768&dpr=3&quality=100&sign=35fa0c2c&sv=2)

### 5. Complete the installation

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fq7G72TFwLWpchLUFm7a2%252Fimage.png%3Falt%3Dmedia%26token%3Dd28285b1-c67f-4340-a5f8-8f1730ac5527&width=768&dpr=3&quality=100&sign=72cac4a6&sv=2)

## Method 2: Silent Installation (command line)

### 1. Download the plugin

### 2. Open Windows Command Prompt

Enter CMD in the Windows search bar and select ‘Run as administrator’ to open the Command Prompt.

### 3. Utilize the "cd" command in the command line to navigate the directory containing the plugin installation package (.exe file).

> E.g. If the plugin installation package is located under the path ****C:\Users\User\Desktop****, we can type `cd C:\Users\User\Desktop` and then Enter.

### 4. Enter the name of the plugin installation package (.exe file) and add the extension

> E.g. `D5_LiveSync_Sketchup_usa_latest.exe`

### 5. Enter the installation instructions on the command line

Paste the command `/sp- /silent /allusers /norestart` OR `/sp- /silent /currentuser /norestart` after the plugin extension.

> E.g.
> In the image below, use the command line to install the D5 LiveSync for SketchUp, the download location of the plugin is at ****C:\Users\Administrator\Downloads****

### 6. Click Enter to start the silent installation

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FU6Sl2wV1oCo45RIvtaSR%252Fcde2af069b7ffb652e56be8f68946606.png%3Falt%3Dmedia%26token%3D3cf2532b-a81a-480b-8f8a-bcfb0c42bcb8&width=768&dpr=3&quality=100&sign=7ba86609&sv=2)

## FAQs

### Q1. Why does it prompt 'please install the latest version of D5 Render, if you have already installed the latest version'?

If you encounter this error, please check if you have installed only D5 Converter but have not installed D5 Render.

The D5 Converter is a bridge plugin between the modeling software and the D5 Render. If you want the run the plugin, please install D5 Render first.

If you want to download D5 Render, please go to the official website. <https://www.d5render.com/?_sasdk=fZ2xvYmFsXzExMDM4Nw>