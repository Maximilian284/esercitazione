from tkinter import * 

class Editor():

  def __init__(self):

    # Create Window
    self.__window = Tk()

    # Base Features
    self.__title = "Text Editor"
    self.__height = 700
    self.__width = 450

    # Set Window's Features
    self.__window.title(self.__title)
    self.__window.geometry(f"{self.__height}x{self.__width}")

    # Text Auto Resizable
    self.__text = Text(self.__window)
    self.__scrollbar = Scrollbar(self.__text)
    self.__window.grid_rowconfigure(0, weight=1)
    self.__window.grid_columnconfigure(0, weight=1)

    # Fill The Window With The Text
    self.__text.grid(sticky = N + E + S + W)

    # Set Menu
    self.__menu_bar = Menu(self.__window)
    self.__file_menu = Menu(self.__menu_bar, tearoff = 0)

    # File Menu
    self.__file_menu.add_command(label = "Esci", command = self.__exit, accelerator = "Ctrl+Q")

    self.__window.bind("<Control-q>", self.__exit)

    self.__menu_bar.add_cascade(label = "File", menu = self.__file_menu)

    # Add Menus
    self.__window.config(menu = self.__menu_bar)
    self.__scrollbar.pack(side = RIGHT, fill = Y)

  # File Menu's Commands
      # close the window
  def __exit(self, __event = None):
    self.__window.destroy()

  # Run Editor
      # start the main loop of the window
  def run(self):
    self.__window.mainloop()

window = Editor()
window.run()
