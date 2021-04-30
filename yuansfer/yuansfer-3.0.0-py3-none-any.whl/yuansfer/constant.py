VERSION = "v3"

SANDBOX_PREFIX = "https://mapi.yuansfer.yunkeguan.com"
PRODUCT_PREFIX = "https://mapi.yuansfer.com"

ONLINE_SECURE_PAY = "/online/"+VERSION+"/secure-pay"
UPDATE_RECURRING = "/creditpay/"+VERSION+"/update-recurring"
RECURRING_APPLY_TOKEN = "/auto-debit/"+VERSION+"/apply-token"
RECURRING_CONSULT = "/auto-debit/"+VERSION+"/consult"
RECURRING_PAY = "/auto-debit/"+VERSION+"/pay"
RECURRING_REVOKE = "/auto-debit/"+VERSION+"/revoke"
ONLINE_PROCESS = "/creditpay/"+VERSION+"/process"

INSTORE_ADD = "/app-instore/"+VERSION+"/add"
INSTORE_PAY = "/app-instore/"+VERSION+"/pay"
INSTORE_TRAN_QRCODE = "/app-instore/"+VERSION+"/create-trans-qrcode"
INSTORE_CASHIER_ADD = "/app-instore/"+VERSION+"/cashier-add"
INSTORE_AUTH_CAPTURE = "/app-instore/"+VERSION+"/auth-capture"
INSTORE_AUTH_UNFREEZE = "/app-instore/"+VERSION+"/auth-unfreeze"

PAYOUT_PAY = "/"+VERSION+"/payouts/pay"
PAYOUT_INQURIES = "/"+VERSION+"/payouts/inquiry"
PAYOUT_CREATE_ACCOUNT = "/v1/customers/account/create"

CUSTOMER_CREATE_ACCOUNT = "/v1/customers/create"
CUSTOMER_RETRIEVE_ACCOUNT = "/v1/customers/retrieve"
CUSTOMER_UPDATE_ACCOUNT = "/v1/customers/update"

MOBILE_PREPAY = "/micropay/"+VERSION+"/prepay"
EXPRESS_PAY = "/micropay/"+VERSION+"/express-pay"

REFUND = "/app-data-search/"+VERSION+"/refund"
REVERSE = "/app-data-search/"+VERSION+"/cancel"
TRAN_QUERY = "/app-data-search/"+VERSION+"/tran-query"
TRANS_LIST = "/app-data-search/"+VERSION+"/trans-list"
SETTLE_LIST = "/app-data-search/"+VERSION+"/settle-list"
WITHDRAWAL_LIST = "/app-data-search/"+VERSION+"/withdrawal-list"
DATA_STATUS = "/app-data-search/"+VERSION+"/data-status"

AUTH_VOUCHER_CREATE = "/app-auth/"+VERSION+"/voucher-create"
AUTH_FREEAE = "/app-auth/"+VERSION+"/auth-freeze"
AUTH_UNFREEZE = "/app-auth/"+VERSION+"/auth-unfreeze"
AUTH_CAPTURE = "/app-auth/"+VERSION+"/auth-capture"
AUTH_DETAIL_QUERY = "/app-auth/"+VERSION+"/auth-detail-query"

THIRDPART_ACQUIRE_CREATE = "/app-thirdpart/"+VERSION+"/acquire-create"