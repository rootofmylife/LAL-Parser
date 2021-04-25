# Add TOP to sentence in constituency parsing

with open('cp_dev_vn.clean', 'w') as fdevout: 
    with open('cp_dev_vn.txt') as fdev:
        for line in fdev:
            fdevout.write("(TOP " + line.strip() + ")")
            fdevout.write('\n')

with open('cp_train_vn.clean', 'w') as ftrainout: 
    with open('cp_train_vn.txt') as ftrain:
        for line in ftrain:
            ftrainout.write("(TOP " + line.strip() + ")")
            ftrainout.write('\n')

with open('cp_test_vn.clean', 'w') as ftestout: 
    with open('cp_test_vn.txt') as ftest:
        for line in ftest:
            ftestout.write("(TOP " + line.strip() + ")")
            ftestout.write('\n')