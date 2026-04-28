---
title: D5 Render — CN Sales FAQ
created: 2026-04-28
updated: 2026-04-28
sources:
  - raw/cn/official/pricing.md
  - raw/cn/official/homepage.md
  - raw/d5-sales-framework.md
  - raw/d5render-knowledge-base.md
  - raw/d5render-competitor-comparison.md
tags: [cn, sales, faq, pricing, competitors, enterprise]
---

Structured answers to common questions from CN customers and prospects. Designed for sales, pre-sales, and customer success teams.

---

## Pricing & Purchase

**Q: D5 价格是多少？**

Four tiers:
- 社区版: 免费 — for students and beginners
- 专业版: ¥200/月 或 ¥1920/年（年付节省¥480）— for individual professionals
- 团队版: 联系商务 — for firms and enterprises
- 学生版: 免费 — for enrolled university students (requires MOE verification)

For current prices see [[cn-pricing]] or d5render.cn/pricing.

---

**Q: 有没有年付优惠？**

Check d5render.cn/pricing for current annual subscription discounts. Annual plans typically offer cost savings vs monthly billing. Subscription rules: d5render.cn/subscription-rules/.

---

**Q: 学生版怎么申请？免费的吗？**

Yes, the student edition is free. Requires uploading 教育部学籍在线验证报告 (Ministry of Education Student Status Online Verification Report in PDF format). Self-service application at d5render.cn/edu/. See [[cn-account]] for details.

---

**Q: 可以开发票吗？**

Yes. Professional and Team edition subscribers can request invoices (发票) via the D5 User Center → Invoice Service: cn.myspace.d5render.com/bill.

---

**Q: 专业版能升级为团队版吗？**

Yes. Contact sales at d5render.cn/price-form. If joining an existing team, the team admin can invite you.

---

**Q: 团队版价格怎么算？**

Team Edition is custom-priced based on team size and requirements. Contact sales for a quote: d5render.cn/team/ or d5render.cn/price-form.

---

## Features & Capabilities

**Q: D5 支持哪些建模软件？**

8 major platforms:

| Software | Connection Type | Supported Versions |
|----------|----------------|-------------------|
| SketchUp | LiveSync (real-time) | 2020.1 – 2026 |
| 3ds Max | LiveSync (real-time) | 2014–2016, 2018–2027 |
| Rhino | LiveSync (real-time) | 6.1+ |
| ArchiCAD | LiveSync (real-time) | 21–29 |
| Cinema 4D | Sync | 20–26, 2023–2026 |
| Blender | Sync | 2.93 LTS – 5.1 |
| Revit | File import | 2018.3 – 2026 |
| Vectorworks | LiveSync (real-time) | 2024 – 2026 |

See [[workflow-plugins]] for full details.

---

**Q: 电脑配置要求是什么？**

- **OS**: Windows 10 v1809 或以上
- **GPU 最低要求**: NVIDIA GTX 1060 6GB / AMD Radeon RX 6400 / Intel Arc A3 或以上
- **渲染技术**: 基于 Windows DX12 DXR（实时光追）

**已确认支持的显卡型号：**

| 系列 | 型号 |
|------|------|
| NVIDIA GTX | GTX 1060 6GB、GTX 1660系列 6GB、GTX 1070系列、GTX 1080系列 |
| NVIDIA RTX | RTX 2060–2080系列、RTX 3050–3090系列、RTX 4050–4090系列、RTX 5060–5090系列 |
| NVIDIA Quadro | RTX A2000–A6000 |
| AMD Radeon™ | RX 6400 至 RX 7900 XTX（含PRO W系列）|
| Intel Arc™ | A310、A380、A750、A770、A550M、A770M、A730M |

大场景建议 RTX 3080 或以上。完整型号列表见 [[src-cn-official-download]] 或 d5render.cn/specs/

---

**Q: AI 功能有限制吗？社区版和专业版有区别吗？**

Yes:
- 社区版: AI Design Assistant limited to 50 uses; text/image generation 10 uses
- 专业版: AI Design Assistant unlimited; text/image generation 10 uses (same cap)
- 团队版: Same as Professional

AI credits are tracked per account. See [[cn-account]] for credit system details.

---

**Q: D5 可以做虚拟漫游吗？**

Yes. D5 supports three types of virtual tours:
1. **全景漫游** (Panorama tour): 360° photo-based navigation
2. **空间漫游** (Spatial tour): full 3D walkthrough
3. **XR漫游** (XR tour): immersive extended reality experience with 3D Gaussian Splatting

Community edition: 1 virtual tour project. Professional/Team: unlimited.
Tours are shared via the Showreel platform — accessible in China without VPN.

See [[virtual-tour]] for details.

---

**Q: 大场景会卡吗？**

D5's proprietary [[d5-engine|D5 Engine]] is optimized for large scenes using full path tracing on GPU with SOA (Structure of Arrays) memory layout. BIG (Bjarke Ingels Group) has specifically cited D5's ability to handle "global-scale and complex projects" as a key reason for adoption. Performance is significantly better than CPU-render-based tools for large architectural projects.

