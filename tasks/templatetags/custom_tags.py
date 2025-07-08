from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def task_heading(context):
    request = context['request']
    url_name = request.resolver_match.url_name
    if url_name == 'task_create':
        return "Add Task"
    elif url_name == 'task_edit':
        return "Edit Task"
    return "Task"
