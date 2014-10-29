import json
from utils.config import DEFAULT


def write_to_json(**entry):

    path = DEFAULT.get('env_obj_storage_path')
    f1 = open(path, 'r')
    output = json.loads(''.join(f1.readlines()))
    f1.close()

    output.update(entry)

    f2 = open(path, 'w')
    f2.write(json.dumps(output))
    f2.close


def delete_from_json(key=None):

    path = DEFAULT.get('env_obj_storage_path')
    f1 = open(path, 'r')
    output = json.loads(''.join(f1.readlines()))
    f1.close()

    del output[key]

    f2 = open(path, 'w')
    f2.write(json.dumps(output))
    f2.close


def read_json():

    path = DEFAULT.get('env_obj_storage_path')
    f1 = open(path, 'r')
    output = json.loads(''.join(f1.readlines()))
    f1.close()

    return output