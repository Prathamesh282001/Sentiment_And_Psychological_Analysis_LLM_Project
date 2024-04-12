import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def analyze_text(text):
    prompt = f""" Based on the context provided below, analyze the sentiment and offer psychological insights about the speakers.
    For instance, identify emotional cues and provide interpretations about their personalities, attitudes, or emotional states.
    Avoid generic summaries or keyword extraction. Your output should delve into the nuances of the conversation, 
    providing deeper insights into the speakers' sentiments and psychological dispositions.
    
    CONTEXT : {text}

    Example : {{Input =  "Hello, Dave. How are you? , Hi, Joseph. I’m good. Yesterday went for a run. What about you? , I’m fine. Today I will read a book. I like reading."
            Output = [speaker2]  likes a sport. It seems he cares about his health’. ‘[Speaker_1] pretends to be smart’.}}
    """

    OpenAI().api_key = os.getenv("OPENAI_API_KEY")
    messages = [
        {"role":"system","content":prompt},
        {"role":"user","content":text}
    ]

    response = OpenAI().chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.1,

    )
    messages.append({"role":"assistant","content":response})

    return response.choices[0].message.content
