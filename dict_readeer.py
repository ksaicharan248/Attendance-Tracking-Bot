import pickle

with open("attendance.pkl" , "rb") as file :
    attendance_dict = pickle.load(file)

with open('attendance_data.pkl' , 'rb') as file :
    total_attendance = pickle.load(file)

with open('past_attendance_data.pkl' , 'rb') as file :
    inital = pickle.load(file)
# print(attendance_dict)
print(total_attendance[0][0] , total_attendance[0][1] , total_attendance[1][0] , total_attendance[1][1])
print(inital)
