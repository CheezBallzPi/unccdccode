from pandas import DataFrame
import retrieve_data, grapher, subset, factorize, neural.solve
from keras.utils import to_categorical
# datavoter = retrieve_data.getData("./data/ncvoter_Statewide.txt", "./data/ncvoter_Statewide.pickle",
#     filt=['county_desc', 'status_cd', 'voter_status_desc', 'reason_cd', 'voter_status_reason_desc',
#         'mail_city', 'ethnic_code', 'party_cd', 'gender_code', 'birth_age', 'birth_state', 'drivers_lic', 
#         'precinct_abbrv', 'municipality_abbrv', 'cong_dist_abbrv', 'super_court_abbrv', 
#         'judic_dist_abbrv', 'nc_senate_abbrv', 'nc_house_abbrv', 
#         'munic_dist_abbrv', 'dist_1_abbrv', 'birth_year', 'vtd_abbrv'])
filt =['county_id','birth_age','party_cd','gender_code','race_code','birth_state']
datavoter = factorize.factorize(retrieve_data.getData("./data/ncvoter_Statewide.txt", "./data/ncvoter_Statewide.pickle", filt=filt))
print("Done!")

print(datavoter['party_cd'])

X = datavoter[['county_id','birth_age','gender_code','race_code','birth_state']]
y = to_categorical(datavoter['party_cd'])

print(X, y)

neural.solve.train(X, y)

# this is a dictionary. Key = name. Value = count
# county_party_total = subset.separateUnique(datavoter, 'county_desc')
# county_party_count = {}
# for key in county_party_total.keys():
#     county_party_total[key] = subset.separateUnique(county_party_total[key], 'party_cd')

# for county, d in county_party_total.items():
#     print("--- " + county + " ---")
#     county_party_count[county] = {}
#     for party, val in d.items():
#         county_party_count[county][party] = val.shape[0]
#         print(party, val.shape[0])

# grapher.graph(county_party_count)