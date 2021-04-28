#!/usr/bin/env python
if __name__ != '__main__': raise Exception("Do not import me!")

from cvargparse import Arg
from cvargparse import BaseParser

from cvmodelz import utils
from cvmodelz.models import ModelFactory

def main(args):

	model = ModelFactory.new(args.model_type, input_size=args.input_size)
	utils.print_model_info(model)

parser = BaseParser()

parser.add_args([
	Arg("model_type", choices=ModelFactory.get_all_models()),

	Arg("--input_size", "-size", type=int, default=None)
])

main(parser.parse_args())
