---
title: "Source: CN Official Download Page (d5render.cn/download)"
created: 2026-04-28
updated: 2026-04-28
sources: [raw/cn/official/download.md]
tags: [cn, download, plugins, compatibility, source-summary]
---

Source summary for `raw/cn/official/download.md` — the CN download page listing the D5 Launcher and all workflow sync plugins.

## Key Takeaways

### D5 Launcher
Entry point for all D5 products. Download the installer, select installation path, and the launcher handles downloading D5 Render, D5 Lite, and sync plugins. Update log: https://forum.d5render.cn/t/topic/5149

### System Requirements
- **GPU**: NVIDIA GTX 1060 6GB / AMD Radeon RX 6400 / Intel Arc A3 or above (minimum)
- **OS**: Windows 10 v1809 or above
- **Rendering tech**: Built on Windows DX12 DXR (DirectX Raytracing); supported GPU list below

### Supported GPU List (全部兼容型号)

D5 实时光追基于 Windows DX12 DXR，以下为全部已确认支持的显卡型号：

| 系列 | 显卡型号 |
|------|---------|
| **NVIDIA GTX** | GTX 1060 6GB、GTX 1660 6GB、GTX 1660 Ti 6GB、GTX 1660 SUPER 6GB、GTX 1070 8GB、GTX 1070 Ti 8GB、GTX 1080 8GB、GTX 1080 Ti 11GB |
| **NVIDIA RTX** | RTX 5090 D 32GB、RTX 5090 32GB、RTX 5080 16GB、RTX 5070 Ti 16GB、RTX 5070 12GB、RTX 5060 Ti 16GB、RTX 5060 8GB、RTX 4090 D 24GB、RTX 4090 24GB、RTX 4080 SUPER 16GB、RTX 4080 16GB / 12GB、RTX 4070 Ti SUPER 16GB、RTX 4070 Ti 12GB、RTX 4070 SUPER 12GB、RTX 4070 12GB / 8GB、RTX 4060 Ti 16GB / 8GB、RTX 4060 8GB、RTX 4050 6GB、RTX 3090 Ti 24GB、RTX 3090 24GB、RTX 3080 Ti 16GB / 12GB、RTX 3080 16GB / 12GB / 10GB / 8GB、RTX 3070 Ti 8GB、RTX 3070 8GB、RTX 3060 Ti 8GB、RTX 3060 12GB / 6GB、RTX 3050 8GB / 4GB、RTX 3050 Ti 4GB、RTX 2080 Ti 11GB、RTX 2080 SUPER 8GB、RTX 2080 8GB、RTX 2070 SUPER 8GB、RTX 2070 8GB、RTX 2060 SUPER 8GB、RTX 2060 12GB / 6GB |
| **NVIDIA Quadro** | RTX A6000、RTX A5500、RTX A5000、RTX A4500、RTX A4000、RTX A3000、RTX A2000 |
| **AMD Radeon™** | RX 7900 XTX、RX 6950 XT、RX 6900 XT、RX 6800 XT、RX 6800、RX 6750 XT、RX 6700 XT、RX 6650 XT、RX 6600 XT、RX 6600、RX 6600M、RX 6500 XT、RX 6400、PRO W6800、PRO W6600 |
| **Intel Arc™ A3/A5/A7** | A770 (16GB)、A770 (8GB)、A750、A380、A310、A550M、A770M、A730M |

完整最新列表参考：NVIDIA官网、AMD官网、Intel官网（链接见 d5render.cn/specs/）

### Workflow Plugin Compatibility (CN)

| Plugin | Supported Host Versions | Min D5 Version | Notes |
|--------|------------------------|----------------|-------|
| SketchUp LiveSync | 2020.1 – 2026 | D5 2.5+ | Non-realtime plugin also available |
| 3ds Max LiveSync | 2014–2016, 2018–2027 | D5 2.6+ | Non-realtime plugin also available |
| Rhino LiveSync | 6.1+ | D5 2.7+ | Non-realtime plugin also available |
| Archicad LiveSync | 21–29, Archicad solo, Archicad SE | — | Non-realtime plugin also available |
| Revit | 2018.3 – 2026 | — | No LiveSync; file-based import |
| Cinema 4D | 20–26, 2023–2026 | — | CN-relevant: widely used in CN interior/animation |
| Blender | 2.93 LTS – 5.1 | — | Full version range |
| Vectorworks LiveSync | 2024 – 2026 | — | Via forum download |

### Download Infrastructure (CN)
CN downloads are served from `cn.cdn.d5converter.d5techs.com` — a CN-localized CDN, ensuring fast download speeds within China without VPN.

## Related Pages

- [[workflow-plugins]] — Entity page with full plugin details
- [[d5-launcher]] — D5 Launcher overview
- [[cn-industry-solutions]] — Which plugins are most relevant per industry
