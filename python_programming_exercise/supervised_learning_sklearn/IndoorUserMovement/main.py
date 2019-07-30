#Indoor User movement classification

# load mapping files
from pandas import read_csv
from os import listdir
from numpy import vstack,array
import matplotlib.pyplot as plt
from numpy.linalg import lstsq
from numpy import savetxt  #save the
from numpy import mean,std
#training the models
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

def load_dataset(prefix=''):
    grps_dir,data_dir=prefix+'groups/',prefix+'dataset/'
    targets = read_csv(data_dir+'MovementAAL_target.csv', header=0)
    groups = read_csv(grps_dir+'MovementAAL_DatasetGroup.csv', header=0)
    paths = read_csv(grps_dir+'MovementAAL_Paths.csv', header=0)

    # load sequences and targets into memory
    sequences = list()
    # target_mapping = None
    for name in listdir(data_dir):
        filename = data_dir + '/' + name
        if filename.endswith('_target.csv'):
            continue
        df = read_csv(filename, header=0)
        values = df.values
        sequences.append(values)
        # print(sequences)
    return sequences, targets.values[:,1], groups.values[:,1], paths.values[:,1]


# create a fixed 1d vector for each trace with output variable
def create_dataset(sequences, targets):
	# create the transformed dataset
	transformed = list()
	n_vars = 4
	n_steps = 19
	# process each trace in turn
	for i in range(len(sequences)):
		seq = sequences[i]
		vector = list()
		# last n observations
		for row in range(1, n_steps+1):
			for col in range(n_vars):
				vector.append(seq[-row, col])
		# add output
		vector.append(targets[i])
		# store
		transformed.append(vector)
	# prepare array
	transformed = array(transformed)
	transformed = transformed.astype('float32')
	return transformed

# load dataset
sequences, targets, groups, paths = load_dataset('D:/Python_programs/datasets/IndoorMovement/')
# summarize shape of the loaded data
print(len(sequences), targets.shape, groups.shape, paths.shape)

# summarize class breakdown
class1,class2 = len(targets[targets==-1]), len(targets[targets==1])
print('Class=-1: %d %.3f%%' % (class1, class1/len(targets)*100))
print('Class=+1: %d %.3f%%' % (class2, class2/len(targets)*100))

# histogram for each anchor point
all_rows = vstack(sequences)
plt.figure()
# variables = [0, 1, 2, 3]
# for v in variables:
# 	plt.subplot(len(variables), 1, v+1)
# 	plt.hist(all_rows[:, v], bins=20)
# plt.show()

# # histogram for trace lengths
# trace_lengths = [len(x) for x in sequences]
# plt.hist(trace_lengths, bins=50)
# plt.show()

# group sequences by paths
paths = [1,2,3,4,5,6]
seq_paths = dict()
for path in paths:
	seq_paths[path] = [sequences[j] for j in range(len(paths)) if paths[j]==path]

# # plot one example of a trace for each path with trend 
# plt.figure()
# for i in paths:
# 	plt.subplot(len(paths), 1, i)
# 	# line plot each variable
# 	for j in [0, 1, 2, 3]:
# 		plt.plot(seq_paths[i][0][:, j], label='Anchor ' + str(j+1))
# 	plt.title('Path ' + str(i), y=0, loc='left')
# plt.show()

# fit a linear regression function and return the predicted values for the series
def regress(y):
	# define input as the time step
	X = array([i for i in range(len(y))]).reshape(len(y), 1)
	# fit linear regression via least squares
	b = lstsq(X, y)[0][0]
	# predict trend on time step
	yhat = b * X[:,0]
	return yhat

# # plot series for a single trace with trend
# seq = sequences[0]
# variables = [0, 1, 2, 3]
# plt.figure()
# for i in variables:
# 	plt.subplot(len(variables), 1, i+1)
# 	# plot the series
# 	plt.plot(seq[:,i])
# 	# plot the trend
# 	plt.plot(regress(seq[:,i]))
# plt.show()

# separate traces
# seq1 = [sequences[i] for i in range(len(groups)) if groups[i]==1]
# seq2 = [sequences[i] for i in range(len(groups)) if groups[i]==2]
# seq3 = [sequences[i] for i in range(len(groups)) if groups[i]==3]
# print(len(seq1),len(seq2),len(seq3))

