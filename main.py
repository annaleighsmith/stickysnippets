from tkinter import (BOTH, BOTTOM, TRUE, TOP, X,
                     LEFT, RIGHT, WORD, Label, LabelFrame,
                     IntVar, Frame, StringVar, Entry,
                     Radiobutton, Button, Toplevel, TclError)
from tkinter import Text as tk_Text
from tkinter.filedialog import asksaveasfile


# --  classes to define font and color formatting  ----------------->


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


# --  constant variables  ------------------------------------------>

application_title = 'Stickies!'
application_font = 'Lucida Bright'
xs_font = (application_font, 8)
small_font = (application_font, 10)
medium_font = (application_font, 12)
large_font = (application_font, 20)
color0 = MyColors('white', '#ffffff', 0)
color1 = MyColors('pink', '#f2c6de', 1)
color2 = MyColors('blue', '#c6def1', 2)
color3 = MyColors('yellow', '#fcf6bd', 3)
color4 = MyColors('green', '#d0f4de', 4)
color5 = MyColors('orange', '#f7d9c4', 5)
color6 = MyColors('purple', '#dbcdf0', 6)
font_tup0 = ('Calibri', 12)
font0 = MyFonts('Calibri', font_tup0, 0)
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

ColorList = (color0, color1, color2, color3, color4, color5, color6)
FontList = (font0, font1, font3, font4, font5, font6, font2)


# -- methods ------------------------------------------------------>


def clear_rbs(array):
    for val in array:
        val.deselect()


# --  create main window  ------------------------------------------>


