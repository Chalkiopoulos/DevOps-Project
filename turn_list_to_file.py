A=["123456","password","123456789","12345678","12345","qwerty","abc123","football","monkey","letmein","admin","welcome","login","princess","dragon","passw0rd","master","hello","freedom","whatever","qazwsx","trustno1","654321","123123"]

with open("./passwords.txt", "w") as f:
    for password in A:
        f.write(password + "\n")