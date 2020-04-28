from lxml import etree

def getXmlElement(arg):
    try:
        arg.capitalize
    except AttributeError:
        element = arg
    else:
        element = etree.fromstring(arg)
    
    return element


def prettifyXml(arg):
    element = getXmlElement(arg)
    
    return etree.tostring(element, pretty_print=True, encoding="unicode")


def pprintXml(arg, **kwargs):
    print(prettifyXml(arg), **kwargs)

__all__ = (
    getXmlElement.__name__, 
    prettifyXml.__name__, 
    pprintXml.__name__, 
)
