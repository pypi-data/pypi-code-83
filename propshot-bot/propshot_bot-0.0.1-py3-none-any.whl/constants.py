import os
from sys import maxsize 

SNAPSHOT_PROPOSAL_URL = "https://snapshot.org/#/%s/proposal/%s"
SNAPSHOT_PROPOSAL_API = "https://hub.snapshot.org/api/%s/proposals"

CHECK_FREQUENCY = int(os.getenv('CHECK_FREQUENCY', 300)) # 5 minutes
EPOCH_LENGTH = 10 # length proposals snapshots uses

# times and color pairs for alert thresholds
EXPIRED=0
ONE_DAY=86400
TWO_DAYS=2*ONE_DAY
FOUR_HOURS=ONE_DAY/6
END_OF_TIME=maxsize
COLORS = {
    'RED':    0xff0000,
    'ORANGE': 0xffa500,
    'YELLOW': 0xffff00,
    'GREEN':  0x00ff00,
    'BLUE':   0x0000ff,
    'PURPLE': 0x301c78,
    'BLACK':  0x000000,
}
ALERT_TIME=0
ALERT_COLOR=1
ALERT_THRESHOLDS = [
    (EXPIRED,     COLORS['BLACK']),   # 0 time left
    (FOUR_HOURS,  COLORS['RED']),     # <4 hours left
    (ONE_DAY,     COLORS['ORANGE']),  # <1 day left
    (TWO_DAYS,    COLORS['YELLOW']),  # <2 days left
    (END_OF_TIME, COLORS['GREEN'])    # >2 days left
]
