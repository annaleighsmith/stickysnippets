import tkinter as tk
from tkinter import BOTH, BOTTOM, TRUE, TOP, X, LEFT, RIGHT
from tkinter.filedialog import asksaveasfile


# main classes


class MyColors:
    def __init__(self, color_name, hex_code, value):
        self.color_name = color_name
        self.hex_code = hex_code
        self.value = value


class MyFonts:
    def __init__(self, font_style, font_style_full, value):
        self.font_style = font_style
        self.font_style_full = font_style_full
        self.value = value


# constant variables
application_title = 'Stickies!'
TINY_FONT = ('Lucida Console', 8)
SMALL_FONT = ('CalibriLight', 10)
MEDIUM_FONT = ('Lucida Bright', 12)
LARGE_FONT = ('Lucida Bright', 20)
RADIO_FONT = ('Lucida Console', 12)
color1 = MyColors('pink', '#f2c6de', 1)
color2 = MyColors('blue', '#c6def1', 2)
color3 = MyColors('yellow', '#fcf6bd', 3)
color4 = MyColors('green', '#d0f4de', 4)
color5 = MyColors('orange', '#f7d9c4', 5)
color6 = MyColors('purple', '#dbcdf0', 6)
font_tup1 = ('Arial', 12)
font1 = MyFonts('Arial', font_tup1, 1)
font_tup2 = ('Times New Roman', 12)
font2 = MyFonts('Times New Roman', font_tup2, 2)
font_tup3 = ('Calibri Light', 12)
font3 = MyFonts('Calibri Light', font_tup3, 3)
font_tup4 = ('FixedSys', 12)
font4 = MyFonts('FixedSys', font_tup4, 4)
font_tup5 = ('Verdana', 12)
font5 = MyFonts('Verdana', font_tup5, 5)
font_tup6 = ('Helvetica', 12)
font6 = MyFonts('Helvetica', font_tup6, 6)
ColorList = (color1, color2, color3, color4, color5, color6)
FontList = (font1, font3, font4, font5, font6, font2)


