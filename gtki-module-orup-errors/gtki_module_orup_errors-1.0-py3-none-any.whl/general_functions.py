""" Общие функции """
from orup_errors import all_errors


def destroy_error_window(canvas, error_win_tag='errorwin', error_txt_tag='errorwintxt', *args, **kwargs):
    canvas.delete(error_win_tag, error_txt_tag)

def draw_brutto_window(text, *args, **kwargs):
    kwargs['photo_object'] = kwargs['brutto_orup_win_png']
    draw_error_window(text=text, **kwargs)

def draw_error_window(canvas, text, xpos, ypos, photo_object, error_win_tag='errorwin', error_txt_tag='errorwintxt',
                      text_color='black', text_font='Times', *args, **kwargs):
    canvas.delete(error_txt_tag)                                                 # Удалить текст ошибки (если он был)
    canvas.create_image(xpos, ypos, image=photo_object, tag=error_win_tag)       # Создать окно ошибки (красный квадрат)
    # Создать текст
    canvas.create_text(xpos, ypos, text=text, font=text_font, fill=text_color, tags=(error_win_tag, error_txt_tag),
                       justify='center')



def check_brutto_orup(brutto_orup_dict, args_dict):
    """ Перебирает словарь ошибок, передавая им словарь аргументов для проверки, возрващает первое совпадение"""
    for error_name, info_dict in brutto_orup_dict.items():
        # Если функция проверки возбуждает алерт, и если алерт еще не показан или не пропускаемый - вернуть словарь
        if info_dict['check_func'](**args_dict) and \
                (info_dict['skippable'] == False or not info_dict['shown'] and info_dict['skippable']):
            return info_dict

def make_errors_unshown(args_dict, *args, **kwargs):
    """ Сделать для всех алертов unshown (пропустить заезд и сбросить счетчики) """
    print(locals())
    for error_name, info_dict in args_dict.items():
        info_dict['shown'] = False

