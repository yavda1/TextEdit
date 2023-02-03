import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
import getpass
user = getpass.getuser()
current = False
from tkinter import colorchooser
selected = False
root = Tk()
root.title("Textedit ++")
root.geometry("2000x1000")
global open_status_name
open_status_name = False
global fsize
#fsize = 16
theme = ""
fontname = ""
my_frame = Frame(root)
my_frame.pack(pady=5)
fontlist = ['Apple Braille Outline 6 Dot',
            'Apple Braille Outline 8 Dot', 'Apple Braille Pinpoint 6 Dot',
            'Apple Braille Pinpoint 8 Dot', 'Apple Braille', 'Apple Symbols', 'Keyboard', 'NewYork', 'NewYorkItalic', 'SFCompact', 'SFCompactItalic', 'SFCompactRounded', 'SFNS', 'SFNSItalic', 'SFNSMono', 'SFNSMonoItalic', 'SFNSRounded', 'Symbol', 'ZapfDingbats', 'Academy Engraved LET Fonts', 'Andale Mono', 'Apple Chancery', 'AppleGothic', 'AppleMyungjo', 'Arial Black', 'Arial Bold Italic', 'Arial Bold', 'Arial Italic', 'Arial Narrow Bold Italic', 'Arial Narrow Bold', 'Arial Narrow Italic', 'Arial Narrow', 'Arial Rounded Bold', 'Arial Unicode', 'Arial', 'Ayuthaya', 'BigCaslon', 'Bodoni 72 Smallcaps Book', 'Bodoni Ornaments', 'Bradley Hand Bold', 'Brush Script', 'Chalkduster', 'Comic Sans MS Bold', 'Comic Sans MS', 'Courier New Bold Italic', 'Courier New Bold', 'Courier New Italic', 'Courier New', 'DIN Alternate Bold', 'DIN Condensed Bold', 'Diwan Thuluth', 'Farisi', 'Georgia Bold Italic', 'Georgia Bold', 'Georgia Italic', 'Georgia', 'Gurmukhi', 'Herculanum', 'Hoefler Text Ornaments', 'Impact', 'Khmer Sangam MN', 'Kokonor', 'Krungthep', 'Lao Sangam MN', 'Luminari', 'Microsoft Sans Serif', 'Mishafi Gold', 'Mishafi', 'NISC18030', 'NotoSansAdlam-Regular', 'NotoSansAvestan-Regular', 'NotoSansBamum-Regular', 'NotoSansBassaVah-Regular', 'NotoSansBatak-Regular', 'NotoSansBhaiksuki-Regular', 'NotoSansBrahmi-Regular', 'NotoSansBuginese-Regular', 'NotoSansBuhid-Regular', 'NotoSansCarian-Regular', 'NotoSansCaucasianAlbanian-Regular', 'NotoSansChakma-Regular', 'NotoSansCham-Regular', 'NotoSansCoptic-Regular', 'NotoSansCuneiform-Regular', 'NotoSansCypriot-Regular', 'NotoSansDuployan-Regular', 'NotoSansEgyptianHieroglyphs-Regular', 'NotoSansElbasan-Regular', 'NotoSansGlagolitic-Regular', 'NotoSansGothic-Regular', 'NotoSansHanifiRohingya-Regular', 'NotoSansHanunoo-Regular', 'NotoSansHatran-Regular', 'NotoSansImperialAramaic-Regular', 'NotoSansInscriptionalPahlavi-Regular', 'NotoSansInscriptionalParthian-Regular', 'NotoSansKaithi-Regular', 'NotoSansKayahLi-Regular', 'NotoSansKharoshthi-Regular', 'NotoSansKhojki-Regular', 'NotoSansKhudawadi-Regular', 'NotoSansLepcha-Regular', 'NotoSansLimbu-Regular', 'NotoSansLinearA-Regular', 'NotoSansLinearB-Regular', 'NotoSansLisu-Regular', 'NotoSansLycian-Regular', 'NotoSansLydian-Regular', 'NotoSansMahajani-Regular', 'NotoSansMandaic-Regular',
            'NotoSansManichaean-Regular', 'NotoSansMarchen-Regular', 'NotoSansMeeteiMayek-Regular', 'NotoSansMendeKikakui-Regular', 'NotoSansMeroitic-Regular', 'NotoSansMiao-Regular', 'NotoSansModi-Regular', 'NotoSansMongolian-Regular', 'NotoSansMro-Regular', 'NotoSansMultani-Regular', 'NotoSansNKo-Regular', 'NotoSansNabataean-Regular', 'NotoSansNewTaiLue-Regular', 'NotoSansNewa-Regular', 'NotoSansOgham-Regular', 'NotoSansOlChiki-Regular', 'NotoSansOldHungarian-Regular', 'NotoSansOldItalic-Regular', 'NotoSansOldNorthArabian-Regular', 'NotoSansOldPermic-Regular', 'NotoSansOldPersian-Regular', 'NotoSansOldSouthArabian-Regular', 'NotoSansOldTurkic-Regular', 'NotoSansOsage-Regular', 'NotoSansOsmanya-Regular', 'NotoSansPahawhHmong-Regular', 'NotoSansPalmyrene-Regular', 'NotoSansPauCinHau-Regular', 'NotoSansPhagsPa-Regular', 'NotoSansPhoenician-Regular', 'NotoSansPsalterPahlavi-Regular', 'NotoSansRejang-Regular', 'NotoSansRunic-Regular', 'NotoSansSamaritan-Regular', 'NotoSansSaurashtra-Regular', 'NotoSansSharada-Regular', 'NotoSansShavian-Regular', 'NotoSansSiddham-Regular', 'NotoSansSoraSompeng-Regular', 'NotoSansSundanese-Regular', 'NotoSansSylotiNagri-Regular', 'NotoSansSyriac-Regular', 'NotoSansTagalog-Regular', 'NotoSansTagbanwa-Regular', 'NotoSansTaiLe-Regular', 'NotoSansTaiTham-Regular', 'NotoSansTaiViet-Regular', 'NotoSansTakri-Regular', 'NotoSansThaana-Regular', 'NotoSansTifinagh-Regular', 'NotoSansTirhuta-Regular', 'NotoSansUgaritic-Regular', 'NotoSansVai-Regular', 'NotoSansWancho-Regular', 'NotoSansWarangCiti-Regular', 'NotoSansYi-Regular', 'NotoSerifAhom-Regular', 'NotoSerifBalinese-Regular', 'PartyLET-plain', 'PlantagenetCherokee', 'Sathu', 'Silom', 'Skia', 'Tahoma Bold', 'Tahoma', 'Times New Roman Bold Italic', 'Times New Roman Bold', 'Times New Roman Italic', 'Times New Roman', 'Trattatello', 'Trebuchet MS Bold Italic', 'Trebuchet MS Bold', 'Trebuchet MS Italic', 'Trebuchet MS', 'Verdana Bold Italic', 'Verdana Bold', 'Verdana Italic', 'Verdana', 'Webdings', 'Wingdings 2', 'Wingdings 3', 'Wingdings', 'Zapfino']

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
def replace_line(filename, line_number, text):
    with open(filename) as file:
        lines = file.readlines()

    if (line_number <= len(lines)):

        lines[line_number - 1] = text + "\n"

        with open(filename, "w") as file:

            for line in lines:
                file.write(line)







