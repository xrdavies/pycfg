## pycfg

pycfg is a simple tool to manage configuration files compatiable with TOML.

### Why I waste time on this simple tool?
Because when I tried to get involved in a new project that needs lots of configurations, while YAML is too complex and TOML (the python library) is wasting time to get your value by search json. pycfg is based on toml, and wrap a simple interface to get the value with just . . . . ,

Just simple as `cfg.get('production.server.host.ip')`

### Install
```
python setup.py install
```

### Example

Create a test TOML file named test.toml.

```
[user]
    name = "Tom"
    email = "tom@example.com"

[products]
    [products.server1]
        host = 'server1'
        ip = '10.0.0.1'
        dc = 'dc10'

    [products.server2]
        host = 'server2'
        ip = '10.0.0.2'
        dc = 'dc20'
```

Sample code

```
import pycfg

conf = pycfg.load_config("./test.toml")
print(conf) # print out the configuration file.
conf.get('user.name') # get the user name.
conf.get('products') # get the products group.
```


