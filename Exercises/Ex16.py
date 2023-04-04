import PySimpleGUI as sg

feet_label = sg.Text("Enter Feet")
feet_input = sg.Input(key="Feet")

inches_label = sg.Text("Enter Inches")
inches_input = sg.Input(key="Inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Converter",
                   layout=[[feet_label, feet_label],
                    [inches_label, inches_input],
                    convert_button, print(feet * .305 + inches * .0254)])