# %%
import csv
import json
import pandas as pd

# {
#     "classes": [
#         "<labelA>",
#         "<labelB>",
#         ...
#     ],
#     "labels": {
#         "<uuid1>": [<target1>, <target2>, ...],
#         "<uuid2>": [<target1>, <target2>, ...],
#         ...
#     }
# }

# classes = ['healthy', 'multiple_diseases', 'rust', 'scab']
# labels = {'image_id': ['healthy', 'multiple_diseases', 'rust', 'scab']}

def csv_to_json(csv_file_path, json_file_path):
    data = pd.read_csv(csv_file_path)
    
    classes = list(data.columns[1:])
    labels = {row[0]: list(row[1:]) for row in data.itertuples(index=False)}
    
    json_data = {
        "classes": classes,
        "labels": labels
    }
    
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

# Example usage
csv_file_path = 'train.csv'
json_file_path = 'labels.json'
csv_to_json(csv_file_path, json_file_path)
# %%
