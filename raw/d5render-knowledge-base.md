# D5 Render 产品知识库 v2.0
> 建立：2026-03-10 | 深度更新：2026-03-10 | 来源：d5render.com 全站爬取（官网+博客+案例+竞品对比）

---

## 🏢 公司概览

- **公司名称：** Dimension 5
- **官网：** https://www.d5render.com / 中文：https://www.d5render.cn
- **品牌标语：** "Your Flow. Unbroken." — From first sketch to final reality, one AI-driven workflow.
- **用户规模：** 300万+ 专业用户，来自190+国家；50,000+全球企业用户
- **市场地位：** G2平台渲染软件排名 **#1**；世界前10大建筑事务所中80%使用D5
- **版本：** 当前最新版 **D5 Render 3.0**（2026年1月发布）
- **联系方式：**
  - 一般咨询：contact@d5techs.com
  - 市场合作：marketing@d5techs.com
  - 企业/团队销售：sales@d5techs.com
  - 技术支持：support@d5techs.com
  - 工作时间：周一至周五 10:00-18:00（GMT+8）

---

## 🧩 产品生态（All-in-One Workflow）

D5 3.0推出"三位一体"生态系统，覆盖设计全流程：

```
D5 Lite（概念阶段）→ D5 Render（生产阶段）→ D5 Works（资产支撑）
```

### 1. D5 Lite — AI原生可视化插件
- **定位：** 嵌入建模工具，设计过程中即时可视化，消除导出摩擦
- **核心卖点：** "Visualize as you design. Iterate with AI."
- **功能亮点：**
  - 内嵌SketchUp（2021.1-2026），无缝运行于建模工具内部
  - AI概念化：输入提示词→生成4种风格方案，锁定方向后一键同步D5 Render
  - 完整版本历史，设计方向留存
  - 实时路径追踪，所见即所得
  - 代理资产（Proxy Assets）：轻量编辑 + 全精度渲染
  - Nano Banana Pro级AI精度（韩国高端市场验证）：保持透视精准度
- **价格：** 免费（AI高级功能需Pro）
- **系统要求：** Windows 10 v1909+，NVIDIA RTX GPU
- **路线图：** 即将支持Rhino、Revit、3ds Max；Mac版开发中

### 2. D5 Render 3.0 — 生产级实时渲染核心
- **定位：** 大型场景+高端动画+AI场景自动化的生产力工具
- **3.0核心新功能（2026年1月发布）：**
  - **Ocean（海洋系统）：** 全新动态海洋，自动海岸线生成，自动焦散，无需手动绘制海岸
  - **Volumetric Clouds（体积云）：** 3D真实体积，与阳光交互、投射阴影，含预设库
  - **Displacement Material（置换材质，Beta）：** 真实几何置换，砖石/岩石表面深度物理准确
  - **AI Scene Match：** 描述氛围→AI生成参考图→一键匹配灯光和后期
  - **AI Image to 3D：** 二维参考图→秒级生成3D模型（D5内部完成）
  - **Procedural Buildings（程序化建筑）**
  - **D5 Works集成至Launcher**
- **自研技术架构（D5 Engine）：**
  - 专为建筑可视化从零构建，非游戏引擎改造
  - Native Full Path Tracing（物理优先管线，非混合算法）
  - 集成 Radiance Cache、ReSTIR、Multi-Layer Denoising
  - 原生支持 Windows DX12 + macOS Metal（定制shader架构，无翻译层损耗）
  - 真正WYSIWYG：实时视口 = 最终输出
- **输出能力：**
  - 图像：最高16K，.exr/.png/.tif等多格式
  - 视频：最高8K（Teams），4K@120FPS（Pro），.mp4/.avi
  - 帧序列，多通道渲染（Material ID/Sky Mask/Reflection/AO/Z-depth等）
  - VR（SteamVR：HTC Vive、Oculus Rift）
  - 全景漫游（Panorama Tour）/空间漫游（Spatial Tour）
  - XR Tour（基于3D Gaussian Splatting，任何浏览器可访问）
