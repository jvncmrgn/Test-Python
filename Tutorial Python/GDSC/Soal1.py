import string
dict = {}
bool = False
user_string = input("Masukkan Huruf = ")
String_Num = ""

for i, char in enumerate(string.ascii_lowercase):
    dict[i] = char

for val in user_string.lower():
    if(val.isdigit()):
        print("Sorry")
        bool = True
        break
    for key, value in dict.items():
        if(val == value):
            String_Num += str(key+1)
            String_Num += " "
if(not bool):
    print(String_Num)