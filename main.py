from c_calc import Calc_block as c_calc
from logger import result_logger as write_log
import data_transformation as d_t
import console_ui as c_ui


def button_click():
    i = d_t.data_formatting(c_ui.input_data())
    calc_result = c_calc(i)
    c_ui.view_data(calc_result, 'Ответ:')
    write_log(i, calc_result)

button_click()