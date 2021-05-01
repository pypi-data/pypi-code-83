import dataclasses
import datetime

from typing import Any, Dict, List, Optional


@dataclasses.dataclass(frozen=True)
class User:
  username: str
  last_name: str
  friends_count: Optional[int]
  is_group: bool
  is_active: bool
  trust_request: Optional[bool]
  phone: Optional[str]
  profile_picture_url: str
  is_blocked: bool
  id: str
  identity: Optional[str]
  date_joined: datetime.datetime
  about: str
  display_name: str
  first_name: str
  friend_status: str
  email: str
  is_payable: bool
  identity_type: str
  is_venmo_team: bool = False

  @classmethod
  def new(cls, **data: Dict[str, Any]) -> 'User':
    data = dict(
        data,
        date_joined=datetime.datetime.fromisoformat(data['date_joined']))
    return cls(**data)


@dataclasses.dataclass(frozen=True)
class Merchant:
  braintree_merchant_id: str
  datetime_updated: datetime.datetime
  display_name: str
  image_datetime_updated: datetime.datetime
  is_subscription: bool
  image_url: str
  paypal_merchant_id: str
  id: str
  datetime_created: datetime.datetime

  @classmethod
  def new(cls, braintree_merchant_id, datetime_updated, display_name,
      image_datetime_updated, is_subscription, image_url, paypal_merchant_id,
      id, datetime_created) -> 'User':
    datetime_updated = datetime.datetime.fromisoformat(datetime_updated)
    image_datetime_updated = datetime.datetime.fromisoformat(image_datetime_updated)
    datetime_created = datetime.datetime.fromisoformat(datetime_created)
    return cls(braintree_merchant_id, datetime_updated, display_name,
        image_datetime_updated, is_subscription, image_url, paypal_merchant_id,
        id, datetime_created)
