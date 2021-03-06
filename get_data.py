import tensorflow_datasets as tfds
import pickle
def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

ds = tfds.load('gigaword',split="train")
d = ds.take(120000)

# path = 'reddit_data/'
# f_train = open(path + "train" + ".csv", "w")
# f_test = open(path + "test" + ".csv", "w")
# f_val = open(path + "val" + ".csv", "w")
# f_train.write("article\tsummary\n")
# f_test.write("article\tsummary\n")
# f_val.write("article\tsummary\n")
train_data = []
test_data = []
val_data = []
for count, text in enumerate(d):
    if count % 1000 == 0:
        print(count)
    article = text['document'].numpy().decode('utf-8')
    # article = str(article)
    # article = article.replace("\n", " ")
    target = text['summary'].numpy().decode('utf-8')
    # target = str(target)
    # target = target.replace("\n", " ")
    if count < 100000:
        train_data.append({"article": article, "summary": target})
        # f_train.write(article + "\t" + target + "\n")
    if 100000 <= count < 110000:
        test_data.append({"article": article, "summary": target})
        # f_test.write(article + "\t" + target + "\n")
    if 11000 <= count < 120000:
        val_data.append({"article": article, "summary": target})
        # f_val.write(article + "\t" + target + "\n")

save_obj(train_data, "gigaword_train")
save_obj(test_data, "gigaword_test")
save_obj(val_data, "gigaword_val")
# f_train.close()
# f_test.close()
# f_val.close()