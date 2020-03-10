### Description
Test task: Currency converter  
Could convert any currency to RUB and vice versa.

### Installation

Install from Github

    pip install git+https://github.com/delatars/converter
    
Usage:
```bash
$ currency_converter -h
usage: Currency converter web server [-h] [-b BIND] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  -b BIND, --bind BIND  The socket to bind. (default: 127.0.0.1:8000)
  --debug               Debug mode
```

### Docker

Build:

    docker build . -t currency_converter
    
    
Run:

    docker run --rm -d -p 8000:8000 currency_converter


### Api
- **GET** `{{url}}/currencies[?currency={eur}&currency={usd}]` - get all available currencies.  
  - parameter(optional): **currency** - set currency name to get.
 
- **GET** `{{url}}/currencies/convert?currency={eur}&count={100}&convert_to={rub}` - convert currency
  - parameter: **currency** - set convertible currency name.
  - parameter: **count** - set convertible currency count.
  - parameter: **convert_to** - set name of the currency to be converted.

   
