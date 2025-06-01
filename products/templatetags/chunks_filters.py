from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(lst, n):
    chunk = []
    result = []
    for data in lst:
        chunk.append(data)
        if len(chunk) == n:
            result.append(chunk)
            chunk = []
    if chunk:
        result.append(chunk)  # Add the last chunk if it has less than n items
    return result

