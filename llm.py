import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com")

def ask_ai(system_prompt, user_input):
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    return response.choices[0].message.content
if __name__ == "__main__":

    result = ask_ai(
        "你是Python导师",
        "我学Python三个月不会做项目"
    )

    print(result)