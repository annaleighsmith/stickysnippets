import tkinter as tk
from tkinter.filedialog import asksaveasfile
from tkinter import BOTH, LEFT, BOTTOM, TRUE, TOP
from typing import Tuple, Callable

TINY_FONT = ('Lucida Console', 8)
SMALL_FONT = ('CalibriLight', 10)
MEDIUM_FONT = ('Lucida Bright', 12)
LARGE_FONT = ('Lucida Bright', 20)
RADIO_FONT = ('Lucida Console', 12)


class MyColors:
    def __init__(self, colorname, hexcode, value):
        self.colorname = colorname
        self.hexcode = hexcode
        self.value = value


class MyFonts:
    def __init__(self, font_style, font_style_full, value):
        self.font_style = font_style
        self.font_style_full = font_style_full
        self.value = value


color1 = MyColors('pink', '#f2c6de', 1)
color2 = MyColors('blue', '#c6def1', 2)
color3 = MyColors('yellow', '#fcf6bd', 3)
color4 = MyColors('green', '#d0f4de', 4)
color5 = MyColors('orange', '#f7d9c4', 5)
color6 = MyColors('purple', '#dbcdf0', 6)
color7 = MyColors('white', '#ffffff', 7)

font_tup1 = ('Arial', 12)
font1 = MyFonts('Arial', font_tup1, 1)
font_tup2 = ('Times New Roman', 12)
font2 = MyFonts('Times New Roman', font_tup2, 2)
font_tup3 = ('Calibri Light', 12)
font3 = MyFonts('Calibri Light', font_tup3, 3)
font_tup4 = ('FixedSys', 12)
font4 = MyFonts('FixedSys', font_tup4, 4)
font_tup5 = ('Lucida Console', 12)
font5 = MyFonts('Lucida Console', font_tup5, 5)
font_tup6 = ('Helvetica', 12)
font6 = MyFonts('Helvetica', font_tup6, 6)

ColorList = (color2, color7, color3, color4, color5, color6, color1)
FontList = (font1, font2, font3, font4, font5, font6)


class StickyWindow:
    def __init__(
        self,
        name: str,
        color: str,
        font: str,
        parent: tk.Tk,
        get_size: Callable[[], Tuple[int, int]],
    ) -> None:

        self.sticky_window = tk.Toplevel(parent)
        self.sticky_window.wm_title(name)  # wm stands for windows manager
        if name == '':
            name = 'Untitled'
        self.name = name

        if color == '':
            color = '#ffffff'
        if color == '1':
            color = color1.hexcode
        if color == '2':
            color = color2.hexcode
        if color == '3':
            color = color3.hexcode
        if color == '4':
            color = color4.hexcode
        if color == '5':
            color = color5.hexcode
        if color == '6':
            color = color6.hexcode
        if color == '7':
            color = color7.hexcode
        self.color = color
        # =======================
        if font == '':
            font = '#ffffff'
        if font == '1':
            font = font1.font_style_full
        if font == '2':
            font = font2.font_style_full
        if font == '3':
            font = font3.font_style_full
        if font == '4':
            font = font4.font_style_full
        if font == '5':
            font = font5.font_style_full
        if font == '6':
            font = font6.font_style_full
        self.font = font

        self.sticky_window.config(bg=color)
        top_note_frame = tk.LabelFrame(
            self.sticky_window, bg='#ffffff',
        )

        save_button = tk.Button(top_note_frame, text='Save', command=self.save_file,)
        save_button.pack(pady=5, expand=TRUE, side=LEFT)

        hide_button = tk.Button(top_note_frame, text='Hide', command=self.hide_sticky)
        hide_button.pack(pady=5, expand=TRUE, side=LEFT)

        show_button = tk.Button(top_note_frame, text='Show', command=self.show_sticky)
        show_button.pack(pady=5, expand=TRUE, side=LEFT)

        delete_button = tk.Button(top_note_frame, text='Delete', command=self.delete_sticky)
        delete_button.pack(pady=5, expand=TRUE, side=LEFT)

        top_note_frame.pack(fill=BOTH, side=BOTTOM,)

        self.get_size = get_size
        width, height = get_size()
        self.sticky_window.geometry(f'{width}x{height}')
        self.get_size = get_size
        width, height = get_size()
        self.sticky_window.geometry(f'{width}x{height}')

        self.T = T = tk.Text(self.sticky_window, height=20, width=40,)
        T.pack(fill=BOTH, expand=TRUE)
        self.T.configure(bg=color, font=font)

    def save_file(self) -> None:
        txt_content = self.T.get('1.0', 'end-1c')
        f = asksaveasfile(
            initialfile=self.name,   # replaced name with default type to test
            defaultextension='.txt',
            filetypes=(
                ('Text Documents', '*.txt'),
                ('All Files', '*.*'),
                ('Python', '*.py')
            ),
        )
        if f is not None:
            f.write(txt_content)
            self.sticky_window.destroy()

    def show_sticky(self) -> None:
        width, height = self.get_size()
        self.sticky_window.geometry(f'{width}x{height}')

    def hide_sticky(self) -> None:
        self.sticky_window.geometry('0x50')

    def delete_sticky(self) -> None:
        self.sticky_window.destroy()


