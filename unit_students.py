from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, list_of_students, list_of_rooms):
        self.students = list_of_students
        self.rooms = list_of_rooms

    @abstractmethod
    def unit(self):
        pass


class UnitStudentsToRooms(Unit):
    """
    Class for unit student
    """
    def unit(self):
        """
        Return rooms with students in each room
        """
        for room in self.rooms:
            for student in self.students:
                if room['id'] == student['room']:
                    if "students" not in room:
                        room["students"] = []
                    room["students"].append(student)
        return self.rooms
