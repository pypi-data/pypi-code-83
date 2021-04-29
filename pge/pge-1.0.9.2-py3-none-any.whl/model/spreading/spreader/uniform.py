import numpy as np
from random import choice, randint

from pge.model.spreading.spreader.fix_size import FixSpreadModel


class UniformFixGossip(FixSpreadModel):
    def iteration(self):
        ind = randint(0, self.ids.size-1)
        node = self.ids[ind]

        others = self.graph.get_out_degrees(node)

        if others.size != 0:
            u = choice(others)
            old = list(self.status[node])
            (self.status[node]).update(self.status[u])

            if self.received[ind] != len(self.status[node]):
                self.received[ind] = len(self.status[node])
                nws = np.setdiff1d(list(self.status[node]), old)
                self.messes[np.isin(self.ids, nws)] += 1
