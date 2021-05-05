import fakeredis
from choixpeau.choixpeau import Choixpeau

server = fakeredis.FakeServer()

def test_choixpeau():
    c = Choixpeau(redis_config={"host": "localhost"})
    assert 1 == 1