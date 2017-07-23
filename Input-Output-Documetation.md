# Input and Output Documentation

### Taking Input
  
The reasons for taking user input may vary, and Cthulhu offers support for each of the situations, providing 3 useful ways of taking input:
 
- You can take input using the function `»`. This allows you to take any kind of Data type as input, as shown in the table below (see *[Types and Formats](https://github.com/Mr-Xcoder/Cthulhu/blob/Readme.md-edits/Input-Output-Documetation.md#types-and-formats)*).

- If you want to take input as a String and not worry about quote formatting, you can hapily use `‘`, which is similar to Python 2's `raw_input()` function. That automatically converts your input to a String, no matter its original data type. For instance, `123` gets converted to `"123"` and `abcd` becomes `"abcd"`.

- If you are looking to take input as an number (floating point or integer), you should use the function `µ`, which stands for float input. If the interpreter is not able to convert the given input to a number, it will throw an error and the program will terminate.

### Providing Output

Take note that outputting isn't implicit in Cthulhu, hence you must explicitly "announce" the interpreter whenever you want to print something. There are two ways of providing output:

- `«` - Outputs the result given by the piece of code from its occurrence all the way to the end of the program. 

- `›` - Outputs the result given by the piece of code from its occurrence up until the first `‹` symbol. Take note that if no occurernce of `‹` is detected after a `›`, the interpreter will most likely throw an error. This is the only function in Cthulhu that has unbounded arity.

### Types and Formats

Data Type |  Format  |  Example
 ---------|----------|-----------
Integers|`<integer>`|`100`
Floating point Number|`<integer part>.<decimal part>`|`100.0`
Strings|`"<string>"`|`"100"`
Boolean Values|`<True/False>`|`True`
Lists of Integers|`[<integer>,...,<integer>]`|`[100, 99, 98]`
Lists of Floats|`[<float>,...,<float>]`|`[100.0, 99.5, 98.4]`
Lists of Strings|`["<string>",...,"<string>"]`|`["100", "99", "98"]`
Lists of Booleans|`[<True/False>,...,<True/False>]`|`[False, False, True]`
