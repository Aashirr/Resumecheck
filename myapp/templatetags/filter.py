from django import template
register =template.Library()

@register.filter(name='remove_special')
def remove_chars(val,arg):
    print("Arg",arg)
    print("Value",val)
    for character in arg:
        print(character)
        val=val.replace(character,"")
    return val    