from openai import OpenAI

client = OpenAI(api_key='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')

# Set your OpenAI GPT-3 API key
def get_completion(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Extract the generated response from the OpenAI API response
    chat_response = response.choices[0].message.content
    return chat_response
