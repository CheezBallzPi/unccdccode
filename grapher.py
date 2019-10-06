import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd
import pygal

def Nmaxelements(dict1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        maxnum = 0
        maxname = ""
          
        for key, val in dict1.items():      
            if val > maxnum: 
                maxnum = val; 
                maxname = key
                  
        dict1.pop(key); 
        final_list.append(key)
    return final_list

def graph(total):
    # this is the name of each county and the total votes 
    print("--- graph test ---")   
    county_and_votes = {}
    county_names = []
    county_votes = []
    for county_name, d in total.items():
        county_names.append(county_name)
        total_votes = 0
        for party_name, count in total[county_name].items():
            total_votes = total_votes + total[county_name][party_name]
        county_and_votes[county_name] = total_votes
    top_five_names = Nmaxelements(county_and_votes, 5)
    
    my_config = pygal.Config()
    my_config.x_label_rotation = 0
    my_config.x_label_font_size = 14
    my_config.show_legend = True
    my_config.truncate_label = 15
    my_config.width = 1000
    chart = pygal.StackedBar(my_config)
    chart.title = 'Parties'
    chart.x_labels = top_five_names
    chart.add('UNA', [total[x]['UNA'] for x in top_five_names])
    chart.add('DEM', [total[x]['DEM'] for x in top_five_names])
    chart.add('REP', [total[x]['REP'] for x in top_five_names])
    chart.add('LIB', [total[x]['LIB'] for x in top_five_names])
    chart.add('GRE', [total[x]['GRE'] for x in top_five_names])
    chart.add('CST', [total[x]['CST'] for x in top_five_names])
    chart.render_in_browser()