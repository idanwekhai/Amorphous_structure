import os
import re
import glob
import pickle
import xgboost as xg

pattern = re.compile(r'\\([^\\]+)_file\.html')
work_dir = os.getcwd()
all_html_dirs = {}
all_htmls = glob.glob(f"{work_dir}\\plotly_files\\*.html")
for file in all_htmls:
    text = pattern.search(file).group(1)
    all_html_dirs[text] = file

print(all_html_dirs)

with open('geo_models_metrics.pickle', 'rb') as fi:
    models = pickle.load(fi)