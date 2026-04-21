# 工作流插件 | SketchUp-D5同步插件

目前D5渲染器支持直读.skp格式的模型文件。D5转换器-SketchUp可以帮助您无缝链接SketchUp。  演示案例下载：[「场景列车」Vol.108丨客餐厅](https://cn.forum.d5render.com/t/topic/14603)

---

## 下载和安装

### 安装环境和版本支持

SketchUp 2017 - SketchUp 2023版本

### 下载exe

[点击下载](https://cn.cdn.d5converter.d5techs.com/installer/sketchup/latest/D5_Converter_SketchUp_cn_latest.zip)下载完成后双击.exe文件，根据提示安装D5转换器-SketchUp。

### 下载rbz

(适用于使用exe程序安装失败的场景)点击↓下载D5\_Converter\_SketchUp\_cn\_0.8.5.0001.rbz2.8 MBD5\_Converter\_SketchUp\_cn\_0.8.4.0004.rbz2.8 MB

1. 下载并解压.zip文件，得到.rbz安装文件
2. 在SU菜单栏中点击“扩展程序” - “扩展程序管理器”
3. 在弹出的扩展程序管理器中，点击左下角“安装扩展程序”
4. 在弹出的文件窗口中选择要安装的D5\_Converter\_SketchUp\_cn\_X.X.X.rbz，再点击“打开”，在弹出的对话框中点击“是”完成安装。

0.8.4.0003 & 0.8.4.0004版本区别两版本分别对应不同的灯光成组方式，具体内容请参考：[D5转换器 - SketchUp、3ds Max 灯光成组方案 多版本下载 - 工作流 - D5渲染器 (d5render.com)](https://cn.forum.d5render.com/t/topic/30510)

---

## 功能说明

### 在SketchUp一键启动D5渲染器

* 将正在编辑的新模型导入D5渲染器，开启实时渲染工作
* 请在透视视角（Perspective）下进行联动，获得最佳视角同步体验
* 当渲染项目进行中的模型文件需要改动时，开启联动可以与原始模型建立连接或者替换新的模型。

### 模型/材质/场景同步

* 当前模型在SketchUp内完成改动后，使用同步按钮，可以快速将改动后的模型和材质同步至D5渲染器，且保留已经在D5渲染器内调整好的材质和场景等其他参数。
* 支持一键同步SketchUp中的场景列表至D5渲染器

### 视角联动

* 在水平方向上保持SketchUp与D5渲染器的视角保持一致
* 支持一键开启或者关闭视角联动

### 灯光联动

![](https://saas.bk-cdn01.com/t/18217684-957c-4109-9021-5866cc58cc60/u/b2b089df-cb81-4043-b79c-df8b2dc9bba1/1661786124297/%E7%81%AF%E5%85%89.png)

* 点击添加光源按钮，可以在新的窗口选择D5光源（点光源、聚光灯、灯带、区域光）并将其添加至场景中。
* 添加的光源位置和相关参数会实时同步至D5渲染器

---

## 卸载

![](https://saas.bk-cdn01.com/t/18217684-957c-4109-9021-5866cc58cc60/u/b2b089df-cb81-4043-b79c-df8b2dc9bba1/1661786247089/%E5%8D%B8%E8%BD%BD.png)

* 在SketchUp菜单栏中选择“窗口-扩展程序管理器”，选择“su\_to\_d5render”，选择卸载。
* 在目录 C:\Users\Administrator\AppData\Roaming\SketchUp\当前SketchUp版本\SketchUp\Plugins，找到文件“su\_to\_d5render.rb”后删除。

2023-12-22

#### 本页目录
