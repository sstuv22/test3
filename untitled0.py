from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MyApp(App):
    
    def build(self):
        root_widget = BoxLayout(orientation = 'vertical')
        output_label = Label(size_hint_y=1)
        button_symbols = ( '1', '2', '3', '+',
                           '4', '5', '6', '-',
                           '7', '8', '9', '.',
                           '0', '*', '/', '=')
        button_grid = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text = symbol))
            
        clear_button = Button(text='Clear', size_hint_y=1)
        
        def print_button(instance):
            output_label.text += instance.text
        
        for button in button_grid.children[1:]:
            button.bind(on_press = print_button)
            
        def resize_label(label, new_height):
            label.font_size = 0.5 * label.height
            
        output_label.bind(height = resize_label)
        
        def result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                output_label.text = 'Error!'
                
        button_grid.children[0].bind(on_press=result)
        
        def clear(instance):
            output_label.text = ''
            
        clear_button.bind(on_press = clear)
        
        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)
        
        return root_widget
    
MyApp().run()