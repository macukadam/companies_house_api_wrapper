# COMPANIES HOUSE API Client

This is a Python client for the COMPANIES HOUSE API

## Installation

You can install the package into your project via pip:

```sh
pip install companies_house_api_client
```

# USAGE

To use the COMPANIES HOUSE API client, you first need to set up environment variables for the required credentials:

```sh
export COMPANIES_HOUSE_APIKEY=your-api-key
export COMPANIES_HOUSE_HOST=https://api.company-information.service.gov.uk
```

# EXAMPLE

By setting the test parameter to true, you can play arround with api:

```python
from companies_house_api_client import CompaniesHouse

# Create a Companies House API client instance
ch = CompaniesHouse()

# Call an API method
companies = ch.get_company_profile("12312312")

```

# TESTS

Make sure pytest is installed on your environment

```sh
python3 -m pytest
```
