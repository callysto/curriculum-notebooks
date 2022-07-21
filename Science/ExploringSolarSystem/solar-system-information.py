import ipywidgets as widgets
from IPython.display import display, clear_output, SVG

major_objects_output = widgets.Output()

class SolarSystemObject:
    def __init__(self, label, image):
        self.label = label
        self.image = image
        self.html = []
    
    def add_html(self, html):
        self.html.append(html)

class SolarSystem:
    def __init__(self):
        self.contents = [None]
        self.current = 0

    def add(self, label, image):
        self.last = SolarSystemObject(label, image)
        self.contents.append(self.last)

    def increment(self):
        self.current = (self.current + 1) % len(self.contents)

    def current_object(self):
        return self.contents[self.current]

    def next_object(self):
        return self.contents[(self.current + 1) % len(self.contents)]

solar_system = SolarSystem()

solar_system.add("the Sun", "solar_system_01_sun.svg")
solar_system.last.add_html("""<b>Circumference</b>: 109 x Earth <br> <b>Volume</b>: 1,301,019 x Earth <br> <b>Mass</b>: 333,060 x Earth <br> <b>Temperature</b>: 5,500<sup>o</sup>C <br> <b>Spectral Type</b>: Yellow dwarf <br> <b>Age</b>: 4.6 billion years""")
solar_system.last.add_html("The Sun is the most prominent feature of the Solar System, and it accounts for approximately 99.86% of all its mass. The main components of the Sun are hydrogen and helium, which make up 73% and 25% of the mass, respectively. The remaining 2% consists of heavier elements, such as oxygen, carbon, and iron. The Sun is so large that it could fit over 1 million Earths inside its volume. Within the core, nuclear fusion converts hydrogen into helium. This process releases an enormous amount of energy which radiates from the Sun in the form of heat and light.")

solar_system.add("Mercury", "solar_system_02_mercury.svg")
solar_system.last.add_html("""<b>Circumference</b>: 0.383 x Earth <br> <b>Volume</b>: 0.056 x Earth <br> <b>Mass</b>: 0.055 x Earth <br> <b>Distance from Sun</b>: 0.3871 AU (or 58 million km) <br> <b>Year</b>: 87.969 days <br> <b>Day</b>: 1407.5 hours <br> <b>Temperature</b>: -173/427<sup>o</sup>C (min/max) <br> <b>Atmosphere</b>: O<sub>2</sub>, Na, H<sub>2</sub>""")
solar_system.last.add_html("Mercury is the smallest and closest planet to the Sun. It is so small that 18 Mercury-sized planets could fit inside the volume of the Earth. The surface of Mercury is covered in craters due to its thin atmosphere, which provides little protection from meteors. Mercury has the smallest tilt of any planet in the Solar System at just 0.033 degrees. The planet was named after the Roman god often associated with trade and profit. Mercury has no known moons.")

solar_system.add("Venus", "solar_system_03_venus.svg")
solar_system.last.add_html("""<b>Circumference</b>: 0.950 x Earth <br> <b>Volume</b>: 0.857 x Earth <br> <b>Mass</b>: 0.815 x Earth <br> <b>Distance from Sun</b>: 0.723 AU (or 108 million km) <br> <b>Year</b>: 224.701 days <br> <b>Day</b>: 5832.4 hours <br> <b>Temperature</b>: 462<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: CO<sub>2</sub>, N<sub>2</sub>""")
solar_system.last.add_html("Venus is the second planet from the Sun and the second brightest object in our night sky. The surface of Venus is extremely hostile due to its thick atmosphere of carbon dioxide. This atmosphere creates a greenhouse effect by trapping heat from the Sun. Consequently, the surface temperature on Venus is 462<sup>o</sup>C, hot enough to melt lead. Unlike most of the other planets, Venus rotates in the opposite direction about its axis; an observer on Venus would see the Sun rise in the west and set in the east. The only other planet to exhibit this type of rotation is Uranus. The planet was named after the Roman goddess of love and beauty. Venus has no known moons.")

