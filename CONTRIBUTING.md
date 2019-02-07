# Contributing Guidelines
Create a branch off of staging for your Jira task.
After your content review as assigned on Jira, make the recommended changes and open a pull request from your branch to staging, for your code review.

## Organization
If you have files accompanying your notebook they should be in a directory along with your notebook.
Images should all be in an `images` folder.

## Naming Conventions
Your notebook name should be kebab-case and it should not contain your Jira task identifier. 
If your notebook is in a directory, your directory should have the same name as your notebook but in UpperCamelCase. 
All files should have descriptive names.

## Reading Input
Our automated testing cannot provide input to a notebook, so any cell that reads from stdin (using `input()` or `sys.stdin()`) will fail.
In most cases you should be able to adapt your notebook to use Jupyter's [string widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#String-widgets) instead.
This is *strongly* encouraged since it allows those cells to be tested.

### Widgets
Here's a basic example of reading from stdin:

```python
user_input = input("Type something: ")

# Do something with user_input...
```

Using widgets, it would become:

```python
w = widgets.Text(
    value='Default value',
    placeholder='Placeholder if empty',
    description='Type something',
    disabled=False
)

def callback(widget):
    # Called after the user enters something in the widget
    # The input will be in widget.value

w.on_submit(callback)

display(w)
```

The big difference now is that the input is asynchronous; the notebook will continue to execute rather than waiting for the user to enter something. This means that any code depending on the user input must go in or be called from the `callback()` function. Accessing `widget.value` outside of the callback will likely just give you the default value.

### Skipping Tests
If you do have to read from stdin, the *very first line* of the cell must be `#NBVAL_SKIP`:

```python
#NBVAL_SKIP

user_input = input("Type something: ")
```

This will cause the cell to be skipped by the automated testing.
One side effect is that any other cell that depends on that input will also fail testing:

```python
# user_input won't be defined since the previous cell was skipped
if user_input == "How are you?":
    print("Fine, thanks!")
```

The two solutions are to either use `#NBVAL_SKIP` like above or provide a default value:

```python
if not "user_input" in locals() and not "user_input" in globals():
    user_input = "How are you?"

if user_input == "How are you?":
    print("Fine, thanks!")
```

The advantage of the latter option is that the cell will still be tested, but if the cell happens to also read from stdin then it must be skipped regardless.
