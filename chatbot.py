from groq import Groq

client = Groq(
    api_key="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"
)

def get_chatbot_response(prompt):

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"