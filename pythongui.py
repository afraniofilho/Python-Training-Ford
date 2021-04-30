from dearpygui.core import *
from dearpygui.simple import *
import pandas as pd

df = pd.DataFrame (columns = ['Prefix', 'Base', 'Sufix'])

def add(sender, data):
    global df
    with window("Main"):
        info = [get_value("InputPrefix"),get_value("InputBase"), get_value("InputSufix")]
        pred.append(data)
        add_row("Table Example", [info[0], info[1], info[2]])
        df = df.append({'Prefix': info[0], 'Base': info[1], 'Sufix': info[2]}, ignore_index=True)
        print(df)



pred=[]
info ={}
set_main_window_size (540,720)
set_global_font_scale(1.25)
set_theme("Gold")
set_style_window_padding(30,30)

with window("Main", width = 520, height=677):
    print("GUI is running")
    set_window_pos("Main", 0,0)
    add_drawing("logo", width = 520, height=210)
    add_separator()
    add_spacing(count=5)
    add_text("6Sigma Application", color=[232,163,33])
    add_spacing(count=12)
    add_input_text("InputPrefix", width=100, default_value= "", label="Prefix")
    add_spacing(count=12)
    add_input_text("InputBase", width=100, default_value= "", label="Base")
    add_spacing(count=12)
    add_input_text("InputSufix", width=100, default_value= "", label="Sufix")
    add_spacing(count=12)
    add_button("Add", callback=add, callback_data=info)
    add_spacing(count=12)
    add_table("Table Example", ["Prefix", "Base", "Sufix"])
 

draw_image("logo", "6sigma.jpg", [0,0], [458,192])
start_dearpygui()