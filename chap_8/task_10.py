messages=["hello..","what's up?","Everything is good?","Nice to meet you!"]
sent_messages=[]
def send_messages(messages,sent_messages):
    while messages:
        current_messages=messages.pop(0)
        print(f"sending message : {current_messages}")
        sent_messages.append(current_messages)
send_messages(messages,sent_messages)
print("\nMessages list after sending : ")
print(messages)
print("\nSent messegas: ")
print(sent_messages)