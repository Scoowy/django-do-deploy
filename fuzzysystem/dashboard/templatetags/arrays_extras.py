from django.template import Library

register = Library()


@register.filter(name='array_index')
def arrayIndex(array, index):
    return array[index]


@register.filter(name='array_index_add_one')
def arrayIndex(array, index):
    return array[index + 1]


@register.filter(name='tuple_index')
def tuple_index(t, index):
    return t[index]


@register.simple_tag(name='tupled_values')
def tupled_values(array_a: list[str], array_b: list[float]):
    new_array_a = []
    new_array_b = []

    for i in range(0, len(array_a), 2):
        new_array_a.append(tuple([array_a[i], array_a[i+1]]))
        new_array_b.append(tuple([str(array_b[i]), str(array_b[i+1])]))

    return zip(new_array_a, new_array_b)
