# Ventera Developer Challenge - Ben Langley

## Overview
The following files perform two major tasks:
1. Transform the input JSON data to the new format following example below
1. Analyze the data with the following metrics
    - Total revenue (sum of quantity times price of all items)
    - Vendor with the most revenue
    - Quantity of hats sold (items where the key is exactly 'hat')
    - ID of the customer that bought the most ice in October

### Sample JSON Transformation
```js
// Old format
{
    "id": 123,
    "vendor": "example",
    "date": 10/03/2017,
    "customer": {
        "id": 321,
        "name": "John Doe",
        "address": "123 some st"
    },
    "order": {
        "foo": {
            "quantity": 1,
            "price": 1.5
        },
        "bar": {
            "quantity": 4,
            "price": 4
        }
    }
}
// New format
{
    "id": 123,
    "vendor": "example",
    "date": 10/03/2017,
    "customerId": 321,
    "details": [
        {
            "item": "foo",
            "quantity": 1,
            "price": 1.5,
            "revenue": 1.5
        },
        {
            "item": "bar",
            "quantity": 4,
            "price": 4,
            "revenue": 16
        }
    ]
}
```

## Implementation details
There are three files in the directory with unique tasks. From heighest to lowest level of abstraction they are `JSONHelper.py`, `transform.py`, and `analyze.py`. Below is a description of each

### JSONHelper
This file contains wrappers for reading and writing JSON files. Since these methods are used in both steps mentioned above, it was abstracted away to its own file which can be imported into any file in the same directory using the syntax `import JSONHelper`.

### transform
This file contains the heavy lifting for step 1 - transforming the input JSON data from the old format to the new format. Following python convention, methods beginning with `_` should not be accessed outside the file. The only method which should be used is `transform(inputJSONfile="data.json", outputJSONfile="transformed.json")`, which takes in an input JSON file in the old format, converts it into JSON of the new format and both writes the new JSON to the outoutJSONfile and returns the JSON data dictionary (it is the underlying JSON dictionary not JSON itself). To use this method in other files within the same directory use the import command `from transform import transform`. 

### analyze
This file makes use of `transform()` method in `transform.py`, and then computes the desired metrics mentioned in the Overview. The results are output to the terminal window.

### Assumptions
There are a few assumptions for this implementation
1. All dates are provided in the format MM/DD/YYYY
1. The input JSON is in the old format
1. If there is a tie between vendor revenues or customer sales items (such as ice in October), the one who appears first in the list will be returned.

## Usage
Before analyzing the data ensure you have the following directory structure
```
Project Root
|   JSONHelper.py
|   data.json
|   transform.py
|   analyze.py
```
Once this is verified and the `data.json` is verified to be the correct format and the data set you wish to analyze the metrics can be computed by running:
```
$ python3 analyze.py
```
If the input and output JSON files must be changed this can be done by modifying lines 15 and 16 in `analyze.py`
```
######################
## Global Variables ##
######################
inputJSONFile = "data.json"
outputJSONFile = "transformed.json"
```

## Future Improvements
The current implementation can be improved in the following ways
1. If the input/output files are constantly changing then `analyze.py` should be modified to take command line arguments with the defaults set above
1. If we know a single transaction will not contain the same item twice, we can break a few loops early
1. If multiple data transformations will be implemented the `transform.py` file should be modified to have different classes of each transformation. External files can then import the specific module from the file

## Final Output
Using the given `data.json` the final output of `python3 analyze.py` is:
```
Total Revenue:  7536
Vendor with Heighest Revenue:  partyco
Quantity of Hats Sold:  115
Customer who Bought Most Ice (October):  d7aa81e3-2991-474b-87b8-85ce12a7d3ea
```
