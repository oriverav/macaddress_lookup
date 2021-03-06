# MAC address lookup

Use the https://macaddress.io API to query for MAC address information.

## Installation

```bash
git clone https://github.com/oriverav/macaddress_lookup.git
cd macaddress_lookup
```
## Requirements

requests and tabulate modules are required
```bash
pip install requests
pip install tabulate
```

## Usage

Create an account in https://macaddress.io to get your apiKey.

Substitute the apiKey in file macaddress_lookup.py in section "X-Authentication-Token".

```python
"X-Authentication-Token": ""  # ADD YOUR APIKEY HERE
```

After adding your API KEY, input the mac address to look up as argument.

```bash
python macaddress_lookup.py [mac_address]
```

### For Docker

Docker already running

```bash
docker build -t [image-name] .
docker run [image-name]
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
 