solar_system.add("Earth", "solar_system_04_earth.svg")
solar_system.last.add_html("""<b>Circumference</b>: 40,030 km <br> <b>Volume</b>: 1.083 x 10<sup>12</sup> km<sup>3</sup> <br> <b>Mass</b>: 5.972 x 10<sup>24</sup> kg <br> <b>Distance from Sun</b>: 1 AU (or 150 million km) <br> <b>Year</b>: 365.25 days <br> <b>Day</b>: 24 hours <br> <b>Temperature</b>: -89/57<sup>o</sup>C (min/max) <br> <b>Atmosphere</b>: N<sub>2</sub>, O<sub>2</sub>""")
solar_system.last.add_html("Earth is the third planet from the Sun, the largest of the inner rocky planets, and the fifth largest planet in the Solar System. It is the only planet in the Solar System known to support life. The main surface feature of the Earth is its oceans, which cover more than 71% of its surface. The age of the Earth has been estimated to be around 4.54 billion years old. It is the only planet not named after a Roman or Greek deity. Instead the name is derived from an English word meaning ground. The Earth has one moon, simply called 'the moon'.")
    
solar_system.add("Mars", "solar_system_05_mars.svg")
solar_system.last.add_html("""<b>Circumference</b>: 0.532 x Earth <br> <b>Volume</b>: 0.151 x Earth <br> <b>Mass</b>: 0.107 x Earth <br> <b>Distance from Sun</b>: 1.524 AU (or 228 million km) <br> <b>Year</b>: 686.971 days <br> <b>Day</b>: 24.6 hours <br> <b>Temperature</b>: -153/20<sup>o</sup>C (min/max) <br> <b>Atmosphere</b>: CO<sub>2</sub>, N<sub>2</sub>, Ar""")
solar_system.last.add_html("Mars is the fourth planet from the Sun. It is considerably colder and drier than Earth, with a thin dusty atmosphere. The surface of Mars is covered in red, rusty soil. Yet despite this hostile description, the planet contains many striking features, such as polar ice caps, canyons, craters, mountains, volcanoes, and deserts. During an earlier and warmer era, the surface of Mars once featured lakes and oceans of liquid water. Mars was named after the Roman god often associated with war. Mars has two moons, Phobos and Deimos.")

solar_system.add("the Asteroid Belt", "solar_system_06_asteroid_belt.svg")
solar_system.last.add_html("The Asteroid Belt is a region of space located between the orbits of Mars and Jupiter. It is occupied by millions of oddly-shaped objects called asteroids. The four largest asteroids within the belt are Ceres, Vesta, Pallas, and Hygiea. These four asteroids contain about half of all the mass within the entire Asteroid Belt. In the early history of the Solar System, protoplanets developing within this region would have been greatly affected by the gravity of Jupiter. As Jupiter passed by, it would have pulled on the protoplanets, causing numerous collisions between them, which prevented them from fusing together. What resulted instead of a planet was a belt of asteroids. The orbits of these asteroids are still significantly affected by Jupiter to this day.")

solar_system.add("Jupiter", "solar_system_07_jupiter.svg")
solar_system.last.add_html("<b>Circumference</b>: 10.973 x Earth <br> <b>Volume</b>: 1,321 x Earth <br> <b>Mass</b>: 317.8 x Earth <br> <b>Distance from Sun</b>: 5.203 AU (or 778 million km) <br> <b>Year</b>: 4,332.59 days <br> <b>Day</b>: 9.92 hours <br> <b>Temperature</b>: -145<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: H<sub>2</sub>, He")
solar_system.last.add_html("Jupiter is the fifth planet from the Sun and the first of the gas giants. It is also the largest planet in the Solar System. The mass of Jupiter is greater than 2.5 times the mass of all the other planets combined. As a gas giant, Jupiter lacks a well-defined solid surface. The atmosphere of Jupiter features many layers of clouds and a Great Red Spot, which is a persistent anticyclonic storm larger in size than the Earth. The planet was named after the king of the Roman gods, who is often associated with the sky and thunder. Jupiter has 79 known moons. The largest include Io, Europa, Ganymede, and Callisto.")

