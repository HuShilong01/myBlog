# Markdown图片使用示例

本文档展示如何在博客中使用优化的图片，同时保持标准Markdown语法。

## 标准Markdown语法（推荐）

### 基本用法
```markdown
![图片描述](/images/example.jpg)
```

### 带标题的图片
```markdown
![图片描述](/images/example.jpg "图片标题")
```

### 相对路径
```markdown
![图片描述](./images/example.jpg)
```

## 优化后的Markdown语法

### 首屏图片（高优先级）
```markdown
{% include markdown-image-optimizer.html 
  src="/images/hero.jpg" 
  alt="主图" 
  first_image="true" %}
```

### 普通图片（懒加载）
```markdown
{% include markdown-image-optimizer.html 
  src="/images/content.jpg" 
  alt="内容图片" %}
```

### 带标题的优化图片
```markdown
{% include markdown-image-optimizer.html 
  src="/images/example.jpg" 
  alt="图片描述" 
  title="图片标题" %}
```

## 实际使用示例

### 文章中的图片
```markdown
## 介绍

这是一段介绍文字。

{% include markdown-image-optimizer.html 
  src="/images/2025-6-18-ASCII/ASCII码表.jpg" 
  alt="ASCII码表" 
  first_image="true" %}

## 详细说明

更多内容...

{% include markdown-image-optimizer.html 
  src="/images/detail.jpg" 
  alt="详细说明图" %}
```

### 多图片文章
```markdown
## 图片展示

{% include markdown-image-optimizer.html 
  src="/images/image1.jpg" 
  alt="第一张图片" 
  first_image="true" %}

{% include markdown-image-optimizer.html 
  src="/images/image2.jpg" 
  alt="第二张图片" %}

{% include markdown-image-optimizer.html 
  src="/images/image3.jpg" 
  alt="第三张图片" %}
```

## 优化效果

### 自动优化功能
1. **首屏图片**: 自动设置 `loading="eager"` 和 `fetchpriority="high"`
2. **其他图片**: 自动设置 `loading="lazy"`
3. **CSS样式**: 自动应用 `.optimized-image` 类
4. **响应式**: 自动适应不同屏幕尺寸

### 性能提升
- 减少首屏加载时间
- 节省带宽（懒加载）
- 改善用户体验
- 提升Core Web Vitals分数

## 注意事项

1. **图片路径**: 确保图片路径正确
2. **文件格式**: 支持JPG、PNG、WebP等格式
3. **文件大小**: 建议压缩图片以获得更好性能
4. **Alt文本**: 始终提供有意义的alt文本

## 故障排除

### 图片不显示
- 检查路径是否正确
- 确认文件存在
- 验证文件权限

### 优化不生效
- 确认包含文件存在
- 检查语法是否正确
- 验证CSS样式是否加载 