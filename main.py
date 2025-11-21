import requests
import datetime
import os

def get_quote():
    """抓取每日编程名言"""
    try:
        # 使用一个免费公开的 API 获取名言
        response = requests.get("https://api.quotable.io/random?tags=technology,programming")
        if response.status_code == 200:
            data = response.json()
            return f"> **\"{data['content']}\"** \n>\n> — *{data['author']}*"
    except Exception as e:
        print(f"Error fetching quote: {e}")
    
    # 如果抓取失败，返回默认备选
    return "> **\"Code is like humor. When you have to explain it, it’s bad.\"** \n>\n> — *Cory House*"

def update_readme(quote):
    """更新 README.md 内容"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    readme_content = f"""
# 🤖 Daily Auto-Digest

这里是我的自动化每日看板，每天由 GitHub Actions 自动更新。

## 📅 今日更新 ({current_time})

### 💡 每日编程名言
{quote}

---
*Last Automated Update: {current_time}*
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    quote = get_quote()
    update_readme(quote)
    print("README updated successfully.")
