"""Utility functions related to component objects."""


def refractive_index(port, symbolic=False):
    """Obtains the refractive index of the space attached to
    the port/node `port`.

    Parameters
    ----------
    port : :class:`.Port` or :class:`.Node`
        Port or node.

    Returns
    -------
    nr : float
        The refractive index of the space attached to the port / node.
        Returns unity if no space is present.
    """
    get_nr = lambda space, symbol: space.nr.ref if symbol else space.nr.eval()

    space = port.space
    if space is not None:
        nr = get_nr(space, symbolic)
    else:
        from finesse.components import Beamsplitter

        # If we're at a beamsplitter then get nr
        # of port on same surface
        if isinstance(port.component, Beamsplitter):
            adj_port = port.component.get_adjacent_port(port)
            space = adj_port.space
            if space is None:
                # FIXME (sjr) This should probably raise an exception but parsing
                #             (at least for legacy files) means that both spaces
                #             can be None initially somehow when symbolising
                #             Beamsplitter ABCD matrices
                nr = 1
            else:
                nr = get_nr(space, symbolic)
        else:
            nr = 1

    return nr
