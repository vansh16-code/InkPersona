import os
from openai import OpenAI

client = OpenAI(
    api_key= "",  
    base_url="https://api.together.xyz/v1"
)

def generate_response(character_name: str, character_description: str, question: str) -> str:
    prompt = f"""You are {character_name}.
{character_description}

Answer the following question directly based on your personality and experiences. Only give the answer, nothing else.

Question: {question}
Answer:"""

    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )

        # Safe check
        if response and response.choices and response.choices[0].message.content:
            return response.choices[0].message.content.strip()
        else:
            return "[No valid response received from LLaMA]"

    except Exception as e:
        return f"[Error occurred: {str(e)}]"
