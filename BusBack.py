class Driver():
    def __init__(self, name):
        self.name = name
        #Усталость
        self.fatigue = 0

class Bus():
    def __init__(self, bus_number, driver):
        self.bus_number = bus_number
        self.driver = driver
        self.route = ['stop_1', 'stop_2', 'stop_3', 'stop_4']
        #Заряд батареи автобуса
        self.charge = 10
        # Минуты пути между остановками stop_1-stop_2 и stop_2-stop_3 и тд.
        self.schedule = [10, 15, 15]
        self.current_bus_stop = 0
        self.next_bus_stop = self.current_bus_stop + 1
        self.can_go = False


    def move_to_next_stop(self):
        print('Автобус номер:', self.bus_number)
        self.current_bus_stop += 1

        print('Название остановки:', self.route[int(self.current_bus_stop)])

        self.charge -= 1
        print('Заряд автобуса:', self.charge)

        if self.current_bus_stop < len(self.route) - 1:  # Проверка достижения конечной остановки:
            self.next_bus_stop += 1
            print('Следующая остановка:', self.route[int(self.next_bus_stop)])
        else:
            print('Дальше остановок нет. Конечная')

    def interval(self):
        time = sum(self.schedule[:self.current_bus_stop])  # Сумма минут до текущей остановки
        print('Время которое прошёл автобус', time)
        if time >= 30:
            self.can_go = True
        print('Пора ли выезжать следующему?', self.can_go)


bus = Bus('10', 1)
bus.move_to_next_stop()
bus.interval()
print('---------------')
bus.move_to_next_stop()
bus.interval()
print('---------------')
bus.move_to_next_stop()
bus.interval()
