no_contact_or_file = 'Телефонная книга пуста или не открыта'

load_successful = 'Телефонная книга успешно загружена'

new_contact_successful = 'Новый контакт успешно добавлен'

save_successful = 'Телефонная книга успешно сохранена'

new_name = 'Введите имя контакта: '
new_phone = 'Введите телефон контакта: '
new_comment = 'Введите комментарий к контакту: '

is_changed = 'Были внесены изменения. Сохранить?'
bye_bye = 'До свидания! Всего хорошего!'

input_keyword = 'Введите элемент, который нужно найти: '

def not_found(word: str) -> str:
    return f'Контакты, содержащие "{word}", не найдены!'

enter_or_empty = 'Введите новые значения или оставьте пустым для сохранения оригинального значения'

def successful_edited(name: str) -> str:
    return f'Контакт {name} успешно изменен!'

input_index = 'Введите номер изменяемого контакта: '

input_delete_index = 'Введите индекс контакта, который хотите удалить: '

def confirm_delete(name: str) -> str:
    return f'Вы точно хотите удалить контакт {name}?'

def delete_contact(name: str) -> str:
    return f'Контакт {name} успешно удален!'
