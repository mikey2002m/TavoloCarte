from flask import Flask, render_template, url_for, session, request, redirect, jsonify
from strutture import Mazzo, Carta, Tavolo, Giocatore
import json

app = Flask(__name__)
tavolo = Tavolo()


@app.route('/')
def index():
    return render_template('index.html', mazzo=Mazzo().carte)


@app.route('/iscrizione')
def iscrizione():
    username = request.args.get('username')
    tavolo.nuovo_giocatore(Giocatore(username))
    return 'eseguito'


@app.route('/aggiornamento')
def aggiornamento():
    username = request.args.get('username')
    res = {}
    tav = []
    for c in tavolo.visibili:
        tav.append({'giocatore': c['giocatore'], 'carta': c['carta'].id})
    res['tavolo'] = tav
    giocatori = []
    for g in tavolo.giocatori:
        giocatori.append({'nome': g.nome, 'n_carte': g.carte.__len__()})
    res['giocatori'] = giocatori
    if tavolo.giocatori.__len__() > 0:
        res['mazziere'] = tavolo.giocatori[tavolo.mazziere].nome
    if username != '':
        if tavolo.trova_giocatore(username) is not None:
            carte = []
            for carta in tavolo.trova_giocatore(username).carte:
                carte.append(carta.id)
            res['carte'] = carte
    res['mazzo'] = tavolo.mazzo.carte.__len__()
    return res


@app.route('/ritira_carte')
def ritira_carte():
    tavolo.ritira_carte()
    return 'eseguito'


@app.route('/scarta_tavolo')
def scarta_tavolo():
    username = request.args.get('username')
    c_id = int(request.args.get('c_id'))
    tavolo.scarta_tavolo(tavolo.trova_giocatore(username), c_id)
    return 'eseguito'


@app.route('/rimuovi_tavolo')
def rimuovi_tavolo():
    c_id = int(request.args.get('c_id'))
    tavolo.rimuovi_tavolo(c_id)
    return 'eseguito'


@app.route('/scarta')
def scarta():
    username = request.args.get('username')
    c_id = int(request.args.get('c_id'))
    tavolo.scarta(tavolo.trova_giocatore(username), c_id)
    return 'eseguito'


@app.route('/mazziere_carta_tavola')
def mazziere_carta_tavolo():
    tavolo.mazziere_carta_tavolo()
    return 'eseguito'


@app.route('/mischia')
def mishia():
    tavolo.mazzo.mischia()
    return 'eseguito'


@app.route('/mazziere_carta_giocatore')
def mazziere_carta_giocatore():
    username = request.args.get('username')
    tavolo.mazziere_dai_carta(tavolo.trova_giocatore(username))
    return 'eseguito'


@app.route('/cambiamenti')
def cambiamenti():
    return {'cambiamenti': tavolo.aggiornamento}


@app.route('/fondi')
def fondi():
    return render_template('fondi.html')


@app.route('/fondi_update')
def fondi_update():
    res = {'piatto': tavolo.piatto}
    giocatori = []
    for g in tavolo.giocatori:
        giocatori.append({
            'nome': g.nome,
            'fondi': g.fondi
        })
    res['lista_fondi'] = giocatori
    return res


@app.route('/dividi_piatto')
def dividi_piatto():
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    tavolo.dividi_piatto(a, b, c)
    return 'eseguito'


@app.route('/invia_piatto')
def invia_piatto():
    giocatore = request.args.get('giocatore')
    importo = int(request.args.get('importo'))
    tavolo.invia_piatto(giocatore, importo)
    return 'eseguito'


@app.route('/invia_giocatore')
def invia_giocatore():
    giocatore = request.args.get('giocatore')
    ricevente = request.args.get('ricevente')
    importo = int(request.args.get('importo'))
    tavolo.invia_a(giocatore, ricevente, importo)
    return 'eseguito'


if __name__ == '__main__':
    app.run()
