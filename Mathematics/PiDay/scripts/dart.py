circle_centerx=circle_centery=circle_radius=0.5
x_inside=[]
y_inside=[]
x_outside=[]
y_outside=[]
for i in range(number_of_darts):
    x=random.random()
    y=random.random()
    if (x-circle_centerx)**2+(y-circle_centery)**2<circle_radius**2:
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)
circle2 = plt.Circle((circle_centerx, circle_centery), circle_radius,color='b',fill=False)
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(x_inside,y_inside, 'o', color='y',alpha=0.4)
ax.plot(x_outside,y_outside, 'o', color='r',alpha=0.4)
ax.add_artist(circle2)
plt.ylim(0, 1) 
plt.xlim(0, 1) 
plt.show()
print("Number of  darts inside the circle: "+str(len(x_inside)))
print("Total number of darts: "+str(number_of_darts))
print("Estimated π = ("+str(len(x_inside))+"/"+str(number_of_darts)+")×4 = "+str(len(x_inside)*4/number_of_darts)) 