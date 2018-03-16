class LRUNode:
    def __init__(self, key=None, val=None):
        self.value = val
        self.key = key
        self.next = None
        self.prev = None

class LRUList:
    def __init__(self):                                         
        self.head = LRUNode()
        self.tail = LRUNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        #node is always added to front
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def pop(self):
        node = self.tail.prev
        #cache is empty
        if node == self.head:
            return
        self.delete(node)
        return node
    
    def make_recent(self, node):
        self.delete(node)
        self.insert(node)

        
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lru_list = LRUList()
        self.lru_map = {}
        self.capacity = capacity    
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru_map:
            node = self.lru_map[key]
            self.lru_list.make_recent(node)
            return node.value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # cache hit
        if key in self.lru_map:
            node = self.lru_map[key]
            node.value = value
            self.lru_list.make_recent(node)
        else:
            # cache full? pop lru item
            if len(self.lru_map) == self.capacity:
                node = self.lru_list.pop()
                del self.lru_map[node.key]
            node = LRUNode(key=key, val=value)
            self.lru_list.insert(node)
            self.lru_map[key] = node