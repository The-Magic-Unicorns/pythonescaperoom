import random
import string
from EscapeRoom import EscapeRoom


class Charly_das_letzte_Einhorn(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("The Unicorn Project", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

    ### LEVELS ###

    def create_level1(self):
        flowers = ["RED", "INDIGO", "GREEN", "RED", "RED", "YELLOW", "GREEN", "VIOLETT", "INDIGO", "ORANGE", "BLUE", "BLUE", "YELLOW", "ORANGE", "BLUE", "VIOLETT", "YELLOW", "INDIGO", "GREEN", "ORANGE", "RED"]

        task_messages = [
            "Charlie beschloss sich erst einmal auf der Lichtung umzusehen, wo er schon mal hier war. Die Wolken zogen behäbig über den Himmel und ihre sanften Schatten dämpften das grelle Glitzern des taubedecktes Grases in der Morgensonne. Charlie fragte die Vögel, die Dachse, die Maulwürfe und den Fuchs ob sie etwas gesehen hatten doch alle waren ratlos. “Vielleicht haben die Bienen etwas gesehen, die sind immer schon früh unterwegs”, dachte sich Charlie und machte sich auf den Weg richtung Bienenstock der von einem Blumenmeer umgeben war. Vorsichtig darauf achtend keine Blumen unter seinen goldenen Hufen zu zertrampeln ging er auf eine Biene zu. 'Hallo fleißige Biene, du weißt nicht zufällig wo die anderen Einhörner sind?'</p>",
            "'Hm, vielleicht weiß ich etwas darüber', summte die Biene, 'Da gibt es nur ein Problem: Sieh, ich bin gar nicht so fleißig wie es immer heißt. Und unsere Königin ist nicht nur unersättlich sondern auch sehr wählerisch. Sie möchte unseren frischen Honignektar nur in einer ganz bestimmten Zusammensetzung trinken. Die Blumen stehen aber so wild durcheinander, dass es furchtbar mühsam ist sie in der richtigen Reihenfolge anzufliegen. Und zu allem Übel habe ich auch noch vergessen was die Reihenfolge war die die Königin befohlen hatte. Hilfst du mir? Dann verrate ich dir was ich über die anderen Einhörner weiß.'</p>",
            "Charlie sah sich die Blumen an, es gab: blaue, rote, grüne, gelbe, lilane, orangene und indigofarbene. Mit seiner magischen Einhornmagie war es ein Leichtes für ihn sie in anderer Reihenfolge einzupflanzen, nur in welcher Reihenfolge könnte die Königin diese Farben haben wollen?",
            "Bisher standen sie so:",
            "<b>" + self.getColors(flowers) + "</b>"
        ]
        hints = [
            "Anzahl einzelner Farben irrelevant",
            "Natürliches Phänomen, (Regen + Sonne)",
            "ROYGBIV"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solveLevel1, "data": flowers}

    def create_level2(self):
        riddle = "Gehe zum dunklen Wald"
        key = 2

        task_messages = [
            "<p>Es war ein milder Frühlingmorgen als Charlie das Einhorn von den ersten Strahlen der Sonne geweckt wurde. Er gähnte, streckte sich und sah sich auf der Lichtung um die er als Schlafplatz gewählt hatte. Tausende kleine Blumen wiegten sich in der sachten Brise und die Waldtiere waren bereit geschäftig. Schmetterlinge und Bienen umschwirrten die Blüten, Eichhörnchen suchten im Unterholz nach Nüssen und die Vögel zwitscherten fröhlich ihre Lieder. Nur eines fehlte: die anderen Einhörner. “Seltsam”, dachte sich Charlie, “Wo sind sie denn alle hin?”. Er beschloss die Anderen zu suchen, wo startete er seine Suche?</p>",
            "<p>1. Am See:<br />Auch hier waren keine Einhörner zu sehen. Nun begann Charlie sich wirklich Sorgen zu machen, was sollte er nur tun? Hier auf die anderen warten? Sie suchen gehen? Während er darüber grübelte beobachtete er gedankenverloren die Wolken ziehen die sich auf der Oberfläche des klaren Sees spiegelten. Dann wanderte sein Blick zu seiner eigenen Reflektion und einen Moment lang bewunderte er sein strahlend weißes Fell, seine wallende Mähne und sein goldenes Horn. Da fiel es ihm ein! “Mein Horn! Ich bin ein Einhorn! Ich bitte einfach den See mit meiner magischen Einhornmagie um einen Hinweis!” Gesagt, getan. Charlie bündelte seine Magie und erbat einen Hinweis zum Verbleib der anderen Einhörner. Der See leuchtete kurz hell auf und Charlie starrte konzentriert in die dunklen Tiefen. Plötzlich sah Charlie in der Spiegelung des Wassers wie die Wolken ihre Form zu verändern begannen. Sie bildeten… Buchstaben und Zeichen! Charlie merkte sich die Zeichenfolge: <b>" + self.encrypt(riddle, key) + "</b></p>"
        ]
        hints = [
            "Denke an den verdrehten Gaius Iulius Caesar",
            "Aus ABCabc wird dcbDCB",
            "Schlüssel sind variabel"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solveLevel2, "data": self.encrypt(riddle, key)}

    def create_level3(self):
        riddle = "Vokale verboten"
        task_messages = [
            "Nach der korrekten Eingabe des Codes wird nun geheimnisvolle Musik abgespielt und eine Stimme sagt mehrfach: ",
            "</b>" + riddle + "</b>"
        ]
        hints = [
            "Wie lautet der Spruch '" + riddle + "' wenn Vokale verboten sind?",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solveLevel3, "data": riddle}

    def create_level4(self):
        riddle = ""
        task_messages = [
            "",
            ""
        ]
        hints = [
            ""
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solveLevel4, "data": riddle}

    def create_level5(self):
        riddle = ""
        task_messages = [
            "",
            ""
        ]
        hints = [
            ""
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solveLevel5, "data": riddle}

    def create_level6(self):
        riddle = {"matrix_size": 3, "magical_sum": 15}
        task_messages = [
            "",
            ""
        ]
        hints = [
            ""
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solveLevel6(), "data": riddle, "algorithm": self.testLevel6Solution()}

    ### Functions for level design ####

    def getColors(self, flowers):
        colored_output = "- "
        for flower in flowers:
            colored_output = colored_output + '<font color="' + flower.lower() + '">' + flower + '</font> - '
        return colored_output

    ### SOLUTIONS ###

    def solveLevel1(self, riddle):
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

    ### Level 2 ###

    def solveLevel2(self, text):
        def decrypt(self, text, key):
            key = key * -1
            return self.encrypt(text, key)
        def encrypt(self, text, key):
            reverseText = text[::-1]
            encrypted = self.caesar(reverseText, key)
            return encrypted
        def caesar(self, text, key):
            encrypted = ""
            for uChr in text:
                iChr = ord(uChr)
                eChr = chr((iChr + key) %128)
                encrypted += eChr
            return encrypted
        return self.decrypt(text, 2)

    ### Level 3 ###

    def solveLevel3(self, word):
        result = ""
        vowels = ["a", "e", "i", "o", "u"]
        for c in word:
            if not c in vowels:
                result = result + c
        return result

    ### Level 4 ###
    # Result should be in lower case
    def solveLevel4(self, riddle):
        result = ""
        for word in riddle.split():
            if word.isdigit():
                continue
            # This means not all poitions in word are numeric, now it could be iterated over word using different methods:
            # via char index
            # via similar for loop as above
            # via slicing operator
            # this is not necessary in our example but described in our slides
            result += word[0].lower()
        return result

    ### Level 5 ###
    #Count of all combination possibilities of a given word
    def solveLevel5(self, riddle):
        def recursive_combinations(input_word, combinations=['']):
            if len(input_word) == 0:
                return combinations
            first_letter = input_word[0]
            reduced_word = input_word[1:]
            combinations = combinations + list(map(lambda x: x + first_letter, combinations))
            return recursive_combinations(reduced_word, combinations)
        return recursive_combinations(riddle).count()

    ### Level 6 ###
    # The 9 field problem - one possible solution could be to create an full magic square or our simple solution
    def solveLevel6(riddle):
        import random

        result = []
        all_numbers = set([i for i in range(1, riddle["matrix_size"]**2 + 1)])

        for i in range(riddle["matrix_size"]):
            row = []
            while sum(row) != riddle["magical_sum"]:
                row = random.sample(all_numbers, 3)
                if (1 in all_numbers) and (1 not in row):
                    row = []
                    continue
            all_numbers = all_numbers.difference(set(row))
            result.append(row)
        return result

    # the 9 field problem - testing algorithm
    def testLevel6Solution(result):
        def test_row(matrix_row):
            row_length = len(matrix_row)
            magical_sum = int((row_length**3 + row_length) / 2)
            return sum(matrix_row) == magical_sum
        def test_numbers(matrix):
            value_list = []
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    value_list.append(matrix[i][j])
            list.sort(value_list)
            counter = 1
            for index in range(len(value_list)):
                if value_list[index] != counter:
                    return False
                counter += 1
            return True
        return test_row(result[0]) and test_row(result[1]) and test_row(result[2]) and test_numbers(result)
