from src.CircuitConcept.Node import Node


class NodeSet(set):
    """
        节点集合
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pos_set = set()
        self._name_list = list()

    def add(self, obj):
        if isinstance(obj, Node):
            super().add(obj)
        else:
            raise KeyboardInterrupt("%s应为Node类型" % obj)

    def update(self, obj):
        if isinstance(obj, NodeSet):
            super().update(obj)
        else:
            raise KeyboardInterrupt("%s应为NodeSet类型" % obj)
