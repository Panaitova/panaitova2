# TODO Напишите функцию для поиска индекса товара
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def find_item_index(items, item_list):
    try:
        return item_list.index(items)
    except ValueError:
        return None


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(find_item, items_list)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
