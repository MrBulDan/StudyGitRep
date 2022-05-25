def is_alive(health):
    if health < 0:
        return False
    else:
        return True


print(is_alive(5))
print(is_alive(7))
print(is_alive(-2))
print(is_alive(0))
