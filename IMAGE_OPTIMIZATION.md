# 图片优化指南

本文档说明如何在本博客中使用优化的图片加载方式，同时保持标准Markdown语法。

## 优化特性

### 1. 自动图片优化
- **Jekyll插件自动处理**: 标准Markdown图片语法自动转换为优化HTML
- **保持语法简洁**: 继续使用 `![alt](src)` 语法
- **智能优先级**: 自动识别首屏图片并设置高优先级

### 2. 懒加载 (Lazy Loading)
- 使用 `loading="lazy"` 属性
- 支持 Intersection Observer API
- 降级处理：不支持时直接加载

### 3. 图片预加载 (Preload)
- 关键图片使用 `fetchpriority="high"`
- 在 `<head>` 中添加预加载链接
- 优先加载首屏重要图片

### 4. 现代图片格式
- 支持 WebP 格式（自动检测）
- 使用 `<picture>` 元素提供回退
- 保持向后兼容性

## 使用方法

### 标准Markdown语法（推荐）
```markdown
![图片描述](/images/example.jpg)
```

### 带标题的图片
```markdown
![图片描述](/images/example.jpg "图片标题")
```

### 相对路径图片
```markdown
![图片描述](./images/example.jpg)
```

### 外部图片
```markdown
![图片描述](https://example.com/image.jpg)
```

## 自动优化功能

### 1. 智能优先级分配
- **首屏图片**: 自动设置为 `fetchpriority="high"` 和 `loading="eager"`
- **其他图片**: 自动设置为 `loading="lazy"`
- **Logo和Hero图片**: 自动识别并设置高优先级

### 2. WebP格式支持
- 自动生成WebP版本的图片链接
- 使用 `<picture>` 元素提供格式回退
- 现代浏览器使用WebP，旧浏览器使用原始格式

### 3. 响应式优化
- 自动添加响应式样式
- 移动端优化
- 自适应容器宽度

## 配置选项

在 `_config.yml` 中可以配置：

```yaml
image_optimizer:
  enabled: true          # 启用图片优化
  webp_support: true     # 启用WebP支持
  lazy_loading: true     # 启用懒加载
  priority_loading: true # 启用优先级加载
```

## 性能优化建议

### 1. 图片格式选择
- **WebP**: 现代浏览器，文件更小
- **JPEG**: 照片类图片
- **PNG**: 需要透明度的图片
- **AVIF**: 最新格式，压缩率最高

### 2. 图片尺寸优化
- 使用合适的图片尺寸
- 避免过大的图片文件
- 考虑使用多尺寸图片

### 3. 压缩优化
- 使用工具压缩图片
- 保持视觉质量的同时减小文件大小
- 推荐工具：TinyPNG, ImageOptim, Squoosh

### 4. CDN使用
- 考虑使用图片CDN
- 利用CDN的缓存和压缩功能
- 减少服务器负载

## 浏览器支持

| 特性 | 支持情况 |
|------|----------|
| 懒加载 | Chrome 76+, Firefox 75+, Safari 15.4+ |
| WebP | Chrome 23+, Firefox 65+, Safari 14+ |
| AVIF | Chrome 85+, Firefox 93+, Safari 16+ |
| fetchpriority | Chrome 101+, Firefox 113+ |

## 故障排除

### 图片不显示
1. 检查图片路径是否正确
2. 确认图片文件存在
3. 检查文件权限

### 懒加载不工作
1. 确认浏览器支持
2. 检查JavaScript是否加载
3. 查看控制台错误信息

### 性能问题
1. 检查图片文件大小
2. 确认使用了合适的格式
3. 验证预加载设置

## 监控和分析

### 使用工具
- **Lighthouse**: 性能分析
- **PageSpeed Insights**: 页面速度测试
- **WebPageTest**: 详细性能分析
- **Chrome DevTools**: 网络分析

### 关键指标
- **LCP (Largest Contentful Paint)**: 最大内容绘制
- **FID (First Input Delay)**: 首次输入延迟
- **CLS (Cumulative Layout Shift)**: 累积布局偏移

## 更新日志

- **v2.0**: 重构为Jekyll插件，保持Markdown语法
- **v1.2**: 优化错误处理和加载状态
- **v1.1**: 添加WebP支持和响应式图片
- **v1.0**: 初始版本，支持基本懒加载和预加载 