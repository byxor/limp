# limp

A general purpose programming language, built with the aim to materialise the following ideas:

1. Simplicity - There is very little syntax.
2. Immutability - Existing state cannot be modified.
3. Less Misdirection - Comments cannot be abused, code is self-documenting.
4. Granularity - Functions must remain small.

## Installation

Install globally: `pip install limp`  
Install for user: `pip install limp --user`

## Try it out (REPL)

```python
$ python
>>> import limp
>>> repl = limp.Repl().start()
Welcome to LIMP! You're now in a REPL, have fun.
> 5
5
> (+ 1 2)
3
> (define bits-in-byte 256)
None
> (if (= bits-in-byte (** 2 8)) "You know it.")
You know it.
```
