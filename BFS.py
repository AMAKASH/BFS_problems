# ID: 19101533
# Name: Abid Mahmood Akash
# Section: 06

# Two Classes has been defined for solving two tasks and the runner codes are written at the end of both classes
# For Task 2 I appended a new line end the end of file to read it from file easily else it shows error as in the last
# line only n-1 inputs are found


class InfectedTracer:
    movements = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    def __init__(self, path):
        self.regions = []
        self.queue = []
        self.counter = 0
        file = open(path, 'r')
        data = file.readlines()
        file.close()
        for i, d in enumerate(data):
            data[i] = d[:-1].split()

        # print(data)
        self.data_matrix = list(map(self.to_binary, data))
        # print(self.data_matrix)
        self.calc_regions()
        # print(self.regions)

    def get_max_region(self):
        return max(self.regions)

    def calc_regions(self):
        for i in range(len(self.data_matrix)):
            for j in range(len(self.data_matrix[i])):
                if self.data_matrix[i][j] == 1:
                    self.queue.append((i, j))
                    while self.queue:
                        index = self.queue.pop(0)
                        # print(index)
                        self.find_all_adjacent_infected(index)
                        self.counter = self.counter + 1
                        self.data_matrix[index[0]][index[1]] = -1
                    self.regions.append(self.counter)
                    self.counter = 0

    def find_all_adjacent_infected(self, cords):
        for direction in InfectedTracer.movements:
            index = self.move(cords, direction)
            if index:
                x, y = index
                if self.data_matrix[x][y] == 1:
                    if index not in self.queue:
                        self.queue.append(index)

    def move(self, cords, direction):
        zipped = zip(cords, direction)
        mapped = map(sum, zipped)
        sum_tuple = tuple(mapped)
        (x, y) = sum_tuple
        if x < 0 or y < 0 or x > len(self.data_matrix) - 1 or y > len(self.data_matrix[0]) - 1:
            return False
        else:
            return x, y

    def to_binary(self, data_list):
        converted_list = []
        for data in data_list:
            if data == 'Y':
                converted_list.append(1)
            else:
                converted_list.append(0)

        return converted_list


class AlienInvasion:
    movements = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def __init__(self, path):
        self.alien_index = []
        self.infected_index = []
        self.number_aliens = 0
        self.number_human = 0
        self.time = 0
        file = open(path, 'r')
        data = file.readlines()
        file.close()
        self.data = data[2:]
        for i, d in enumerate(self.data):
            self.data[i] = d[:-1].split()
        # print(self.data)
        self.calc_invasion_time()

    def calc_invasion_time(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == 'A':
                    self.number_aliens = self.number_aliens + 1
                    self.alien_index.append((i, j))
                elif self.data[i][j] == 'H':
                    self.number_human = self.number_human + 1

        while True:
            for index in self.alien_index:
                self.find_all_adjacent_infected(index)
            self.number_human = self.number_human - len(self.infected_index)
            # print(self.infected_index)
            if not self.infected_index:
                break
            # print(self.data)
            self.time = self.time + 1
            self.alien_index = self.infected_index
            self.infected_index = []

        # print(self.time)
        # print(self.number_human)

    def get_invasion_time(self):
        return self.time

    def get_survivors(self):
        return self.number_human

    def find_all_adjacent_infected(self, cords):
        for direction in AlienInvasion.movements:
            index = self.move(cords, direction)
            if index:
                x, y = index
                if self.data[x][y] == "H":
                    if index not in self.infected_index:
                        self.data[x][y] = "A"
                        self.infected_index.append(index)

    def move(self, cords, direction):
        zipped = zip(cords, direction)
        mapped = map(sum, zipped)
        sum_tuple = tuple(mapped)
        (x, y) = sum_tuple
        if x < 0 or y < 0 or x > len(self.data) - 1 or y > len(self.data[0]) - 1:
            return False
        else:
            return x, y


def runner():
    # Task 1 Infected Tracer

    path = 'input 2.txt'
    tracer = InfectedTracer(path)
    print(tracer.get_max_region())

    # Task 2 Alien Invasion

    path = 'Question2 input2.txt'
    invasion = AlienInvasion(path)
    time = invasion.get_invasion_time()
    survivors = invasion.get_survivors()
    print('Time:', time, 'Minute(s)')
    if survivors == 0:
        print('NO One Survived')
    else:
        print(survivors, 'survived')


if __name__ == '__main__':
    runner()
