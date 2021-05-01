

import threading

thread_local = threading.local()

def set_cur_txn(txn):
    setattr(thread_local, 'nextapm_cur_txn', txn)

def ser_cur_context(txn):
    set_cur_txn(txn)

def clear_cur_context():
    ser_cur_context(None)

def get_cur_txn():
    return getattr(thread_local, 'nextapm_cur_txn', None)

def is_txn_active():
    txn = get_cur_txn()
    return txn is not None

def is_no_active_txn():
    txn = get_cur_txn()
    return txn is None

