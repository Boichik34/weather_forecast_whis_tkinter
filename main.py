from main_window import Window

if __name__ == '__main__':
    root = Window()
    root.resizable(width=False, height=False)
    root.title('Прогноз погоды')
    root.geometry('300x350')
    root.mainloop()