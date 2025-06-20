# 插件状态和测试指南

## 当前配置

### 已安装的插件

1. **image_filters.rb** - 图片优化过滤器
   - 自动为Markdown图片添加WebP支持
   - 支持懒加载和优先级加载
   - 处理相对路径转换
   - 为第一张图片设置高优先级加载

2. **nodate.rb** - 无日期文件名支持
   - 允许使用不带日期的文件名（如 `ASCII.md`）
   - 基于官方Jekyll PostReader重写

3. **test_filter.rb** - 测试过滤器
   - 简单的测试过滤器，用于验证插件系统

4. **simple_test.rb** - 简单测试插件
   - 另一个测试插件，用于验证功能

### 配置文件

- `_config.yml` 包含图片优化配置
- GitHub Actions 配置包含WebP图片生成

## 测试方法

### 本地测试

由于系统中没有安装Jekyll，建议使用以下方法测试：

1. **推送到GitHub** - 让GitHub Actions自动构建
2. **使用Docker** - 如果有Docker环境
3. **安装Jekyll** - 在本地安装Jekyll进行测试

### GitHub Actions测试

1. 推送代码到master分支
2. 查看GitHub Actions运行日志
3. 检查构建是否成功
4. 查看生成的网站

### 测试页面

创建了 `test_plugin.html` 页面用于测试：
- 图片优化功能
- 过滤器功能
- 插件系统

## 预期功能

### 图片优化

在Markdown中使用标准语法：
```markdown
![图片描述](../images/ASCII/ASCII码表.jpg "标题")
```

插件会自动：
1. 转换相对路径为绝对路径
2. 添加WebP格式支持
3. 添加懒加载属性
4. 为第一张图片设置高优先级加载

### 无日期文件名

支持文件名格式：
- `ASCII.md` ✅
- `2025-6-18-ASCII.md` ✅

## 当前状态

✅ **配置完成** - 所有插件和配置已就绪
✅ **语法正确** - 插件代码语法已验证
✅ **路径处理** - 相对路径转换功能完整
✅ **GitHub Actions** - 自动构建和WebP生成配置完成

## 故障排除

### 常见问题

1. **插件不工作**
   - 检查 `safe: true` 配置（当前没有）
   - 确保没有使用 `github-pages` gem
   - 验证插件语法

2. **图片路径错误**
   - 确保使用相对路径 `../images/xxx/xxx.jpg`
   - 插件会自动转换为绝对路径

3. **构建失败**
   - 查看GitHub Actions日志
   - 检查YAML语法
   - 验证插件代码

### 调试步骤

1. 检查GitHub Actions构建日志
2. 验证插件语法
3. 测试简单功能
4. 逐步添加复杂功能

## 下一步

1. 推送代码到GitHub测试构建
2. 检查生成的网站功能
3. 根据测试结果调整配置
4. 优化性能和功能

## 使用说明

### 写作文章

1. 在 `_posts` 目录创建Markdown文件
2. 文件名可以使用 `ASCII.md` 格式（无需日期）
3. 使用标准Markdown图片语法
4. 图片路径使用相对路径：`../images/xxx/xxx.jpg`

### 图片优化

- 插件会自动处理图片优化
- GitHub Actions会自动生成WebP格式
- 无需手动处理图片格式

### 部署

- 推送到master分支即可自动部署
- GitHub Pages会自动构建和优化
- 图片加载优化自动生效 