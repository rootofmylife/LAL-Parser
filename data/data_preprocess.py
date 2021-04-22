import os

print("======================")
print("Start processing data...")

full_dataset = 10394
print("Total dataset: " + str(full_dataset))

train_dataset = int(full_dataset * 0.7) + 2
dev_dataset = int(full_dataset * 0.2)
test_dataset = int(full_dataset * 0.1)

print("Train dataset: " + str(train_dataset))
print("Dev dataset: " + str(dev_dataset))
print("Test dataset: " + str(test_dataset))

print("Sum of train + dev + test dataset: " + str(train_dataset + dev_dataset + test_dataset))
print("======================")

print("Remove old files if needed...")
# Check if file exists to delete
if os.path.isfile('./cp_train_vn.txt'):
    os.remove('./cp_train_vn.txt')

if os.path.isfile('./cp_dev_vn.txt'):
    os.remove('./cp_dev_vn.txt')

if os.path.isfile('./cp_test_vn.txt'):
    os.remove('./cp_test_vn.txt')

if os.path.isfile('./dp_train_vn.txt'):
    os.remove('./dp_train_vn.txt')

if os.path.isfile('./dp_dev_vn.txt'):
    os.remove('./dp_dev_vn.txt')

if os.path.isfile('./dp_test_vn.txt'):
    os.remove('./dp_test_vn.txt')

print("Done removing files")

print("======================")
print("Split data of constituency...")
# Read constituency data, each line is a sentence
with open('./cp_train_vn.txt', 'w') as fcptrain, \
    open('./cp_dev_vn.txt', 'w') as fcpdev, \
        open('./cp_test_vn.txt', 'w') as fcptest:
    with open('./cp_vn.txt') as fcpin:
        for cp_id, cp_line in enumerate(fcpin):
            if cp_id < train_dataset:
                fcptrain.write(cp_line)
            elif cp_id >= train_dataset and cp_id < train_dataset + dev_dataset:
                fcpdev.write(cp_line)
            elif cp_id >= train_dataset + dev_dataset:
                fcptest.write(cp_line)
print("Done splitting data of constituency.")

print("~~~~~~~~~")

print("Split data of dependency...")
# Read dependency data, each line is a word of sentence, sentence is seperated by empty line
count_empty = 0 # count emty line, which represents number of sentence.
with open('./dp_train_vn.txt', 'w') as fdptrain, \
    open('./dp_dev_vn.txt', 'w') as fdpdev, \
        open('./dp_test_vn.txt', 'w') as fdptest:
    with open('./dp_vn.txt') as fdpin:
        for dp_line in fdpin:
            if count_empty < train_dataset:
                fdptrain.write(dp_line)
            elif count_empty >= train_dataset and count_empty < train_dataset + dev_dataset:
                fdpdev.write(dp_line)
            elif count_empty >= train_dataset + dev_dataset:
                fdptest.write(dp_line)

            if len(dp_line.strip()) == 0:
                count_empty += 1
print("Done splitting data of dependency.")

print("======================")
# Statistical for constituency data (updating...)

# Statistical for dependency data (updating...)