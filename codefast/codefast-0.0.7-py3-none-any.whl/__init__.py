import sys
import codefast.utils as utils

# Export methods and variables
debug = utils.debug
warning = utils.warning
error = utils.error
info = utils.info

json = utils.JsonIO
text = utils.TextIO
file = utils.TextIO
csv = utils.CSVIO
net = utils.Network

p = utils.p
pp = utils.pp
say = utils.TextIO.say

sys.modules[__name__] = utils.wrap_mod(sys.modules[__name__],
                                       deprecated=['text'])
