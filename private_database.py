import torch
num_entries = 5000
db = torch.rand(num_entries) > 0.5

def get_parallel_db(db,remove_index):
    return torch.cat((db[0:remove_index],db[remove_index+1:]))
new_db = get_parallel_db(db,0)
print(new_db[0:5])
print(db[0:5])