import dataclasses
import datetime

from typing import Any, Dict, List, Literal, Optional

from venmo_client.model import user as user_lib

@dataclasses.dataclass(frozen=True)
class FundingSource:
  transfer_to_estimate: datetime.datetime
  is_default: bool
  last_four: str
  account_status: str
  id: str
  bank_account: Optional[str]
  assets: Dict[str, Any]
  asset_name: str
  name: str
  image_url: Dict[str, Any]
  card: Optional[None]
  type: str
  
  @classmethod
  def new(cls, **data):
    data = dict(data,
        transfer_to_estimate=datetime.datetime.fromisoformat(data['transfer_to_estimate']))
    return cls(**data)


@dataclasses.dataclass(frozen=True)
class PaymentMethod:
  top_up_role: str
  default_transfer_destination: str
  fee: Optional[str]
  last_four: str
  id: str
  card: Optional[str]
  assets: Dict[str, Any]
  peer_payment_role: str
  name: str
  image_url: str
  bank_account: Dict[str, Any]
  merchant_payment_role: str
  type: str
  
  @classmethod
  def new(cls, **data):
    return cls(**data)


@dataclasses.dataclass(frozen=True)
class Target:
  type: str
  phone: Optional[str]
  email: Optional[str]
  redeemable_target: Optional[str]
  user: Optional[user_lib.User] = None
  merchant: Optional[str] = None

  @classmethod
  def new(cls, *, type, phone, email, redeemable_target, **kwargs):
    target_kwargs = {}
    if type == 'user':
      target_kwargs['user'] = user_lib.User.new(**kwargs['user'])
    else:
      raise NotImplementedError(f'Unknown target type: {type}')
    return cls(type, phone, email, redeemable_target, **target_kwargs)


@dataclasses.dataclass(frozen=True)
class Payment:
  status: str
  id: str
  date_authorized: Optional[datetime.datetime]
  date_completed: datetime.datetime
  target: Target
  audience: str
  actor: user_lib.User
  note: str
  amount: float
  action: str
  date_created: datetime.datetime
  date_reminded: Optional[datetime.datetime]
  external_wallet_payment_info: Optional[str]

  @classmethod
  def new(cls, **data):
    data = dict(data,
        actor=user_lib.User.new(**data['actor']),
        target=Target.new(**data['target']),
        date_authorized=datetime.datetime.fromisoformat(
          data['date_authorized']) if data['date_authorized'] else None,
        date_created=datetime.datetime.fromisoformat(data['date_created']),
        date_completed=datetime.datetime.fromisoformat(data['date_completed']),
        date_reminded=datetime.datetime.fromisoformat(
          data['date_reminded']) if data['date_reminded'] else None,
        )
    return cls(**data)


@dataclasses.dataclass(frozen=True)
class Transfer:
  type: str
  status: str
  amount: float
  date_requested: datetime.datetime
  amount_cents: int
  amount_fee_cents: int
  amount_requested_cents: int
  payout_id: Optional[str] = None
  date_completed: Optional[datetime.datetime] = None
  source: Optional[FundingSource] = None
  destination: Optional[FundingSource] = None

  @classmethod
  def new(cls, *, type, status, amount, date_requested, amount_cents,
      amount_fee_cents, amount_requested_cents,
      date_completed=None,
      **kwargs):
    transfer_kwargs = {}
    if type == 'add_funds':
      transfer_kwargs['source'] = FundingSource.new(**kwargs['source'])
    elif type == 'destination':
      transfer_kwargs['destination'] = FundingSource.new(**kwargs['destination'])
    date_requested = datetime.datetime.fromisoformat(date_requested)
    if date_completed is not None:
      transfer_kwargs['date_completed'] = datetime.datetime.fromisoformat(date_completed)
      transfer_kwargs['payout_id'] = kwargs['payout_id']
    return cls(type, status, amount, date_requested, amount_cents,
        amount_fee_cents, amount_requested_cents, **transfer_kwargs)


