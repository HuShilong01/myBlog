# Gleipnir's Blog

[在线访问](https://hushilong01.github.io/myBlog)

基于 Jekyll 和 GitHub Pages 的个人博客系统，支持自动图片优化和 Markdown 文件转换。

## 📋 目录

- [项目概述](#项目概述)
- [功能特性](#功能特性)
- [快速开始](#快速开始)
- [图片优化](#图片优化)
- [Markdown 转换工具](#markdown-转换工具)
- [项目结构](#项目结构)
- [配置说明](#配置说明)
- [故障排除](#故障排除)

## 🎯 项目概述

这是一个基于 Jekyll 的现代化博客系统，专为 GitHub Pages 优化。主要特点包括：

- **零配置部署** - 推送到 GitHub 即可自动部署
- **自动图片优化** - 智能图片加载和 WebP 支持
- **批量文件转换** - 一键转换标准 Markdown 为博客文章
- **响应式设计** - 完美适配各种设备

## ✨ 功能特性

### 🖼️ 图片优化系统
- **智能优先级加载** - 首屏图片优先，其他图片懒加载
- **WebP 格式支持** - 自动生成和提供 WebP 格式
- **响应式图片** - 自动适应不同屏幕尺寸
- **零配置使用** - 使用标准 Markdown 语法即可

### 📝 Markdown 转换工具
- **自动 Front Matter** - 生成包含日期、标题、作者的元数据
- **智能标题处理** - 自动提取和移除重复标题
- **图片路径转换** - 自动转换为 GitHub Pages 兼容路径
- **批量处理** - 一次性处理整个文件夹

### 🚀 自动化工作流
- **GitHub Actions** - 自动构建和部署
- **WebP 生成** - 自动转换图片格式
- **错误检测** - 构建失败时自动通知

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/HuShilong01/myBlog.git
cd myBlog
```

### 2. 配置个人信息
编辑 `_config.yml` 文件：
```yaml
name: "你的博客名称"
description: "博客描述"
baseurl: "/myBlog"  # 你的仓库名
```

### 3. 添加文章
使用转换工具或手动创建：
```bash
python convert_md_to_posts.py ./your-notes-folder
```

### 4. 推送部署
```bash
git add .
git commit -m "添加新文章"
git push
```

## 🖼️ 图片优化

### 使用方法

在 Markdown 文件中使用标准语法：

```markdown
![图片描述](/images/example.jpg)
![图片描述](/images/example.jpg "图片标题")
```

### 自动优化特性

- **智能优先级**：首屏图片自动设置高优先级加载
- **懒加载**：非首屏图片自动懒加载
- **WebP 支持**：自动检测并提供 WebP 格式
- **响应式**：自动适应不同屏幕尺寸

### 配置选项

在 `_config.yml` 中配置：

```yaml
image_optimizer:
  enabled: true          # 启用图片优化
  webp_support: true     # 启用WebP支持
  lazy_loading: true     # 启用懒加载
  priority_loading: true # 启用优先级加载
```

## 📝 Markdown 转换工具

### 功能特点

✅ **自动添加 Jekyll Front Matter** - 生成包含日期、标题、作者等信息的元数据  
✅ **智能标题提取** - 从文件内容或文件名中自动提取标题  
✅ **移除一级标题** - 自动移除内容中的一级标题，避免与 front matter 中的 title 重复  
✅ **图片路径转换** - 自动将相对路径转换为 GitHub Pages 兼容的绝对路径  
✅ **批量处理** - 一次性处理整个文件夹中的所有 Markdown 文件  
✅ **跳过已处理文件** - 自动跳过已经包含 front matter 的文件  
✅ **自定义配置** - 支持自定义日期、作者、baseurl 等参数  

### 使用方法

#### 方法一：Python 脚本（推荐）
```bash
# 基本用法
python convert_md_to_posts.py <源文件夹路径>

# 指定日期和作者
python convert_md_to_posts.py ./notes --date 2025-01-20 --author "Your Name"

# 自定义输出目录
python convert_md_to_posts.py ./notes --output _posts --baseurl /myBlog
```

#### 方法二：Windows 批处理脚本
```cmd
# 双击运行，按提示输入
convert_md_to_posts.bat

# 或者直接指定参数
convert_md_to_posts.bat "C:\path\to\notes" "2025-01-20" "Your Name"
```

### 转换示例

**输入文件：** `notes/ASCII.md`
```markdown
# ASCII码表

基于拉丁字母的一套电脑编码标准，主要用于显示现代英语和其他西欧语言。

![ASCII码表](../images/ASCII/ASCII码表.jpg)
```

**输出文件：** `_posts/2025-01-20-ASCII.md`
```markdown
---
layout: post
title: ASCII码表
date: 2025-01-20
author: Gleipnir
tags: []
toc: true
---

基于拉丁字母的一套电脑编码标准，主要用于显示现代英语和其他西欧语言。

![ASCII码表](/myBlog/images/ASCII/ASCII码表.jpg)
```

### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `source_dir` | 源文件夹路径（必需） | - |
| `--date` | 指定日期 (YYYY-MM-DD) | 当前日期 |
| `--author` | 作者名称 | Gleipnir |
| `--baseurl` | GitHub Pages baseurl | /myBlog |
| `--output` | 输出目录 | _posts |

## 📁 项目结构

```
myBlog/
├── _posts/                    # 博客文章
│   └── *.md                  # Markdown 文章文件
├── _layouts/                 # Jekyll 布局文件
│   ├── default.html
│   ├── post.html
│   └── page.html
├── _includes/                # Jekyll 包含文件
│   ├── head.html
│   ├── footer.html
│   └── nav.html
├── _sass/                    # Sass 样式文件
├── images/                   # 图片资源
│   └── */                    # 分类图片文件夹
├── assets/                   # 静态资源
├── .github/workflows/        # GitHub Actions
│   └── build.yml            # 自动构建配置
├── convert_md_to_posts.py    # Markdown 转换工具
├── convert_md_to_posts.bat   # Windows 批处理脚本
├── _config.yml              # Jekyll 配置文件
└── README.md                # 项目说明文档
```

## ⚙️ 配置说明

### Jekyll 配置

主要配置在 `_config.yml` 中：

```yaml
# 基本信息
name: "Gleipnir's Blog"
description: "Imagine Another World"
baseurl: "/myBlog"

# 图片优化配置
image_optimizer:
  enabled: true
  webp_support: true
  lazy_loading: true
  priority_loading: true

# 插件配置
plugins:
  - jekyll-sitemap
  - jekyll-feed
  - jekyll-paginate
```

### GitHub Actions 配置

自动构建和部署配置在 `.github/workflows/build.yml` 中：

- 自动安装依赖
- 生成 WebP 图片
- 构建 Jekyll 网站
- 上传构建产物

## 🛠️ 故障排除

### 常见问题

#### 1. 构建失败
**问题**：GitHub Actions 构建失败
**解决**：
- 检查 `_config.yml` 语法是否正确
- 确认所有引用的文件都存在
- 查看 Actions 日志获取详细错误信息

#### 2. 图片不显示
**问题**：图片在网站上不显示
**解决**：
- 检查图片路径是否正确
- 确认图片文件已上传到 `images/` 目录
- 验证图片文件名和路径大小写

#### 3. 转换工具报错
**问题**：Python 转换脚本运行失败
**解决**：
- 确认 Python 3.6+ 已安装
- 检查源文件夹路径是否正确
- 验证文件编码为 UTF-8

#### 4. 文章不显示
**问题**：新文章在网站上不显示
**解决**：
- 确认文件名格式为 `YYYY-MM-DD-title.md`
- 检查 front matter 格式是否正确
- 验证文件已推送到 GitHub

### 调试步骤

1. **本地测试**：
   ```bash
   bundle install
   bundle exec jekyll serve
   ```

2. **检查配置**：
   ```bash
   bundle exec jekyll doctor
   ```

3. **查看日志**：
   - GitHub Actions 构建日志
   - 浏览器开发者工具控制台

## 📚 参考资源

- [Jekyll 官方文档](https://jekyllrb.com/docs/)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [Markdown 语法指南](https://www.markdownguide.org/)
- [图片优化最佳实践](https://web.dev/explore/fast)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢以下开源项目：
- [Jekyll](https://jekyllrb.com/)
- [GitHub Pages](https://pages.github.com/)
- [Jekyll Now](https://github.com/barryclark/jekyll-now)

---

**开始你的博客之旅吧！** 🚀
