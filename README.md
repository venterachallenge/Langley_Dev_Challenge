# Good Title Goes Here

Your team's client has just acquired a new company and has some oddly specific questions about their recent sales. Your team was given a file, included in this repo as `data.json`, that contains some dummy data from the inventory system of the new company. Your team must develop a script or application that can answer the following:

1. Total revenue (sum of quantity times price of all items)
1. Vendor with the most revenue
1. Quantity of hats sold (items where the key is exactly 'hat')
1. ID of the customer that bought the most ice in October

Your team quickly realized the data structure is not particularly convenient to work with and also carries some personally identifiable information  (PII) unnecessarily. You whiteboarded a transformation that the team liked:
```js
// Old format
{
    "id": 123,
    "vendor": "example",
    "customer": {
        "id": 321,
        "name": "John Doe"
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
To split the work, two stories were written, one to create a function that performs that transformation, and another to take care of answering the client's questions, which would accept the new data format for input.

You are expected to complete one or both of the stories. A version of `data.json` that has been already transformed is provided as `data-transformed.json` so either story can be executed on first.

## Tech details
- You may assume the data files are not too large to read into memory.
- There is no need to develop a user interface, it is acceptable to assume the input will be in the current directory as `data.json`, or `data-transformed.json` if only the second story is completed. If an interface is provided please also provide clear instructions for its use.
- The output for either story can be a file or written to standard out, it must be valid JSON.
