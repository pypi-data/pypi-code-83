import slai
import pandas as pd


class ModelHandler(slai.base_handler):
    def model_inputs(self):
        return {
            "age": slai.inputs.Float,
            "weight": slai.inputs.Float,
            "height": slai.inputs.Float,
        }

    def input(self, **inputs):
        x = pd.Series(
            [inputs["age"], inputs["weight"], inputs["height"]],
            index=["age", "weight", "height"],
        )
        return x

    def output(self, model_output):
        return model_output