- **性能技术：**
  - DLSS（NVIDIA深度学习超级采样）
  - Intel XeSS（支持Arc A5/A7）
  - D5 SR图像渲染（自研神经网络超分辨率）
  - 大场景分层加速 + Texture Streaming（降低RAM占用）
  - D5 2.7+动画渲染速度提升100%+（含大量反射和材质场景）

### 3. D5 Works — 空间设计资产平台（Beta）
- **官网：** https://www.d5works.com
- **定位：** AEC专业人员的3D资产中枢，创作者与设计师协作平台
- **特点：**
  - 39,200+高级资产（持续增长）
  - 直接集成至D5 Launcher，无需切换浏览器
  - 资产拖拽即用，光标变为实时缩略图，一键放置
  - AEC-ready：预优化性能和保真度
  - 覆盖建筑/景观/室内全品类，专注高保真家具和室内元素

---

## 🤖 AI功能体系（15+项，D5 3.0起）

### 设计阶段
| 功能 | 描述 | 所属产品 |
|------|------|----------|
| AI Conceptualization | 提示词→基于当前模型生成概念方案（4种选项） | D5 Lite |
| AI Scene Match | 描述氛围/"秋日黄昏"/输入参考图→一键匹配灯光、天空、后期 | D5 Render |
| AI Agent: Smart Planting | 根据场地/气候/偏好自动生成种植方案，自动生成植物清单 | D5 Render |
| AI Asset Recommendation | 自动推荐适合场景的植被和人物角色 | D5 Render |
| AI Image to 3D | 二维图片→3D模型（Meshy驱动），内置示例库 | D5 Render |

### 材质阶段
| 功能 | 描述 |
|------|------|
| AI PBR Material Snap | 照片→即时生成高质量PBR材质，推荐相似资产 |
| AI-generated Material Texture Maps | 基础色贴图→自动生成法线/粗糙度/高度/AO通道（U-Net/GAN） |
| AI Ultra HD Texture | 一键将纹理超分辨率至4K |
| AI Make Seamless | AI Inpainting，碎片纹理→无缝纹理 |

### 后期阶段
| 功能 | 描述 |
|------|------|
| AI Enhancer | 增强渲染图细节（灯光/材质/人物/植被），支持局部/全图 |
| AI Style Transfer | 一键转换水彩/卡通/比例模型/素描/体素，及日落/夜景/四季 |
| AI Inpainting | 自动修复天空/水/植被/人物 |
| AI Atmosphere Match | 参考图→自动匹配环境和效果参数 |
| Motion Blur | AI辅助动态模糊，一键应用于人物和车辆 |

**AI数据安全：**
- GDPR合规，ISO 27001 & ISO 27701认证
- 不使用用户数据训练AI模型，数据仅用于功能交付
- 传输加密 + 静态加密

---

## 💰 定价方案

| 方案 | 月付 | 年付 | 目标用户 | 核心内容 |
|------|------|------|----------|----------|
| **Community** | 免费 | 免费 | 学习者/初学者 | 无限项目，~2,100资产，基础功能，16K图，50次AI试用 |
| **Pro** | $38/月 | $360/年（省20%）| 专业个人 | 全部15+AI功能，16,000+资产，VR，帧序列，4K视频，项目合并，技术支持 |
| **Teams** | $75/月/席 | $708/年/席（省21%）| 团队/工作室 | Pro全部+多人同步编辑，权限管理，100GB云空间，共享资源库，8K视频，虚拟导览 |
| **Education** | 免费 | 免费 | 学生/教育工作者 | 申请即用 |
| **Lab** | 咨询 | 咨询 | 学校机房 | 网络授权 |

**一个Pro订阅包含：** D5 Render高级功能 + D5 Lite AI功能 + D5 Works资产折扣
**Teams企业试用：** 提供最长1个月免费团队试用 + 产品演示 + 入职培训

---

## 🛠️ 核心工具集

