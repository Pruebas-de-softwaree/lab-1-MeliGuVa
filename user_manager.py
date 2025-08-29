import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    #Caso de prueba 1
    user_manager = UserManager()
    for i in range(1000):
         user_manager.add_user(i,f"Yo soy el num:{i}")

    #Caso de prueba 2
    # user_manager.add_user(1, "Hola")
    # user_manager.add_user(1, "Adiós")

    #Caso de prueba 3
    #user = user_manager.find_user(1)

    #Caso de prueba 4
    #user_manager.delete_user(1)

    #Caso de prueba 5
    #print(user_manager.get_all_names())

    #Caso de prueba 6
    #average = user_manager.average_user_id()

    #Caso de prueba 7
    # users = user_manager.get_all_names()
    # average = user_manager.average_user_id()
    # user_manager.delete_user(2)

    # print(user_manager.find_user(2))

    #Caso de prueba 8
    #print(user_manager.find_user(350))

    #Caso de prueba 9
    user_manager.add_user(1, "Hola")
    user_manager.add_user(1, "Adiós")

    user_manager.delete_user(1)    

    print("end")