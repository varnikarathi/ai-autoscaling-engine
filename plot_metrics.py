import matplotlib.pyplot as plt
times=[]
rps_count=[]
with open("metrics.txt") as f:
    for line in f:
        time_elapsed, _,rps=line.strip().split(",")
        times.append(float(time_elapsed))
        rps_count.append(float(rps)) 
plt.plot(times,rps_count)
plt.xlabel("Time(seconds)")
plt.ylabel("Requests per seconds")
plt.title("Server load over Time")
plt.show()
