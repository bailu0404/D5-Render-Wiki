# 如何通过命令行安装D5（静默安装）？

方便IT管理员通过脚本进行自动化部署和配置。

# 静默安装

## 1. 获取安装程序

点击[`D5 部署工具`](https://cn.api.d5render.com/d5-admin/sl/Ht9KVeQ4)下载安装D5所需的安装文件。请将下载的.zip文件解压得到以下三个安装包，放在同一个文件夹中。

* **D5Launcher-windows-x.x.x.xxxx.exe**：用于统一管理D5 Render及后续可能推出的其他产品，以及项目文件等，必须安装
* **D5\_Render\_installer-x.xx.xx.xxxx.exe**：渲染器客户端，必须安装
* **D5DeployTool-windows-1.1.0.0076.exe**：安装管理工具

![](https://saas.bk-cdn01.com/t/18217684-957c-4109-9021-5866cc58cc60/u/7531f9aa-9f13-43a5-858c-19dac517bbc6/1768532197152/image.png)示例---将三个安装文件放在“D5 Deployment Kit”的文件夹中提示若您需要同时安装适合您工作流的DCC同步插件，请前往官网下载对应的插件，并按照2.4节的说明进行安装

## 2. 静默安装

### 2.1 命令行参数

|  |  |
| --- | --- |
| **必要参数** |  |
| `--agreeEula=true` | 同意最终用户许可协议 |
| `--launcherPath="path"` | 替换`path`为 *D5Launcher.exe* 文件路径 |
| `--renderPath="path"` | 替换`path`为 D5Render.exe 文件路径 |
| `--installPath="path"` | 替换`path`为自定义 D5 Render 安装路径（D5 Launcher不支持自定义路径） |
| **可选参数** |  |
| `--pluginPath="path"` | 替换`path`为 D5 DCC同步插件 安装文件所在路径(见2.4节) |
| `--logDirPath="path"` | 替换`path`为自定义安装日志输出路径，若不指定则默认为`%TEMP%/D5Deploy/` |
| `--isForCurrentUser=true/false` | 是否仅为当前用户安装 ，若不指定默认为 true |
| `--workspacePath="path"` | 替换`path`为自定义 D5 工作空间路径（“工作空间”功能支持设置全部在线素材库的素材、本地素材库，以及自定义 HDR / LUT / IES 文件和部分临时文件的存储位置），若不指定则默认在剩余空间最大的盘符中创建D5 Workspace文件夹。覆盖安装时则会使用原有的工作空间路径 |
| `--configPath="path"` | 替换`path`为.ini格式配置文件路径并按照配置文件内容进行（见2.5节） |

### 2.2 开始安装

1. 以管理员身份运行命令提示符.2. 输入`"X:\...\D5DeployTool-windows-x.x.x.xxx.exe"` 以及所有必要参数及可选参数后即可开始安装（所有参数之间用空格隔开）替换其中的`X:\...\`为你在第1节下载的 D5 部署工具所在路径，替换`D5DeployTool-windows-x.x.x.xxx.exe`为该部署工具的文件名称（实际名称可能因版本号不同而有所区别）

### 2.3 安装示例1: 仅安装 D5 Launcher 和 D5 Render

在命令提示符窗口内输入以下命令，将安装 D5 Launcher 及 D5 Render（替换其中的路径、文件名、密钥为你的实际内容） **仅安装D5 Launcher和D5 Render↓**`"C:\D5 Deployment Kit\D5DeployTool-windows-1.1.0.0076.exe" --agreeEula="true" --launcherPath="C:\D5 Deployment Kit\D5Launcher-windows-1.1.0.0309.exe" --renderPath="C:\D5 Deployment Kit\D5_Render_installer-2.11.10.1771.exe" --installPath="C:\Program Files\D5 Render"`

### 2.4 安装示例2: 同时安装 D5 Launcher、D5 Render 及 DCC 同步插件

若要同时安装DCC同步插件如SketchUp同步插件、Revit同步插件、Rhino同步插件等，请先前往 [D5 渲染器官网](https://www.d5render.cn/)工作流页面下载对应的插件安装包。在命令提示符窗口内输入以下命令，将安装 D5 Launhcer、 D5 Render 及所选的 DCC 同步插件，多个插件可同时安装（替换其中的路径、文件名、密钥为你的实际内容）**同时安装D5 Launcher、D5 Render及DCC 同步插件↓**`"C:\D5 Deployment Kit\D5DeployTool-windows-1.1.0.0076.exe" --agreeEula="true" --launcherPath="C:\D5 Deployment Kit\D5Launcher-windows-1.1.0.0309.exe" --renderPath="C:\D5 Deployment Kit\D5_Render_installer-2.11.10.1771.exe" --installPath="C:\Program Files\D5 Render" --pluginPath="C:\DCC\D5_LiveSync_Sketchup_usa_1.6.1.0020.exe" --pluginPath="C:\DCC\D5_Live_Sync_Rhino_usa_1.1.2.0005"`

### 2.5 安装示例3:使用.ini配置文件进行安装

支持 .ini 格式配置文件，你可以将所有参数存储在文件中进行部署。**配置文件实例（config.ini）↓**`[InstallConfig]
agreeEula=true
launcherPath="C:\\D5 Deployment Kit\\D5Launcher-windows-1.1.0.0309.exe"
renderPath="C:\\D5 Deployment Kit\\D5_Render_installer-2.11.10.1771.exe"
pluginPath1="C:\\DCC\\D5_LiveSync_Sketchup_usa_1.6.1.0020.exe" //注意：此处参数名带有序号，即使只安装1个插件，也应使用pluginPath1
pluginPath2="C:\\DCC\\D5_Live_Sync_Rhino_usa_1.1.2.0005" //注意：此处参数名带有序号
logDirPath="C:\\Logs"
workspacePath="C:\\D5Workspace"
installPath="C:\\Program Files\\D5 Render"
isForCurrentUser=false`在命令提示符窗口内输入以下命令，将使用配置文件进行安装（替换其中的路径、文件名为你的实际内容）注意在上述config.ini文件里，必须用两道斜杠： \\**使用.ini配置文件进行安装↓**`"C:\D5 Deployment Kit\D5DeployTool-windows-1.1.0.0076.exe" --configPath="C:\Config\deployment.ini"`

## 3. 批量安装

你可以使用你的批量部署工具，按照上述命令进行批量安装。如需要协助，请与我们的销售人员联系。

---

# 静默升级程序

需要集中升级D5版本时，仅需把**新的D5安装包**下载下来，运行安装命令行时安装到上次相同的目录，并移除 -workspacePath 参数即可，覆盖安装等同升级。[D5 Render最新安装包下载链接](https://cn.api.d5render.com/d5-admin/sl/TO81V9bi)`D5_Render_installer-cn2-2.x.x.xxxx.exe -silent -agreeEula -isForCurrentUser=false -installPath="E:/D5 Render" -logPath="E:/"`注意：D5\_Render\_installer-cn2-2.x.x.xxxx.exe请替换成对应下载更新的软件程序名称。

---

# 静默卸载程序

卸载程序位于安装目录下 Uninstall.exe，找到文件位置运行如下命令行：`"E:/D5 Render/Uninstall.exe" -silent -deleteUserConfig`![](https://saas.bk-cdn01.com/t/18217684-957c-4109-9021-5866cc58cc60/u/7531f9aa-9f13-43a5-858c-19dac517bbc6/1742199096147/image.png)

# 注意事项

1. 确保您已下载了D5渲染器的相应版本（例如v2.9.5或更高版本）。
2. 注意：在Windows上，命令行参数中的反斜杠 \ 被视为转义符，使用以下方法处理：将文件路径括在双引号中，并使用 / 替代 \ ，例如 ”C:/Program Files/D5 Render” 。
3. 如果使用参数 “-isForCurrentUser=false” 为所有用户安装，则必须以管理员身份运行脚本或命令，否则会安装异常。
4. 在实际部署前，先在测试环境中运行静默安装，确保正确执行。
5. 注意备份用户配置和设置，以避免在安装或卸载过程中丢失数据。

2026-01-26

#### 本页目录
