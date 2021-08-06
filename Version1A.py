import tkinter as tk
from tkinter.filedialog import asksaveasfile
from tkinter import BOTH, LEFT, BOTTOM, TRUE, FALSE
from typing import Tuple, Callable

TINY_FONT = ('Lucida Console', 8)
SMALL_FONT = ('CalibriLight', 10)
MEDIUM_FONT = ('Lucida Bright', 12)
LARGE_FONT = ('Lucida Bright', 20)


class StickyWindow:
    def __init__(
        self,
        name: str,
        color: str,
        parent: tk.Tk,
        get_size: Callable[[], Tuple[int, int]],
        default_type: str,
    ) -> None:
        # function invoked when you click the create button ont the main frame

        if default_type == '':
            default_type = '.txt'
        self.default_type = default_type
        self.new_window = tk.Toplevel(parent)
        if name == '':
            name = 'Untitled'
        self.name = name

        self.new_window.wm_title(name)
        top_note_frame = tk.LabelFrame(
            self.new_window, bg='#ffffff', font=SMALL_FONT,
        )

        save_button = tk.Button(top_note_frame, text='Save', command=self.save_file)
        save_button.pack(pady=5, expand=TRUE, side=LEFT)

        hide_button = tk.Button(top_note_frame, text='Hide', command=self.hide_sticky)
        hide_button.pack(pady=5, expand=TRUE, side=LEFT)

        show_button = tk.Button(top_note_frame, text='Show', command=self.show_sticky)
        show_button.pack(pady=5, expand=TRUE, side=LEFT)

        top_note_frame.pack(fill=BOTH, side=BOTTOM)

        self.get_size = get_size
        width, height = get_size()
        self.new_window.geometry(f'{width}x{height}')
        self.get_size = get_size
        width, height = get_size()
        self.new_window.geometry(f'{width}x{height}')

        choose_font = SMALL_FONT
        self.T = T = tk.Text(self.new_window, height=20, width=40,)
        T.pack(fill=BOTH, expand=TRUE)
        self.T.configure(bg=color)
        T.configure(font=choose_font)

        # TODO allow user to choose font in settings

    def save_file(self) -> None:
        txt_content = self.T.get('1.0', 'end-1c')
        f = asksaveasfile(
            initialfile=self.name,
            defaultextension=self.default_type,
            filetypes=(
                ('Text Documents', '*.txt'),
                ('All Files', '*.*'),
                ('Python', '*.py')
            ),
        )
        if f is not None:
            f.write(txt_content)
            self.new_window.destroy()

    def show_sticky(self) -> None:
        width, height = self.get_size()
        self.new_window.geometry(f'{width}x{height}')

    def hide_sticky(self) -> None:
        self.new_window.geometry('0x50')


class SettingsWindow:
    def __init__(self, parent: tk.Tk):
        self.window = tk.Toplevel(parent)
        self.window.wm_title('Settings')
        settings_frame = tk.LabelFrame(
            self.window, bg='#ffffff', text='Settings', font=MEDIUM_FONT,
        )
        def save_settings():
            self.window.destroy()

        # ----------------------FILE TYPE SETTING
        frame_filetype = tk.LabelFrame(
            settings_frame, text='Default File Type', bg='#ffffff', font=MEDIUM_FONT,
        )
        frame_filetype.pack(fill=BOTH, padx=10, pady=10)
        # retrived later
        my_default = tk.StringVar
        file_type_entry = tk.Entry(
            frame_filetype, bg='#ffffff', textvariable=my_default, font=MEDIUM_FONT
        )

        file_type_entry.pack(padx=10, pady=10)
        #color defult
        frame_color = tk.LabelFrame(
            settings_frame, text='Default Color', bg='#ffffff', font=MEDIUM_FONT,
        )
        frame_color.pack(fill=BOTH, padx=10, pady=10)

        frame_label = tk.Label(
            frame_color, text='enter new color hex code, format like #ffffff', font=TINY_FONT, bg='#ffffff'
        )
        frame_label.pack()
        # retrived later
        default_color = tk.StringVar
        color_entry = tk.Entry(
            frame_color, bg='#ffffff', textvariable=default_color, font=MEDIUM_FONT
        )
        color_entry.pack(padx=10, pady=10)

        save_settings = tk.Button(settings_frame, text='Save Settings', command= save_settings)
        save_settings.pack(padx=10, pady=10)
        settings_frame.pack(padx=10, pady=10)

