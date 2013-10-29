isbn_converter
==============
A simple isbn automatic converter.

Usage
--------------
### Usage as a command line tool.

``` shell
    python isbn_converter.py 7302274754
    python isbn_converter.py 9787540434496
    python isbn_converter.py 7302274754 9787540434496
```

### Usage as a module
``` python
    import isbn_converter as isbn
    print isbn.isbn_converter("7302274754")
    print isbn.isbn_converter("9787540434496")
```

TODO
--------------
* Format converted result use '-'
