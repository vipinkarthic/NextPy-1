"""Welcome to Nextpy! This file outlines the steps to create a basic app."""
from xtconfig import config

from documentation.templates import template

from documentation import mdsite
import nextpy as xt
import documentation.mdsite as mdsite


# def index() -> xt.Component:
#     return ()


@template(route='/', title="Index")
def database_overview():
    return xt.box(
        *mdsite.render_file("docs/introduction.md")
    )

# Add state and page to the app.
app = xt.App()
# app.add_page(index)

