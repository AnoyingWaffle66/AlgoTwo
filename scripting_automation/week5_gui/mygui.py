import PySimpleGUI as sg

sg.theme('DarkAmber') # Add colors

layout = [[sg.Text('Enter Something'), sg.Input(k='-IN-')],
        [sg.Text('Output will go here', size=(30, 1), k='-OUT-')],
        [sg.Button('OK'), sg.Button('Exit')]]

window = sg.Window('Title', layout)

event = ''
while event != 'Exit' and event != sg.WIN_CLOSED:
    event, values = window.read()
    window['-OUT-'].update(values['-IN-'])

window.close()