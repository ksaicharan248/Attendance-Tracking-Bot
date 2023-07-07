import pickle

with open("attendance.pkl", "rb") as file:
    attendance_dict = pickle.load(file)


print(attendance_dict)