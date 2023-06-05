class Tag:
    def __init__(self, tag_name):
        self.tag_name = tag_name
        self.content = ''
    
    def __enter__(self):
        self.open_tag()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close_tag()
    
    def open_tag(self):
        HTML.code += f'<{self.tag_name}>\n'
    
    def close_tag(self):
        HTML.code += f'</{self.tag_name}>\n'
    
    def add_content(self, content):
        self.content += content


class HTML:
    code = ''
    
    def get_code(*args):
        return HTML.code
    
    def add_tag(tag_name, content=''):
        HTML.code += f'<{tag_name}>{content}</{tag_name}>\n'
    
    def body(*args):
        return Tag('body')
    
    def div(*args):
        return Tag('div')
    
    def p(*kwargs, content):
        HTML.add_tag('p', content)
 
    
html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p(content='Первая строка.')
            html.p(content='Вторая строка.')
        with html.div():
            html.p(content='Третья строка.')

print(html.get_code())