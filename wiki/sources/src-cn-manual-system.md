---
title: "CN Manual — System, Hardware & Troubleshooting (docs.d5render.cn)"
created: 2026-04-20
updated: 2026-04-20
sources:
  - raw/cn/manual/hardware-configuration.md
  - raw/cn/manual/hardware-configuration -- 84d9.md
  - raw/cn/manual/hardware-configuration -- gpu-driver.md
  - raw/cn/manual/error-message.md
  - raw/cn/manual/error-message -- b541.md
  - raw/cn/manual/error-message -- 8fae.md
  - raw/cn/manual/error-message -- f0a5.md
  - raw/cn/manual/error-message -- ad77.md
  - raw/cn/manual/getting-started.md
  - raw/cn/manual/getting-started -- hi.md
  - raw/cn/manual/getting-started -- industry-scenes.md
tags: [cn, hardware, system-requirements, troubleshooting, errors, limits]
---

CN documentation for hardware configuration, system requirements, GPU drivers, and common error messages with resolution steps. Source: docs.d5render.cn.

## Getting Started (新手上路)

D5 Render (D5渲染器) is a GPU rendering software. D5 has self-developed industry-leading real-time GI and video denoising algorithms, making interactive rendering intuitive and establishing a real-time architectural visualization workflow.

**New user resources:**
- Beginner tutorial series: Bilibili channel space.bilibili.com/201466127 → 新手入门系列教程
- CN help center: cn.docs.d5render.com
- CN forum (feedback/requests): cn.forum.d5render.com

**Industry scene sample downloads** (`.drs` files) available for:
- Architecture: Zaha Hadid Architects OPUS, 上陇书店
- Interior: 干净的办公空间, 现代简约侘寂风客厅
- Landscape/Garden: 江南园林, 秋日庭院
- Event/Banquet: 梵心舞台
- Game environment: The Last of Us Part 2 recreation

*Source: raw/cn/manual/getting-started.md, raw/cn/manual/getting-started -- hi.md, raw/cn/manual/getting-started -- industry-scenes.md*

## Hardware Requirements

D5 Render requires NVIDIA RTX-class GPUs (hardware ray tracing support). System requirements documented at docs.d5render.cn/hardware-configuration/84d9.

**Tools:**
- **Hardware Detection** (硬件检测): Built-in check that verifies whether the system meets minimum requirements
- **Performance Benchmark** (性能测试工具 / benchmark): Tests GPU performance for D5 workloads; useful for comparing hardware
- **Support Tool**: Diagnostic tool at docs.d5render.cn/hardware-configuration/dc3e for collecting system info when reporting issues
- **Statistics Panel** (统计信息): Shows real-time GPU memory usage, VRAM usage, driver version, and other rendering metrics

*Source: raw/cn/manual/hardware-configuration.md*

## GPU Driver Notes

Critical driver compatibility notes for Windows users:

1. **Windows 10 1909 and below + NVIDIA driver 531+**: Known incompatibility. Users on Win10 1809–1909 should upgrade to Win10 **20H2 or later**.
2. **NVIDIA driver below 527.27**: May cause D5 to get stuck on "Initializing" when running version 2.7+. Clean install to **driver 540+** is recommended.

*Source: raw/cn/manual/hardware-configuration -- gpu-driver.md*

## 3D Mouse Support

D5 supports 3Dconnexion® SpaceMouse (3D mouse) as a beta feature. Configuration: docs.d5render.cn/hardware-configuration/ee70.

*Source: raw/cn/manual/hardware-configuration.md*

## Scene Limits (from Error Messages)

The CN error message documentation reveals the following hard limits enforced by D5:

| Limit | Value | Error Message |
|-------|-------|---------------|
| Total lights | 4,096 | "灯光数量不能超过4096个" |
| Caustic lights | 64 | "焦散灯光数量不能超过64个" |
| Plants | (unspecified max) | "场景中植物数量已达上限" |
| Emissive surfaces | (unspecified max) | "场景中自发光已达上限" |

These limits apply globally per scene. Exceeding them triggers the listed error messages.

*Source: raw/cn/manual/error-message -- 8fae.md, raw/cn/manual/error-message -- b541.md, raw/cn/manual/error-message -- f0a5.md, raw/cn/manual/error-message -- ad77.md*

## Common Errors & Solutions

| Error | Cause | Resolution |
|-------|-------|------------|
| "程序启动失败。系统环境错误" / "无法启动此程序，因为系统中部分DLL文件错误" | Missing system DLL | Follow the linked tutorial to repair DLLs |
| "显卡驱动程序崩溃并被重置" | GPU driver crash/TDR | Update to latest NVIDIA driver; reduce scene complexity |
| "此材质不可复用" | Attempting to reuse a non-shareable material | Use a different material or create a new one |
| "由于找不到 Qt5Core.dll，无法继续执行代码" (first launch) | Missing Qt5Core.dll runtime | Reinstall D5 or install Visual C++ Redistributable |
| "权限不足，请使用管理员权限后重试操作" (downloading assets/plugins) | Insufficient Windows permissions | Run D5 as administrator |

*Source: raw/cn/manual/error-message.md*

## Storage Usage Note

D5 occupies significant disk space due to:
- Asset library downloads (3D models, textures)
- Scene cache files
- Render output storage

See docs.d5render.cn/hardware-configuration/0fb7 for explanation and cleanup guidance.

## See Also

- [[cn-overview]] — Chinese market overview
- [[render-output]] — Render output (path tracing, D5 SR)
- [[src-cn-manual-account]] — Account, AI credits quotas
