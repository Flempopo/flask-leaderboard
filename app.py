from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def fetch_players(start=1, count=100):
    response = requests.get(f"https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start={start}&count={count}")
    players = response.json()['leaderboard']
    
    # Round the win rate to two decimal places for each player
    for player in players:
        player['win_rate'] = round((player['wins'] / player['games']) * 100, 2)
    
    return players

@app.route('/')
def leaderboard():
    data = fetch_players()
    return render_template('index.html', data=data)

@app.route('/load-more')
def load_more():
    start = int(request.args.get('start', 101))
    count = int(request.args.get('count', 100))
    data = fetch_players(start=start, count=count)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
