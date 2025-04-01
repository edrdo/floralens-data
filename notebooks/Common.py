import os
import pandas as pd

def top1(data, ground_truth_col='species'):
    r = pd.DataFrame()
    r['top1'] = (data[ground_truth_col] == data['rank1']).astype(float) 
    return r['top1'].mean()

def top5(data, ground_truth_col='species'):
    r = pd.DataFrame()
    r['top5'] = (data[ground_truth_col] == data['rank1']).astype(float) + \
                    (data[ground_truth_col] == data['rank2']).astype(float)  + \
                        (data[ground_truth_col] == data['rank3']).astype(float)  + \
                        (data[ground_truth_col] == data['rank4']).astype(float)  + \
                            (data[ground_truth_col] == data['rank5']).astype(float) 
    return r['top5'].mean()

def mrr(data, ground_truth_col='species'):
    r = pd.DataFrame()
    r['mrr'] = (data[ground_truth_col] == data['rank1']).astype(float) + \
            (data[ground_truth_col] == data['rank2']).astype(float) / 2 + \
                (data[ground_truth_col] == data['rank3']).astype(float) / 3 + \
                    (data[ground_truth_col] == data['rank4']).astype(float) / 4 + \
                        (data[ground_truth_col] == data['rank5']).astype(float) / 5 
    return r['mrr'].mean()


def read_lines_in_file(filename):
  with open(filename) as inp:
    return [ line.strip() for line in inp.readlines() ]

def read_floralens_model_labels():
  return read_lines_in_file('model-files/dict.txt')

def unzip_archive(archive):
  os.system('unzip -qo ' + archive)

def cleanup_dir(directory):
  for filename in os.listdir(directory): 
    if filename != '.gitignore':
      os.remove(directory + '/' + filename)