# # separate target
# targets1 = [targets[i] for i in range(len(groups)) if groups[i]==1]
# targets2 = [targets[i] for i in range(len(groups)) if groups[i]==2]
# targets3 = [targets[i] for i in range(len(groups)) if groups[i]==3]
# print(len(targets1),len(targets2),len(targets3))

# # create ES1 dataset
# es1 = create_dataset(seq1+seq2, targets1+targets2)
# print('ES1: %s' % str(es1.shape))
# savetxt('es1.csv', es1, delimiter=',')

# # create ES2 dataset
# es2_train = create_dataset(seq1+seq2, targets1+targets2)
# es2_test = create_dataset(seq3, targets3)
# print('ES2 Train: %s' % str(es2_train.shape))
# print('ES2 Test: %s' % str(es2_test.shape))
# savetxt('es2_train.csv', es2_train, delimiter=',')
# savetxt('es2_test.csv', es2_test, delimiter=',')


# # load dataset
# dataset = read_csv('es1.csv', header=None)
# # split into inputs and outputs
# values = dataset.values
# X, y = values[:, :-1], values[:, -1]

# # create a list of models to evaluate
# #models
# models=[]
# # logistic
# lr=LogisticRegression()
# models.append(('LR',lr))
# # knn
knn=KNeighborsClassifier()
# models.append(('KNN',knn))

# # cart
cart=DecisionTreeClassifier()
# models.append(('CART',cart))
# # svm
# svc=SVC()
# models.append(('SVM',svc))

# # random forest
# rf=RandomForestClassifier()
# models.append(('RF',rf))
# # names.append('RF')
# # gbm
# gbm=GradientBoostingClassifier()
# models.append(('GBM',gbm))
# # names.append('GBM')

# # evaluate models
# all_scores = list()
# for name,model in models:
# 	# create a pipeline for the model
# 	s = StandardScaler()
    # p = Pipeline(steps=[('s',s), ('m',model[model])])
# 	scores = cross_val_score(p, X, y, scoring='accuracy', cv=5, n_jobs=-1)
# 	all_scores.append(scores)
# 	# summarize
# 	m, s = mean(scores)*100, std(scores)*100
# 	print('%s %.3f%% +/-%.3f' % (name, m, s))
# # plot
# plt.boxplot(all_scores, labels=name)
# plt.show()





# Work around for using name main in python multi-processing  
# https://stackoverflow.com/questions/45110287/workaround-for-using-name-main-in-python-multiprocessing

# main_program.py
# import os, pickle, shutil, subprocess, sys, tempfile

# def file_hasher(filenames):
#     try:
#         subprocess_directory = tempfile.mkdtemp()
#         input_arguments_file = os.path.join(subprocess_directory, 'input_arguments.dat')
#         with open(input_arguments_file, 'wb') as func_inputs:
#             pickle.dump(filenames, func_inputs)
#         current_path = os.path.dirname(os.path.realpath(__file__))
#         file_hasher = os.path.join(current_path, 'file_hasher.py')
#         python_interpreter = sys.executable
#         proc = subprocess.call([python_interpreter, file_hasher, subprocess_directory],
#                                timeout=60, 
#                               )
#         output_file = os.path.join(subprocess_directory, 'function_outputs.dat')
#         with open(output_file, 'rb') as func_outputs:
#             hashlist = pickle.load(func_outputs)
#     finally:
#         shutil.rmtree(subprocess_directory)
#     return hashlist



# file_hasher.py
# #! /usr/bin/env python
# import argparse, hashlib, os, pickle
# from multiprocessing import Pool

# def file_hasher(input_file):
#     with open(input_file, 'rb') as f:
#         data = f.read()
#         md5_hash = hashlib.md5(data)
#     hashval = md5_hash.hexdigest()
#     return hashval

# if __name__=='__main__':
#     argument_parser = argparse.ArgumentParser()
#     argument_parser.add_argument('subprocess_directory', type=str)
#     subprocess_directory = argument_parser.parse_args().subprocess_directory

#     arguments_file = os.path.join(subprocess_directory, 'input_arguments.dat')
#     with open(arguments_file, 'rb') as func_inputs:
#         filenames = pickle.load(func_inputs)

#     hashlist = []
#     p = Pool()
#     for r in p.imap(file_hasher, filenames):
#         hashlist.append(r)

#     output_file = os.path.join(subprocess_directory, 'function_outputs.dat')
#     with open(output_file, 'wb') as func_outputs:
#         pickle.dump(hashlist, func_outputs)