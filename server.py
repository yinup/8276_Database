# CST8276
# Date: May 30th, 2022
# Created by Hongxin Yin (041013285)
import sys
from consolemenu import *
from consolemenu.items import *


def handle_placeholder():
    pass

option_dict = {
    "Load data to memory": handle_placeholder,
    "Export in-memory data to file": handle_placeholder,
    "Select and display record(s) from the in-memory data": handle_placeholder,
    "Create a new record": handle_placeholder,
    "Edit a record in memory": handle_placeholder,
    "Delete a record in memory": handle_placeholder,
    "Illustrate Inheritance and Polymorphism": handle_placeholder,
    "View horizontal bar chart for the price of a specific month": handle_placeholder
}


class View:
    def __init__(self, option_dict=None) -> None:
        self.option_dict = option_dict

    def setup_menu(self, option_dict) -> None:
        self.option_dict = option_dict

    def create_prompt_screen(self):
        return PromptUtils(Screen())

    def display_message(self, message) -> None:
        ps = self.create_prompt_screen()
        ps.println(message, "\n")
        ps.enter_to_continue()

    def show(self) -> None:
        if self.option_dict is None:
            print(f"menu option is empty! Initializing menu failed")
            sys.exit()

        # Create the root menu
        menu = ConsoleMenu("Assignment_02 Menu", "Created by Hongxin Yin")

        for key in self.option_dict:
            menu.append_item(FunctionItem(key, self.option_dict[key]))

        # Show the menu
        menu.start()
        menu.join()


if __name__ == "__main__":
    v = View(option_dict)
    v.show()
