import data_provider 
import user_interface
import logger


def button_click():
    n = user_interface.menu()
    data_provider.init(n)

logger.log()
    