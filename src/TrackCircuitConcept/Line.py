from src.TrackCircuitConcept.Rail import RailGroup


class Line:
    """
        线路类型
    """

    def __init__(self, parent, bas_name, **kwargs):
        self.parent = parent
        self._bas_name = bas_name
        self._name = None
        self.rails = RailGroup()
        self.element = list()

        self.load_kwargs(**kwargs)

    @property
    def rlt_pos(self):
        return 0

    @property
    def abs_pos(self):
        return 0

    def add_element(self, ele):
        self.element.append(ele)
        ele.parent = self

    @property
    def bas_name(self):
        if self._bas_name is None:
            return ''
        else:
            return self._bas_name

    @property
    def name(self):
        if self.parent is None:
            return self.bas_name
        else:
            name = self.parent.name + '_' + self.bas_name
            self._name = name
            return name

    def load_kwargs(self, **kwargs):
        if 'rails' in kwargs:
            rails = kwargs['rails']
            if isinstance(rails, RailGroup):
                self.rails = rails

        if 'elements' in kwargs:
            elements = kwargs['elements']
            for ele in elements:
                self.add_element(ele)


class LineGroup:
    """
        线路组类型
    """

    def __init__(self, parent, bas_name, **kwargs):
        self.parent = parent
        self._bas_name = bas_name
        self._name = None
        self.lines = list()

        self.load_kwargs(**kwargs)

    @property
    def bas_name(self):
        if self._bas_name is None:
            return ''
        else:
            return self._bas_name

    @property
    def name(self):
        if self.parent is None:
            return self.bas_name
        else:
            name = self.parent.name + '_' + self.bas_name
            self._name = name
            return name

    def add_line(self, line):
        if isinstance(line, Line):
            self.lines.append(line)
            line.parent = self

    def load_kwargs(self, **kwargs):
        if 'lines' in kwargs:
            lines = kwargs['lines']
            for line in lines:
                if isinstance(line, Line):
                    self.add_line(line)