class MyApp:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title(string='Stickies')
        self.window.attributes('-alpha', 0.95)
        self.window.configure(bg='#ffffff')
        self.mainloop = self.window.mainloop

        width, height = self.screen_size_fraction(0.3, 0.5)
        self.window.geometry(f'{width}x{height}+{width+70}+10')

        frame = tk.LabelFrame(
            self.window, text='Stickies', bg='#ffffff', font=LARGE_FONT,
        )
        frame_name = tk.LabelFrame(
            frame, text='Name your note', bg='#ffffff', font=MEDIUM_FONT,
        )
        frame_colors = tk.LabelFrame(
            frame, text='Pick your Color', bg='#ffffff', font=MEDIUM_FONT,
        )

        self.name_entry = tk.StringVar()
        name_entry = tk.Entry(
            frame_name, textvariable=self.name_entry, font=MEDIUM_FONT, bg='#f1f1f1',
        )

        #color_list = ['purple', 'blue', 'orange', 'green', 'yellow', 'pink']
        self.mydefaultcolor = tk.StringVar()
        self.purple = tk.StringVar()
        self.blue = tk.StringVar()
        self.orange = tk.StringVar()
        self.green = tk.StringVar()
        self.yellow = tk.StringVar()
        self.pink = tk.StringVar()

        def deselect_default():
            color1.deselect()
            color2.deselect()
            color3.deselect()
            color4.deselect()
            color5.deselect()
            color6.deselect()

        def deselect_orange():
            defaultcolor.deselect()
            color1.deselect()
            color2.deselect()
            color3.deselect()
            color4.deselect()
            color6.deselect()

        def deselect_purple():
            defaultcolor.deselect()
            color5.deselect()
            color2.deselect()
            color3.deselect()
            color4.deselect()
            color6.deselect()

        def deselect_green():
            defaultcolor.deselect()
            color1.deselect()
            color3.deselect()
            color4.deselect()
            color5.deselect()
            color6.deselect()

        def deselect_blue():
            defaultcolor.deselect()
            color1.deselect()
            color2.deselect()
            color4.deselect()
            color5.deselect()
            color6.deselect()

        def deselect_pink():
            defaultcolor.deselect()
            color1.deselect()
            color2.deselect()
            color3.deselect()
            color5.deselect()
            color6.deselect()

        def deselect_yellow():
            defaultcolor.deselect()
            color1.deselect()
            color2.deselect()
            color3.deselect()
            color4.deselect()
            color5.deselect()

        Radio_button_font = ('Lucida Console', 12)
        defaultcolor = tk.Radiobutton(
            frame_colors, text='default', indicator=0, bg='#FFFFFF', variable=self.mydefaultcolor, font=Radio_button_font, value=1,
            selectcolor='#FFFFFF', command=deselect_default
        )

        color1 = tk.Radiobutton(
            frame_colors, text='purple', indicator=0, bg='#dbcdf0', variable=self.purple, font=Radio_button_font, value=1,
            selectcolor='#dbcdf0', command=deselect_purple,
        )
        color2 = tk.Radiobutton(
            frame_colors, text='green', indicator=0, indicatoron=0, bg='#d0f4de', variable=self.green, font=Radio_button_font,
            selectcolor='#d0f4de', value=1, command=deselect_green,
        )

        color3 = tk.Radiobutton(
            frame_colors, text='blue', indicator=0, bg='#c6def1', variable=self.blue, font=Radio_button_font,
            selectcolor='#c6def1', value=1, command=deselect_blue,
        )

        color4 = tk.Radiobutton(
            frame_colors, text='pink', indicator=0, bg='#f2c6de', variable=self.pink, font=Radio_button_font,
            selectcolor='#f2c6de', value=1, command=deselect_pink,
        )

        color5 = tk.Radiobutton(
            frame_colors, text='orange', indicator=0, bg='#f7d9c4', variable=self.orange, font=Radio_button_font,
            selectcolor='#f7d9c4', value=1, command=deselect_orange,
        )

        color6 = tk.Radiobutton(
            frame_colors, text='yellow', indicator=0, bg='#fcf6bd', variable=self.yellow, font=Radio_button_font,
            selectcolor='#fcf6bd', value=1, command=deselect_yellow,
        )
        default_padding = 10
        default_padding2 = default_padding * 0.5
        pack_colors = [defaultcolor, color1, color2, color3, color4, color5, color6]

        for my_colors in pack_colors:
            my_colors.pack(fill = tk.Y, padx = default_padding, pady = default_padding2)

        frame_name.pack(padx=10, pady=10, fill=BOTH)
        name_entry.pack(padx=5, pady=5)
        frame.pack(expand=FALSE, fill=BOTH, padx=10, pady=10)
        frame_colors.pack(padx=10, pady=10, fill=BOTH)

        # Tells the program to return to the create sticky function on click
        my_create_button = tk.Button(
            frame, text='Create', command=self.create_sticky, font=MEDIUM_FONT,
        )
        my_create_button.pack(expand=TRUE, fill= BOTH,padx=5, pady=5,side=LEFT,)
        settings_button = tk.Button(
            frame, text='Settings', font=MEDIUM_FONT, command=self.open_settings,
        )
        settings_button.pack(expand=TRUE, fill=BOTH,padx=5, pady=5, side=LEFT,)

    @property
    def color(self) -> str:
        if self.orange.get() == '1':
            return '#f7d9c4'
        if self.blue.get() == '1':
            return '#c6def1'
        if self.purple.get() == '1':
            return '#dbcdf0'
        if self.green.get() == '1':
            return '#d0f4de'
        if self.yellow.get() == '1':
            return '#fcf6bd'
        if self.pink.get() == '1':
            return '#f2c6de'
        return '#FFFFFF'

    def open_settings(self) -> None:
        SettingsWindow(parent=self.window)

    def screen_size_fraction(self, fx: float = 0.3, fy: float = 0.3) -> Tuple[int, int]:
        return (
            int(fx*self.window.winfo_screenwidth()),
            int(fy*self.window.winfo_screenheight()),
        )

    def create_sticky(self) -> None:
        StickyWindow(
            name=self.name_entry.get(), color=self.color, parent=self.window,
            get_size=self.screen_size_fraction,default_type=''
        )


if __name__ == '__main__':
    MyApp().mainloop()
