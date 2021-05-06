""" Основной класс взаимодействия """
from orup_errors import general_functions
from orup_errors import all_errors


class OrupErrorsOperator:
    def __init__(self, canvas, brutto_orup_win_png, tara_orup_win_png, trash_types_list=None, trash_cats_list=None,
                 tko_name='ТКО-4', ar_busy_status='Занят', *args, **kwargs):
        self.all_args = locals()
        self.all_args.update(kwargs)
        print("ALL ARGS", self.all_args)


    def check_brutto_orup(self, all_args):
        """ Проверить данные перед началом взвешивания брутто """
        # Если найдет причину для алерта: вернет словарь с данными
        check_result = general_functions.check_brutto_orup(all_errors.orup_brutto_errors, all_args)
        if check_result:
            general_functions.draw_brutto_window(text=check_result['error_text'], **all_args)
            check_result['shown'] = True
            print("ERROR")
            return check_result
        else:
            general_functions.destroy_error_window(**all_args)
            general_functions.make_errors_unshown(all_errors.orup_brutto_errors)
            print("CLEAR!")

