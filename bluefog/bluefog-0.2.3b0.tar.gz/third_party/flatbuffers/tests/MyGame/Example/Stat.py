# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Stat(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsStat(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Stat()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def StatBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4D\x4F\x4E\x53", size_prefixed=size_prefixed)

    # Stat
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Stat
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Stat
    def Val(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # Stat
    def Count(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

def StatStart(builder): builder.StartObject(3)
def StatAddId(builder, id): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)
def StatAddVal(builder, val): builder.PrependInt64Slot(1, val, 0)
def StatAddCount(builder, count): builder.PrependUint16Slot(2, count, 0)
def StatEnd(builder): return builder.EndObject()


class StatT(object):

    # StatT
    def __init__(self):
        self.id = None  # type: str
        self.val = 0  # type: int
        self.count = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        stat = Stat()
        stat.Init(buf, pos)
        return cls.InitFromObj(stat)

    @classmethod
    def InitFromObj(cls, stat):
        x = StatT()
        x._UnPack(stat)
        return x

    # StatT
    def _UnPack(self, stat):
        if stat is None:
            return
        self.id = stat.Id()
        self.val = stat.Val()
        self.count = stat.Count()

    # StatT
    def Pack(self, builder):
        if self.id is not None:
            id = builder.CreateString(self.id)
        StatStart(builder)
        if self.id is not None:
            StatAddId(builder, id)
        StatAddVal(builder, self.val)
        StatAddCount(builder, self.count)
        stat = StatEnd(builder)
        return stat
