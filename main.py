from clases import Automovil

def run():
    auto1 = Automovil("Honda", "City", 2022, 10000, "Auto")
    print(auto1)
    auto1.avanzar(12)
    auto1.frenar()
    
    
    
    
if __name__ == "__main__":
    run()