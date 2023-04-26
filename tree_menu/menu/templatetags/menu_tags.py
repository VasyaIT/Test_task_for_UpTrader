from django import template
from menu.models import Subject

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu) -> dict:
    """The main logic of menu rendering"""
    try:
        subjects = Subject.objects.filter(menu__title=menu)
        values_subjects = subjects.values()
        primary_subject = [i for i in values_subjects.filter(parent=None)]
        # print(primary_subject)
        subject_id = int(context['request'].GET[menu])
        # print(subject_id)
        subject = subjects.get(id=subject_id)
        # print(subject)
        list_subjects_id = get_subject_id_list(subject, primary_subject, subject_id)

        for subject in primary_subject:
            if subject['id'] in list_subjects_id:
                subject['child_subjects'] = get_child_subjects(values_subjects, subject['id'], list_subjects_id)
            result = {'subjects': primary_subject}

    except KeyError:
        result = {
            'subjects': [
                subject for subject in Subject.objects.filter(menu__title=menu, parent=None).values()
            ]
        }

    result['menu'] = menu
    result['others'] = get_url_string(context, menu)
    # print(result)
    return result


def get_subject_id_list(parent, primary_subject, subject_id) -> list:
    """Getting the subject id in the list"""
    list_subjects_id = []

    while parent:
        list_subjects_id.append(parent.id)
        parent = parent.parent
    if not list_subjects_id:
        for subject in primary_subject:
            if subject['id'] == subject_id:
                list_subjects_id.append(subject_id)
    # print(list_subjects_id)
    return list_subjects_id


def get_child_subjects(subjects_values, current_subject_id, list_subjects_id) -> list:
    """Getting child subjects and check if he is in our id list"""
    subject_list = [subject for subject in subjects_values.filter(parent_id=current_subject_id)]
    for subject in subject_list:
        if subject['id'] in list_subjects_id:
            subject['child_subjects'] = get_child_subjects(subjects_values, subject['id'], list_subjects_id)
    # print(subject_list)
    return subject_list


def get_url_string(context, menu) -> str:
    """Getting the URL string"""
    string_args = []
    for i in context['request'].GET:
        if i != menu:
            string_args.append(i + '=' + context['request'].GET[i])
    url_string = ('&').join(string_args)
    # print(url_string)
    return url_string
