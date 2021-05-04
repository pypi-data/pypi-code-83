from tempfile import TemporaryDirectory

import os
import importlib.util

import numpy as np
import onnx
import onnxruntime
from onnxruntime.tools.symbolic_shape_infer import SymbolicShapeInference
import pytest
import torch

from onnx_model_maker import *
from onnx_model_maker.ops import *
from onnx_pytorch import code_gen

torch.set_printoptions(8)


class TestModel:

  def _run(self, inputs_np, onnx_model):
    model = onnx.ModelProto()
    model.CopyFrom(onnx_model)
    sess_options = onnxruntime.SessionOptions()
    session = onnxruntime.InferenceSession(model.SerializeToString(),
                                           sess_options)
    ort_outputs = session.run(None, {k: v for k, v in inputs_np})
    model.graph.ClearField("value_info")
    model = SymbolicShapeInference.infer_shapes(model, 2**31 - 1, True, True, 1)
    with TemporaryDirectory() as tmpdir:
      code_gen.gen(model, output_dir=tmpdir)
      spec = importlib.util.spec_from_file_location(
          "model", os.path.join(tmpdir, "model.py"))
      mod = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(mod)
      pt_outputs = mod.test_run_model(
          [torch.from_numpy(v) for _, v in inputs_np])
      assert np.allclose(ort_outputs, [o.detach().numpy() for o in pt_outputs],
                         atol=1e-5,
                         rtol=1e-5,
                         equal_nan=True)

  def test_ugmarketing(self):
    ugmarkering_model_path = "/Users/wenhao/Projects/ai_speed/saved_model/model.onnx"
    if not os.path.exists(ugmarkering_model_path):
      return False
    model = onnx.load(ugmarkering_model_path)
    self._run(
        [("import/whole_input:0", np.random.randn(1, 2905).astype(np.float32))],
        model)


if __name__ == '__main__':
  pytest.main(['-s', 'test_onnx_model_zoo.py'])
