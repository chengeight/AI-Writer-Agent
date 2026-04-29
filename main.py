from agents.planner import generate_outline
from agents.writer import write_article
from agents.editor import polish_article

def run_agent(topic):
    print(f"\n🧠 Topic: {topic}\n")

    outline = generate_outline(topic)
    print("📌 Outline:")
    print(outline)

    draft = write_article(topic, outline)
    print("\n✍️ Draft:")
    print(draft)

    final = polish_article(draft)
    print("\n✅ Final Article:")
    print(final)

    return final

if __name__ == "__main__":
    topic = input("请输入写作主题: ")
    run_agent(topic)
