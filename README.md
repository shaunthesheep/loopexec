# ExecChecker

Python module for testing the progress of a *for* loop execution and predition of the completion time.

### Version
0.1

### Installation

ExecChecker requires [Python2.7](https://www.python.org/) to run. Download the source code and run
```sh
$ python setup.py install
```

### Usage

Initialize the checker right before the beginning of the loop and update after an iteration on the loop is completed.
```sh
> collection_size = len(the_list)
> ec = ExecChecker(collection_size)
> for i in the_list:
>   # operations in the loop
>   ec.update()
```
The checker prints a status bar into the standard output. 

### Tests

Run tests from the main directory *loopexec* with

```sh
$ nosetests
```

A sample program using the module can be found under sample/sample.py.