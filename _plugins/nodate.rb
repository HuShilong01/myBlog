# Jekyll插件：支持无日期的文件名
# 基于 https://mrinalcs.github.io/remove-date-from-jekyll-posts

class Jekyll::PostReader
  def read_posts(dir)
    read_publishable(dir, "_posts", /.*\.(markdown|md)$/)
  end
  
  def read_drafts(dir)
    read_publishable(dir, "_drafts", /.*\.(markdown|md)$/)
  end
end 