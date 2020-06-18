"""
Basic example of a Mkdocs-macros module
"""

import math
import os
# import html

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

    # add to the dictionary of variables available to markdown pages:
    env.variables['baz'] = "John Doe"

    # NOTE: you may also treat env.variables as a namespace,
    #       with the dot notation:
    env.variables.baz = "John Doe"

    @env.macro
    def bar(x):
        return (2.3 * x) + 7

    # If you wish, you can  declare a macro with a different name:
    def f(x):
        return x * x
    env.macro(f, 'barbaz')

    # or to export some predefined function
    env.macro(math.floor) # will be exported as 'floor'

    @env.macro
    def code_from_file(fn: str, start: int = None, stop: int = None, flavor: str = "", download=True):
        """
        Load code from a file and save as a preformatted code block.
        Start and stop can also be used to indicate the starting line and the stopping line
        you wish to extract from the file. 
        If a flavor is specified, it's passed in as a hint for syntax highlighters.

        Example usage in markdown:

            {{ code_from_file("code/myfile.py", flavor = "python") }}
            {{ code_from_file("code/myfile.py", 2, 5) }}
            {{ code_from_file("code/myfile.py", stop = 5) }}
            {{ code_from_file("code/myfile.py", 2, 5, "python") }}
        """
        docs_dir = env.variables.get("docs_dir", "docs")
        fn = os.path.abspath(os.path.join(docs_dir, fn))
        if not os.path.exists(fn):
            return f"""<b>File not found: {fn}</b>"""
        with open(fn, "r") as f:
            output=""
            # return (
            #     f"""<div class="codehilight"><pre><code class="{flavor}">{html.escape(f.read())}</code></pre></div>"""
            # )
            temp = []
            x = f.readlines()
            
            # a fix to change python slicing to code line numbers, includes the final integer now.
            if start is not None and start > 0:
                start = start -1 
            if stop is not None:
                stop = stop + 1
            
            for line in x:
                temp.append(line)

            output+=f"""```python \n{''.join(temp[start:stop])} \n```"""
            return output

    @env.macro
    def external_markdown(fn: str):
        """
        Load markdown from files external to the mkdocs root path.
        Example usage in markdown:

            {{external_markdown("../../README.md")}}

        """
        docs_dir = env.variables.get("docs_dir", "docs")
        fn = os.path.abspath(os.path.join(docs_dir, fn))
        if not os.path.exists(fn):
            return f"""<b>File not found: {fn}</b>"""
        with open(fn, "r") as f:
            return f.read()
    
    
    # create a jinja2 filter
    @env.filter
    def reverse(x):
        "Reverse a string (and uppercase)"
        return x.upper()[::-1]
    
    
