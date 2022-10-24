import pickle 

with open("data.pckl", "w") as f:
    pickle.dump(data,f)

with open("data.pckl") as f:
    data = pickle.load(f)
