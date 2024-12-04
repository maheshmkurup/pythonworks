text=["apple","iphone","orange","pottatto"]

long=max([len(w) for w in text])

longest=[w for w in text if len(w)==long]

print(longest)

