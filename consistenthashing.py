import hashlib
import requests
from os.path import exists
from bisect import bisect_right, bisect
from utilities.storagenode import StorageNode, servers


def hash_fn(key, total_slots):
    sha = hashlib.sha256()
    sha.update(bytes(key,'utf-8'))
    return int(sha.hexdigest(), 16) % total_slots


class ConsistentHash:
    def __init__(self):
        self._keys = []  # indexes taken on the ring
        self.nodes = []  # nodes in the ring
        self.total_slots = 3000

    def add_node(self, node):
        if len(self._keys) == self.total_slots:
            raise Exception('Full')

        key = hash_fn(node.host, self.total_slots)
        index = bisect(self._keys, key)

        if index > 0 and self._keys[index - 1] == key:
            raise Exception('Collision Detected')

        self.nodes.insert(index, node)
        self._keys.insert(index, key)
        return key

    def upload(self, file_name):
        key = hash_fn(file_name, self.total_slots)
        index = bisect_right(self._keys, key)

        file = {'avatar': open(file_name, 'rb')}
        host = self.nodes[index].host
        name = self.nodes[index].name

        print(f'Uploading: {file_name} To: {name} Host: {host}')
        return requests.post(f'http://{host}/upload-avatar', files=file).text


ch = ConsistentHash()


# Add the available servers to the pool
for node in servers:
    ch.add_node(node)

# Upload File
for i in range(10):
    if not exists(f'newPic_{i}.txt'):
        f = open(f'newPic_{i}.txt', 'x')
    ch.upload(f'newPic_{i}.txt')
