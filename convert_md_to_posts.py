#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown 文件转换脚本
将指定文件夹中的标准 Markdown 文件转换为 GitHub Pages 兼容格式并保存到 _posts 文件夹

使用方法:
    python convert_md_to_posts.py <源文件夹路径> [选项]

示例:
    python convert_md_to_posts.py ./notes
    python convert_md_to_posts.py ./notes --date 2025-01-20
    python convert_md_to_posts.py ./notes --author "Your Name"
"""

import os
import sys
import re
import argparse
from datetime import datetime
from pathlib import Path
import shutil

def extract_title_from_content(content):
    """从 Markdown 内容中提取标题"""
    lines = content.split('\n')
    for line in lines:
        # 查找第一个 # 开头的标题
        if line.strip().startswith('#'):
            # 移除 # 符号和空格
            title = re.sub(r'^#+\s*', '', line.strip())
            return title
    return None

def extract_title_from_filename(filename):
    """从文件名中提取标题"""
    # 移除 .md 扩展名
    name = filename.replace('.md', '')
    # 将下划线或连字符替换为空格
    name = re.sub(r'[_-]', ' ', name)
    # 首字母大写
    return name.title()

def convert_image_paths(content, baseurl="/myBlog"):
    """转换图片路径为 GitHub Pages 兼容格式"""
    # 匹配 Markdown 图片语法: ![alt](src)
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    
    def replace_image(match):
        alt_text = match.group(1)
        src = match.group(2)
        
        # 如果已经是绝对路径或 URL，保持不变
        if src.startswith('http') or src.startswith('/'):
            return f'![{alt_text}]({src})'
        
        # 如果是相对路径，转换为绝对路径
        if src.startswith('./'):
            src = src[2:]  # 移除 ./
        elif src.startswith('../'):
            src = src[3:]  # 移除 ../
        
        # 添加 baseurl 前缀
        if not src.startswith('/'):
            src = f'{baseurl}/images/{src}'
        else:
            src = f'{baseurl}{src}'
        
        return f'![{alt_text}]({src})'
    
    return re.sub(pattern, replace_image, content)

def remove_first_level_headers(content):
    """移除内容中的一级标题（# 开头的标题）"""
    lines = content.split('\n')
    result_lines = []
    
    for line in lines:
        # 跳过一级标题（以单个 # 开头的行）
        if line.strip().startswith('# ') or line.strip() == '#':
            continue
        result_lines.append(line)
    
    return '\n'.join(result_lines)

def generate_front_matter(title, date_str, author="Gleipnir", tags=None, toc=True):
    """生成 Jekyll front matter"""
    if tags is None:
        tags = []
    
    front_matter = f"""---
layout: post
title: {title}
date: {date_str}
author: {author}
tags: [{', '.join(tags)}]
toc: {str(toc).lower()}
---

"""
    return front_matter

def process_markdown_file(file_path, output_dir, date_str, author, baseurl):
    """处理单个 Markdown 文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有 front matter
        if content.startswith('---'):
            print(f"跳过 {file_path.name} - 已包含 front matter")
            return
        
        # 提取标题
        title = extract_title_from_content(content)
        if not title:
            title = extract_title_from_filename(file_path.name)
        
        # 移除一级标题
        content = remove_first_level_headers(content)
        
        # 转换图片路径
        content = convert_image_paths(content, baseurl)
        
        # 生成新的文件名（带日期）
        date_prefix = date_str.replace('-', '-')
        new_filename = f"{date_prefix}-{file_path.name}"
        output_path = output_dir / new_filename
        
        # 生成 front matter
        front_matter = generate_front_matter(title, date_str, author)
        
        # 组合新内容
        new_content = front_matter + content
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ 转换完成: {file_path.name} -> {new_filename}")
        
    except Exception as e:
        print(f"✗ 处理 {file_path.name} 时出错: {e}")

def main():
    parser = argparse.ArgumentParser(description='将 Markdown 文件转换为 GitHub Pages 兼容格式')
    parser.add_argument('source_dir', help='源文件夹路径')
    parser.add_argument('--date', help='指定日期 (YYYY-MM-DD 格式)', 
                       default=datetime.now().strftime('%Y-%m-%d'))
    parser.add_argument('--author', help='作者名称', default='Gleipnir')
    parser.add_argument('--baseurl', help='GitHub Pages baseurl', default='/myBlog')
    parser.add_argument('--output', help='输出目录', default='_posts')
    
    args = parser.parse_args()
    
    # 检查源目录是否存在
    source_dir = Path(args.source_dir)
    if not source_dir.exists():
        print(f"错误: 源目录 '{args.source_dir}' 不存在")
        sys.exit(1)
    
    # 创建输出目录
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)
    
    # 验证日期格式
    try:
        datetime.strptime(args.date, '%Y-%m-%d')
    except ValueError:
        print(f"错误: 日期格式不正确，请使用 YYYY-MM-DD 格式")
        sys.exit(1)
    
    print(f"开始转换 Markdown 文件...")
    print(f"源目录: {source_dir}")
    print(f"输出目录: {output_dir}")
    print(f"日期: {args.date}")
    print(f"作者: {args.author}")
    print("-" * 50)
    
    # 查找所有 .md 文件
    md_files = list(source_dir.glob('*.md'))
    
    if not md_files:
        print("未找到任何 .md 文件")
        return
    
    print(f"找到 {len(md_files)} 个 Markdown 文件:")
    
    # 处理每个文件
    for md_file in md_files:
        process_markdown_file(md_file, output_dir, args.date, args.author, args.baseurl)
    
    print("-" * 50)
    print(f"转换完成！共处理 {len(md_files)} 个文件")
    print(f"输出目录: {output_dir.absolute()}")

if __name__ == '__main__':
    main() 