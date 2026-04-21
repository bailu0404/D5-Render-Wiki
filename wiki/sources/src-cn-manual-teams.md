---
title: "CN Manual — Team Edition (docs.d5render.cn/teams)"
created: 2026-04-20
updated: 2026-04-20
sources:
  - raw/cn/manual/teams.md
  - raw/cn/manual/teams -- 07d2.md
  - raw/cn/manual/teams -- 29d0.md
  - raw/cn/manual/teams -- 622d.md
  - raw/cn/manual/teams -- 3d5e.md
  - raw/cn/manual/teams -- 69ec.md
  - raw/cn/manual/teams -- 5013.md
  - raw/cn/manual/teams -- cb1d.md
  - raw/cn/manual/teams -- e947.md
  - raw/cn/manual/teams -- 1287.md
tags: [cn, teams, collaboration, enterprise, sso, baidu-netdisk, cesium, showreel]
---

CN documentation for D5 Team Edition, covering all collaboration and enterprise management features. Source: docs.d5render.cn/teams.

## Team Edition Module Overview

The CN manual organizes Team Edition into 9 functional modules:

| Module | CN Name | Description |
|--------|---------|-------------|
| Organization Setup | — | Initial team configuration and billing |
| Organization Management | 组织管理 | Account/permission management |
| Asset Management | 资产管理 | Shared team asset library |
| D5 Studio | D5 Studio | Preset sharing and cloud space |
| Multi-User Editing | 多人编辑 | Real-time collaborative scene editing |
| Comments & Notes | 评论备注 | In-app scene annotation |
| Showreel Platform | Showreel平台 | Client presentation portal |
| Data Analytics | 数据分析 | Team usage dashboard |
| App Integrations | 应用集成 | Third-party service connections |
| SSO | SSO单点登录 | Enterprise single sign-on |

## Organization Management (组织管理)

- Activate and manage Team Edition subscriptions
- Invite members, configure role-based permissions
- Assign project resources and define member access scopes
- Team Edition usage rights are separated from personal D5 account ownership — protecting both enterprise and individual data

*Source: raw/cn/manual/teams -- 29d0.md*

## Multi-User Editing (多人编辑)

Real-time collaborative scene editing: multiple team members can work on the same D5 scene simultaneously.

*Source: raw/cn/manual/teams -- 622d.md*

## Comments & Notes (评论备注)

In-scene annotation system enabling designers and clients to leave spatial comments attached to specific scene locations. Integrates with D5 Showreel for client review workflows.

*Source: raw/cn/manual/teams -- 5013.md*

## Showreel Platform

Web-based client presentation portal. Shares rendered panoramas, virtual tours, and project previews via link or QR code. Supports:
- Panorama tour comments (spatial annotation)
- 3D Dollhouse view with location-pinned comments
- Text, location, and image comment types

*Source: raw/cn/manual/teams -- cb1d.md*

## Data Analytics Dashboard (数据分析)

Team usage data dashboard for management decision-making:
- View rendering hours, asset usage, member activity
- Usage: Team Admin Portal → Data Analytics

*Source: raw/cn/manual/teams -- 07d2.md*

## App Integrations (应用集成)

Two CN-relevant integrations:

### Cesium Integration
- Connects D5 to Cesium 3D geospatial data
- Enables real-world terrain and satellite imagery context for urban/landscape projects
- Documented: docs.d5render.cn/teams/3d5e/ffb1

### Baidu Netdisk Integration (百度网盘集成) — CN-Specific
- Direct Baidu Netdisk cloud storage integration for project file sharing
- Allows teams without enterprise NAS to share files via China's dominant cloud storage platform
- Launched in D5 2.11
- Documented: docs.d5render.cn/teams/3d5e/0aef

*Source: raw/cn/manual/teams -- 3d5e.md*

## SSO Single Sign-On (SSO单点登录)

Enterprise SSO integration, allowing organizations to authenticate D5 team members through their existing corporate identity provider (e.g., Active Directory, SAML-based systems).

*Source: raw/cn/manual/teams -- e947.md*

## See Also

- [[d5-for-teams]] — D5 Team Edition overview (English wiki)
- [[virtual-tour]] — Virtual tours and Showreel
- [[cn-overview]] — Chinese market overview
- [[src-cn-news]] — Team Edition blog coverage
