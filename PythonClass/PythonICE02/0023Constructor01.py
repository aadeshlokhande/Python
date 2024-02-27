# Constructor - easy way

class student:
    def __init__(self,name):
        self.name = name 
        print(f"Hello {self.name}")
    
    def __del__(self):
        print(f"bye bye {self.name}")


print("Creating instance")
pragati = student("Pragati")
print("Code end")