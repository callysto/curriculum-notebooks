# Contributing Guidelines

Create a branch off of master for your task. After completing your notebook(s) and content review, make the recommended changes and open a pull request from your branch to master. 

We consider it a best practice to clear all cell outputs before commiting. This can be done with 'Kernel > Restar & Clear Output' (or 'Edit > Clear All Outputs' in JupyterLab) from the top menu bar. 

## Naming Conventions

Your notebook name should be kebab-case and it should not contain a Jira task identifier. 
If your notebook is in a directory, your directory should have the same name as your notebook but in UpperCamelCase. 
All files should have descriptive names.

## Organization

If you have files accompanying your notebook they should be in a directory along with your notebook.
Images should all be in an `images` folder, with the exception of the [header](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true) and [footer](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true).

## Banners

The markdown to display the banner in the header should be

`![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)`

and in the footer

`[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)`

## General Considerations

Similar to [Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python), your descriptions and code should be readable and easy to explain, and simple is better than complex.

Aim for concise wording and short notebooks, and check that the reading level is appropriate for your audience. Assume that your readers have access to other resources on the topic, or explicitly link to other learning resources.
