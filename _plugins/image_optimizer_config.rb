# 图片优化配置
# 在_config.yml中可以通过image_optimizer配置

module Jekyll
  class ImageOptimizerConfig
    def self.load_config(site)
      config = site.config['image_optimizer'] || {}
      
      {
        'enabled' => config['enabled'] != false,
        'webp_support' => config['webp_support'] != false,
        'lazy_loading' => config['lazy_loading'] != false,
        'priority_loading' => config['priority_loading'] != false,
        'quality' => config['quality'] || 85,
        'max_width' => config['max_width'] || 1920,
        'thumbnail_width' => config['thumbnail_width'] || 800
      }
    end
  end
end 