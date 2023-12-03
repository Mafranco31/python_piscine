class Account(object):
    
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
    
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):
        if not isinstance(new_account, Account):
            print("Failed: New account is not an instance of Account")
            return False
        for i in self.accounts:
            if i.name == new_account.name:
                print("Failed: Account already exists")
                return False
        self.accounts.append(new_account)
    
    def transfer(self, origin, dest, amount):
        if not isinstance(origin, Account) or not isinstance(dest, Account):
            print("Failed: Origin or destination is not an instance of Account")
            return False
        if origin not in self.accounts or dest not in self.accounts:
            print("Failed: Origin or destination is not in the bank")
            return False
        if amount < 0 or origin.value < amount:
            print("Failed: Amount is negative or origin has not enough money")
            return False
        try:
            amount = int(amount)
        except:
            print("Failed: Amount is not an integer")
            return False
        dir_origin = dir(origin)
        dir_dest = dir(dest)
        x = 0
        val_origin = 0
        while x < len(dir_origin):
            if dir_origin[x][0] == '_':
                dir_origin.pop(x)
                x = 0
            elif dir_origin[x][0] == 'b':
                print("Failed: Origin has an attribute starting with 'b'")
                return False
            elif dir_origin[x][:3] == 'zip' or dir_origin[x][:4] == 'addr':
                val_origin = 1
            x += 1
        if val_origin == 0:
            print("Failed: Origin has no zip or addr attribute")
            return False
        y = 0
        val_dest = 0
        while y < len(dir_dest):
            if dir_dest[y][0] == '_':
                dir_dest.pop(y)
                y = 0
            elif dir_dest[y][0] == 'b':
                print("Failed: Destination has an attribute starting with 'b'")
                return False
            elif dir_dest[y][:3] == 'zip' or dir_dest[y][:4] == 'addr':
                val_dest = 1
            y += 1
        if val_dest == 0:
            print("Failed: Destination has no zip or addr attribute")
            return False
        if len(dir_origin) % 2 == 0 or len(dir_dest) % 2 == 0:
            print(len(dir_origin))
            print("Failed: Origin or destination has an even number of attributes")
            return False
        if not "name" in dir_origin or not "name" in dir_dest:
            print("Failed: Origin or destination has no 'name' attribute")
            return False
        if not "value" in dir_origin or not "value" in dir_dest:
            print("Failed: Origin or destination has no 'value' attribute")
            return False
        if not "id" in dir_origin or not "id" in dir_dest:
            print("Failed: Origin or destination has no 'id' attribute")
            return False
        if isinstance(origin.name, str) == False or isinstance(dest.name, str) == False:
            print("Failed: Origin or destination name is not a string")
            return False
        if isinstance(origin.id, int) == False or isinstance(dest.id, int) == False:
            print("Failed: Origin or destination id is not an integer")
            return False
        if isinstance(origin.value, float) == False and isinstance(origin.value, int) == False:
            print("Failed: Origin value is not a float or an integer")
            return False
        if isinstance(dest.value, float) == False and isinstance(dest.value, int) == False:
            print("Failed: Destination value is not a float or an integer")
            return False
        origin.value -= amount
        dest.value += amount
        print("Success: Transfer done")

    def fix_account(self, name):
        print("Fixing account of", name, "...")
        if not isinstance(name, str):
            return False
        for i in self.accounts:
            if i.name == name:
                try:
                    i.id = int(i.id)
                    try:
                        i.value = int(i.value)
                    except:
                        i.value = float(i.value)
                except:
                    return False
                x = 0
                val_origin = 0
                dir_origin = dir(i)
                while x < len(dir_origin):
                    if dir_origin[x][0] == '_':
                        dir_origin.pop(x)
                        x = 0
                    elif dir_origin[x][0] == 'b':
                        del name.dir(i)[x]
                    elif dir_origin[x][:3] == 'zip' or dir_origin[x][:4] == 'addr':
                        val_origin = 1
                    x += 1
                if val_origin == 0:
                    setattr(i, "zip", "")
                    dir_origin.append("zip")
                if len(dir_origin) % 2 == 0:
                    setattr(i, "addr", "")
                return True
        return False

bank = Bank()
a = Account("mathis", value=100)
b = Account("victoria", value=100)
bank.add(a)
bank.add(b)
if bank.transfer(a, b, 50) == False:
    bank.fix_account("mathis")
    bank.fix_account("victoria")
    bank.transfer(a, b, 50)
print(a.value, b.value)
#instance = Account("mathis", value=100)
#attributes_of_instance = dir(instance)
#print(attributes_of_instance)