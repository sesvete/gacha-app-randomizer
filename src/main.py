# ta datoteka bo služila za radnomizacij podatkov
# uporabnik bo imel možnost izbrati mode - SQL oz NoSQL
# izbral bo tudi število uporabnikov in koliko pullov z vsak banner

import json

# mora biti tudi la standard in weapon banner
# mora biti za vse igre

json_data = """
{
    "users":{
        "$uid":{
            "games":{
                "genshin_impact":{
                    "limited":{
                        "counter_progress":{
                            "guaranteed": false,
                            "number": 0
                        },
                        "pulled_units":{
                            "$pulled_unit":{
                                "date": "date",
                                "fromBanner": false,
                                "numOfPull": 80,
                                "unitName": "LOST"
                            }
                        }
                    }
                }
            }
        }
    }
}
"""

x =  '{ "name":"John", "age":30, "city":"New York"}'

data = json.loads(json_data)

print(data)

