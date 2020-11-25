from unit_students import UnitStudentsToRooms
from output_file import OutputJSON, OutputXML
from parses import ParserJSON
import argparse


load_students = ParserJSON("students.json")
load_rooms = ParserJSON("rooms.json")


def test(students_file_name, rooms_file_name, format_output):
    students = load_students.loader(students_file_name)
    rooms = load_rooms.loader(rooms_file_name)

    rooms_with_students = UnitStudentsToRooms(students, rooms).unit()

    format_file = 'result.'+format_output
    if format_output == 'xml':
        OutputXML(format_file).write(rooms_with_students)
    elif format_output == 'json':
        OutputJSON(format_file).write(rooms_with_students)


def create_args():
    parser = argparse.ArgumentParser(description='Processes json files')
    parser.add_argument('-students', action="store", dest="students", type=str, help='Input students_file_path')
    parser.add_argument('-rooms', action="store", dest="rooms", type=str, help='Input rooms_file_path')
    parser.add_argument('-format', action="store", dest="format_output", type=str, help='Choose XML or JSON format_file')
    return parser


if __name__ == '__main__':
    parser_ = create_args()
    args = parser_.parse_args()
    test(args.students, args.rooms, args.format_output)

