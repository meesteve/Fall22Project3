updates = []

def update_all():
    for u in updates:
        u.update()

def register(thing):
    updates.append(thing)

def deregister(thing):
    updates.remove(thing)