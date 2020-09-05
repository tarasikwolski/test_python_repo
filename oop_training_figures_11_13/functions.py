def sum_of_figures(figures: list)->float:
    suma = 0.0
    for figure in figures:
        suma += figure.get_area()

    return suma