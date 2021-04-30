import matplotlib.pyplot as plt

record_size = [128, 256, 384, 512, 640, 768, 896, 1024]
obs1 = [368, 850, 1544, 3035, 6650, 13887, 28059, 50916]
obs2 = [375, 850, 1644, 3123, 6839, 14567, 27439, 52129]
obs3 = [393, 824, 1533, 3235, 6768, 13456, 27659, 51350]

plt.scatter(record_size, obs1)
plt.xlabel("Record Size")
plt.ylabel("Observation 1")
plt.show()

plt.scatter(record_size, obs2)
plt.xlabel("Record Size")
plt.ylabel("Observation 2")
plt.show()

plt.scatter(record_size, obs3)
plt.xlabel("Record Size")
plt.ylabel("Observation 3")
plt.show()