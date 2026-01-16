

import chromadb

client = chromadb.PersistentClient(path="./chromadb")

collection = client.get_or_create_collection("docs")


with open("k8s.txt", "r") as file:
  text = file.read()


collection.upsert(documents=[text], ids=["k8s"])

print("Embedding stored in Chroma")




