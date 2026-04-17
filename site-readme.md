# D5 Render Wiki — Agent Remote Access

本站是 D5 Render LLM Wiki 的 GitHub Pages 部署，供 AI Agent 远程查阅。

## 访问方式

### 第一步：查索引

```
https://bailu0404.github.io/D5-Render-Wiki/manifest.json
```

返回所有页面的元数据列表，每条包含：

| 字段 | 说明 |
|------|------|
| `name` | 页面标识（对应 wikilink 名） |
| `title` | 页面标题 |
| `path` | 相对路径，如 `wiki/entities/ai-capabilities.md` |
| `tags` | 标签列表 |
| `sources` | 来源列表 |
| `category` | 分类：entities / concepts / sources / analyses / root |
| `updated` | 最后更新日期 |

按 `name` 或 `tags` 搜索定位目标页面。

### 第二步：读页面

用 `base_url` + `/` + `path` 拼接完整 URL：

```
https://bailu0404.github.io/D5-Render-Wiki/{path}
```

### 第三步：追踪 wikilink

页面内的 `[[page-name]]` 引用，回到 manifest 查找该 name 的 path，再拼接读取。

## 常用入口

| 用途 | URL |
|------|-----|
| 搜索索引 | https://bailu0404.github.io/D5-Render-Wiki/manifest.json |
| 全局速查 | https://bailu0404.github.io/D5-Render-Wiki/wiki/compact.md |
| 页面目录 | https://bailu0404.github.io/D5-Render-Wiki/wiki/index.md |
| 总览 | https://bailu0404.github.io/D5-Render-Wiki/wiki/overview.md |

## Wiki 范围

- 涵盖 D5 Render 2.x–3.x 版本
- 内容：功能特性、渲染概念、工作流插件、AI 工具、资产库、团队协作、虚拟漫游、动画系统
- 不含：内部实现细节、API/SDK 文档、定价与许可证
