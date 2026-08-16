import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock
import math

class JarvisCoreUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 40
        self.angle = 0

        self.status_label = Label(
            text="J.A.R.V.I.S. // ONLINE",
            font_size='18sp',
            bold=True,
            color=(0, 0.8, 1, 1)
        )
        self.add_widget(self.status_label)
        self.bind(pos=self.draw_hud, size=self.draw_hud)
        Clock.schedule_interval(self.animate_core, 1.0 / 30.0)

    def draw_hud(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.02, 0.02, 0.05, 1)
            import kivy.graphics
            kivy.graphics.Rectangle(pos=self.pos, size=self.size)
            
            cx, cy = self.center_x, self.center_y
            radius = 80 + math.sin(self.angle) * 10
            
            Color(0, 0.5, 1, 0.2)
            Ellipse(pos=(cx - radius - 20, cy - radius - 20), size=((radius + 20)*2, (radius + 20)*2))
            
            Color(0, 0.9, 1, 0.9)
            Ellipse(pos=(cx - radius, cy - radius), size=(radius*2, radius*2))

    def animate_core(self, dt):
        self.angle += 0.08
        self.draw_hud()

class JarvisApp(App):
    def build(self):
        return JarvisCoreUI()

if __name__ == '__main__':
    JarvisApp().run()
  
