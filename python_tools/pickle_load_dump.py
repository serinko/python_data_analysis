"""Pickle - basic import and export"""

import pickle 
#with open("data.pckl", "w") as f:
#    pickle.dump(data,f)

objects = []

with open("~/src/narodnik/coins-price-jan-mar-22.pkl", "rb") as f:
#    data = pickle.load(f)
    while True:
        try:
            objects.append(pickle.load(f))
        except EOFError:
            break
print(objects)