---

## Competitor Comparisons

**Q: D5 和 Lumion 比哪个好？**

| Dimension | D5 Render | Lumion |
|-----------|-----------|--------|
| Rendering quality | Real-time path tracing, physically accurate | Rasterization-based, less physically accurate |
| Large scenes | Strong GPU-accelerated path tracing | Can struggle at very large scale |
| AI features | 15+ integrated AI tools | Limited AI integration |
| Asset library | 16,000+ (Pro) + D5 Works platform | Large library but closed ecosystem |
| Plugin ecosystem | 8 integrations incl. LiveSync | Strong, wide integrations |
| Price (CN) | ¥200/月 (Pro) | Higher price point |
| Learning curve | Moderate; CN docs and community | Moderate |

D5 wins on rendering quality and AI; Lumion wins on plugin breadth and brand recognition in some markets.

---

**Q: D5 和 Enscape 比哪个好？**

| Dimension | D5 Render | Enscape |
|-----------|-----------|---------|
| Standalone capability | Yes (full standalone app) | Plugin-only (embedded in Revit/SketchUp etc.) |
| Rendering quality | Full path tracing | Real-time GI; less accurate at fine detail |
| AI features | Extensive | Limited |
| Asset library | 16,000+ | Smaller built-in library |
| Virtual tour | XR-capable Showreel platform | Basic VR/panorama |
| Price | ¥200/月 (Pro) | Higher, seat-based |

D5 wins on standalone capability, AI, and virtual tour depth. Enscape wins on Revit/ArchiCAD integration workflow simplicity.

---

**Q: D5 和 Twinmotion 比哪个好？**

| Dimension | D5 Render | Twinmotion |
|-----------|-----------|------------|
| Price | ¥200/月 (Pro); 社区版免费 | Free for revenue <$1M; paid otherwise |
| Rendering quality | Full path tracing | Path tracing mode available (Unreal Engine) |
| AI features | 15+ integrated tools | Limited AI |
| Asset library | 16,000+ (Pro) | Quixel Megascans integration (large) |
| Plugin ecosystem | 8 integrations | Revit, SketchUp, Rhino, ArchiCAD |
| CN ecosystem | Dedicated CN site, CN docs, CN forum, Baidu Netdisk, CN support | International-only; no CN localization |
| Team collaboration | D5 for Teams with real-time multi-user | Limited |

D5 wins significantly on CN localization, AI features, team collaboration. Twinmotion wins on Unreal Engine rendering depth and Megascans library breadth.

See [[d5-vs-lumion-vs-enscape]] for a full tri-way comparison.

---

## Enterprise & Team Questions

**Q: 公司采购团队版需要什么流程？**

1. Contact sales: d5render.cn/price-form or d5render.cn/team/
2. Discuss team size, usage needs, and deployment requirements
3. Receive custom quote
4. Sign agreement and set up team admin account
5. Admin invites team members
Optional: request onboarding/training support

---

**Q: 团队版数据安全吗？**

Yes. Team Edition supports:
- **Enterprise Project Library**: LAN (local area network) deployment for project files, preventing external data leakage
- **Role-based permissions**: Admin controls who can access which projects and assets
- **Baidu Netdisk integration**: CN cloud storage option for teams using domestic cloud

---

**Q: 是否支持单机离线使用？**

D5 Render requires internet connectivity for account authentication and AI features. Core rendering can function offline once assets are downloaded, but some features (cloud storage, AI, virtual tour sharing) require internet. Check d5render.cn/subscription-rules/ for specific offline terms.

---

**Q: 有没有试用期？**

Community edition is permanently free and can be used indefinitely as a trial. For Team Edition, a trial period may be available — contact sales to discuss.

---

## Technical Support

**Q: 遇到问题去哪里求助？**

取决于订阅版本：

**专业版 / 团队版**：可直接联系人工客服（三个入口任选）：
1. D5启动器 → 左侧「帮助」→「联系客服」
2. D5启动器 → 左下角「个人账号」→「联系客服」
3. D5官网 → 登录个人中心 → 左侧「帮助」→「联系客服」

**社区版**：
1. 搜索 docs.d5render.cn 或 forum.d5render.cn
2. 使用 D5 Bot（软件内AI助手）初步排查
3. 在论坛「互助小组」发帖，官方技术团队24h内回复

账单/订阅问题：cn.myspace.d5render.com
企业采购：d5render.cn/price-form

See [[cn-support]] for the full channel map.

---

## See Also

- [[cn-pricing]] — Full pricing page with feature comparison table
- [[cn-support]] — Support channels and learning resources
- [[cn-industry-solutions]] — Industry-specific use cases and workflows
- [[d5-vs-lumion-vs-enscape]] — Detailed three-way competitor analysis
- [[src-sales-framework]] — Internal sales argument framework (USP / parity tiers)
- [[src-competitor-comparison]] — Detailed multi-dimensional competitor data
