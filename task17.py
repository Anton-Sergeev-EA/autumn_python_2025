#todo: Заданы множества
# Все пользователи.
all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
# Пользователи не в сети.
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}
# Вычислить пользователей online.

# Вычисляем онлайн-пользователей через разность множеств.
online_users = all_users - offline_users

print("Все пользователи:", all_users)
print("Пользователи не в сети:", offline_users)
print("Пользователи online:", online_users)



