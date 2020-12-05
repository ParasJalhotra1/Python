data = {1: [101, "Ram", 25000],
2: [102, "Ravi", 25000],
3: [103, "Siva", 25000],
4: [104, "Suraj", 25000]
}
print ("{:<5} {:<10} {:<10} {:<10}".format('S.No','ID','Name','Salary'))
print("******************************************")
for k, ls in data.items():
    id, name, salary = ls
    print ("{:<5} {:<10} {:<10} {:<10}".format(k, id, name, salary))