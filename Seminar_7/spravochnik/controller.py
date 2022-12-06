import model
import view

def button_click():
    selector = view.choice()
    model.init(selector)
    view.view_data(selector)