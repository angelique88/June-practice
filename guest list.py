guest = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}


def greeting(name):
    if name in guest:
        return "Hi! I'm {}, and I'm from {}.".format(name, guest[name])
    else:
        return "Hi! I'm a guest."


print(greeting("Rand"))
print(greeting("Randy"))