solar_system.add("Saturn", "solar_system_08_saturn.svg")
solar_system.last.add_html("<b>Circumference</b>: 9.140 x Earth <br> <b>Volume</b>: 763.594 x Earth <br> <b>Mass</b>: 95.161 x Earth <br> <b>Distance from Sun</b>: 9.5 AU (or 1,427 million km) <br> <b>Year</b>: 10,759.22 days <br> <b>Day</b>: 10.66 hours <br> <b>Temperature</b>: -178<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: H<sub>2</sub>, He")
solar_system.last.add_html("Saturn is the sixth planet from the Sun, the second of the gas giants, and the second largest planet in the Solar System. It is the only planet less dense than water. Saturn's most distinguishing feature is its spectacular ring system, which is composed primarily of ice and rock. These rings extend over 282,000 km from the planet and are thought to be fragments of comets, asteroids, or moons that were broken up by Saturn's powerful gravitational field. The planet was named after the Roman god who fathered Jupiter. Saturn has 53 official moons, with an additional 9 known moons awaiting confirmation. The largest include Titan, Rhea, and Iapetus.")
 
solar_system.add("Uranus", "solar_system_09_uranus.svg")
solar_system.last.add_html("<b>Circumference</b>: 3.981 x Earth <br> <b>Volume</b>: 63.085 x Earth <br> <b>Mass</b>: 14.536 x Earth <br> <b>Distance from Sun</b>: 19.2 AU (or 2,871 million km) <br> <b>Year</b>: 30,687.15 days <br> <b>Day</b>: 17.23 hours <br> <b>Temperature</b>: -216<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: H<sub>2</sub>, He, CH<sub>4</sub>")
solar_system.last.add_html("Uranus is the seventh planet from the Sun and the first of the ice giants. It is the only planet known to rotate on its side with an axial tilt of 97.77 degrees. This peculiar axis of rotation may have resulted from a collision with another planet-sized object in Uranus' early history. Like Venus, Uranus also features a retrograde rotation about its axis. More than 80% of its mass consists of icy materials (primarily water, methane, and ammonia). Uranus features a system of rings, though they are considerably fainter than those of Saturn. The planet was named after the Greek god of the Sky. It is the only planet named after a god of Greek mythology. Uranus has 27 known moons. The largest include Miranda, Ariel, Umbriel, Titania, and Oberon.")

solar_system.add("Neptune", "solar_system_10_neptune.svg")
solar_system.last.add_html("<b>Circumference</b>: 3.865 x Earth <br> <b>Volume</b>: 57.723 x Earth <br> <b>Mass</b>: 17.148 x Earth <br> <b>Distance from Sun</b>: 30.1 AU (or 4,498 million km) <br> <b>Year</b>: 60,190.03 days <br> <b>Day</b>: 16.11 hours <br> <b>Temperature</b>: -201<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: H<sub>2</sub>, He, CH<sub>4</sub>")
solar_system.last.add_html("Neptune is the eighth planet from the Sun, the second of the ice giants, and the most distant planet in the Solar System. It is also the windiest planet in the solar system, with clouds moving across the atmosphere at speeds exceeding 2,100 km/h. Neptune was named after the Roman god of the sea. Neptune has 6 faint rings and 13 moons. The largest of these moons is Triton, which comprises more than 99.5% of the mass orbiting Neptune.")

solar_system.add("the Kuiper Belt", "solar_system_11_kuiper_belt.svg")
solar_system.last.add_html("The Kuiper Belt is a region of space located beyond the orbit of Neptune. Like the Asteroid Belt, the Kuiper Belt is occupied by millions of small bodies that formed during the early stages of the Solar System. However, unlike the Asteroid Belt, the majority of these small bodies are composed of icy materials instead of rock. The most notable objects in the Kuiper Belt include the dwarf planets Pluto, Eris, Haumea, and Makemake. The objects within the Kuiper Belt are strongly influenced by Neptune's gravity, and vice versa. One of Neptune's moons, Triton, may have originated from the Kuiper Belt.")

#Toggle images
def show_major_objects():
    current_object = solar_system.current_object()
    if current_object:
        display(SVG("Images/%s" % current_object.image))
        display(*[widgets.HTMLMath(value=html) for html in current_object.html])
    else:
        display(SVG("Images/solar_system_00_blank.svg"))
    next_object = solar_system.next_object()
    if next_object:
        display(widgets.HTMLMath(value="<b><i>Press the 'Explore!' button again to learn more about %s.</i></b>" % next_object.label))
        
explore_major_objects_button = widgets.Button(description="Explore!", button_style = 'success')
display(explore_major_objects_button)

def major_objects_clicked(button):
    solar_system.increment()
    with major_objects_output:
        clear_output(wait=True)
        show_major_objects()

explore_major_objects_button.on_click(major_objects_clicked)
display(major_objects_output)
with major_objects_output:
    show_major_objects()