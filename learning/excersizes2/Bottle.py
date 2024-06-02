class Bottle():
    def __init__(self,volume, material, brand) -> None:
        self.volume = volume
        self.material = material
        self.brand = brand

    def pack(self,dest):
        print(f"Packed for {dest}")

    def __str__(self) -> str:
        return f" Name : {self.brand}, Volume : {self.volume}, Material : {self.material}"


bottle = Bottle('1.5L','plastic','evian')


print(bottle.__str__)
print(bottle.pack('Delhi'))