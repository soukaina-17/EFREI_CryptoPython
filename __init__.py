from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
      #Comm3                                                                                                                                 
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/', methods=['POST'])
def decryptage():
    try:
        data = request.get_json()
        encrypted_text = data.get('encrypted_text')

        if not encrypted_text:
            return jsonify({"error": "Champ 'encrypted_text' manquant"}), 400

        decrypted_text = f.decrypt(encrypted_text.encode()).decode()
        return jsonify({"decrypted_text": decrypted_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
