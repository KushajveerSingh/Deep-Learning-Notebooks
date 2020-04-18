from tracemalloc import start, take_snapshot  

class Resistor:
    def __init__(self, number, manufacturer, resistance):
        self.number = number
        self.manufacturer = manufacturer
        self.resistance = resistance

start()
before = take_snapshot()
r = Resistor('10-232-1412', 'honhai', 10)
after = take_snapshot()

for stat in (stat for stat in after.compare_to(before, 'lineno') if stat.traceback[0].filename == __file__):
    print(stat)