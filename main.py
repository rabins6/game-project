import geopy.distance
import queries.insert
import queries.select
import queries.update

want_to_play = input('Would you like to play a game? (Type y for yes OR n for no) : ')


def getLocationBySerialNum(serial_num):
    return queries.select.select('latitude_deg, longitude_deg', 'airport', f"serial_num='{serial_num}'")


def calculateDistanceInKilometer(location_1, location_2):
    return geopy.distance.distance(location_1, location_2).km


if want_to_play.lower() == 'y':
    CURRENT_LOCATION = '60.3172, 24.963301'

    player_name = None
    player_email = input('Please, type in your email : ')

    existing_player = queries.select.select('email', 'user', f"email='{player_email}'")

    if existing_player is None:
        player_name = input('Please, type in your name : ')
        queries.insert.insert('user',
                              f"email, player_name, location",
                              f"'{player_email}', '{player_name}', 'LOCATION'")

    user = queries.select.select('co2_consumed', 'user', f"email='{player_email}'")

    while int(user[0]) < 10000:
        user = queries.select.select('co2_consumed', 'user', f"email='{player_email}'")
        chosen_num_by_player = input('Please, choose number from (1,2,3,4,5,6,7,8,9,10) : ')

        chosen_location = getLocationBySerialNum(chosen_num_by_player)

        distanceInKilometer = calculateDistanceInKilometer(CURRENT_LOCATION, chosen_location)

        co2_consumed_by_player = int(distanceInKilometer * 0.4) + int(user[0])
        print(f"co2 consumed {co2_consumed_by_player}")

        queries.update.update('user', f"co2_consumed={co2_consumed_by_player}", f"email='{player_email}'")

        if co2_consumed_by_player > 10000:
            exit()
