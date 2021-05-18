This program is used to generate the datasets used in this application.

## Steps:

1. Run generate_items.py to get the required list of items. This list is stored in the `items` directory.
2. Run generate_dataset.py to get a JSON dataset out of the item list. This dataset is stored in the `dataset` directory.
3. Run generate_csvdataset.py to get the CSV version of the JSON dataset. This dataset is stored in the `dataset` directory.

### NOTE:
- While opening the CSV dataset in GitHub, you may see a column mismatch error. That error is intentional because that's how the dataset is created.
- Market basket analysis datasets generally do not have the same number of columns for each row.

## License:

This dataset generator is licensed under the terms of the MIT License. 
Each module is licensed under the terms of the MIT License, unless mentioned otherwise.
