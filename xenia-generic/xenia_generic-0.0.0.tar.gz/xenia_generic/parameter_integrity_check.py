# TODO: la classe è da testare

from loguru import logger


class ParameterIntegrityCheck:
    """
    La classe viene usata per testare l'integrità dei parametri dei vari metodi.
    """
    @staticmethod
    def check(o_parameter: object, s_parameter_name: str, o_parameter_class: object,
              s_method_name: str, s_method_class_name: str,
              b_accept_none: bool = False, b_sized: bool = True, b_accept_empty: bool = False):
        """
        Controlla l'integrità di un parametro. Se il parametro risponde ai controlli non fa nulla. Atrimenti solleva la corrispondente eccezione.

        :param o_parameter: è il valore del parametro da controllare
        :param s_parameter_name: è il nome del parametro da controllare
        :param o_parameter_class: è il tipo del parametro da controllare
        :param s_method_name: è il metodo che usa il parametro da controllare
        :param s_method_class_name: è la classe a cui appartiene il metodo che usa il parametro da controllare
        :param b_accept_none: è True se il parametro può essere None. False altrimenti
        :param b_sized: è True se il parametro possiede un metodo len() per verificare se è vuoto o meno
        :param b_accept_empty: è True se il parametro può essere vuoto. False altrimenti.
        """
        # check for 'check' parameters integrity
        if s_parameter_name is None:
            logger.critical("[ParameterIntegrityCheck][check]: s_parameter_name is None !")
            raise ValueError("[ParameterIntegrityCheck][check]: s_parameter_name is None !")
        if len(s_parameter_name) == 0:
            logger.critical("[ParameterIntegrityCheck][check]: s_parameter_name is empty !")
            raise ValueError("[ParameterIntegrityCheck][check]: s_parameter_name is empty !")

        if o_parameter_class is None:
            logger.critical("[ParameterIntegrityCheck][check]: o_parameter_class is None !")
            raise ValueError("[ParameterIntegrityCheck][check]: o_parameter_class is None !")

        if b_accept_none is None:
            logger.critical("[ParameterIntegrityCheck][check]: b_accept_none is None !")
            raise ValueError("[ParameterIntegrityCheck][check]: b_accept_none is None !")
        if type(b_accept_none) != bool:
            logger.critical("[ParameterIntegrityCheck][check]: excepted <class bool> for 'b_accept_none'. Found  !".format(type(b_accept_none)))
            raise ValueError("[ParameterIntegrityCheck][check]: excepted <class bool> for 'b_accept_none'. Found  !".format(type(b_accept_none)))

        if b_sized is None:
            logger.critical("[ParameterIntegrityCheck][check]: b_sized is None !")
            raise ValueError("[ParameterIntegrityCheck][check]: b_sized is None !")
        if type(b_sized) != bool:
            logger.critical("[ParameterIntegrityCheck][check]: excepted <class bool> for 'b_sized'. Found  !".format(type(b_sized)))
            raise ValueError("[ParameterIntegrityCheck][check]: excepted <class bool> for 'b_sized'. Found  !".format(type(b_sized)))

        if b_accept_empty is None:
            logger.critical("[ParameterIntegrityCheck][check]: b_accept_empty is None !")
            raise ValueError("[ParameterIntegrityCheck][check]: b_accept_empty is None !")
        if type(b_accept_empty) != bool:
            logger.critical("[ParameterIntegrityCheck][check]: excepted <class bool> for 'b_accept_empty'. Found  !".format(type(b_accept_empty)))
            raise ValueError("[ParameterIntegrityCheck][check]: excepted <class bool> for 'b_accept_empty'. Found  !".format(type(b_accept_empty)))

        # check if parameter is None
        if o_parameter is None:
            if not b_accept_none:
                logger.critical("[{}][{}]: parameter '{}' is None !".format(s_method_class_name, s_method_name, s_parameter_name))
                raise ValueError("[{}][{}]: parameter '{}' is None !".format(s_method_class_name, s_method_name, s_parameter_name))
            return
        else:
            # check if parameter match the type
            if type(o_parameter) != o_parameter_class:
                logger.critical("[{}][{}]: expected {} for parameter '{}'. Found {} instead !".format(s_method_class_name, s_method_name, o_parameter_class, s_parameter_name, type(o_parameter)))
                raise TypeError("[{}][{}]: expected {} for parameter '{}'. Found {} instead !".format(s_method_class_name, s_method_name, o_parameter_class, s_parameter_name, type(o_parameter)))
            # check if parameter is empty
            if b_sized and not b_accept_empty:
                try:
                    if len(o_parameter) == 0:
                        logger.critical("[{}][{}]: parameter '{}' is empty !".format(s_method_class_name, s_method_name, s_parameter_name))
                        raise ValueError("[{}][{}]: parameter '{}' is empty !".format(s_method_class_name, s_method_name, s_parameter_name))
                except TypeError:
                    logger.critical("[{}][{}]: parameter '{}' has not a len method !".format(s_method_class_name, s_method_name, s_parameter_name))
                    # raise ValueError("[{}][{}]: parameter '{}' has not a len method !".format(s_method_class_name, s_method_name, s_parameter_name))


if __name__ == '__main__':
    ParameterIntegrityCheck.check([], "l_names", list, "main", "MAIN", b_sized=True, b_accept_empty=True)
