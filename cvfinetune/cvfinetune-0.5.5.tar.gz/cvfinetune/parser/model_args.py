import abc

from cvargparse import Arg
from cvfinetune.parser.utils import get_info_file
from cvfinetune.parser.utils import parser_extender

from chainer_addons.links import PoolingType
from chainer_addons.models import PrepareType

class ModelChoices(object):

	def __init__(self, choices=[]):
		super(ModelChoices, self).__init__()
		self.choices = choices

	def __contains__(self, value):
		return value.startswith("cv2_") or value in self.choices

	def __iter__(self):
		return iter(self.choices + ["cv2_<any other model>"])

@parser_extender
def add_model_args(parser):

	info_file = get_info_file()
	choices = None if info_file is None else info_file.MODELS.keys()

	_args = [
		Arg("--model_type", "-mt",
			default="cv2_resnet50", choices=ModelChoices(choices),
			help="type of the model"),

		Arg("--input_size", type=int, nargs="+", default=0,
			help="overrides default input size of the model, if greater than 0"),

		Arg("--parts_input_size", type=int, nargs="+", default=0,
			help="overrides default input part size of the model, if greater than 0"),

		PrepareType.as_arg("prepare_type",
			help_text="type of image preprocessing"),

		PoolingType.as_arg("pooling",
			help_text="type of pre-classification pooling"),

		Arg("--load", type=str,
			help="ignore weights and load already fine-tuned model (classifier will NOT be re-initialized and number of classes will be unchanged)"),

		Arg("--weights", type=str,
			help="ignore default weights and load already pre-trained model (classifier will be re-initialized and number of classes will be changed)"),

		Arg("--headless", action="store_true",
			help="ignores classifier layer during loading"),

		Arg("--load_strict", action="store_true",
			help="load weights in a strict mode"),

		Arg("--load_path", type=str,
			help="load path within the weights archive"),
	]

	parser.add_args(_args, group_name="Model arguments")


class ModelParserMixin(abc.ABC):
	def __init__(self, *args, **kwargs):
		super(ModelParserMixin, self).__init__(*args, **kwargs)
		add_model_args(self)


__all__ = [
	"ModelParserMixin",
	"add_model_args"
]
