"""Welcome to Nextpy! This file outlines the steps to create a basic app."""
from xtconfig import config

from documentation.templates import template

# from documentation import mdsite
import nextpy as xt


# def index() -> xt.Component:
#     return ()
class MarkdownRenderer():
    path: str
    def render_file(path: str):
        new_path = repr(path)[1:-1]
        f = open(new_path, "r")
        flines = f.readlines()
        f.close()
        for i in range(len(flines)):
            new_string = xt.markdown(flines[i])
            flines[i] = new_string
            
        # print(type(flines[4]))
        return flines
                    


@template(route='/', title="Index")
def database_overview():
    # return mdsite.render_file("docs/introduction.md")
    return xt.box(
        *MarkdownRenderer.render_file('documentation/docs/introduction.md')
    )

# Add state and page to the app.
app = xt.App() 
# app.add_page(index)