| 工具 | 描述 |
|------|------|
| D5 Scatter | PCG程序化散布工具，按颜色区域分植物，Random Placement |
| Scatter预设库 | 数十种植被散布预设，拖拽秒建景观 |
| Brush工具 | 快速刷植被 |
| Path工具 | 沿路径绘制植物 |
| 地形 & 海洋 | 地形系统 + 3.0全新动态海洋 |
| 城市生成器 + Cesium | 程序化建筑生成 + 真实地理数据场景定位 |
| 剖切工具 | 剖面展示 |
| 阶段动画 | 建筑建造阶段可视化，无需手动设置关键帧 |
| 灯光系统 | 8种补光类型：点光、聚光、面光、IES灯、投影仪、Stage Light、发光材质等 |
| D5 Studio | 资产/场景/预设管理 |

---

## 🔌 工作流集成

**LiveSync实时同步支持（双向即时更新）：**
SketchUp · Rhino · Revit · 3ds Max · Blender · Archicad · Cinema 4D · Vectorworks

**文件导入支持：** SKP / FBX / OBJ / 主流3D格式

---

## 🏗️ 行业解决方案矩阵

| 维度 | 解决方案 |
|------|----------|
| **按行业** | 建筑 / 景观 / 室内 / 城市规划 |
| **按用例** | 动画 / 演示提案 / 实时协作 / 竞标 |
| **按规模** | 自由职业者 / 中小型事务所 / 大型企业 |
| **按角色** | 设计团队 / IT部门 / 项目管理 / 可视化艺术家 |

**行业特色功能：**
- 建筑：2,000+高质材质库，精准反射/折射，实时动画出图
- 景观：3,800+植物模型（全球各地区），AI SmartPlanting，D5 Scatter程序化景观
- 室内：3,500+家具/软装模型，高精度发光材质，SSS半透明材质
- 企业：多人实时协同编辑，权限管理，100GB云存储，数据看板

---

## 🏆 标杆客户数据

| 客户 | 规模/背景 | D5效果 | 引用 |
|------|-----------|--------|------|
| **BIG（Bjarke Ingels Group）** | 700+人，9个全球办公室，世界顶级建筑事务所 | "Think of D5 as a speedy V-Ray, an easy DaVinci Resolve, and Photoshop with built-in AI — all rolled into one." | "D5彻底革命性改变了我们的工作方式，处理世界上最大最复杂项目的能力是完全的游戏改变者。" |
| **KPF** | 世界13座最高建筑中的6座设计方 | 设计迭代时间缩短80%；3个月内扩展至150+用户 | "与我们团队工作流最契合的工具，而非绝对最好的工具" |
| **SWA Shanghai** | 65年景观设计公司，上海办公室19人 | 实时反馈加速决策，减少软件切换 | "D5增强了设计、模型和渲染之间的连接，简化了工作流程。" |
| **ARQBR** | 巴西建筑事务所，13人，2024 ArchDaily年度建筑奖 | 快速材质测试，加快渲染决策 | "材质和模型库帮助我们加快了测试渲染速度" |
| **VK Group** | 印度，300+人，大型城镇项目 | 交付时间缩短80%，可视化成为贯穿项目全程的基础设施 | "D5将我们的交付时间缩短了近80%" |
| **AO Architects** | 美国，325人，17个工作室 | 从单一Atlanta工作室试验扩展至全公司目标 | "速度重要，但真正的价值在于沟通质量" |
| **Nihon Sekkei** | 日本最大多学科设计公司之一，1967年创立 | 多编辑者实时协同，跨专业协调提升30% | 大规模复杂项目的可视化协作解决方案 |
| **Ennead** | 美国，200人，大型公共建筑 | 可视化从"末端交付物"变为"设计决策媒介" | 30+设计师跨6种建筑类型使用D5 |
| **AiSA Architecture** | 土耳其，2人小工作室 | 1分钟动画从6天→30分钟（快12倍）；从Lumion完全切换 | "他看呆了——D5的更自然，而且我在半小时内就做出来了" |
| **TISSA** | 企业用户 | "1小时内，整个团队都自信地使用D5" | 直觉界面，工程师也能快速上手 |

