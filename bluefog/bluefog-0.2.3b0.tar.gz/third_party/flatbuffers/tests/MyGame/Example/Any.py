# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

class Any(object):
    NONE = 0
    Monster = 1
    TestSimpleTableWithEnum = 2
    MyGame_Example2_Monster = 3


def AnyCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == Any().Monster:
        import MyGame.Example.Monster
        return MyGame.Example.Monster.MonsterT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == Any().TestSimpleTableWithEnum:
        import MyGame.Example.TestSimpleTableWithEnum
        return MyGame.Example.TestSimpleTableWithEnum.TestSimpleTableWithEnumT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == Any().MyGame_Example2_Monster:
        import MyGame.Example2.Monster
        return MyGame.Example2.Monster.MonsterT.InitFromBuf(table.Bytes, table.Pos)
    return None
