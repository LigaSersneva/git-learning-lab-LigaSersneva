<<<<<<< HEAD
from flask import Flask, render_template
import requests  # Bibliotēka, kas prot paņemt datus no citiem interneta serveriem

app = Flask(__name__)

@app.route('/')
def majaslapa():
    try:
        # 1. Pieprasām nejaušu vakariņu recepti no bezmaksas API servera
        atbilde = requests.get("https://themealdb.com", timeout=5)
        dati = atbilde.json()
        
        # 2. Izvelkam no datiem vajadzīgo informāciju
        ēdiens = dati['meals'][0]
        
        recepte = {
            "nosaukums": ediens['strMeal'],
            "bilde": ediens['strMealThumb']  # Bildes saite no interneta
        }
    except Exception as e:
        # Ja nav interneta vai API nedarbojas, parādām kļūdu
        recepte = {
            "nosaukums": "Neizdevās ielādēt vakariņas (Pārbaudi internetu)",
            "bilde": "https://unsplash.com" # Noklusējuma bilde
        }
        
    return render_template('index.html', recepte=recepte)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
=======
from flask import Flask, render_template
import requests  # Bibliotēka, kas prot paņemt datus no citiem interneta serveriem

app = Flask(__name__)

@app.route('/')
def majaslapa():
    try:
        # 1. Pieprasām nejaušu vakariņu recepti no bezmaksas API servera
        atbilde = requests.get("https://www.themealdb.com/api/json/v1/1/random.php", timeout=5)
        dati = atbilde.json()
        
        # 2. Izvelkam no datiem vajadzīgo informāciju
        ediens = dati['meals'][0]
        
        recepte = {
            "nosaukums": ediens['strMeal'],
            "bilde": ediens['strMealThumb']  # Bildes saite no interneta
        }
    except Exception as e:
        # Ja nav interneta vai API nedarbojas, parādām kļūdu
        recepte = {
            "nosaukums": "Neizdevās ielādēt vakariņas (Pārbaudi internetu)",
            "bilde": "https://unsplash.com" # Noklusējuma bilde
        }
        
    return render_template('index.html', recepte=recepte)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> 156cf59a4432835287444585badd61216d88580d
