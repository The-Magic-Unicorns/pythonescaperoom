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
            """Charlie beschloss sich erst einmal auf der Lichtung umzusehen, wo er schon mal hier war. Die Wolken zogen behäbig über den Himmel und ihre sanften Schatten dämpften das grelle Glitzern des taubedecktes Grases in der Morgensonne. Charlie fragte die Vögel, die Dachse, die Maulwürfe und den Fuchs ob sie etwas gesehen hatten doch alle waren ratlos. “Vielleicht haben die Bienen etwas gesehen, die sind immer schon früh unterwegs”, dachte sich Charlie und machte sich auf den Weg richtung Bienenstock der von einem Blumenmeer umgeben war. Vorsichtig darauf achtend keine Blumen unter seinen goldenen Hufen zu zertrampeln ging er auf eine Biene zu. “Hallo fleißige Biene, du weißt nicht zufällig wo die anderen Einhörner sind?”
            “Hm, vielleicht weiß ich etwas darüber”, summte die Biene, “Da gibt es nur ein Problem: Sieh, ich bin gar nicht so fleißig wie es immer heißt. Und unsere Königin ist nicht nur unersättlich sondern auch sehr wählerisch. Sie möchte unseren frischen Honignektar nur in einer ganz bestimmten Zusammensetzung trinken. Die Blumen stehen aber so wild durcheinander, dass es furchtbar mühsam ist sie in der richtigen Reihenfolge anzufliegen. Und zu allem Übel habe ich auch noch vergessen was die Reihenfolge war die die Königin befohlen hatte. Ich weiß nur noch, dass sie gestern aus einem Fenster des Bienenstocks geschaut hatte und etwas gesehen hat, das sie auf die Idee brachte. Hilfst du mir? Dann verrate ich dir was ich über die anderen Einhörner weiß.”
            Charlie sah sich die Blumen an, es gab: blaue, rote, grüne, gelbe, lilane, orangene und indigofarbene. Mit seiner magischen Einhornmagie war es ein Leichtes für ihn sie in anderer Reihenfolge einzupflanzen, nur in welcher Reihenfolge könnte die Königin diese Farben haben wollen? 
            <br/> Bisher standen sie so: """,
            "<b>" + self.getColors(flowers) + "</b>"
        ]
        success_meesage = "Charlie richtete sein Horn auf die Blumen, es blitzte hell auf und alle Blümchen erhoben sich, samt einem Klumpen Erde an der Wurzel, in die Lüfte um sich dann, schön geordnet in den Farben des Regenbogens in einem halbkreis um den Bienenstock herum selbst wieder einzupflanzen. Die Biene summte fröhlich und flog ein paar Loopings. “Ich weiß, dass du die anderen Einhörner bestimmt schneller wieder siehst wenn du jetzt nicht auf der Lichtung bleibst. Also hopp hopp, weg mit dir, tiefer in den Wald.” Diese Aussage fand Charlie nun doch sehr mysteriös aber die Biene war bereits wieder in den Stock geflogen und so machte er sich auf den Weg zum See."
        hints = [
            "Es standen tausende kleine Blumen auf der Lichtung, Charlie pflanzte nur einige davon um. Es ist für die Lösung des Rätsels unerheblich wie viele Blumen es sind, es geht nur um die Reihenfolge der Farben.",
            "Die Königin kam gestern auf die Idee diese bestimmte Reihenfolge zu wollen als sie etwas sah das ihr gefiel. Charlie erinnerte sich, dass es gestern zwar im Allgemeinen sonnig war, es zwischendurch aber immer wieder kurze Regenschauer gab.",
            "R O Y G B I V"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solveLevel1, "data": flowers, "success_meesage": success_meesage}

    def create_level2(self):
        riddle =  "gehe zum fluss" #"llney fns xaxz" # gehe zum fluss
        key = 19

        task_messages = [
            """<p>
                Auch hier waren keine Einhörner zu sehen. Nun begann Charlie sich wirklich Sorgen zu machen, was sollte er nur tun? Hier auf die anderen warten? 
                Sie suchen gehen? Während er darüber grübelte beobachtete er gedankenverloren die Wolken ziehen die sich auf der Oberfläche des klaren Sees spiegelten. 
                Dann wanderte sein Blick zu seiner eigenen Reflektion und einen Moment lang bewunderte er sein strahlend weißes Fell, seine wallende rosa Mähne in die 
                er sich vor Kurzem blaue Strähnchen färben ließ um seine Männlichkeit zu unterstreichen, und sein goldenes Horn. Da fiel es ihm ein! “Mein Horn! 
                Ich bin ein Einhorn! Ich bitte einfach den See mit meiner magischen Einhornmagie um einen Hinweis!” Gesagt, getan. Charlie bündelte seine Magie und 
                erbat einen Hinweis zum Verbleib der anderen Einhörner. Der See leuchtete kurz hell auf und Charlie starrte konzentriert in die dunklen Tiefen. 
                Plötzlich sah er in der Spiegelung des Wassers wie die Wolken ihre Form zu verändern begannen. 
                Sie bildeten… Buchstaben und Zeichen! Charlie merkte sich die Zeichenfolge: “
                """,
                 self.encrypt(riddle, key),
                "”</p>"
        ]
        success_meesage = "Charlie beschloss dem Hinweis zu folgen und dort weiter zu suchen."
        hints = [
            "Denke an den verdehten Gaius Julius Caesar.",
            "Charlie sah die Wolkenbuchstaben in der Spiegelung des Sees. Vielleicht hat er sie sich deshalb spiegelverkehrt gemerkt? Aus AbCaBc würde so cBaCbA werden.",
            "Die Schlüssel sind variabel."
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solveLevel2, "data": self.encrypt(riddle, key), "success_meesage": success_meesage}

    def create_level3(self):
        riddle = "Vokale verboten"
        task_messages = [
            """<p>
                Klickklickklack Klickklack Klickklackklick... Charlie spitzte die Ohren. Das klang ja… wie Tastaturklicken… und dann schwere Seufzer dazwischen. 
                Er folgte dem seltsamen Geräusch. Auf einem Fleck grünem Gras saß ein Kaninchen vor einem alten Laptop und tippte eifrig auf der Tastatur herum. 
                “Hallo” grüßte Charlie freundlich “irgendwas sagt mir dass du vielleicht Hilfe brauchen könntest?” Das Kaninchen seufzte noch einmal schwer und 
                blickte zu Charlie auf “Ja, allerdings. Ich bin auf der Suche nach einer netten Kaninchendame und weil den ganzen Tag durch den Wald hoppeln 
                so furchtbar anstrengend ist, dachte ich ich probiere es mal mit Onlinedating. Aber auf diesem blöden Ding ist die Tastatur kaputt und ich kann 
                nur Großbuchstaben tippen! So denken doch die Damen gleich ich wäre unhöflich. Du kannst nicht zufällig mit deiner magischen Einhornmagie dafür 
                sorgen, dass alle Buchstaben zu Kleinbuchstaben konvertiert werden?”
                “Klar kann ich das” sagte Charlie, der noch immer etwas perplex war über ein Kaninchen das nicht nur einen Laptop nutzte sondern sich auch am 
                Online-Dating probierte. Aber dann fiel ihm ein dass er ein Einhorn war und deshalb Logik nicht viel zählte in diesem Wald. Es war eine seiner 
                einfachsten Übungen den gelungen Anmachspruch des Kaninchens zu konvertieren: “SUCHE NETTE KANINCHENDAME ZUM FAMILIE ERWEITERN!”</p>
            """
        ]
        success_meesage = """<p>
                ‘Erweitern?’ dachte sich Charlie, ‘seltsame Wortwahl’ aber dann dachte er sich nichts weiter dabei und verhexte den Laptop sodass nun alles 
                klein geschrieben wurde. “Vielen Dank!” sagte das Kaninchen “Bestimmt hat meine Frau oder eins meiner Kinder wieder heimlich beim Chatten 
                Möhren gemümmelt und in die Tastatur gekrümelt”</p>
                <p>Charlie schaute das Kaninchen perplex an. Seine Frau? Eins seiner Kinder? 
                Aber Kaninchensitten waren eben andere als Einhornsitten und so setzte Charlie kommentarlos seine Suche fort.</p>"""
        hints = [
           "In diesem Rätsel ist nichts Besonderes gefordert, ein einfacher Algorithmus der Uppercase zu Lowercase umwandelt reicht aus"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solveLevel3, "data": riddle, "success_meesage": success_meesage}

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
                if uChr == ' ':
                    encrypted += uChr
                    continue
                iChr = ord(uChr) - 97
                eChr = chr((iChr + key) %26 + 97)
                encrypted += eChr
            return encrypted
        return self.decrypt(text, 2)

    ### Level 3 ###
    # Result should be in lower case
    def solveLevel3(self, riddle):
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

    ### Level 4 ###
    #Count of all combination possibilities of a given word
    def solveLevel4(self, riddle):
        def recursive_combinations(input_word, combinations=['']):
            if len(input_word) == 0:
                return combinations
            first_letter = input_word[0]
            reduced_word = input_word[1:]
            combinations = combinations + list(map(lambda x: x + first_letter, combinations))
            return recursive_combinations(reduced_word, combinations)
        return recursive_combinations(riddle)

    ### Level 5 ###
    def solveLevel5(self, word):
        result = ""
        vowels = ["a", "e", "i", "o", "u"]
        for c in word:
            if not c in vowels:
                result = result + c
        return result

    #Permutations
    def solveLevel5b(riddle):
        result = []
        def permutations(input_word, permutation=""):
            if len(input_word) == 0:
                result.append(permutation)
            for i in range(len(input_word)):
                new_permutation = permutation + input_word[i]
                rest_of_word = input_word[0:i] + input_word[i+1:]
                permutations(rest_of_word, new_permutation)
        permutations(riddle)
        return result


    ### Level 6 ###
    # The 9 field problem - one possible solution could be to create a full magic square or our simple solution
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