def save_as_file():
    global current
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir=f"users/{user}" , title = "Save File")
    if text_file:
        current = True
        name = text_file
        name = name.replace("users/"+user, "")
        root.title(f"{name} Textedit ++")
        status_bar.config(text = f"{name}       ")
        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        messagebox.showinfo("Saved", f"Successfully saved file {name}")

        text_file.close()
def cut_text(e):
    global selected
    if my_text.selection_get():
        selected = my_text.selection_get()
        my_text.delete("sel.first", "sel.last")
def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)
            root.clipboard_clear()
            root.clipboard_append(selected)



def pckg_dwnl():
    pass



def exit_file():
    root.destroy()
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir="users/" +user, title = "Open")
    if text_file:
        global open_status_name
        open_status_name = text_file
    name = text_file
    status_bar.config(text = f"{name}       ")
    name = name.replace("users/"+user, "")
    root.title(f"{name} Textedit ++")
    text_file = open(text_file, "r")
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
def new_file():
    my_text.delete("1.0", END)
    root.title("New File, Textedit ++")
    status_bar.config(text = "New File        ")
    global open_status_name
    open_status_name = False
def save_file():
    global current
    global open_status_name
    if current == True:
        text_file = open(open_status_name, "w")
        text_file.write(my_text.get(1.0, END))
        status_bar.config(text = "saved      ")

    else:
        save_as_file()
with open("config.txt", "r") as file:
    fsize = file.readlines()[0].rstrip()

file.close()
with open("config.txt", "r") as file:
    syn1 = file.readlines()[4].rstrip()

file.close()
with open("config.txt", "r") as file:
    syn2 = file.readlines()[5].rstrip()

file.close()
with open("config.txt", "r") as file:
    syn3 = file.readlines()[6].rstrip()

file.close()
with open("config.txt", "r") as file:
    syn4 = file.readlines()[7].rstrip()

file.close()
with open("config.txt", "r") as file:
    syn5 = file.readlines()[8].rstrip()

file.close()
with open("config.txt", "r") as file:
    syn6 = file.readlines()[9].rstrip()

file.close()
with open("config.txt", "r") as file:
    theme = file.readlines()[1].rstrip()

