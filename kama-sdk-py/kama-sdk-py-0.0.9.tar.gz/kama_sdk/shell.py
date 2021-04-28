import code
import os
from typing import Optional, Dict

import yaml
from k8kat.res.base.kat_res import KatRes
from k8kat.res.config_map.kat_map import KatMap
from k8kat.res.dep.kat_dep import KatDep
from k8kat.res.node.kat_node import KatNode
from k8kat.res.ns.kat_ns import KatNs
from k8kat.res.pod.kat_pod import KatPod
from k8kat.res.svc.kat_svc import KatSvc

from kama_sdk.core.core import utils, updates_man
from kama_sdk.core.core.config_man import config_man
from kama_sdk.core.core import prom_api_client as prom_client
from kama_sdk.core.telem import telem_man
from kama_sdk.model.base.model import models_man, Model


def models_context():
  return {c.__name__: c for c in models_man.classes()}


def k8kat_context():
  return {c.__name__: c for c in kat_res_classes}


def misc_context():
  return {
    'Model': Model,
    'utils': utils,
    'r': load_dict_from_scratch,
    'config_man': config_man,
    'models_man': models_man,
    'updates_man': updates_man,
    'telem_man': telem_man,
    'use_prom': use_prom
  }


def start():
  context = {
    **models_context(),
    **k8kat_context(),
    **misc_context()
  }

  setup_console_history()
  code.interact(None, None, context, None)


def setup_console_history():
  import os as loc_os
  import atexit
  import readline
  import rlcompleter

  history_path = os.path.expanduser("~/.pyhistory")

  def save_history(_history_path=history_path):
    import readline
    readline.write_history_file(_history_path)

  if os.path.exists(history_path):
    readline.read_history_file(history_path)

  atexit.register(save_history)
  del loc_os, atexit, readline, rlcompleter, save_history, history_path


def load_dict_from_scratch(_id: str = None) -> Optional[Dict]:
  scratch_file_path = f"{os.getcwd()}/scratch.yaml"
  with open(scratch_file_path, 'r') as scratch_file:
    model_dicts = list(yaml.full_load_all(scratch_file.read()))
    if _id:
      finder = lambda d: d.get('id') == _id
      if res := next(filter(finder, model_dicts), None):
        return res
      else:
        print(f"[kama_sdk:shell] {_id} not found in {scratch_file_path}")
    else:
      if len(model_dicts) > 0:
        return model_dicts[0]
      else:
        print(f"[kama_sdk:shell] scratch {scratch_file_path} has 0 defs")


def use_prom():
  config_man.patch_prefs({
    'monitoring': {
      prom_client.LOCATION_KEY: 'in',
      prom_client.IS_PROXY_KEY: True,
      prom_client.SVC_NS_KEY: 'monitoring',
      prom_client.SVC_NAME_KEY: 'monitoring-kube-prometheus-prometheus'
    }

  })


kat_res_classes = [
  KatRes,
  KatPod,
  KatDep,
  KatSvc,
  KatMap,
  KatNs,
  KatNode
]
