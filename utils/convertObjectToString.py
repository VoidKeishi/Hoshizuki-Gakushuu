def convertObjectToString(objectConversations):
  conversation = ""
  for objectConversation in objectConversations:
    if (objectConversation["role"] == "system"):
      continue
    conversation = conversation + objectConversation["role"] + ":  " + objectConversation["content"] + "\n"
  conversation = conversation + "\n"  

  return conversation