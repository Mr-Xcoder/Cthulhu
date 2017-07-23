*Note: The README.md page is written before the release of the language, hence many things will probably change / won't be implemented.*

# Cthulhu
*Cthulhu* is (will be) a recreational programming language designed for code golf and number-manipulation.

#### Some Things to keep in mind

- Cthulhu will heavily rely on the *arities* (see below) of its functions, and there won't be any functions of unbounded arity (an exception to the rule is printing with `§`), because that wouldn't be beneficial for golfing. 

- Cthulhu uses *prefix notation*. That might seem strange at first, but it has a lot of benefits. For example, many programming languages use infix notation, like so: `2 + 2`. The Cthulhu equivalent of that expression is `+2 2`, with the operator before the two elements it's operating on.

- Because it is designed for number manipulation, Cthulhu has a lot of numerical constants. That is very helpful, especially when performing arithmetic-related tasks. It also has the advantage of removing some whitespace, between the numeric literals. See the sections below for more details.

- Cthulhu does *not* have implicit printing. That means you must explicitly tell the interpreter that you want to output something. You can use `«` for printing everything until the end of the whole program, or you can use the alternative `§` to print everything up until the first occurence of the character `‹`. If `‹` is missing when you have an occurence of `§`, the program will most likely throw an error, because `‹` is not implicitly added at the end.
