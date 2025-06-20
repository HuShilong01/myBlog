/**
 * 图片优化脚本
 * 提供懒加载、错误处理、加载状态等功能
 */

(function() {
  'use strict';

  // 检查浏览器是否支持 Intersection Observer
  const supportsIntersectionObserver = 'IntersectionObserver' in window;

  // 图片懒加载实现
  function initLazyLoading() {
    if (!supportsIntersectionObserver) {
      // 降级处理：直接加载所有图片
      loadAllImages();
      return;
    }

    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          loadImage(img);
          observer.unobserve(img);
        }
      });
    }, {
      rootMargin: '50px 0px', // 提前50px开始加载
      threshold: 0.01
    });

    // 观察所有懒加载的图片
    document.querySelectorAll('img[loading="lazy"]').forEach(img => {
      imageObserver.observe(img);
    });
  }

  // 加载单个图片
  function loadImage(img) {
    if (img.dataset.src) {
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
    }
    
    // 添加加载状态
    img.classList.add('loading');
    
    img.onload = function() {
      img.classList.remove('loading');
      img.classList.add('loaded');
      // 触发淡入效果
      img.style.opacity = '1';
    };
    
    img.onerror = function() {
      img.classList.remove('loading');
      img.classList.add('error');
      handleImageError(img);
    };
  }

  // 处理图片加载错误
  function handleImageError(img) {
    const errorPlaceholder = `
      <div style="
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        padding: 20px;
        text-align: center;
        color: #6c757d;
        border-radius: 8px;
        font-size: 14px;
      ">
        <div>📷</div>
        <div>图片加载失败</div>
        <div style="font-size: 12px; margin-top: 5px;">${img.alt || '未知图片'}</div>
      </div>
    `;
    
    img.style.display = 'none';
    img.insertAdjacentHTML('afterend', errorPlaceholder);
  }

  // 降级处理：直接加载所有图片
  function loadAllImages() {
    document.querySelectorAll('img[data-src]').forEach(img => {
      loadImage(img);
    });
  }

  // 预加载关键图片
  function preloadCriticalImages() {
    const criticalImages = document.querySelectorAll('img[fetchpriority="high"]');
    criticalImages.forEach(img => {
      if (img.dataset.src) {
        const preloadLink = document.createElement('link');
        preloadLink.rel = 'preload';
        preloadLink.as = 'image';
        preloadLink.href = img.dataset.src;
        document.head.appendChild(preloadLink);
      }
    });
  }

  // 图片格式检测和优化
  function detectImageFormat() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
      // 检查是否支持WebP
      if (supportsWebP() && img.src && !img.src.includes('.webp')) {
        const webpSrc = img.src.replace(/\.(jpg|jpeg|png)$/i, '.webp');
        // 这里可以添加WebP版本的预加载逻辑
      }
    });
  }

  // 检测WebP支持
  function supportsWebP() {
    const canvas = document.createElement('canvas');
    canvas.width = 1;
    canvas.height = 1;
    return canvas.toDataURL('image/webp').indexOf('data:image/webp') === 0;
  }

  // 初始化
  function init() {
    // 预加载关键图片
    preloadCriticalImages();
    
    // 初始化懒加载
    initLazyLoading();
    
    // 检测图片格式
    detectImageFormat();
    
    // 添加全局错误处理
    window.addEventListener('error', function(e) {
      if (e.target.tagName === 'IMG') {
        handleImageError(e.target);
      }
    }, true);
  }

  // DOM加载完成后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})(); 