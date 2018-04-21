# isbit-python-client
> IsbitClient - Python API Client for ISBIT Exchange

## Installation

```sh
pip install git+https://github.com/ISBITX/isbit-client-python.git
```

## Getting Started

```python
from isbit_client import IsbitClient

client = IsbitClient(
  access_key = "YOUR ACCESS KEY FROM /api_tokens",
  secret_key = "YOUR SECRET KEY FROM /api_tokens",
  # Feel free to test at https://is-pos.com:3443
  endpoint = "https://isbit.co")

print(client.get_public("/api/v2/markets.json"))

print(client.get_public("/api/v2/depth.json", params = {"market": "btcmxn"}))

print(client.get("/api/v2/members/me.json"))


from isbit_client import StreamingIsbitClient

sc = StreamingIsbitClient(
  access_key = "YOUR ACCESS KEY FROM /api_tokens",
  secret_key = "YOUR SECRET KEY FROM /api_tokens")

def on_message(msg):
  print(msg)

sc.run(on_message)
```

## Release History

* 1.0.0
    * It just works

## Meta

Based upon https://github.com/isbitexchange/isbit-client-ruby.git
Copyright ISBIT S. A. de C. V. Some rights reserved.

[https://github.com/ISBITX/](https://github.com/ISBITX/)

## Contributing

1. Fork it (<https://github.com/ISBITX/isbit-client-python/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->

