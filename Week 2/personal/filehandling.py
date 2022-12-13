#file = open("my_file.txt","w")

#file.write("\nhello, its me.")

file = open("password.txt","w")
file.write("anup,anup123")
user_pwd = open('password.txt',"r").read()
print(user_pwd[0])
