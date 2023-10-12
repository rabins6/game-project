import queries.insert


want_to_play = input('Would you like to play a game? (Type y for yes OR n for no) : ')


if want_to_play == 'y':
    player_name = input('Please, type in your name : ')
    player_email = input('Please, type in your email : ')

    queries.insert.insert('user',
                          f"email, player_name, co2_consumed, co2_budget, location",
                          f"'{player_email}', '{player_name}', '8000', '10000', 'ttt'")
