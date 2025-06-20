# Jekyll图片优化过滤器
# 自动为Markdown内容中的图片添加优化属性

module Jekyll
  module ImageFilters
    def optimize_images(content)
      return content unless content.is_a?(String)
      
      # 获取配置
      config = @context.registers[:site].config['image_optimizer'] || {}
      enabled = config['enabled'] != false
      
      return content unless enabled
      
      # 匹配Markdown图片语法: ![alt](src "title")
      content.gsub(/!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)/) do |match|
        alt_text = $1
        src = $2
        title = $3
        
        # 生成优化的HTML
        generate_optimized_image_html(alt_text, src, title, content, match, config)
      end
    end

    private

    def generate_optimized_image_html(alt_text, src, title, full_content, original_match, config)
      # 检查是否是文章中的第一张图片
      is_first_image = is_first_image_in_content?(src, full_content, original_match)
      
      # 确定加载策略
      loading = if config['lazy_loading'] != false
                  is_first_image ? 'eager' : 'lazy'
                else
                  'eager'
                end
                
      fetchpriority = if config['priority_loading'] != false
                        is_first_image ? 'high' : 'auto'
                      else
                        'auto'
                      end
      
      # 生成WebP格式的srcset
      webp_support = config['webp_support'] != false
      webp_src = webp_support ? src.sub(/\.(jpg|jpeg|png)$/i, '.webp') : nil
      
      html = '<picture class="optimized-image-container">'
      
      # WebP格式（现代浏览器）
      if webp_support && webp_src
        html += "<source srcset=\"#{webp_src}\" type=\"image/webp\">"
      end
      
      # 原始格式（回退）
      html += "<img src=\"#{src}\""
      html += " alt=\"#{alt_text}\"" if alt_text && !alt_text.empty?
      html += " title=\"#{title}\"" if title && !title.empty?
      html += " loading=\"#{loading}\""
      html += " fetchpriority=\"#{fetchpriority}\""
      html += " onload=\"this.style.opacity='1'\""
      html += " style=\"opacity: 0; transition: opacity 0.3s ease-in-out;\""
      html += ">"
      
      html += '</picture>'
      
      html
    end

    def is_first_image_in_content?(src, content, current_match)
      # 找到当前匹配在内容中的位置
      current_position = content.index(current_match)
      
      # 在当前位置之前查找其他图片
      content_before = content[0...current_position]
      
      # 如果没有找到其他图片，说明这是第一张
      !content_before.match(/!\[([^\]]*)\]\(([^)\s]+)/)
    end
  end
end

# 注册过滤器
Liquid::Template.register_filter(Jekyll::ImageFilters) 