from scipy import stats
import matplotlib.pyplot as plt

record_size = [128, 256, 384, 512, 640, 768, 896, 1024]
obs1 = [368, 850, 1544, 3035, 6650, 13887, 28059, 50916]
obs2 = [375, 850, 1644, 3123, 6839, 14567, 27439, 52129]
obs3 = [393, 824, 1533, 3235, 6768, 13456, 27659, 51350]

m1, b1, r_value1, p_value1, std_err1 = stats.linregress(record_size, obs1)
linha_reg1 = [m1*i + b1 for i in range(max(record_size))]

plt.scatter(record_size, obs1)
plt.plot(linha_reg1, 'r')
plt.xlabel("Record Size")
plt.ylabel("Observation 1")
plt.show()


m2, b2, r_value2, p_value2, std_err2 = stats.linregress(record_size, obs2)
linha_reg2 = [m2*i + b2 for i in range(max(record_size))]

plt.scatter(record_size, obs2)
plt.plot(linha_reg2, 'r')
plt.xlabel("Record Size")
plt.ylabel("Observation 2")
plt.show()


m3, b3, r_value3, p_value3, std_err3 = stats.linregress(record_size, obs3)
linha_reg3 = [m3*i + b3 for i in range(max(record_size))]

plt.scatter(record_size, obs3)
plt.plot(linha_reg3, 'r')
plt.xlabel("Record Size")
plt.ylabel("Observation 3")
plt.show()