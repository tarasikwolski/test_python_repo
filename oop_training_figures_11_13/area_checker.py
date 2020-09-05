class AreaChecker:
    @staticmethod
    def check_area(area: float, figures: list) -> bool:
        suma = 0.0
        for figure in figures:
            suma += figure.get_area()
        return area >= suma