@dataclasses.dataclass(frozen=True)
class Authorization:
  status: str
  merchant: user_lib.Merchant
  authorization_types: List[str]
  rewards: Optional[str]
  is_venmo_card: bool
  decline: Optional[str]
  payment_method: PaymentMethod
  story_id: str
  created_at: datetime.datetime
  acknowledged: bool
  atm_fees: Optional[str]
  rewards_earned: bool
  descriptor: str
  amount: int
  user: user_lib.User
  captures: List[str]
  id: str
  point_of_sale: Dict[str, Any]

  @classmethod
  def new(cls, *, merchant, payment_method, created_at, user, **kwargs):
    merchant = user_lib.Merchant.new(**merchant)
    payment_method = PaymentMethod.new(**payment_method)
    created_at = datetime.datetime.fromisoformat(created_at)
    user = user_lib.User.new(**user)
    return cls(merchant=merchant, payment_method=payment_method,
        created_at=created_at, user=user, **kwargs)


@dataclasses.dataclass(frozen=True)
class Capture:
  id: str
  payment_id: str
  amount_cents: int
  authorization_id: str
  datetime_created: datetime.datetime
  top_up: Optional[Dict[str, Any]]
  authorization: Authorization

  @classmethod
  def new(cls, *, id, payment_id, amount_cents, authorization_id, datetime_created, 
      authorization, top_up):
    datetime_created = datetime.datetime.fromisoformat(datetime_created)
    authorization = Authorization.new(**authorization)
    return cls(id, payment_id, amount_cents, authorization_id, datetime_created,
        top_up, authorization)



TransactionType = Literal[
    'authorization',
    'capture',
    'credit_repayment',
    'credit_repayment_refund',
    'credit_reward',
    'direct_deposit',
    'direct_deposit_reversal',
    'disbursement',
    'dispute',
    'internal_balance_transfer'
    'payment',
    'refund',
    'top_up',
    'transfer',
]


TRANSACTION_MAPPINGS = {
    'authorization': Authorization,
    'capture': Capture,
    'payment': Payment,
    'transfer': Transfer,
}


class Transaction:

  def __init__(self,
      type: TransactionType,
      id: str,
      datetime_created: datetime.datetime,
      note: str,
      amount: float,
      *, 
      funding_source: Optional[FundingSource] = None,
      authorization: Optional[Authorization] = None,
      capture: Optional[Capture] = None,
      credit_repayment: Optional[Any] = None,
      credit_repayment_refund: Optional[Any] = None,
      credit_reward: Optional[Any] = None,
      direct_deposit: Optional[Any] = None,
      direct_deposit_reversal: Optional[Any] = None,
      disbursement: Optional[Any] = None,
      dispute: Optional[Any] = None,
      internal_balance_transfer: Optional[Any] = None,
      payment: Optional[Payment] = None,
      refund: Optional[Any] = None,
      top_up: Optional[Any] = None,
      transfer: Optional[Transfer] = None
      ):
    self.type = type
    self.id = id
    self.datetime_created = datetime_created
    self.note = note
    self.amount = amount
    self.funding_source = funding_source
    self.authorization = authorization
    self.capture = capture,
    self.credit_repayment = credit_repayment
    self.credit_repayment_refund = credit_repayment_refund
    self.credit_reward = credit_reward
    self.direct_deposit = direct_deposit
    self.direct_deposit_reversal = direct_deposit_reversal
    self.disbursement = disbursement
    self.dispute = dispute
    self.internal_balance_transfer = internal_balance_transfer
    self.payment = payment
    self.refund = refund
    self.top_up = top_up
    self.transfer = transfer

  @classmethod
  def new(cls, *, type, id, datetime_created, note, amount, **kwargs) -> 'Transaction':
    datetime_created = datetime.datetime.fromisoformat(datetime_created)
    transaction_kwargs = {}
    if type not in TRANSACTION_MAPPINGS:
      raise NotImplementedError(f'Unknown transaction type: {type}, {kwargs[type]}')
    transaction_kwargs[type] = TRANSACTION_MAPPINGS[type].new(**kwargs[type])
    return cls(type, id, datetime_created, note, amount, **transaction_kwargs)

  def __repr__(self):
    return (f'Transaction(type={self.type}, '
            f'id={self.id}, datetime_created={self.datetime_created},'
            f'note={self.note}, amount={self.amount}, '
            f'{self.type}={getattr(self, self.type)})')
