import hy.macros
from hy.core.language import eval, read_str
hy.macros.require('hy.contrib.walk', None, assignments=[['let', 'let']],
    prefix='')
import hy


class Jedhy:

    def __init__(self, jedhy, logger=None):
        self.jedhy = jedhy
        self.logger = logger
        return None

    def refresh_ns(self, __imports__):
        for __i__ in __imports__:
            self.logger.info('import/require: ' + __i__)
            try:
                _hy_anon_var_2 = eval(read_str(__i__))
            except BaseException as e:
                _hy_anon_var_2 = self.logger.info('import/require failed: ' +
                    repr(e))
        return self.jedhy.set_namespace(locals_=locals(), globals_=globals(
            ), macros_=__macros__)

    def complete(self, prefix_str):
        return self.jedhy.complete(prefix_str)

    def docs(self, candidate_str):
        return self.jedhy.docs(candidate_str)

