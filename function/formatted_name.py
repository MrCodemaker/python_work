def get_formatted_name(first_name, last_name):
    """Возвращает аккурано оформатированное полное имя."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
