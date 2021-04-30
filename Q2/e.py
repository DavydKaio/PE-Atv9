from scipy import stats

record_size = [128, 256, 384, 512, 640, 768, 896, 1024]
obs2 = [375, 850, 1644, 3123, 6839, 14567, 27439, 52129]

m2, b2, r_value2, p_value2, std_err2 = stats.linregress(record_size, obs2)

valor = m2*(2**20)+b2
print('valor: ', valor)