import queries.select


def getAirportsByICAO():
    queries.select.select('latitude_deg, longitude_deg', 'airport')


getAirportsByICAO()

