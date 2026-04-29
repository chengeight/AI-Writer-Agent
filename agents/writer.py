import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def write_article(topic, outline):
    prompt = f"""
根据以下主题和大纲写一篇完整文章：

主题：{topic}

大纲：
{outline}

要求：
- 结构清晰
- 内容有逻辑
- 语言自然
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