file.close()


with open("config.txt", "r") as file:
    fontname = file.readlines()[2].rstrip()

file.close()
with open("config.txt", "r") as file:
    pckg = file.readlines()[3].rstrip()

file.close()
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)
my_text = Text(my_frame, wrap=WORD, width=1000, height=500, font=(fontname, fsize), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set) #wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat().pattern, re.S)
def light():
    main_color = "#FFFFFF"
    secondery_color = "#dae3dc"
    text_color = "#000000"
    root.config(bg=main_color)
    #status_bar.config(bg=main_color, fg =text_color)
    my_text.config(bg=main_color,fg = text_color)
def dark():
    main_color = "#000000"
    secondery_color = "#dae3dc"
    text_color = "#FFFFFF"
    root.config(bg=main_color)
    #status_bar.config(bg=main_color, fg =text_color)
    my_text.config(bg=main_color,fg = text_color)
if theme == "Light Mode":

    cdg.tagdefs['MYGROUP'] = {'foreground': syn1, 'background': '#FFFFFF'}
    cdg.tagdefs['COMMENT'] = {'foreground': syn2, 'background': '#FFFFFF'}
    cdg.tagdefs['KEYWORD'] = {'foreground': syn3, 'background': '#FFFFFF'}
    cdg.tagdefs['BUILTIN'] = {'foreground': syn4, 'background': '#FFFFFF'}
    cdg.tagdefs['STRING'] = {'foreground': syn5, 'background': '#FFFFFF'}
    cdg.tagdefs['DEFINITION'] = {'foreground': syn6, 'background': '#FFFFFF'}
    light()
elif theme == "Dark Mode":
    cdg.tagdefs['MYGROUP'] = {'foreground': syn1, '#000000': '#FFFFFF'}
    cdg.tagdefs['COMMENT'] = {'foreground': syn2, '#000000': '#FFFFFF'}
    cdg.tagdefs['KEYWORD'] = {'foreground': syn3, '#000000': '#FFFFFF'}
    cdg.tagdefs['BUILTIN'] = {'foreground': syn4, '#000000': '#FFFFFF'}
    cdg.tagdefs['STRING'] = {'foreground': syn5, '#000000': '#FFFFFF'}
    cdg.tagdefs['DEFINITION'] = {'foreground': syn6, '#000000': '#FFFFFF'}
    dark()



def settings():


    global fsize
    setpane = Tk()
    fff = Label(setpane, text = "Font Size")
    fff.pack()
    setpane.geometry("300x500")
    setpane.title("Settings, Textedit ++")
    e = Entry(setpane, width = 50, borderwidth=5)
    e.pack()
    def closesetpane():
        if messagebox.askokcancel("Quit", "In order for all changes to properly take effect you must restart the editor."):
            setpane.destroy()
    global clicked
    clicked = StringVar()
    def setf():
        global font
        global fsize
        fsize = e.get()
        replace_line("config.txt", 1, fsize)

        my_text.config(font = (fontname, fsize))
        setpane.destroy()
    def setff():


        replace_line("config.txt", 2, "Light Mode")

        cdg.tagdefs['MYGROUP'] = {'foreground': syn1, '#000000': '#FFFFFF'}
        cdg.tagdefs['COMMENT'] = {'foreground': syn2, '#000000': '#FFFFFF'}
        cdg.tagdefs['KEYWORD'] = {'foreground': syn3, '#000000': '#FFFFFF'}
        cdg.tagdefs['BUILTIN'] = {'foreground': syn4, '#000000': '#FFFFFF'}
        cdg.tagdefs['STRING'] = {'foreground': syn5, '#000000': '#FFFFFF'}
        cdg.tagdefs['DEFINITION'] = {'foreground': syn6, '#000000': '#FFFFFF'}
        light()


        #elif th == "Dark Mode":


        setpane.destroy()

    def choose_color():
        color_code = colorchooser.askcolor(title="Choose color")
        option = color_code[1]
        syn2=option
        replace_line("config.txt", 6, syn2)
    def choose_color3():
        color_code = colorchooser.askcolor(title="Choose color")
        option = color_code[1]
        syn3=option
        replace_line("config.txt", 7, syn3)
    def choose_color4():
        color_code = colorchooser.askcolor(title="Choose color")
        option = color_code[1]
        syn4=option
        replace_line("config.txt", 8, syn4)
    def choose_color5():
        color_code = colorchooser.askcolor(title="Choose color")
        option = color_code[1]
        syn5=option
        replace_line("config.txt", 9, syn5)
    def choose_color6():
        color_code = colorchooser.askcolor(title="Choose color")
        option = color_code[1]
        syn5=option
        replace_line("config.txt", 10, syn5)


    def setfff():
        replace_line("config.txt", 2, "Dark Mode")


        cdg.tagdefs['MYGROUP'] = {'foreground': syn1, '#000000': '#FFFFFF'}
        cdg.tagdefs['COMMENT'] = {'foreground': syn2, '#000000': '#FFFFFF'}
        cdg.tagdefs['KEYWORD'] = {'foreground': syn3, '#000000': '#FFFFFF'}
        cdg.tagdefs['BUILTIN'] = {'foreground': syn4, '#000000': '#FFFFFF'}
        cdg.tagdefs['STRING'] = {'foreground': syn5, '#000000': '#FFFFFF'}
        cdg.tagdefs['DEFINITION'] = {'foreground': syn6, '#000000': '#FFFFFF'}
        dark()

        setpane.destroy()
    e.pack()

    f = Button(setpane, text = "Enter", command = setf)
    f.pack()
    fe = Button(setpane, text = "Light Mode", command = setff)
    fe.pack()
    fef = Button(setpane, text = "Dark Mode", command = setfff)
    fef.pack()
    cfff=Button(setpane, text = "MYGROUP Syntax Color", command = choose_color)
    cfff.pack()
    cffff=Button(setpane, text = "COMMENT Syntax Color", command = choose_color3)
    cffff.pack()
    cfffff=Button(setpane, text = "KEYWORD Syntax Color", command = choose_color4)
    cfffff.pack()
    cffffff=Button(setpane, text = "BUILTIN Syntax Color", command = choose_color5)
    cffffff.pack()
    cfffffff=Button(setpane, text = "STRING Syntax Color", command = choose_color6)
    cfffffff.pack()

    clicked = StringVar()
    clicked.set("Times New Roman")
    drop = OptionMenu(setpane, clicked, *fontlist)
    drop.pack()
    def changefont():
        f = clicked.get()
        fontname=f
        replace_line("config.txt", 3, fontname)
        my_text.config(font = (fontname, fsize))
    en = Button(setpane, text = "Enter", command = changefont)
    en.pack()
    def pckg():
        fontname=f
        replace_line("config.txt", 4, "TKExtensions")
    end = Button(setpane, text = "Add tkinter Package", command = pckg)
    setpane.protocol("WM_DELETE_WINDOW", closesetpane)
    end.pack()


    setpane.mainloop()
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Settings",command=settings)
file_menu.add_separator()
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_command(label = "Save As", command = save_as_file)
file_menu.add_separator()

