series_l_x=[0]
series_l_y=[4]
series_n_x=[0]
series_n_y=[3]
ans = 3
j = 2
ans1 = 4
j1 = 3
for step in range(1,50):
    series_l_x.append(step)
    series_n_x.append(step)
    if step % 2 == 1:
        ans += 4.0 / (j * (j + 1) * (j + 2))
        ans1 -= 4.0 / j1
    else:
        ans -= 4.0 / (j * (j + 1) * (j + 2))
        ans1 += 4.0 / j1
    ans=round(ans,15)
    ans1=round(ans1,15)
    series_n_y.append(ans)
    series_l_y.append(ans1)
    j += 2 
    j1 += 2
fig = plt.figure(figsize=(17,7))  
plt.scatter(series_n_x,series_n_y)
plt.plot(series_n_x,series_n_y,label='Nilakantha Series')
plt.scatter(series_l_x,series_l_y, color="r")
plt.plot(series_l_x,series_l_y,color="r", label="Gregory-Leibniz Series")
plt.title("Calculating Pi - Infinite Series")
plt.ylabel('Estimated Pi')
plt.xlabel('Number of Elements')
plt.grid()
plt.legend()
plt.show()