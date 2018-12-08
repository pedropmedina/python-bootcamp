# From Fluent Python
def tag(name, *content, cls=None, **attrs):
    '''Generate HTML tags'''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attrs_str = ''.join(
            [f'{attr}="{value}"' for attr, value in sorted(attrs.items())]
        )
    else:
        attrs_str = ''
    if content:
        return '\n'.join([f'<{name} {attrs_str}>{c}<{name}/>' for c in content])
    else:
        return f'<{name} {attrs_str} />'


# print(tag('h1', 'This is a title', cls='title', id='title-id'))

# A way to ensure that all arguments are passed as intended is by using
# the inspect library
import inspect


def foo(name, age=0, *args, **kwargs):
    pass


signature = inspect.signature(foo)
bound_args = signature.bind('jane', 20, 'single', gender='female')
print(bound_args.arguments)
print(bound_args.args)
print(bound_args.kwargs)
# OrderedDict([('name', 'jane'), ('age', 20), ('args', ('single',)), ('kwargs', {'gender': 'female'})])
#  ('jane', 20, 'single')
# {'gender': 'female'}
