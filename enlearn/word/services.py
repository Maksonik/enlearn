# Сбор информации слова в правильном формате

def _get_description(word):
    """Собрать descriptions для облегченной работы в html"""
    descriptions = {}
    for desc in word['descriptions']:
        descriptions.setdefault(desc['part_of_speech'], {})
        descriptions[desc['part_of_speech']].setdefault(
            desc['general_meaning'], [])
        descriptions[desc['part_of_speech']][desc['general_meaning']].append(
            (desc['deep_meaning'], desc['translate']))
    return descriptions

def _get_form(word):
    """Собрать forms для облегченной работы в html"""
    forms = {}
    for form in word['forms']:
         forms.setdefault(form['part_of_speech'], [])
         forms[form['part_of_speech']].append([form['condition'], form['value']])
    return forms

def _get_dict_words_with_short_description(words):
    """Получить словарь нужных нам слов с кратким описанием"""
    directory = []
    for word in words:
        directory.append(
            {'name': word.name, 'short_description': word.short_description})
    return directory