class NoteApplication:
    def __init__(self) -> None:
        # ------------------------------------PARAMETER SELF + INSTANCE ATTRIBUTES
        self.window = tk.Tk()
        self.name_entry = tk.StringVar()
        self.color_choice = tk.StringVar()
        self.font_choice = tk.StringVar()
        self.default_type = tk.StringVar()
        self.window.title(string='Stickies!')
        self.window.attributes('-alpha', 0.95)
        self.window.configure(bg='#ffffff')

        # ------------------------------------PARAMETER SELF + TK MISC
        self.mainloop = self.window.mainloop
        mainframe = tk.LabelFrame(self.window, text='Stickies', bg='#ffffff', font=LARGE_FONT,)
        mainframe.pack(padx=5, pady=5)
        # ------------------------------------NAME LABEL INSTRUCTIONS
        label_name = tk.Label(mainframe, text='Name your note', font=MEDIUM_FONT, bg='#ffffff',)
        label_name.pack(expand=TRUE, side=TOP, padx=5, pady=5,)
        # ------------------------------------NAME ENTRY ELEMENT
        name_entry = tk.Entry(mainframe, textvariable=self.name_entry, font=MEDIUM_FONT, bg='#f1f1f1',)
        name_entry.pack(expand=TRUE, side=TOP, padx=5, pady=5,)
        # ------------------------------------COLOR SELECTION BELOW NOTE NAMING ELEMENTS 1 & 2
        frame_colors = tk.Frame(mainframe, bg='#ffffff')
        frame_colors.pack()
        color_label = tk.Label(frame_colors, text='Choose a color for your sticky:', bg='#FFFFFF', font=MEDIUM_FONT)
        color_label.pack(expand=TRUE, fill=BOTH, side=TOP,)
        for x in ColorList:
            tk.Radiobutton(frame_colors, text=x.colorname, font=MEDIUM_FONT, value=x.value, bg=x.hexcode,
                           selectcolor=x.hexcode, indicator=0, var=self.color_choice).pack(padx=5, pady=1, fill=BOTH)
        frame_font = tk.Frame(mainframe, bg='#ffffff')
        frame_font.pack()
        font_label = tk.Label(frame_font, text='Choose a font for your sticky:', bg='#FFFFFF', font=MEDIUM_FONT)
        font_label.pack(expand=TRUE, fill=BOTH, side=TOP)
        for f in FontList:
            tk.Radiobutton(frame_font, text=f.font_style, font=f.font_style_full, value=f.value, bg='lightgray',
                           selectcolor='white', indicator=0, var=self.font_choice).pack(fill=BOTH)
        # ------------------------------------CREATE AND SETTINGS BUTTONS (ON MAINFRAME OF NOTEAPP)
        my_create_button = tk.Button(mainframe, text='Create', command=self.open_sticky, font=MEDIUM_FONT, bg='white')
        my_create_button.pack(expand=TRUE, fill=BOTH, padx=10, pady=20, side=TOP, )

    def screen_size_fraction(self, fx: float = 0.35, fy: float = 0.35) -> Tuple[int, int]:
        return (
            int(fx*self.window.winfo_screenwidth()),
            int(fy*self.window.winfo_screenheight()),
        )

    def open_sticky(self) -> None:
        StickyWindow(name=self.name_entry.get(), parent=self.window, get_size=self.screen_size_fraction,
                     color=self.color_choice.get(), font=self.font_choice.get())


if __name__ == '__main__':
    NoteApplication().mainloop()
