import unidecode

path = ""

with open(path + "whoscored_data.txt", "r", encoding="utf-8") as f:
    data_list = f.readlines()

data_list = ",".join(data_list).replace("\n", "").replace("\t", ",").split(",")
data_list = list(filter(lambda x: x != "", data_list))

# print(data_list)

with open(path + "clean_data.txt", "w") as wf:
    for i in range(0, len(data_list), 15):
        # print(data_list[i:i+15])
        data = unidecode.unidecode(",".join(data_list[i : i + 15]))
        # print(data)
        wf.write(data + "\n")

