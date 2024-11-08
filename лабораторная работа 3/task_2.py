# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    common_participant = list(participants1.intersection(participants2))
    common_participant.sort()
    return common_participant


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common_participants}")

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(f"Общие участники: {common_participants}")
