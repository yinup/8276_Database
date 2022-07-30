from sqlite3 import connect
import sys, time
from controller import *
from consolemenu import *
from consolemenu.items import *

controller = Controller()
controller.connect(r'E:\Algonquin\2022Spring\CST8276_Database\demo\8276_Database\CST8276')

def progressBar(ps, iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration, ps):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        message = f'\r{prefix} |{bar}| {percent}% {suffix}'
        ps.printf(message)
    # Initial Call
    printProgressBar(0, ps)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1, ps)
    # Print New Line on Complete
    ps.println()

def read_video_meta():
    ps = PromptUtils(Screen())
    ps.println(video_info)
    ps.enter_to_continue()

def save_video_into_db():
    ps = PromptUtils(Screen())
    items = list(range(0, 57))

    # A Nicer, Single-Call Usage
    for item in progressBar(ps, items, prefix = 'Progress:', suffix = 'Complete', length = 50):
        # Do stuff...
        time.sleep(0.1)
    ps.enter_to_continue()


def retrive_video_info_from_db():
    ps = PromptUtils(Screen())
    video = controller.get()
    metainfo = video.metainfo
    url = video.url 

    # anaylyze the data via JSON library
    metainfo_json = controller.convert_metainfo_to_json(metainfo)
    ps.println("\033[1;32mvideo information:\033[0m")
    ps.println('bit_rate: ' + metainfo_json['bit_rate'])
    ps.println('codec_name: ' + metainfo_json['codec_name'])
    ps.println('codec_type: ' + metainfo_json['codec_type'])
    ps.println('coded_height: ' + str(metainfo_json['coded_height']))
    ps.println('coded_width: ' + str(metainfo_json['coded_width']))
    ps.println('display_aspect_ratio: ' + metainfo_json['display_aspect_ratio'])
    ps.println('display_aspect_ratio: ' + metainfo_json['display_aspect_ratio'])
    ps.println('disposition -> timed_thumbnails: ' + str(metainfo_json['disposition']['timed_thumbnails']))
    ps.println('disposition -> visual_impaired: ' + str(metainfo_json['disposition']['visual_impaired']))
    ps.println('duration: ' + str(metainfo_json['duration']) + ' Seconds')

    ps.println("\033[0;33mvideo url:\033[0m " + '\033[1;4m' + url + '\033[0m')
    ps.enter_to_continue()

option_dict = {
    "read video information": read_video_meta,
    "Save video information into database and upload it to youtube": save_video_into_db,
    "Retrieve video information from database ": retrive_video_info_from_db
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
        menu = ConsoleMenu("Database CST8276", "Create by Hongxin Yin")

        for key in self.option_dict:
            menu.append_item(FunctionItem(key, self.option_dict[key]))

        # Show the menu
        menu.start()
        menu.join()


if __name__ == "__main__":
    v = View(option_dict)
    v.show()
