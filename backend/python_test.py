# backend/python_basics.py
name = "学习 Agent"
week = 1
finished = False
messages = [
 {"role": "system", "content": "你是一名老师"},
 {"role": "user", "content": "什么是 Agent？"},
]
for message in messages:
 print(message["role"], "=>", message["content"])
 name = "学习 Agent"