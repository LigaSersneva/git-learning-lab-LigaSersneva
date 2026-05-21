from flask import Flask, render_template
import requests  # Bibliotēka, kas prot paņemt datus no citiem interneta serveriem

app = Flask(__name__)

@app.route('/')
def majaslapa():
    try:
        # 1. Pieprasām datus tieši no DESERTU kategorijas filtra
        atbilde = requests.get("https://themealdb.com", timeout=5)
        dati = atbilde.json()
        
        # 2. Serveris datus atsūta zem atslēgas 'meals'. Izvēlamies no tiem vienu nejaušu desertu:
        import random
        izveletais_deserts = random.choice(dati['meals'])
        
        recepte = {
            "nosaukums": izveletais_deserts['strMeal'],
            "bilde": izveletais_deserts['strMealThumb']  # Bildes saite no interneta
        }
    except Exception as e:
        # Ja nav interneta vai API nedarbojas, parādām noklusējuma kļūdu
        recepte = {
            "nosaukums": f"Neizdevās ielādēt desertu: {e}",
            "bilde": "https://unsplash.com" # Strādājoša virtuļu bilde
        }
        
    return render_template('index.html', recepte=recepte)

if __name__ == '__main__':
    # Šis pieraksts ar 'os.environ' palīdzēs Render mākonim pašam pārvaldīt portu 3000 pēc tam
    import os
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
