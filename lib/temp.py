def home_dict():
    return {
        "ApartmentBuilding": {
            "Address": {"house_number":5, "street": "ffstreet" },
            "colors": ["Wine", "Gold"],
            "Apartments": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
            ],
        },
            
        "ApartmentBuilding2": {
           "Address": {"house_number":11 , "street": "blockstreet" },
           "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
            ]
        }
    }


def home_colors(home_name):
    home_data = home_dict()
    for building in home_data.values():
        if building["home_name"] == home_name:
            print(building["colors"])

def building_Address():
    home_data = home_dict()
    for building in home_data.values():
        print(building["Address"])
        
def home_numbers(home_name):
    home_data = home_dict()
    for building in home_data.values():
        if building["home_name"] == home_name:
            print(building["players"]["number"])
            