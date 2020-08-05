class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def display(self):
        print(self)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict/dtd', '')
        self.end_tag = ''  # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self):
        super().__init__('head', "")
        self._head_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._head_contents.append(new_tag)

    def display(self):
        for tag in self._head_contents:
            self.contents += str(tag)
        super().display()


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')  # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display()


# all classes before this have used inheritance, this class uses polymorphism since it calls other classes but isn't
# inheriting the properties and methods from those classes
# This is an example of 'composition', the class is 'composed' of other classes
class HtmlDoc(object):

    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_body_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def add_head_tag(self, name, contents):
        self._head.add_tag(name, contents)

    def display(self):
        self._doc_type.display()
        print('<html>')
        self._head.display()
        self._body.display()
        print('</html>')


if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_body_tag('h1', 'Mina heading')
    my_page.add_body_tag('h2', 'sub-heading')
    my_page.add_body_tag('p', 'This is a paragraph that will appear on the page')
    my_page.add_head_tag('title', 'Document title')
    with open('test_doc.html' , 'w') as test_doc:
        my_page.display()

# the following code is an example of aggregation

new_body = Body()
new_body.add_tag('h1', 'Aggregation')
new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                      "of objects to build up another object.")
new_body.add_tag('p', "The composes object doesn't actually own the objects that it's composed of"
                      " - if it's destroyed, those objects continue to exist")

# give our document new content by switching it's body
my_page._body = new_body
# 'my_page' could be deleted but 'new_body' could still be used in another instance since it can stand alone
with open('test2.html', 'w') as

"""Below is a recreation of the 'HtmlDoc' init constructor but build with aggregation, not composition"""

# class HtmlDoc(object):
#     def __init__(self, doc_type, head, body):
#         self._doc_type = doc_type
#         self._head = head
#         self._body = body

"""Now you would create the doc_type, head, and body first and then pass them as parameters when creating an
instance of the class, see below"""

# new_docType = DocType()
# new_header = Head('Aggregation document')
# my_page = HtmlDoc(new_docType, new_header, new_body)
