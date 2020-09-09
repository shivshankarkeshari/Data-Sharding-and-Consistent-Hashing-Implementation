class StorageNode:
    def __init__(self, name=None, host=None):
        self.name = name
        self.host = host


servers = [
    StorageNode(name='A', host='aserver1.local:3000'),
    StorageNode(name='B', host='bserver2.local:3001'),
    StorageNode(name='C', host='cserver3.local:3002'),
    StorageNode(name='D', host='dserver4.local:3003'),
    StorageNode(name='E', host='eserver5.local:3004'),
    StorageNode(name='F', host='fserver6.local:3005'),
    StorageNode(name='G', host='gserver7.local:3006'),
    StorageNode(name='H', host='hserver8.local:3007'),
    StorageNode(name='I', host='iserver9.local:3008'),
    StorageNode(name='J', host='jserver10.local:3009'),
]
