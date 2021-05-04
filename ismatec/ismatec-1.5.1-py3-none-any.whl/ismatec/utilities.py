from decimal import Decimal


def float_to_mmmmse(value: float) -> str:
    """
    Convert a float into a string with the form mmmmse; represents the scientific notation of m.mmm x 10se. For
    example, 1.200 x 10-2 (equal to 1.200E-2) is represented by 1200-2.
    This corresponds to Volume Type 1 for the RegloICC peristaltic pump

    :param value:
    :return:
    """
    s = '%.3E' % Decimal(value)
    # here s result is in the form 'm.mmmEsee', so the leading 'e', the 'E', and the '.' must be removed
    s = s[0:-2] + s[-1:]
    s = s.replace('.', '')
    s = s.replace('E', '')
    return s