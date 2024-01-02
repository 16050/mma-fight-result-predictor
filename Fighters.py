import pandas as pd
ufc_fighters = pd.read_csv('csv_data/ufc_fighter_data.csv', parse_dates = ['fighter_dob'])
fighters_data = ufc_fighters[['fighter_id','fighter_f_name','fighter_l_name','fighter_height_cm','fighter_weight_lbs','fighter_reach_cm','fighter_stance']]

#get all weight classes
ufc_fights = pd.read_csv('csv_data/ufc_fight_data.csv')
weight_classes = ufc_fights.weight_class.unique().tolist()
weight_classes = weight_classes[:-1]

#add weightclass attribute for each fighter
def add_weightclass():
    fighters_data['weight_class']=''
    for i, r in fighters_data.iterrows():
        weight = r['fighter_weight_lbs']
        gender = r['fighter_weight_lbs']
        if weight <= 115:
            fighters_data.loc[i, 'weight_class'] = "Women's Strawweight"
        elif (weight <= 125)&(weight > 115) :
            fighters_data.loc[i, 'weight_class'] = "Flyweight"
        elif (weight <= 135)&(weight > 125) :
            fighters_data.loc[i, 'weight_class'] = "Bantamweight"
        elif (weight <= 145)&(weight > 135) :
            fighters_data.loc[i, 'weight_class'] = "Featherweight"
        elif (weight <= 155)&(weight > 145) :
            fighters_data.loc[i, 'weight_class'] = "Lightweight"
        elif (weight <= 170)&(weight > 155) :
            fighters_data.loc[i, 'weight_class'] = "Welterweight"
        elif (weight <= 185)&(weight > 170) :
            fighters_data.loc[i, 'weight_class'] = "Middleweight"
        elif (weight <= 205)&(weight > 185) :
            fighters_data.loc[i, 'weight_class'] = "Light Heavyweight"
        elif (weight <= 265)&(weight > 205) :
            fighters_data.loc[i, 'weight_class'] = "Heavyweight"
        elif (weight > 265) :
            fighters_data.loc[i, 'weight_class'] = "Open Weight"
    return fighters_data

def fighters_weightclass(weightclass):
    add_weightclass()
    a = fighters_data.loc[fighters_data['weight_class'] == weightclass, ['fighter_id', 'fighter_f_name','fighter_l_name']]
    a = a.where(pd.notnull(a), None)
    return [r for r in a.to_dict(orient='records')]
