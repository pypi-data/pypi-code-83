import time
from .constants import SNAPSHOT_PROPOSAL_URL, SNAPSHOT_PROPOSAL_API

def get_current_epoch(num_digits):
    """Return epoch time with length of num_digits."""
    return int(str(time.time_ns())[:num_digits]) 

def snapshot_proposal_url(proposal):
    """Returns the url for a specific snapshot proposal."""
    return SNAPSHOT_PROPOSAL_URL % (proposal.space, proposal.ipfs_hash)

def api_snapshot_proposal_url(space):
    """Returns the url to get the proposals from a snapshot space,"""
    return SNAPSHOT_PROPOSAL_API % space