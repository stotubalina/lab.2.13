#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sample


if __name__ == "__main__":
    sample_string = (
        "Уважаемый %F% %N%! Вы делаете работу по замыканиям функции."
    )
    name, surname = input("Введите имя и фамилию: ").split()
    print(sample.sample(sample_string, name, surname))
