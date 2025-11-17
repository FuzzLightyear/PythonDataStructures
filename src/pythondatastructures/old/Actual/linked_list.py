#Author FuzzLightyear, aka. Fuzzifier, aka. SudoScientist
#Date 12/27/2020
#Linked List with added features. Stack, Queue built off of LinkedList

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
        
import networkx as nx
            
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
    
    def nx_node(self, G):
        data = {
            "label": f"{self.value}",
            "index": self.idx,
        }
        x = G.add_node(node_for_adding=self, **data)
        # x = nx.node(data)
        # G.add_node(x, **data)
        # nx.add_node(G, x)
        if (nxt:=self.nxt) is not None:
            data["next"] = nxt.idx
            nodes, edges = nxt.nx_node(G)
            
            # G.add_edge(x, nxt.nx_node(G))
            # nx.add_edge(G, x, nxt.nx_node(G))
            e = G.add_edge(x, nodes[0], **edges[0]) 
            nodes.append(x)
            edges.append(e)
            return nodes, edges
        return [x], []
    
    def nx_graph(self, G):
        node = G.add_node(self.value, index=self.idx)
        if (nxt:=self.nxt) is not None:
            x = nxt.nx_graph(G)
            G.add_edge(self.value, nxt.value)
            # G.add_edge(node, G.nodes[self.idx+1])

        return node
        
            
    
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
        
    def __iter__(self):
        n = [self.root]
        run = 1
        while n:
            print(n)
            yield n[0]
            old = n.pop(0)
            if (nxt:=old.nxt) is None:
                n = [nxt]

        
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
    
    def nx_graph(self):
        g = nx.DiGraph()
        if self.root is not None:
            # self.root.nx_node(G=g)
            self.root.nx_graph(G=g)
        g.graph["rankdir"] = "LR"
        g.graph["dpi"] = 100
        g.graph["nodesep"] = 0.5
        # g.plot = lambda: nx.nx_agraph.view_pygraphviz(g, prog="dot")
        # nx.draw(g, with_labels=True)
        # g.plot()
        return g
        
    
        
