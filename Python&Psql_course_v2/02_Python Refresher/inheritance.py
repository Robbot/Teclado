class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})" # the !r after {self.name} calls __repr__ method

    def disconnected(self):
        self.connected = False
        print("Disconnected")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super(Printer, self).__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Device("Printer", "USB")
print(printer)
printer.disconnected()

# again the same but after adding inheriting class Printer
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnected()