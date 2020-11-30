def run(riddle):
    def get_color_value(color):
        return {
            'RED': 1,
            'ORANGE': 2,
            'YELLOW': 3,
            'GREEN': 4,
            'BLUE': 5,
            'INDIGO': 6,
            'VIOLETT': 7
            }.get(color)
    return sorted(riddle, key=lambda flower: get_color_value(flower))
