def battle(prompt):
    msgs = [{"role":"user","content":prompt}]
    # A - OpenAi's gpt model
    a = openai_client.chat.completions.create(model="openai/gpt-oss-120b",messages=msgs)
    # B - Llama on groq(same code, different brain)
    b= groq_client.chat.completions.create(model="llama-3.3-70b-versatile",messages=msgs)
    
    return a.choices[0].message.content, b.choices[0].message.content