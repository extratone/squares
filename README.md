![squares](https://github.com/user-attachments/assets/703c25c9-37fe-4c96-bf6b-e0624c2fb819)

# `squares`

`squares` is a Python-based command-line application that finds the two closest square numbers to a given input number.

## Installation

To install `squares`, use `pip`:

```bash
pip install squares-cli
```

This will install the `squares` command, allowing you to find the closest square numbers directly from the command line.

## Usage

The `squares` command can find the two closest square numbers (one above and one below) to a given input number. You can use it in various ways, specifying options to control the output.

### Basic Command

```bash
squares [OPTIONS] <number>
```

If no options are specified, `squares` will output both the closest square number below and the closest square number above the given input, separated by a comma.

### Options

- `--below` - Outputs only the closest square below the input number.
- `--above` - Outputs only the closest square above the input number.
- `--both`  - Outputs both the closest squares (this is the default behavior if no option is specified).
- `-h` or `--help` - Displays the help message.

### Examples

Here are some example commands and their expected outputs:

#### Default (Both Closest Squares)

```bash
squares 12
```

**Output:**
```
9, 16
```

In this example, `squares 12` finds the closest squares around 12, returning both the closest square below (9) and the closest square above (16).

#### Closest Square Below

```bash
squares --below 12
```

**Output:**
```
9
```

This example uses `--below` to return only the closest square below 12, which is 9.

#### Closest Square Above

```bash
squares --above 12
```

**Output:**
```
16
```

Here, `--above` is used to return only the closest square above 12, which is 16.

#### Explicitly Returning Both (Same as Default)

```bash
squares --both 12
```

**Output:**
```
9, 16
```

Using `--both` explicitly returns both closest squares around 12. This produces the same result as the default behavior.

### Man Page

A man page is also included in the installation. You can access it by typing:

```bash
man squares
```

This will display comprehensive information about the command, options, and examples, similar to what is provided in this README.

## Additional Notes

- **Operating System Compatibility**: `squares` is compatible with UNIX-like systems (Linux and macOS) and Windows, though the man page installation may vary depending on the OS.
- **Python Version**: This package requires Python 3.6 or higher.[

## License

This project is licensed under the MIT License.

---

This `README.md` provides a clear description of what the package does, how to install and use it, and includes examples and notes for further clarification. Let me know if there’s anything else you’d like added or modified!]
