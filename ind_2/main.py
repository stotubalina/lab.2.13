#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from flights import get_fl, disp, select


if __name__ == '__main__':
    flights = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            flight = get_fl.get_flight()
            flights.append(flight)
            if len(flights) > 1:
                flights.sort(
                    key=lambda item:
                    item.get('flight_destination', ''))

        elif command == 'list':
            disp.display_flights(flights)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            airplane_type = (parts[1].capitalize())
            print(f"Для типа самолета {airplane_type}:")
            selected = select.select_flights(flights, airplane_type)
            disp.display_flights(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список всех рейсов;")
            print("select <тип самолета> - запросить рейсы указанного типа "
                  "самолета;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)