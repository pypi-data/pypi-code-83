import os
import pickle
import requests
import time

from sys import maxsize 

from .proposal import Proposal
from .utils import get_current_epoch, api_snapshot_proposal_url
from .constants import ALERT_TIME, ALERT_COLOR, ALERT_THRESHOLDS


class ProposalMonitor():
    """
    class to track active snapshot proposals.

    an 'Active' proposal is defined as voting is currently allowed on that proposal. 
        Which is decided on the proposals end_time epoch is less than current time epoch. 

    arguments:
    :spaces: (list of str) - list of snapshot spaces to monitor proposals
    :alert_thresholds: (a list of 2-tuples) 
        ~ The 2-tuples define thresholds that dictate when to alert a proposal. The 2-tuples 
          first element is number of seconds until voting is closed and the second element is 
          a hex color to associate with. The list is expected to be in ascending order
          of until voting is closed (first element). See constants.py for default values.
    """

    def __init__(self, **kwargs):
        self._proposals = set()  # all proposals 
        self._active    = set()  # active proposals
        self._spaces    = kwargs.get('spaces', os.getenv('SPACES').split(' ')) # snapshot spaces
        self._alert_thresholds = kwargs.get('alert_thresholds', ALERT_THRESHOLDS)

    def _get(self, url):
        """Return the respone from url as a dict."""
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()

    def get_proposal_color(self, proposal):
        """Get the color associated with alert_threshold of a proposal."""
        return self._alert_thresholds[proposal.last_alert_index][ALERT_COLOR]

    def clean_actives(self):
        """Remove expired proposals from self._active."""
        for expired in self.expired_proposals():
            self._active.remove(expired)

    def active_proposals(self):
        """Return a set of active proposals in self._proposal."""
        return set(filter(lambda prop: prop.is_active(), self._proposals))

    def expired_proposals(self):
        """Return a set of expired proposls in self._active."""
        return set(filter(lambda prop: prop.is_expired(), self._active))

    def update_proposals(self):
        """Updates self._proposals set and self._active proposals."""
        proposals = {}
        for space in self._spaces:
            url = api_snapshot_proposal_url(space)
            try:
                space_proposals = self._get(url)
                proposals.update(space_proposals)
            except: # service 503, skip proposal update 
                pass
        
        for ipfs_hash in proposals:
            proposal = Proposal(ipfs_hash, proposals[ipfs_hash])
            if proposal not in self._proposals:
                self._proposals.add(proposal)
            if proposal.is_active():
                self._active.add(proposal)

    def _alert_index(self, proposal):
        """Get the index of the lowest alert threshold index for proposal.
        This function assumes self._alert_thresholds is sorted in ascending order of the alert times.

        arguments:
        :proposal: (Proposal) - proposal to decide its current alert threshold index
        """
        alert_threshold_index = 0
        time_to_expire = proposal.time_until_expire()
        for idx, threshold in enumerate(self._alert_thresholds):
            if time_to_expire <= threshold[ALERT_TIME]: 
                alert_threshold_index = idx 
                break
        return alert_threshold_index 

    def needs_alert(self, proposal):
        """Returns True if the proposal time until expire is in a new alert threshold or newly active.
        Sets attribute on proposal for 'last_alert_index'.

        arguments:
        :proposal: (Proposal) - proposal under consideration for alert

        """
        if (proposal not in self._active) and proposal.is_expired():
            return False
        update_alert = True 
        alert_threshold_index = self._alert_index(proposal)
        if hasattr(proposal, 'last_alert_index'):
            update_alert = alert_threshold_index < proposal.last_alert_index
        proposal.last_alert_index = alert_threshold_index
        return update_alert

    def get_proposals_to_alert(self):
        """Return proposals that have triggered an alert by entering a new alert threshold."""
        self.update_proposals()
        to_alert = set()
        expired = False
        for proposal in self._active:
            needs_alert = self.needs_alert(proposal)
            if needs_alert:
                to_alert.add(proposal)
            if proposal.is_expired():
                to_alert.add(proposal) 
                expired = True 
        # remove expired proposals from actives
        if expired:
            self.clean_actives()
        return to_alert

    def _pickle_filename(self, persistent_location):
        """Returns the path to the name of the pickled instance"""
        return os.path.join(persistent_location, 'pickled_proposal_monitor')

    def dump(self, persistent_location):
        """Pickles instance to persistent_location.

        arguments:
        :persistent_location: (str) - filepath to dump pickled instance
        """
        pickle_filename = self._pickle_filename(persistent_location)
        with open(pickle_filename, 'wb') as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, persistent_location):
        """Load pickled instance into the instance.
        NOTE: configurations should happen after calling loads otherwise they will be lost
        
        arguments:
        :persistent_location: (str) - filepath to pickled instance to be loaded
        """
        pickle_filename = self._pickle_filename(persistent_location)
        if not os.path.exists(pickle_filename):
            return 
        with open(pickle_filename, 'rb') as f:
            stored = pickle.load(f)
        if isinstance(stored, self.__class__):
            self._proposals = stored._proposals
            self._active = stored._active
            self._alert_thresholds = stored._alert_thresholds
            self._spaces = stored._spaces