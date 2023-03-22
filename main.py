from TravelAgent import TravelAgent

def main():
    travel_agent = TravelAgent('Go Jaan')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC','PRA','19/05/2020')
    # print ('Aircraft ',trip_info1.aircraft)
    # print ('price ', trip_info1.cost)

    trip_citites = ['DUB','LHR','ORD','DAC','SYD','JFK']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route(trip_citites,'05/05/2020')
    print('price',trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)



if __name__== '__main__':
    main()