# cdp-py

The Ciholas Data Protocol (CDP) provides a method of communication between devices and services. CDP data is transmitted over Ethernet as User Datagram Protocol (UDP) packets. _cdp-py_ contains a set of structural definitions of the CDP data items that make up these UDP packets.

To get started with CDP, see the official [documentation](http://cuwb.io/docs/v3.3/software-integration/cdp-output-definition/). For more information regarding the individual data items, visit the [data items documentation](https://github.com/ciholas/cdp-py/blob/master/DATA_ITEMS.md).

## Getting Started

### Prerequisites

You need Python 3 or higher to use _cdp-py_. Make sure you have Python installed and that the expected version is available from your command line. You can check this by running:

```
$ python --version
```

### Installing

_cdp-py_ can be installed using pip. To install the latest version use:

```
$ pip install cdp-py
```

Now that _cdp-py_ package is installed, you can start using the _cdp_ module by adding the following import statement to your Python script:

```python
import cdp
```
For a tutorial about how to use the _cdp_ module, visit: [Using CDP - Python](http://cuwb.io/docs/v3.3/application-notes/using-cdp-python/#using-cdp-python).

### Upgrading

To upgrade to the latest version use:

```
$ pip install --upgrade cdp-py
```

## License

This work is licensed under the [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) License.