file_menu.add_command(label = "Exit", command = exit_file)
edit_menu = Menu(my_menu, tearoff=False)
pckg_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
my_menu.add_cascade(label = "Packages", menu = pckg_menu)
edit_menu.add_command(label = "Cut", accelerator = "Cmd+X", command = lambda: cut_text(False))
edit_menu.add_command(label = "Copy", accelerator = "Cmd+C",command = lambda: copy_text(False))
edit_menu.add_command(label = "Paste", accelerator = "Cmd+V",command = lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label = "Undo", command = my_text.edit_undo, accelerator="Cmd+Z")
edit_menu.add_command(label = "Redo", command = my_text.edit_redo, accelerator="Cmd+Y")
def add_button():
    my_text.insert(INSERT, "myButton = Button(root, text = , command = ) \nmyButton.pack()")
def create_win():
    my_text.insert(INSERT, "from tkinter import * \nroot = Tk()")
def add_label():
    my_text.insert(INSERT, "myLabel = Label(root, text = )\nmyLabel.pack()")
def add_entry():
    my_text.insert(INSERT, "myEntry = Entry(root)\nmyEntry.pack()")
def playsound():
    my_text.insert(INSERT, "from playsound import playsound\nplaysound(\"path\", block = false)")

if pckg == "TKExtensions":
    pckg_menu.add_command(label="Initizalise", command=create_win)
    pckg_menu.add_command(label="Label", command=add_label)
    pckg_menu.add_command(label="Button", command=add_button)
    pckg_menu.add_command(label="Entry", command=add_entry)




status_bar =Label(root, text = "Ready        ", anchor=E)
status_bar.pack(fill=X, side = BOTTOM, ipady=5)
ip.Percolator(my_text).insertfilter(cdg)
def light():
    main_color = "#FFFFFF"
    secondery_color = "#dae3dc"
    text_color = "#000000"
    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg =text_color)
    my_text.config(bg=main_color,fg = text_color)
def dark():
    main_color = "#000000"
    secondery_color = "#dae3dc"
    text_color = "#FFFFFF"
    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg =text_color)
    my_text.config(bg=main_color,fg = text_color)
#dark()

root.bind("<Command-Key-X>", cut_text)
root.bind("<Command-Key-C>", copy_text)
root.bind("<Command-Key-V>", paste_text)
root.bind("<Command-Key-Z>", my_text.edit_undo)
root.bind("<Command-Key-Y>", my_text.edit_redo)



root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()