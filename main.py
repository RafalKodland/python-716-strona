from flask import Flask, render_template
from random import choice

app = Flask(__name__)

facts = [
    "Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń.",
    "Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów.",
    "Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.",
    "Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy.",
    "Jednym ze sposobów walki z uzależnieniem od technologii jest poszukiwanie zajęć, które sprawiają przyjemność i poprawiają nastrój.",
    "Elon Musk twierdzi, że sieci społecznościowe są zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.",
    "Elon Musk opowiada się także za regulacją sieci społecznościowych i ochroną danych osobowych użytkowników. Twierdzi, że sieci społecznościowe gromadzą o nas ogromną ilość informacji, które następnie można wykorzystać do manipulowania naszymi myślami i zachowaniami.",
    "Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi."
]

@app.route("/")
def hello_world():
    return "<p>Witaj! <a href='/losowy_fakt'>Kliknij tutaj</a>, aby przenieść się na strone z losowymi faktami!</p>"

@app.route("/losowy_fakt")
def random_fact():
    wylosowany_fakt = choice(facts)
    losowy_kolor = choice(["blue", "black", "red", "green"])
    return render_template("index.html", fakt = wylosowany_fakt, kolor = losowy_kolor)

app.run(debug=True)