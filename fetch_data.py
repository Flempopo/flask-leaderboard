import requests

def fetch_players(start=1, count=100):
    response = requests.get(f"https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start={start}&count={count}")
    return response.json()

data = fetch_players()
print(data)
