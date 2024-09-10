"""
Copyright (c) 2024 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Joel Jose <joeljos@cisco.com>"
__copyright__ = "Copyright (c) 2024 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import requests

#10.103.1.182:32722
    
def dochat(prompt,llm="llama3",type="prompt"):
    if(llm=="gemma"):
        url = 'http://10.103.1.181:31256/v1/chat/completions'
        model = "google/gemma-2-9b-it"
        
        
    elif(llm=="llama3"):
        url = 'http://10.103.1.181:30482/v1/chat/completions'
        model = "meta/llama3-8b-instruct"
    #elif(llm=="llama3.1"):
    #    url = '10.103.1.182:32722/v1/chat/completions'
    #    model = "meta/llama3.1-8b-instruct"
    else:
        return "Given LLM not found."
        

    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
    }
    messages = []
    if(type=="prompt" and (llm=="llama3.1" or llm=="llama3")):
        messages = [
                        {
                            "role": "system",
                            "content": "You are a Cisco Infrastructure Expert."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
    elif(type=="prompt" and llm=="gemma"):
        messages = [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
    else:
        messages = prompt
    data = {
        "messages": messages,
        "model": model,
        "max_tokens": 3000,
        "top_p": 0.5,
        "n": 1,
        "stream": False,
        "temperature": 0.1,
        "seed":1
    }
    # Create a chat completion
    try:
        #print("data:",data,llm)
        response = requests.post(url, headers=headers, json=data)
        chat_completion = response.json()
        #print("chat_completion:",chat_completion)
        return chat_completion['choices'][0]['message']['content']
    except Exception as e:
        return str(e)

if(__name__=="__main__"):
    print(dochat("Explain the best part about Cisco in a single sentence","gemma"),"gemma")
    print(dochat("Explain the best part about Cisco in a single sentence","llama3"),"llama3")
    print(dochat("Explain the best part about Cisco in a single sentence","llama3.1"),"llama3.1")