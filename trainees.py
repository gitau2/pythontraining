trainees=["John",[2,["James","Mary"]]]
print(trainees)

new_trainees=trainees[1]
print(new_trainees)
print(new_trainees[0])
print(trainees[1][0])

new_trainees2=new_trainees[1]
print(new_trainees2)
print(new_trainees2[0])


print(trainees[1][1][0])

trainees.append(56)
print(trainees)


print(new_trainees2)

new_trainees2.insert(1,"Mike")
print(new_trainees2)

print(new_trainees)
print(new_trainees[0])
new_trainees[0]=8
print(new_trainees)

print(trainees)
del trainees[0]
print(trainees)

print(new_trainees)
print(new_trainees[1])
del new_trainees[1][2]
print(new_trainees)

print(len(trainees))
