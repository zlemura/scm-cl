import pickle

def write_to_dump_file(objects_to_serialize, file_name):
    file_name_to_apply = file_name + ".pkl"
    with open(file_name_to_apply, 'wb') as f:  # open a text file
        pickle.dump(objects_to_serialize, f)  # serialize the list
    f.close()

def open_dump_file(file_name):
    file_name_to_apply = file_name + ".pkl"
    with open(file_name_to_apply, 'rb') as f:
        results = pickle.load(f)  # deserialize using load()

    return results