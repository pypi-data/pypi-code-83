class Subnode(list):
    pass

def nocolor(s): 
    return s

class ParseTree(list):
    tag: str
    source: str
    spos: int
    epos: int
    urn: str
    child: Subnode

    def init(self, tag, source, spos=0, epos=None, urn='(unknown source)'):
        self.tag = tag
        self.source = source
        self.spos = spos
        self.epos = epos if epos is not None else len(source)
        self.urn = urn
        self.child = None

    def getTag(self):
        return self.tag

    def isSyntaxError(self):
        return self.tag == 'err'

    def __eq__(self, tag):
        return self.tag == tag if isinstance(tag, str) else self is tag

    def getPosition(self):
        return rowcol(self.urn, self.source, self.spos)

    def getEndPosition(self):
        return rowcol(self.urn, self.source, self.epos)

    def decode(self):
        source, spos, epos = self.source, self.spos, self.epos
        LF = b'\n' if isinstance(source, bytes) else '\n'
        rows = source[:spos + (1 if len(source) > spos else 0)]
        rows = rows.split(LF)
        linenum, column = len(rows), len(rows[-1])-1
        begin = source.rfind(LF, 0, spos) + 1
        # print('@', spos, begin, source)
        end = source.find(LF, spos)
        # print('@', spos, begin, source)
        if end == -1:
            end = len(source)
        # print('@[', begin, spos, end, ']', epos)
        line = source[begin:end]  # .replace('\t', '   ')
        mark = []
        endcolumn = column + (epos - spos)
        for i, c in enumerate(line):
            if column <= i and i <= endcolumn:
                mark.append('^' if ord(c) < 256 else '^^')
            else:
                mark.append(' ' if ord(c) < 256 else '  ')
        mark = ''.join(mark)
        return (self.urn, spos, linenum, column, line, mark)

    def message(self, msg='Syntax Error'):
        urn, pos, linenum, cols, line, mark = self.decode()
        return '{} ({}:{}:{}+{})\n{}\n{}'.format(msg, urn, linenum, cols, pos, line, mark)

    # def subs(self):
    #     es = []
    #     for i, child in enumerate(self):
    #         es.append((child.spos, '', child))
    #     for key in self.dict:
    #         v = self.dict[key]
    #         if isinstance(v, ParseTree):
    #             es.append((v.spos, key, v))
    #     es.sort()
    #     return [(x[1], x[2]) for x in es]

    def isEmpty(self):
        return self.tag == 'empty'

    def newEmpty(self):
        return ParseTree('empty', self.source, self.epos, self.epos, self.urn)

    def set(self, key, tree):
        assert isinstance(tree, ParseTree)
        if self.child is None:
            self.child = Subnode()
        if key == '':
            self.child.append(tree)
        else:
            setattr(self.child, key, tree)
    
    def getNodeSize(self):
        return 0 if self.child is None else len(self.child)
    
    def __len__(self):
        return 0 if self.child is None else len(self.child)

    def getSubNodes(self):
        return [] if self.child is None else list(self.child)

    def __contains__(self, key):
        if self.child is not None:
            if isinstance(key, str):
                return hasattr(self.child, key)
            elif isinstance(key, int):
                return 0 <= key < len(self.child) or -len(self.child) < key <= -1:
        return False
    
    def has(self, key):
        return self.__contains__(key)

    def __getitem__(self, key):
        if self.child is not None:
            if isinstance(key, str):
                return getattr(self.child, key)
            else:
                return self.child[key]
        return self.NoChild(key)

    def get(self, key):
        return self.__getitem__(key)

    def find(self, *key):
        if self.child is not None:
            for key in keys:
                if key in self:
                    return self[key]
        return self.NoChild(key)
    
    def keys(self):
        if self.child is not None:
            return self.child.__dict__.keys()

    def getToken(self, key=None, default_token=''):
        if key is None:
            s = self.source[self.spos:self.epos]
            return s
        return self[key].getToken() if key in self else default_token

    # def substring(self, start=None, end=None):
    #     if start is None:
    #         if end is None:
    #             return self.getToken()
    #         s = self.source[end.epos:self.epos]
    #     else:
    #         if end is None:
    #             s = self.source[self.spos: start.spos]
    #         else:
    #             s = self.source[start.epos:end.spos]
    #     return s.decode('utf-8') if isinstance(s, bytes) else s

    def str(self):
        s = self.source[self.spos:self.epos]
        return str(s)

    def allEdges(self):
        if self.child is not None:
            edges = []
            for n, tree in enumerate(self.child):
                edges.append((tree.spos, n, tree))
            for edge in self.child.__dict__:
                tree =  self.child.__dict__[edge]
                edges.append((tree.spos, edge, tree))
            edges.sort()
            return edges
        return []

    def repr(self):
        if self.isSyntaxError():
            return self.message('Syntax Error')
        sb = []
        self.strOut(sb, indent='', tab='')
        return "".join(sb)

    def strOut(self, sb, indent='\n  ', tab='  ', prefix='', tag=nocolor, edge=nocolor, token=nocolor):
        sb.append(indent + prefix + "[" + tag(f'#{self.getTag()} '))
        edges = self.allEdges()
        if len(edges) > 0:
            nextindent = indent + tab
            for _, label, child in edges:
                prefix = edge(label) + ': ' if isinstance(label, str) else ''
                child.strOut(sb, nextindent, tab, prefix, tag, edge, token)
            sb.append(indent + "]")
        else:
            sb.append(token(repr(str(self))))
            sb.append("]")
    
    def dump(self, indent='\n', tab='  ', tag=nocolor, edge=nocolor, token=nocolor):
        if self.isSyntaxError():
            print(self.message('Syntax Error'))
        else:
            sb = []
            self.strOut(sb, indent, tab, '', tag, edge, token)
            print("".join(sb))

def rowcol(urn, source, spos):
    source = source[:spos + (1 if len(source) > spos else 0)]
    rows = source.split(b'\n' if isinstance(source, bytes) else '\n')
    return len(rows), len(rows[-1])-1


if __name__ == '__main__':
    t = ParseTree