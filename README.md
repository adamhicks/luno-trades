This tool will export Luno trades to a csv using the API.

Requirements:
- Python 3.7
- pipenv
- Luno API key and secret (https://www.luno.com/wallet/security/api_keys)

Usage:

The Pipfile can be used to initialise an environment, fetching the Luno Python SDK.
```
pipenv shell
```

Then run the script with:
```
python export.py --pair XBTEUR --key [api key here] --secret [api secret here]
```

Which will output the trades to a csv file called "trades.csv"