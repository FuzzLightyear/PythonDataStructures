
FIELDS = {
    "forward": "nxt",
    "backward": "prev"
}

class Edge:
    def __set_name__(self, owner, name):
        self.name = name
        self.private = f"_{name}"
        for k, v in FIELDS.items():
            if k != name:
                self.converse = v
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.private]
    
    def __set__(self, instance, value):
        if value is None:
            if (nxt:=instance.__dict__.get(self.private)) is not None:
                print(f"Trying to set {instance}.{self.name} to None but the Node there has a next node {nxt}.")
            instance.__dict__[self.private] = None
            return
                
        if (old_next:=instance.__dict__.get(self.private)) is not None: # Ex. N1 -> N2 -> N3. setting N1.nxt to N4. If N2 exists
            setattr(value, self.name, old_next) # If N2, Make N4 -> N2 (and N2.prev = N4)
        instance.__dict__[self.private] = value # Make N1.nxt = N4
        value.__dict__[self.converse] = instance # Make N4.prev = N1
        
    def __delete__(self, instance): # ex. N1 -> N2 -> (N3)?. `del N1.nxt`
        if (nxt:=instance.__dict__.pop(self.private)) is not None: # if there is a next node (N2). Should always be since this is when deleting instance.nxt
            if (nxtnxt:=nxt.__dict__.pop(self.private)) is not None: # If next node (N2) has a next node (N3)

                self.__set__(instance, nxtnxt) # Fold over N1 to N3. N1.nxt = N3 and N3.prev = N1
                del nxt
                return
            del nxt # ex for this case. N1 -> N2. `del N1.nxt`
            return
        print(f"Trying to delete {instance}.{self.name} but there is no next node.")
        instance.__dict__[self.private] = None

class ChainNodeMixin(object):
    
    nxt = Edge()
    prev = None
    
    def __init__(self):
        self._nxt = None 
        self.prev = None
            
class Node(ChainNodeMixin):
    value = None 

    def __init__(self, value):
        super().__init__()
        self.value = value
    
    @property
    def idx(self):
        if self.prev is None:
            return 0
        return self.prev.idx + 1
    
    def __len__(self):
        if (nxt:=self.nxt) is None:
            return self.idx + 1
        return len(nxt)
    
    def create(self, new_val):
        return Node(new_val)
    
    def insert(self, new_val):
        nn = self.create(new_val) if not isinstance(new_val, Node) else new_val
        self.nxt = nn
        return nn
        
    def insert_at(self, node, i: int):
        if self.idx < i-1:
            if (nxt:=self.nxt) is not None:
                return nxt.insert_at(node, i)
            return None
        else:
            return self.insert(node)
        
    def append(self, node):
        if (nxt:=self.nxt) is not None:
            return nxt.append(node)
        self.nxt = node if isinstance(node, Node) else self.create(node)
    
    def get(self, value, /, default=None):
        if value == self.value: return self
        if (nxt:=self.nxt) is None:
            return default
        return self.nxt.get(value)
    
    def __repr__(self):
        indent = "  " * self.idx
        return f"{indent}([{self.idx}] Node: {self.value})"
    
    def __str__(self): 
        indent = "  " * self.idx
        return f"{indent}([{self.idx}] Node: {self.value})"
    
    def __hash__(self):
        return hash(self.value)
    
    
class LL(object):
    root = None
    
    def __init__(self, root):
        self.root = root if isinstance(root, Node) else Node(root)
        
    def insert_at(self, node, i: int):
        if not isinstance(node, Node):
            node = Node(node)
        if i == 0:
            getattr(node.__class__, "nxt").__set__(node, self.root)
            # node.nxt.__set__(node, self.root)
            # node.nxt = self.root
            self.__dict__["root"] = node
            return
        self.root.insert_at(node, i)

    append = lambda instance, node: instance.root.append(node)
    get = lambda instance, value, /, default=None: instance.root.get(value, default)
    
        

l = LL(1)

for i in range(2, 10):
    l.root.append(Node(i))
    print(len(l.root))
    
    