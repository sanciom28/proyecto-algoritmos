class Inventory:
    '''Player's backpack.'''
    def __init__(self):
        self.bag = []

    def add(self,obj):
        '''Add an object to the inventory.'''
        self.bag.append(obj)
        print(f'"{obj}" ha sido agregado a tu inventario.')
        return self.bag

    def remove(self,obj):
        '''Remove an object from the inventory.'''
        self.bag.pop(obj)
        print(f'"{obj}" ha sido utilizado.')
        return self.bag

    def show(self):
        '''Shows inventory's contents.'''
        if not self.bag:
            return 'Tu inventario está vacío.'
        s = 'Inventario:\n'
        for i in self.bag:
            s += (f'- {i}\n')

        return s

    def check(self,lives):
        '''Reviews some stuff.'''
        if 'vida extra' in self.bag:
            lives += 1
            self.bag.remove('vida extra')
        return lives

