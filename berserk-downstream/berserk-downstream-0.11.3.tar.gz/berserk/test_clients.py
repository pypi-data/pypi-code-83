import config
from berserk import session
from berserk import clients
from berserk import enums

session = session.TokenSession(config.API_KEYS['ADMIN_LICHESS_TOKEN'])
lichess = clients.Client(session=session)

x = lichess.challenges.decline("WTftZ640", reason=enums.Reason.LATER)
print(x)
