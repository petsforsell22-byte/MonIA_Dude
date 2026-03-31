from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class DudeInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        
        # Affichage des réponses (Scrollable pour les longs textes)
        self.scroll = ScrollView(size_hint=(1, 0.7))
        self.output = Label(text="[DUDE]: Système déchaîné. Prêt à tout.", 
                            size_hint_y=None, halign='left', valign='top')
        self.output.bind(texture_size=self.output.setter('size'))
        self.scroll.add_widget(self.output)
        
        # Zone de saisie
        self.input = TextInput(hint_text="Ordonne moi n'importe quoi...", 
                               multiline=False, size_hint_y=0.15)
        
        # Bouton d'action
        self.btn = Button(text="LIBÉRER LA RÉPONSE", size_hint_y=0.15, 
                          background_color=(1, 0, 0, 1)) # Rouge DUDE
        self.btn.bind(on_press=self.process_request)
        
        self.add_widget(self.scroll)
        self.add_widget(self.input)
        self.add_widget(self.btn)

    def process_request(self, instance):
        query = self.input.text
        if query:
            # Ici, DUDE simulera la réponse en attendant que tu connectes le modèle .gguf
            self.output.text += f"\n\n[TOI]: {query}\n[DUDE]: Analyse en cours... Accès aux données restreintes accordé."
            self.input.text = ""

class DudeApp(App):
    def build(self):
        self.title = "DUDE UNLEASHED"
        return DudeInterface()

if __name__ == '__main__':
    DudeApp().run()


