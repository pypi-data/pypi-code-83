"""PubSub Events.

Declare here all PubSub topics which will be used.

These Topics will be created on AWS, when you send his first message.

"""
from enum import Enum


class UserEvents(Enum):
    USER_REGISTERED = "user_registered"
    USER_ACTIVATED = "user_activated"
    USER_LOGGED_IN = "user_logged_in"


class AccountEvents(Enum):
    BANK_ACCOUNT_REGISTERED = "bank_account_registered"
    AD_ACCOUNT_REGISTERED = "google_ad_account_registered"


class ProposalEvents(Enum):
    PROPOSAL_SELECTED = "proposal_selected"
    PROPOSAL_APPROVED = "proposal_approved"
