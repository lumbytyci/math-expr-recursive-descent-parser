[![Build Status](https://travis-ci.org/lumbytyci/math-expr-recursive-descent-parser.svg?branch=master)](https://travis-ci.org/lumbytyci/math-expr-recursive-descent-parser)

# Recursive Descent Parser 
A simple and lightweight [recursive descent parser](https://en.wikipedia.org/wiki/Recursive_descent_parser) for parsing mathematical expressions.

Currently only parsing is supported, no error handling is provided.

Supported operations are negation, exponentiation, addition, multiplication and grouping.<br />
The recuirsive descent parser works with the following grammar:<br />
```
Expression = Addition
Addition = Multiplication | Addition "+" Multiplication | Addition "-" Multiplication
Multiplication = Exponentiation | Multiplication "*" Exponentiation | Multiplication "/" Exponentiation
Exponentiation = Primary | Exponentiation "^" Primary
Primary = Immediate | "(" Expression ")"
```

Currently the parser runs in a simple [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop):
```    
>>> 2+2+2-6
0.0
>>> 2*4/8
1.0
>>> 2^10
1024.0
>>> (2+2)*2
8.0
>>> 2^2^2
16.0
>>> 2^((3+2)*2)/(2*512)
1.0
```
## Getting started
1. Install virtual-env (skip if already installed)
2. Clone the repository
3. Setup the virtualenv and activate
4. Install the required dependencies
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```



## Contributing
Feel free to help with additional functionality by opening a PR. Follow the styling guidelines. All tests must pass.
Features needed:
* Error handling (Matching brackets, illegal expressions etc.)
* Division order of operation
