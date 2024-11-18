from langserve import RemoteRunnable

chain = RemoteRunnable("http://localhost:8000/chain/c/N4XyA")
res=chain.invoke({"language":"Hindi","text":"Election is comming soon so every polititian is trying to attract peaople for votes"})
print(res)