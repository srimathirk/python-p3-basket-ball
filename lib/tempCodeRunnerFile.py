def num_points_per_game(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player in team["players"]:
            if player["name"] == player_name:
                print (player["points_per_game"])
                return player["points_per_game"]
num_points_per_game("Davis Bertans")
