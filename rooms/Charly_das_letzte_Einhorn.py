import random
import string
from EscapeRoom import EscapeRoom


class Charly_das_letzte_Einhorn(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("André Sünnemann", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

    ### LEVELS ###

    def create_level1(self):
        nextSpot = "Gehe zum dunklen Wald"
        key = 2

        task_messages = [
            "<p>Es war ein milder Frühlingmorgen als Charlie das Einhorn von den ersten Strahlen der Sonne geweckt wurde. Er gähnte, streckte sich und sah sich auf der Lichtung um die er als Schlafplatz gewählt hatte. Tausende kleine Blumen wiegten sich in der sachten Brise und die Waldtiere waren bereit geschäftig. Schmetterlinge und Bienen umschwirrten die Blüten, Eichhörnchen suchten im Unterholz nach Nüssen und die Vögel zwitscherten fröhlich ihre Lieder. Nur eines fehlte: die anderen Einhörner. “Seltsam”, dachte sich Charlie, “Wo sind sie denn alle hin?”. Er beschloss die Anderen zu suchen, wo startete er seine Suche?</p>",
            "<p>1. Am See:<br />Auch hier waren keine Einhörner zu sehen. Nun begann Charlie sich wirklich Sorgen zu machen, was sollte er nur tun? Hier auf die anderen warten? Sie suchen gehen? Während er darüber grübelte beobachtete er gedankenverloren die Wolken ziehen die sich auf der Oberfläche des klaren Sees spiegelten. Dann wanderte sein Blick zu seiner eigenen Reflektion und einen Moment lang bewunderte er sein strahlend weißes Fell, seine wallende Mähne und sein goldenes Horn. Da fiel es ihm ein! “Mein Horn! Ich bin ein Einhorn! Ich bitte einfach den See mit meiner magischen Einhornmagie um einen Hinweis!” Gesagt, getan. Charlie bündelte seine Magie und erbat einen Hinweis zum Verbleib der anderen Einhörner. Der See leuchtete kurz hell auf und Charlie starrte konzentriert in die dunklen Tiefen. Plötzlich sah Charlie in der Spiegelung des Wassers wie die Wolken ihre Form zu verändern begannen. Sie bildeten… Buchstaben und Zeichen! Charlie merkte sich die Zeichenfolge: <b>" + self.encrypt(nextSpot, key) + "</b></p>"
        ]
        hints = [
            "Denke an den verdrehten Gaius Iulius Caesar",
            "Aus ABCabc wird dcbDCB",
            "Schlüssel sind variabel"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solutionLevel1, "data": self.encrypt(nextSpot, key)}

    def create_level2(self):
        task_messages = [
            "Nach der korrekten Eingabe des Codes wird nun geheimnisvolle Musik abgespielt und eine Stimme sagt mehrfach: 'Vokale verboten'"
        ]
        hints = [
            "Wie lautet der Spruch 'Vokale verboten' wenn Vokale verboten sind?",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.remove_vowels, "data": "Vokale verboten"}


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

    ### SOLUTIONS ###

    def solutionLevel1(self, text):
        return self.decrypt(text, 2)

    def decrypt(self, text, key):
        key = key * -1
        return self.encrypt(text, key)

    def remove_vowels(self, word):
        result = ""
        vowels = ["a", "e", "i", "o", "u"]
        for c in word:
            if not c in vowels:
                result = result + c
        return result
