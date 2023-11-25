#Differences between method extend and append
casa = [('corredor', 11.25), ('cozinha', 18), ('sala', 10.75), ('quarto', 9.5), ('banheiro', 9.5)]
casa_extend = casa.copy()
casa_extend.extend(["poolhouse", 24.5])
casa_append = casa.copy()
casa_append.append(["poolhouse", 24.5])
print(f"List using extend method: {casa_extend}")
print(f"List using append method: {casa_append}")