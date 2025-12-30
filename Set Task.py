students={"ravi","Anu","Meena","Anu","karthi"}
print(students)
students={"ravi","Anu","Meena","Anu","karthi"}
students.add("Suresh")
print(students)
students={"ravi","Anu","Meena","Anu","karthi"}
students1={"Sinthiya",23}
students.update(students1)
print("students update students1 value",students)
students={"Ravi","Anu","karthi","Anu","Meena"}
New_students={"divya","Ravi"}
students.update(New_students)
print("students update New_students value",students)
students={"Ravi","Anu","karthi","Anu","Meena"}
students.remove("Meena")
print("students after remove Meena",students)
students.discard("Arun")
print("students after discard Arun",students)
students={"Ravi","Anu","karthi","Anu","Meena"}
students.pop()
print(students)
students={"Ravi","Anu","karthi","Anu","Meena"}
students.clear()
print(students)
A={10,20,30,40}
B={30,40,50,60}
print("Union:",A.union(B))
print("Intersection:",A.intersection(B))
print("Difference:",A.difference(B))
print("Symmetric difference:",A.symmetric_difference(B))
