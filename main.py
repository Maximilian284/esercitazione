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
    self.__window.grid_rowconfigure(0, weight=1) 
    self.__window.grid_columnconfigure(0, weight=1)

    # Fill The Window With The Text
    self.__text.grid(sticky = N + E + S + W)


  # Run Editor
      # start the main loop of the window
  def run(self):
    self.__window.mainloop()

window = Editor()
window.run()
