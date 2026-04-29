import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def polish_article(article):
    prompt = f"""
请对以下文章进行优化：
- 提升表达流畅度
- 优化逻辑结构
- 使语言更有吸引力

文章：
{article}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
