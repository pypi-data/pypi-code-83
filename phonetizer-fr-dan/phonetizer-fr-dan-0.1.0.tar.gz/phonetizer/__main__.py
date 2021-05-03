import sys
from . import PhonetizerModel

word = sys.argv[1]
phon = sys.argv[2]
model = sys.argv[3]
model = PhonetizerModel('cpu', model)
print(model.check_phonetization_error(word, phon))
