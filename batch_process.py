import os

file_path = '/Users/huangqiming/Desktop/Python/jetson-nano-fire-detection/fire/train/ann/'
file_name = []


for i in os.listdir(file_path):
    if i.endswith('.xml'):
        file_name.append(i)

for i in range(len(file_name)):
    out = ''

    with open(file_path + file_name[i], 'r') as fr:
        content = fr.readlines()
        content[3] = content[3][:7] + content[3][67:]
        for j in range(len(content)):
            out += content[j]

    with open(file_path + file_name[i], 'w') as fr:
        fr.write(out)

print("Batch Processing Successfully")
