
# Trade API
Live Link : https://hostingapi.onrender.com/docs

This project provides an API for retrieving and searching trades. The API is built using Python and FastAPI.

## Installation

1. Clone the project repository from Github:

```python
git clone git@github.com:lakshya7878/Lakshya-Sharma_Backend.git
```


2. Install the required Python packages using pip:

```python
pip install -r requirements.txt
```

3. Start the API server:

```python
uvicorn main:app --reload
```



## Usage

The Trade API provides the following endpoints:

### Pagination 

Implemented pagination of list of data while displaying Trades.

```python
GET /trades?page=1&size=50
```

### Sorting

Implemented sorting of list of data by price
```python
GET /sortby/price
```

### List trades

```python
GET /trades
```

Returns a list of all trades.

### Single trade

```python
GET /trades/{id}
```

Returns a single trade by ID.

### Searching trades

```python
GET /trades?search={query}
```

Returns a list of trades that match the search query. The search query can be any text that exists in the fields listed in the overview above.

### Advanced filtering

```python
GET /trades?assetClass={asset_class}&end={end}&maxPrice={max_price}&minPrice={min_price}&start={start}&tradeType={trade_type}
```

Returns a list of trades that match the specified filters. The filters are optional, and can be combined to narrow down the search results.

## API documentation

The API documentation can be accessed at https://hostingapi.onrender.com/docs or http://localhost:8000/docs or http://localhost:8000/redoc after starting the server.

## Contributing

Contributions to this project are welcome. Please create a pull request with your changes and ensure that all tests pass before submitting.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.