---

## ⚙️ 系统要求

| 产品 | OS | GPU |
|------|----|-----|
| D5 Render | Windows 10 v1809+ | NVIDIA GTX 1060 6GB+ / AMD Radeon RX 6000 XT+ / Intel Arc A3+ |
| D5 Lite | Windows 10 v1909+ | NVIDIA RTX系列 |

> ⚠️ NVIDIA驱动>531.14时需Windows 21H2+；AMD目前不支持实时光线追踪

---

## 📚 学习与生态资源

- **文档：** docs.d5render.com
- **论坛：** forum.d5render.com
- **教程：** d5render.com/learning
- **博客：** 337+篇文章（工作流/案例/行业分析/竞品对比）
- **D5 Certification Program：** 认证培训体系
- **Campus Ambassador：** 全球校园大使计划（2026年2月在Cornell等8所高校开展工作坊）
- **Reseller Program：** 全球经销商体系
- **D5 Awards：** 年度创作大奖

---

## 📊 博客内容体系（337+篇文章分类）

| 类别 | 代表内容 |
|------|----------|
| 产品更新 | D5 3.0发布，月度Recap，版本更新日志 |
| 案例研究 | BIG/KPF/SWA/Nihon Sekkei/VK Group等标杆案例 |
| 工作流教程 | 15分钟完成建筑渲染，Revit→动画，SketchUp+D5 Lite等 |
| AI功能 | AI Scene Match, AI Agent SmartPlanting, AI PBR Material等 |
| 竞品对比 | D5 vs Unreal vs Corona, D5 vs V-Ray, AI工具对比等 |
| 行业报告 | AI in Architecture 2025（665人调研），实时渲染工具排名 |
| 行业用例 | 建筑/景观/室内/教育/竞赛/城市规划等 |

---

## 🗺️ D5 Engine 技术优势（2026年3月正式发布详情）

## ⚠️ 渲染引擎架构（重要，销售时务必准确）

**D5 Render（当前版本）：** 基于 UE5 开发，在其上深度定制了建筑可视化专属的渲染管线和工作流

**D5 Lite：** 搭载 D5 自研的全新专有渲染引擎（D5 Engine），从零为空间设计构建，非游戏引擎改造

**路线图：** D5 Engine（自研引擎）将逐步整合进 D5 Render，最终取代 UE5 底层——D5 的长期方向是完全脱离游戏引擎依赖

**销售含义：**
- 对 Unreal 用户：不能说"built from scratch, not from games"——D5 Render 现在还是 UE5 基础；正确说法是"基于UE5，但专为建筑工作流深度优化，WYSIWYG一致性远好于原生Unreal archviz"
- D5 Lite 的自研引擎是真正的差异化技术故事，可以作为前瞻性卖点讲

---

## 🔑 核心差异化优势总结

1. **All-in-One AI工作流生态：** D5 Lite + D5 Render + D5 Works，从概念到交付，一个账号
2. **自研D5 Engine：** 非Unreal/游戏引擎改造，专为空间设计优化
3. **最低上手门槛：** 免费入门，无需申请试用；平均1小时团队上手（TISSA验证）
4. **AI深度集成（15+项）：** 横跨概念/材质/氛围/后期全流程，非点状AI功能
5. **真实WYSIWYG：** 与Enscape/Lumion不同，实时视口真正等于最终输出
6. **企业级大场景能力：** BIG/Nihon Sekkei/VK Group等验证，不牺牲质量
7. **多人实时协同编辑：** 市场稀缺功能，同时编辑同一项目
8. **G2 #1 + 世界前10大事务所80%使用：** 第三方背书
9. **数据安全企业级认证：** ISO 27001/27701，GDPR，不训练用户数据
10. **社区生态完整：** 337+博客，论坛，认证培训，全球校园大使

