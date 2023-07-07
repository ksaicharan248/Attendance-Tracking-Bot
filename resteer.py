s = {'486' : {'percentage' : '77.47' , 'state' : ''} , '467' : {'percentage' : '74.89' , 'state' : ''} ,
     '412' : {'percentage' : '73.87' , 'state' : ''} , '469' : {'percentage' : '71.67' , 'state' : ''} ,
     '491' : {'percentage' : '71.06' , 'state' : ''} , '478' : {'percentage' : '70.82' , 'state' : ''} ,
     '4A3' : {'percentage' : '69.55' , 'state' : ''} , '4B1' : {'percentage' : '67.39' , 'state' : ''} ,
     '408' : {'percentage' : '65.87' , 'state' : ''} , '464' : {'percentage' : '63.52' , 'state' : ''} ,
     '4A5' : {'percentage' : '57.67' , 'state' : ''} , '462' : {'percentage' : '48.71' , 'state' : ''}}

import pickle

with open("attendance.pkl" , "wb") as file :
    pickle.dump(s , file)
