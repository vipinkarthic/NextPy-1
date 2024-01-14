import nextpy as xt
# from nextpy import MarkdownRenderer
from nextpy import markdown
# from nextpy.magic import write

# from .templates.docpage import (
#     code_block_markdown,
#     text_comp,
#     h1_comp,
#     h2_comp,
#     h3_comp,
#     code_comp,
#     doclink2,
# )

# component_map = {
#     "h1": lambda text: h1_comp(text=text),
#     "h2": lambda text: h2_comp(text=text),
#     "h3": lambda text: h3_comp(text=text),
#     "p": lambda text: text_comp(text=text),
#     "a": doclink2,
#     "code": lambda text: code_comp(text=text),
#     "codeblock": code_block_markdown,
# }
class MarkdownRenderer():
    path: str
    def render_file(path: str):
        new_path = "documentation/"+repr(path)[1:-1]
        f = open(new_path, "r")
        flines = f.readlines()
        f.close()
        for i in range(len(flines)):
            new_string = xt.markdown(flines[i])
            flines[i] = new_string
            
        # print(type(flines[4]))
        return flines

# xd = write.MarkdownRenderer()

# Monkeypatch markdown custom components.
# md = xt.markdown("", component_map=component_map)
md = xt.markdown("")
custom = md.get_custom_components()

def get_custom_components(self, seen):
    return custom

xt.Markdown.get_custom_components = get_custom_components

@xt.memo
def markdown_memo(content: str) -> xt.Component:
    # return xt.markdown(content, component_map=component_map)
    return xt.markdown(content)

def render_file(path):
    return MarkdownRenderer.render_file(path)