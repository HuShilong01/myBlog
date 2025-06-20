# Markdown 文件转换工具

这个工具可以将指定文件夹中的标准 Markdown 文件转换为 GitHub Pages 兼容格式，并自动保存到 `_posts` 文件夹中。

## 功能特点

✅ **自动添加 Jekyll Front Matter** - 自动生成包含日期、标题、作者等信息的 front matter  
✅ **智能标题提取** - 从文件内容或文件名中自动提取标题  
✅ **移除一级标题** - 自动移除内容中的一级标题（# 开头的标题），避免与 front matter 中的 title 重复  
✅ **图片路径转换** - 自动将相对路径转换为 GitHub Pages 兼容的绝对路径  
✅ **批量处理** - 一次性处理整个文件夹中的所有 Markdown 文件  
✅ **跳过已处理文件** - 自动跳过已经包含 front matter 的文件  
✅ **自定义配置** - 支持自定义日期、作者、baseurl 等参数  

## 文件说明

- `convert_md_to_posts.py` - Python 转换脚本（主要工具）
- `convert_md_to_posts.bat` - Windows 批处理脚本（方便 Windows 用户使用）
- `README_CONVERTER.md` - 本说明文档

## 使用方法

### 方法一：使用 Python 脚本（推荐）

```bash
# 基本用法
python convert_md_to_posts.py <源文件夹路径>

# 指定日期和作者
python convert_md_to_posts.py ./notes --date 2025-01-20 --author "Your Name"

# 自定义输出目录
python convert_md_to_posts.py ./notes --output _posts --baseurl /myBlog
```

### 方法二：使用 Windows 批处理脚本

```cmd
# 双击运行，按提示输入
convert_md_to_posts.bat

# 或者直接指定参数
convert_md_to_posts.bat "C:\path\to\notes" "2025-01-20" "Your Name"
```

## 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `source_dir` | 源文件夹路径（必需） | - |
| `--date` | 指定日期 (YYYY-MM-DD) | 当前日期 |
| `--author` | 作者名称 | Gleipnir |
| `--baseurl` | GitHub Pages baseurl | /myBlog |
| `--output` | 输出目录 | _posts |

## 转换示例

### 输入文件：`notes/ASCII.md`
```markdown
# ASCII码表

基于拉丁字母的一套电脑编码标准，主要用于显示现代英语和其他西欧语言。

![ASCII码表](../images/ASCII/ASCII码表.jpg)
```

### 输出文件：`_posts/2025-01-20-ASCII.md`
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

**注意**：转换后的一级标题 `# ASCII码表` 被移除，标题信息保存在 front matter 的 `title` 字段中。

## 图片路径转换规则

脚本会自动转换图片路径：

| 原始路径 | 转换后路径 |
|----------|------------|
| `./image.jpg` | `/myBlog/images/image.jpg` |
| `../images/photo.png` | `/myBlog/images/photo.png` |
| `/images/logo.png` | `/myBlog/images/logo.png` |
| `https://example.com/image.jpg` | `https://example.com/image.jpg`（保持不变） |

## 标题处理规则

1. **标题提取**：
   - 优先从内容中提取第一个 `#` 开头的标题
   - 如果没有找到，从文件名提取并转换为标题格式
   
2. **标题移除**：
   - 自动移除内容中的一级标题（`# 标题`）
   - 保留二级及以下标题（`## 标题`、`### 标题` 等）
   - 标题信息保存在 front matter 的 `title` 字段中

### 标题转换示例

| 原始文件名 | 提取的标题 | 转换后标题 |
|------------|------------|------------|
| `ascii_table.md` | ASCII Table | ASCII Table |
| `python_basics.md` | Python Basics | Python Basics |
| `web_development.md` | Web Development | Web Development |

## 注意事项

⚠️ **备份重要文件** - 转换前请备份原始文件  
⚠️ **检查输出** - 转换后请检查生成的文件是否正确  
⚠️ **图片文件** - 确保图片文件存在于正确的位置  
⚠️ **编码格式** - 脚本使用 UTF-8 编码，确保文件编码正确  
⚠️ **标题处理** - 一级标题会被移除，避免与 front matter 中的 title 重复  

## 故障排除

### 常见问题

**Q: 提示 "未找到 Python"**  
A: 请先安装 Python，并确保在 PATH 环境变量中

**Q: 图片路径转换不正确**  
A: 检查 `--baseurl` 参数是否正确设置

**Q: 文件编码问题**  
A: 确保 Markdown 文件使用 UTF-8 编码

**Q: 跳过已处理文件**  
A: 这是正常行为，脚本会自动跳过已包含 front matter 的文件

**Q: 一级标题被移除了**  
A: 这是设计功能，避免与 front matter 中的 title 重复。标题信息保存在 front matter 中

## 系统要求

- Python 3.6 或更高版本
- Windows 系统（使用 .bat 脚本）
- 或任何支持 Python 的系统

## 许可证

本工具遵循 MIT 许可证，可自由使用和修改。 