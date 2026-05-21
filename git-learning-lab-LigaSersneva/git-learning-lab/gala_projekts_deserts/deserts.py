from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def majaslapa():
    try:
        # 1. Pieprasām datus no desertu kategorijas filtra
        atbilde = requests.get("https://themealdb.com", timeout=5)
        dati = atbilde.json()
        
        # 2. Serveris datus vienmēr sūta zem atslēgas 'meals'. Izvēlamies vienu nejaušu desertu:
        import random
        izveletais_deserts = random.choice(dati['meals'])
        
        recepte = {
            "nosaukums": izveletais_deserts['strMeal'],
            "bilde": izveletais_deserts['strMealThumb']  # Bildes saite no interneta
        }
    except Exception as e:
        # Ja nav interneta vai API nedarbojas, parādām noklusējuma kļūdu
        recepte = {
            "nosaukums": "Neizdevās ielādēt desertu (Pārbaudi internetu)",
            "bilde": "https://unsplash.com" # Strādājoša virtuļu bilde
        }
        
    return render_template('index.html', recepte=recepte)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