class App(Frame):
    def __init__(self,
                 master=None,
                 ):
        super().__init__(master)

        self.pack()
        self.color_setting = None
        self.name_entry = StringVar()
        self.color_choice = StringVar()
        self.font_choice = StringVar()
        self.default_type = StringVar()
        self.configure(bg='#ffffff')

        # --  application title  ------------------------------------------->
        main = LabelFrame(self, text=application_title, bg='#ffffff', font=large_font, )
        main.pack(padx=5, pady=5)

        # --  name label and entry box  ------------------------------------>

        label_name = Label(main, text='Name your note', font=medium_font, bg='#ffffff', )
        label_name.pack(expand=TRUE, side=TOP, padx=5, pady=5, )
        name_entry = Entry(main, textvariable=self.name_entry, font=medium_font, bg='#f1f1f1', )
        name_entry.pack(expand=TRUE, side=TOP, padx=5, pady=5, )

        # --  section for color choice  ------------------------------------>
        frame_colors = Frame(main, bg='#ffffff')
        frame_colors.pack()

        # --  function for returning integer variables from input  ---------->
        color_int_var = IntVar()

        # --  frame for color buttons  ------------------------------------->
        frame_colors = Frame(main, bg='#ffffff')
        frame_colors.pack(padx=10, pady=10)
        color_label = Label(frame_colors, text='Choose a color for your sticky:', bg='#FFFFFF', font=medium_font)
        color_label.pack(expand=TRUE, fill=BOTH, side=TOP, )

        # --  radio buttons to select color  ------------------------------->
        r1 = Radiobutton(frame_colors,
                         text=ColorList[1].color_name,
                         variable=color_int_var,
                         value=1,
                         bg=ColorList[1].hex_code,
                         selectcolor=ColorList[1].hex_code,
                         indicator=0,
                         font=small_font, )
        r1.pack(expand=TRUE, fill=BOTH, side=TOP)
        r2 = Radiobutton(frame_colors,
                         text=ColorList[2].color_name,
                         variable=color_int_var,
                         value=2,
                         bg=ColorList[2].hex_code,
                         selectcolor=ColorList[2].hex_code,
                         indicator=0,
                         font=small_font, )
        r2.pack(expand=TRUE, fill=BOTH, side=TOP)
        r3 = Radiobutton(frame_colors,
                         text=ColorList[3].color_name,
                         variable=color_int_var,
                         value=3,
                         bg=ColorList[3].hex_code,
                         selectcolor=ColorList[3].hex_code,
                         indicator=0,
                         font=small_font, )
        r3.pack(expand=TRUE, fill=BOTH, side=TOP)
        r4 = Radiobutton(frame_colors,
                         text=ColorList[4].color_name,
                         variable=color_int_var,
                         value=4,
                         bg=ColorList[4].hex_code,
                         selectcolor=ColorList[4].hex_code,
                         indicator=0,
                         font=small_font, )
        r4.pack(expand=TRUE, fill=BOTH, side=TOP)
        r5 = Radiobutton(frame_colors,
                         text=ColorList[5].color_name,
                         variable=color_int_var,
                         value=5,
                         bg=ColorList[5].hex_code,
                         selectcolor=ColorList[5].hex_code,
                         indicator=0,
                         font=small_font, )
        r5.pack(expand=TRUE, fill=BOTH, side=TOP)
        r6 = Radiobutton(frame_colors,
                         text=ColorList[6].color_name,
                         variable=color_int_var,
                         value=6,
                         bg=ColorList[6].hex_code,
                         selectcolor=ColorList[6].hex_code,
                         indicator=0,
                         font=small_font, )
        r6.pack(expand=TRUE, fill=BOTH, side=TOP)
        rb_list_1 = [r1, r2, r3, r4, r5, r6]
        clear_rbs(rb_list_1)

        font_int_var = IntVar()
        # --  frame for font buttons  -------------------------------------->
        frame_font = Frame(main, bg='#ffffff')
        frame_font.pack(padx=10, pady=10)
        font_label = Label(frame_font, text='Choose a font for your sticky:', bg='#FFFFFF', font=medium_font)
        font_label.pack(expand=TRUE, fill=BOTH, side=TOP)

        # --  radio buttons to select font  -------------------------------->
        rf1 = Radiobutton(frame_font,
                          text=FontList[1].font_style,
                          variable=font_int_var,
                          value=1,
                          font=FontList[1].font_style_full,
                          indicator=0,
                          )
        rf1.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf2 = Radiobutton(frame_font,
                          text=FontList[2].font_style,
                          variable=font_int_var,
                          value=2,
                          font=FontList[2].font_style_full,
                          indicator=0,
                          )
        rf2.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf3 = Radiobutton(frame_font,
                          text=FontList[3].font_style,
                          variable=font_int_var,
                          value=3,
                          font=FontList[3].font_style_full,
                          indicator=0,
                          )
        rf3.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf4 = Radiobutton(frame_font,
                          text=FontList[4].font_style,
                          variable=font_int_var,
                          value=4,
                          font=FontList[4].font_style_full,
                          indicator=0,
                          )
        rf4.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf5 = Radiobutton(frame_font,
                          text=FontList[5].font_style,
                          variable=font_int_var,
                          value=5,
                          font=FontList[5].font_style_full,
                          indicator=0, )
        rf5.pack(expand=TRUE, fill=BOTH, side=TOP)
        rf6 = Radiobutton(frame_font,
                          text=FontList[6].font_style,
                          variable=font_int_var,
                          value=6,
                          font=FontList[6].font_style_full,
                          indicator=0, )
        rf6.pack(expand=TRUE, fill=BOTH, side=TOP)

        rb_list_2 = [rf1, rf2, rf3, rf4, rf5, rf6]
        clear_rbs(rb_list_2)

        # --  frame for main page buttons  --------------------------------->
        main_button_frame = Frame(main, bg='#FFFFFF')
        main_button_frame.pack(side=BOTTOM, padx=10, pady=10)

        # --  button to create a new note  --------------------------------->
        my_create_button = Button(
            main_button_frame,
            text='Create',
            command=lambda: sticky_note(),
            font=medium_font,
            bg='#FFFFFF')
        my_create_button.pack(expand=TRUE, fill=BOTH, side=LEFT)

        # --  button to open settings  ------------------------------------->
        my_settings_button = Button(
            main_button_frame,
            text='Settings',
            command=lambda: settings_window(),
            font=medium_font,
            bg='#FFFFFF')

        my_settings_button.pack(expand=TRUE, fill=BOTH, side=LEFT)

        def clear_selections():
            rb_list_all = [rf1, rf2, rf3, rf4, rf5, rf6, r1, r2, r3, r4, r5, r6]
            clear_rbs(rb_list_all)
            name_entry.delete(0, 'end')

        # --  button to clear all selections  ------------------------------------->

        clear_button = Button(
            main_button_frame,
            text='Clear',
            command=clear_selections,
            font=medium_font,
            bg='#FFFFFF')

        clear_button.pack(expand=TRUE, fill=BOTH, side=LEFT)

        # --  sticky note frame  ------------------------------------------->
        def sticky_note():

            sticky_frame = Toplevel(master=main)
            # -- title of note window
            sticky_frame.wm_title(name_entry.get())
            # -- note size
            sticky_frame.geometry('300x300-10+10')
            # -- buttons at the top of each note
            button_frame = Frame(sticky_frame)
            save_button = Button(button_frame, text='Save Sticky', command=lambda: save_file())
            save_button.pack(side=LEFT, padx=10, pady=5, fill=X, expand=TRUE)
            delete_button = Button(button_frame, text='Delete Sticky', command=lambda: delete_note())
            delete_button.pack(side=RIGHT, padx=10, pady=5, expand=TRUE, fill=X)
            # -- frame for text entry
            button_frame.pack(side=TOP, fill=X, expand=TRUE)
            try:
                color_display = ColorList[color_int_var.get()].hex_code
            except TclError:
                color_display = ColorList[0].hex_code

            try:
                font_display = FontList[font_int_var.get()].font_style_full
            except TclError:
                font_display = FontList[0].font_style_full

            textbox = tk_Text(sticky_frame, wrap=WORD, bg=color_display, font=font_display)
            textbox.pack()
            clear_rbs(rb_list_1)
            clear_rbs(rb_list_2)
            # --  sticky note methods  ----------------------------------------->
            def delete_note() -> None:
                sticky_frame.destroy()

            def save_file() -> None:
                txt_content = textbox.get('1.0', 'end-1c')
                f = asksaveasfile(
                    initialfile=name_entry.get(),
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

        # --  settings frame  ---------------------------------------------->
        def settings_window():
            settings_frame = Toplevel(master=main)
            settings_frame.wm_title(application_title + 'Settings')
            settings_frame.geometry('+300+100')

            main_settings_frame = LabelFrame(settings_frame, bg='#ffffff')
            main_settings_frame.pack()

            color_picker_label = Label(main_settings_frame, text='Default Color:', bg='#ffffff')
            color_picker_label.pack()
            # --  color settings radio buttons  -------------------------------->
            # --  these are the same as the buttons on the main page except with new variable names ->

            r1s = Radiobutton(main_settings_frame,
                              text=ColorList[1].color_name,
                              variable=color_int_var,
                              value=1,
                              bg=ColorList[1].hex_code,
                              selectcolor=ColorList[1].hex_code,
                              indicator=0,
                              )
            r1s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r2s = Radiobutton(main_settings_frame,
                              text=ColorList[2].color_name,
                              variable=color_int_var,
                              value=2,
                              bg=ColorList[2].hex_code,
                              selectcolor=ColorList[2].hex_code,
                              indicator=0,
                              )
            r2s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r3s = Radiobutton(main_settings_frame,
                              text=ColorList[3].color_name,
                              variable=color_int_var,
                              value=3,
                              bg=ColorList[3].hex_code,
                              selectcolor=ColorList[3].hex_code,
                              indicator=0,
                              )
            r3s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r4s = Radiobutton(main_settings_frame,
                              text=ColorList[4].color_name,
                              variable=color_int_var,
                              value=4,
                              bg=ColorList[4].hex_code,
                              selectcolor=ColorList[4].hex_code,
                              indicator=0,
                              )
            r4s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r5s = Radiobutton(main_settings_frame,
                              text=ColorList[5].color_name,
                              variable=color_int_var,
                              value=5,
                              bg=ColorList[5].hex_code,
                              selectcolor=ColorList[5].hex_code,
                              indicator=0,
                              )
            r5s.pack(expand=TRUE, fill=BOTH, side=TOP)
            r6s = Radiobutton(main_settings_frame,
                              text=ColorList[6].color_name,
                              variable=color_int_var,
                              value=6,
                              bg=ColorList[6].hex_code,
                              selectcolor=ColorList[6].hex_code,
                              indicator=0,
                              )
            r6s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rb_list_3 = [r1s, r2s, r3s, r4s, r5s, r6s]
            clear_rbs(rb_list_3)

            font_picker_label = Label(main_settings_frame, text='Default Font:', bg='#ffffff')
            font_picker_label.pack()
            # --  font settings radio buttons  --------------------------------->
            rf1s = Radiobutton(main_settings_frame,
                               text=FontList[1].font_style,
                               variable=font_int_var,
                               value=1,
                               font=FontList[1].font_style_full,
                               indicator=0,
                               )
            rf1s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf2s = Radiobutton(main_settings_frame,
                               text=FontList[2].font_style,
                               variable=font_int_var,
                               value=2,
                               font=FontList[2].font_style_full,
                               indicator=0,
                               )
            rf2s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf3s = Radiobutton(main_settings_frame,
                               text=FontList[3].font_style,
                               variable=font_int_var,
                               value=3,
                               font=FontList[3].font_style_full,
                               indicator=0,
                               )
            rf3s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf4s = Radiobutton(main_settings_frame,
                               text=FontList[4].font_style,
                               variable=font_int_var,
                               value=4,
                               font=FontList[4].font_style_full,
                               indicator=0,
                               )
            rf4s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf5s = Radiobutton(main_settings_frame,
                               text=FontList[5].font_style,
                               variable=font_int_var,
                               value=5,
                               font=FontList[5].font_style_full,
                               indicator=0,
                               )
            rf5s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rf6s = Radiobutton(main_settings_frame,
                               text=FontList[6].font_style,
                               variable=font_int_var,
                               value=6,
                               font=FontList[6].font_style_full,
                               indicator=0,
                               )
            rf6s.pack(expand=TRUE, fill=BOTH, side=TOP)
            rb_list_4 = [rf1s, rf2s, rf3s, rf4s, rf5s, rf6s]
            clear_rbs(rb_list_4)

            close_settings = Button(main_settings_frame, text='Done',
                                    command=lambda: close_settings_window())
            close_settings.pack(side=LEFT, padx=10, pady=5, fill=X, expand=TRUE)

            def close_settings_window():
                settings_frame.destroy()


myapp = App()

# -- method calls to windows manager class --- title, size and opacity --
myapp.master.title(application_title)
myapp.master.geometry('+10+10')
myapp.master.wm_attributes('-alpha', 0.95)

if __name__ == '__main__':
    myapp.mainloop()
