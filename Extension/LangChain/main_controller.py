# Extension/Demo/main_Controller.py

from System.Common.base_controller import BaseController


class mainController(BaseController):

    def demo1(self):
        return "This is demo1 function!"

    def demo2(self):
        # return "This is demo2 function!"
        return f"And Common's temp function: " + self.test()
