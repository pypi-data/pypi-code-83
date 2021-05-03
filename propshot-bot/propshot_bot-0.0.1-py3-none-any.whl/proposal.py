from .utils import get_current_epoch
from .constants import EPOCH_LENGTH

class Proposal:
    """class for snapshot proposals 
    
    Asssumes new/active proposals will only be snapshot api version v0.1.3
    TODO: not assume this, for maybe the lingering longed open v0.1.2 but mainly to ready
          for next version support

    arguments:
    :ipfs_hash: (str) - ipfs hash string of snapshot proposal
    :proposal: (dict) - response from snapshot api as a dictionary
    """
    def __init__(self, ipfs_hash, proposal):

        self._ipfs_hash = ipfs_hash        # ipfs hash of the snapshot
        self._snapshot_proposal = proposal # raw response from snapshots as dictionary

    def __eq__(self, other):
        return self.ipfs_hash == other.ipfs_hash

    def __ne__(self, other):
        return not self.__eq__(other) 

    def __str__(self):
        return self.__dict__.__str__()

    def __hash__(self):
        return hash(self.ipfs_hash) 

    @property
    def version(self):
        """Returns the snapshot version of a proposal instance."""
        return str(self._snapshot_proposal['msg']['version'])

    @property
    def space(self):
        """Returns the space name for a proposal instance."""
        return str(self._snapshot_proposal['msg']['space'])

    @property
    def start_time(self):
        """Returns the start time as an epoch for a proposal instance."""
        return self._get_time('start')

    @property
    def end_time(self):
        """Returns the end time as an epoch for a proposal instance."""
        return self._get_time('end')

    @property
    def name(self):
        """Returns the name of a proposal instance."""
        return str(self._snapshot_proposal['msg']['payload']['name'])

    @property
    def body(self):
        """Returns the body of a proposal instance."""
        return str(self._snapshot_proposal['msg']['payload']['body'])

    @property
    def choices(self):
        """Returns a list of choices for a proposal instance."""
        return self._snapshot_proposal['msg']['payload']['choices']

    @property
    def ipfs_hash(self):
        """Returns the ipfs_hash of a proposal instance."""
        return str(self._ipfs_hash)

    def _get_time(self, time):
        """Return time epoch seconds as an int."""
        return int(self._snapshot_proposal['msg']['payload'][time])

    def is_active(self):
        """Returns true if voting is still allowed on proposal."""
        current_epoch = get_current_epoch(EPOCH_LENGTH) 
        return self.end_time > current_epoch

    def is_expired(self):
        """Returns true if voting is not allowed on proposal."""
        return not self.is_active()

    def time_until_expire(self):
        """Return seconds until voting is over."""
        return max(0, self.end_time - get_current_epoch(EPOCH_LENGTH)) 