class App(tk.Frame):
    def __init__(self,
                 master=None,
                 ):
        super().__init__(master)

        self.pack()
        self.color_setting = None
        self.name_entry = tk.StringVar()
        self.color_choice = tk.StringVar()
        self.font_choice = tk.StringVar()
        self.default_type = tk.StringVar()
        self.configure(bg='#ffffff')

        mainframe = tk.LabelFrame(self, text='Stickies', bg='#ffffff', font=LARGE_FONT, )
        mainframe.pack(padx=5, pady=5)
        # ----------> NAME LABEL INSTRUCTIONS
        label_name = tk.Label(mainframe, text='Name your note', font=MEDIUM_FONT, bg='#ffffff', )
        label_name.pack(expand=TRUE, side=TOP, padx=5, pady=5, )
        # ----------> NAME ENTRY ELEMENT
        name_entry = tk.Entry(mainframe, textvariable=self.name_entry, font=MEDIUM_FONT, bg='#f1f1f1', )
        name_entry.pack(expand=TRUE, side=TOP, padx=5, pady=5, )
        # ----------> COLOR SELECTION BELOW NOTE NAMING ELEMENTS 1 & 2
        frame_colors = tk.Frame(mainframe, bg='#ffffff')
        frame_colors.pack()

        # ----------->

        def sel():
            selection = str(color_int_var.get())
            return selection

        def selected():
            selection_f = str(int_var_font.get())
            return selection_f

        frame_colors = tk.Frame(mainframe, bg='#ffffff')
        frame_colors.pack()
        color_label = tk.Label(frame_colors, text='Choose a color for your sticky:', bg='#FFFFFF', font=MEDIUM_FONT)
        color_int_var = tk.IntVar()
        color_label.pack(expand=TRUE, fill=BOTH, side=TOP, )
        # color radio buttons ---------------------->
        r1 = tk.Radiobutton(frame_colors,
                            text=ColorList[0].color_name,
                            variable=color_int_var,
                            value=1,
                            bg=ColorList[0].hex_code,
                            selectcolor=ColorList[0].hex_code,
                            indicator=0,
                            command=sel)
        r1.pack(expand=TRUE, fill=BOTH, side=TOP)
        r2 = tk.Radiobutton(frame_colors,
                            text=ColorList[1].color_name,
                            variable=color_int_var,
                            value=2,
                            bg=ColorList[1].hex_code,
                            selectcolor=ColorList[1].hex_code,
                            indicator=0,
                            command=sel)
        r2.pack(expand=TRUE, fill=BOTH, side=TOP)
        r3 = tk.Radiobutton(frame_colors,
                            text=ColorList[2].color_name,
                            variable=color_int_var,
                            value=3,
                            bg=ColorList[2].hex_code,
                            selectcolor=ColorList[2].hex_code,
                            indicator=0,
                            command=sel)
        r3.pack(expand=TRUE, fill=BOTH, side=TOP)
        r4 = tk.Radiobutton(frame_colors,
                            text=ColorList[3].color_name,
                            variable=color_int_var,
                            value=4,
                            bg=ColorList[3].hex_code,
                            selectcolor=ColorList[3].hex_code,
                            indicator=0,
                            command=sel)
        r4.pack(expand=TRUE, fill=BOTH, side=TOP)
        r5 = tk.Radiobutton(frame_colors,
                            text=ColorList[4].color_name,
                            variable=color_int_var,
                            value=5,
                            bg=ColorList[4].hex_code,
                            selectcolor=ColorList[4].hex_code,
                            indicator=0,
                            command=sel)
        r5.pack(expand=TRUE, fill=BOTH, side=TOP)
        r6 = tk.Radiobutton(frame_colors,
                            text=ColorList[5].color_name,
                            variable=color_int_var,
                            value=6,
                            bg=ColorList[5].hex_code,
                            selectcolor=ColorList[5].hex_code,
                            indicator=0,
                            command=sel)
        r6.pack(expand=TRUE, fill=BOTH, side=TOP)
        # --------------/ color radio buttons
        int_var_font = tk.IntVar()
        frame_font = tk.Frame(mainframe, bg='#ffffff')
        frame_font.pack()
        font_label = tk.Label(frame_font, text='Choose a font for your sticky:', bg='#FFFFFF', font=MEDIUM_FONT)
        font_label.pack(expand=TRUE, fill=BOTH, side=TOP)
        # ---------> font radio buttons
        rf1 = tk.Radiobutton(frame_font,
                             text=FontList[0].font_style,
                             variable=int_var_font,
                             value=1,
                             font=FontList[0].font_style_full,
                             indicator=0,
                             command=selected)
        rf1.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf2 = tk.Radiobutton(frame_font,
                             text=FontList[1].font_style,
                             variable=int_var_font,
                             value=2,
                             font=FontList[1].font_style_full,
                             indicator=0,
                             command=selected)
        rf2.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf3 = tk.Radiobutton(frame_font,
                             text=FontList[2].font_style,
                             variable=int_var_font,
                             value=3,
                             font=FontList[2].font_style_full,
                             indicator=0,
                             command=selected)
        rf3.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf4 = tk.Radiobutton(frame_font,
                             text=FontList[3].font_style,
                             variable=int_var_font,
                             value=4,
                             font=FontList[3].font_style_full,
                             indicator=0,
                             command=selected)
        rf4.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf5 = tk.Radiobutton(frame_font,
                             text=FontList[4].font_style,
                             variable=int_var_font,
                             value=5,
                             font=FontList[4].font_style_full,
                             indicator=0,
                             command=selected)
        rf5.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf6 = tk.Radiobutton(frame_font,
                             text=FontList[5].font_style,
                             variable=int_var_font,
                             value=6,
                             font=FontList[5].font_style_full,
                             indicator=0,
                             command=selected)
        rf6.pack(expand=TRUE, fill=BOTH, side=TOP)
        # --------------/ font radio buttons

        my_create_button = tk.Button(mainframe, text='Create', command=lambda: sticky_note(), font=MEDIUM_FONT,
                                     bg='white')
        my_create_button.pack(expand=TRUE, fill=BOTH, padx=10, pady=20, side=TOP, )
        my_settings_button = tk.Button(
            mainframe, text='Settings', command=lambda: settings_window(), font=MEDIUM_FONT, bg='white')
        my_settings_button.pack(expand=TRUE, fill=BOTH, side=BOTTOM, padx=10, pady=5, )
        color_label.pack(expand=TRUE, fill=BOTH, side=TOP, )

        def sticky_note():
            sticky_frame = tk.Toplevel(master=mainframe)
            sticky_frame.wm_title(name_entry.get())
            name = name_entry.get()
            sticky_frame.geometry('300x300')
            color_value = int(sel()) - 1
            new_color = ColorList[color_value].hex_code
            sticky_frame.configure(bg=str(new_color))
            font_value = int(selected()) - 1
            new_font = FontList[font_value].font_style_full
            button_frame = tk.Frame(sticky_frame)
            save_button = tk.Button(button_frame, text='Save Sticky', command=lambda: save_file())
            save_button.pack(side=LEFT, padx=10, pady=5, fill=X, expand=TRUE)
            delete_button = tk.Button(button_frame, text='Delete Sticky', command=lambda: delete_note())
            delete_button.pack(side=RIGHT, padx=10, pady=5, expand=TRUE, fill=X)
            button_frame.pack(side=TOP, fill=X, expand=TRUE)
            textbox = tk.Text(sticky_frame, font=new_font, bg=str(new_color))
            textbox.pack()
            textbox = tk.Text(sticky_frame, font=new_font, bg=str(new_color))
            textbox.pack()

            def delete_note() -> None:
                sticky_frame.destroy()

            def save_file() -> None:
                txt_content = textbox.get('1.0', 'end-1c')
                f = asksaveasfile(
                    initialfile=name,  # replaced name with default type to test
                    defaultextension='.txt',
                    filetypes=(
                        ('Text Documents', '*.txt'),
                        ('All Files', '*.*'),
                        ('Python', '*.py')
                    ),
                )
                if f is not None:
                    f.write(txt_content)
                    sticky_frame.destroy()

        def settings_window():
            settings_frame = tk.Toplevel(master=mainframe)
            settings_frame.wm_title('Stickies! Settings')

            main_settings_frame = tk.LabelFrame(settings_frame, bg='#ffffff')
            main_settings_frame.pack()

            color_picker_label = tk.Label(main_settings_frame, text='Default Color:')
            color_picker_label.pack()

            r1s = tk.Radiobutton(main_settings_frame,
                                 text=ColorList[0].color_name,
                                 variable=color_int_var,
                                 value=1,
                                 bg=ColorList[0].hex_code,
                                 selectcolor=ColorList[0].hex_code,
                                 indicator=0,
                                 command=sel)
            r1s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r2s = tk.Radiobutton(main_settings_frame,
                                 text=ColorList[1].color_name,
                                 variable=color_int_var,
                                 value=2,
                                 bg=ColorList[1].hex_code,
                                 selectcolor=ColorList[1].hex_code,
                                 indicator=0,
                                 command=sel)
            r2s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r3s = tk.Radiobutton(main_settings_frame,
                                 text=ColorList[2].color_name,
                                 variable=color_int_var,
                                 value=3,
                                 bg=ColorList[2].hex_code,
                                 selectcolor=ColorList[2].hex_code,
                                 indicator=0,
                                 command=sel)
            r3s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r4s = tk.Radiobutton(main_settings_frame,
                                 text=ColorList[3].color_name,
                                 variable=color_int_var,
                                 value=4,
                                 bg=ColorList[3].hex_code,
                                 selectcolor=ColorList[3].hex_code,
                                 indicator=0,
                                 command=sel)
            r4s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r5s = tk.Radiobutton(main_settings_frame,
                                 text=ColorList[4].color_name,
                                 variable=color_int_var,
                                 value=5,
                                 bg=ColorList[4].hex_code,
                                 selectcolor=ColorList[4].hex_code,
                                 indicator=0,
                                 command=sel)
            r5s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r6s = tk.Radiobutton(main_settings_frame,
                                 text=ColorList[5].color_name,
                                 variable=color_int_var,
                                 value=6,
                                 bg=ColorList[5].hex_code,
                                 selectcolor=ColorList[5].hex_code,
                                 indicator=0,
                                 command=sel)
            r6s.pack(expand=TRUE, fill=BOTH, side=TOP)
            # deselect all after opening settings
            radiobutton_list = [r1s, r2s, r3s, r4s, r5s, r6s]

            for radiobutton in radiobutton_list:
                radiobutton.deselect()

            font_picker_label = tk.Label(main_settings_frame, text='Default Font:')
            font_picker_label.pack()

            rf1s = tk.Radiobutton(main_settings_frame,
                                  text=FontList[0].font_style,
                                  variable=int_var_font,
                                  value=1,
                                  font=FontList[0].font_style_full,
                                  indicator=0,
                                  command=selected)
            rf1s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf2s = tk.Radiobutton(main_settings_frame,
                                  text=FontList[1].font_style,
                                  variable=int_var_font,
                                  value=2,
                                  font=FontList[1].font_style_full,
                                  indicator=0,
                                  command=selected)
            rf2s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf3s = tk.Radiobutton(main_settings_frame,
                                  text=FontList[2].font_style,
                                  variable=int_var_font,
                                  value=3,
                                  font=FontList[2].font_style_full,
                                  indicator=0,
                                  command=selected)
            rf3s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf4s = tk.Radiobutton(main_settings_frame,
                                  text=FontList[3].font_style,
                                  variable=int_var_font,
                                  value=4,
                                  font=FontList[3].font_style_full,
                                  indicator=0,
                                  command=selected)
            rf4s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf5s = tk.Radiobutton(main_settings_frame,
                                  text=FontList[4].font_style,
                                  variable=int_var_font,
                                  value=5,
                                  font=FontList[4].font_style_full,
                                  indicator=0,
                                  command=selected)
            rf5s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf6s = tk.Radiobutton(main_settings_frame,
                                  text=FontList[5].font_style,
                                  variable=int_var_font,
                                  value=6,
                                  font=FontList[5].font_style_full,
                                  indicator=0,
                                  command=selected)
            rf6s.pack(expand=TRUE, fill=BOTH, side=TOP)
            radiobutton_list_f = [rf1s, rf2s, rf3s, rf4s, rf5s, rf6s]

            for radiobutton in radiobutton_list_f:
                radiobutton.deselect()

            # button calls the save_settings function which adds preferences to an array
            # closes the settings window
            close_settings = tk.Button(main_settings_frame, text='Done',
                                       command=lambda: close_settings_window())
            close_settings.pack(side=LEFT, padx=10, pady=5, fill=X, expand=TRUE)

            def close_settings_window():
                settings_frame.destroy()


myapp = App()

# method calls to windows manager class ---> title, size and opacity
myapp.master.title(application_title)
myapp.master.geometry('300x700')
myapp.master.wm_attributes('-alpha', 0.85)

if __name__ == '__main__':
    myapp.mainloop()
