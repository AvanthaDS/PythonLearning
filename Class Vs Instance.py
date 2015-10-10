__author__ = 'Avantha'

class Girls:
    gender ='female'

    def __init__(self, name):
        self.name = name

r = Girls('Rachel')
s = Girls('Stanky')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
