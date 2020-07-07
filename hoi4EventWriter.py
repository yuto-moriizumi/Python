fpCountries = open(
    'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Hearts of Iron IV\\common\\country_tags\\00_countries.txt', "r")
fpResult = open("result.txt", "w")
n = 0

fpResult.write("add_namespace = indmv\n\n")

while True:
    tag = fpCountries.readline()[0:3]
    if not tag:
        break
    fpResult.write("""
country_event={
    id=indmv."""+(str)(n)+"""
    title=indmv.0.t
    desc=indmv.0.d
    picture=picture=GFX_event_test
    trigger={
        has_stability < 0.4
        NOT={country_exists="""+tag+"""}
        any_owned_state={
            is_core_of="""+tag+"""
            NOT={is_core_of=ROOT}
        }
    }
    mean_time_to_happen = {
        random_list = {
            days = 30
            days = 60
            days = 90
            days = 120
            days = 150
            days = 180
        }
    }
    option={
        name=indmv.0.a
        add_threat=-5
        every_owned_state={
            limit={
                is_core_of="""+tag+"""
                NOT={is_core_of=ROOT}
            }
            """+tag+"""={transfer_state=PREV}
        }
        """+tag+"""={
            add_equipment_to_stockpile={
                type=infantry_equipment
                amount=20000
            }
            add_manpower=10000
            add_timed_idea={
                idea=fastmil
                days=180
            }
        }
    }
    option={
        name=indmv.0.b
        every_owned_state={
            limit={
                is_core_of="""+tag+"""
                NOT={is_core_of=ROOT}
            }
            """+tag+"""={transfer_state=PREV}
        }
        """+tag+"""={
            add_equipment_to_stockpile={
                type=infantry_equipment
                amount=20000
            }
            add_manpower=10000
            add_timed_idea={
                idea=fastmil
                days=360
            }
            add_timed_idea={
                idea=indwar
                days=360
            }
            add_political_power=2000
        }
        declare_war_on={
            target="""+tag+"""
            type=annex_everything
        }
        ai_chance={factor=320}
    }
}""")
    n += 1

fpCountries.close()
fpResult.close()
