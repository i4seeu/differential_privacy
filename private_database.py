import torch
num_entries = 5000
db = torch.rand(num_entries) > 0.5

def get_parallel_db(db,remove_index):
    return torch.cat((db[0:remove_index],db[remove_index+1:]))
#new_db = get_parallel_db(db,0)
#print(new_db[0:5])
#print(db[0:5])

def get_parallel_dbs(db):
    parallel_dbs = list()
    for i in range(len(db)):
        pdb = get_parallel_db(db,i)
        parallel_dbs.append(pdb)
    return parallel_dbs
#pdbs = get_parallel_db(db)
def create_db_and_paralles(n_entries):
    db = torch.rand(n_entries) > 0.5
    dbs = get_parallel_dbs(db)
    return db, dbs
db, dbs = create_db_and_paralles(5)

print(db)
print(dbs)