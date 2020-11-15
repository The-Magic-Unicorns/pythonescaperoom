import random
import string
from EscapeRoom import EscapeRoom
from classes.MagicSquare import MagicSquare


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
        dim = random.randint(3, 15)
        if dim % 2 == 0:
            dim -= 1
        square = MagicSquare()
        storage = square.deploy(dim)
        nuts = square.magicNumber

        task_messages = [
            "<p>Charlie war klar, dass er das Rätsel so nicht lösen konnte, er brauchte mehr Hinweise und beschloss deshalb noch die anderen Orte zu besuchen.</p>",
            "<p>2. Dunkler Wald:<br />Charlie traf ein Eichhörnchen das behauptet etwas zum Verbleib der Einhörner zu wissen, es will aber seine Informationen nur preisgeben wenn Charlie ihm vorher bei einem Problem hilft. Es hat " + str(nuts) + " Nüsse gesammelt und möchte diese in seiner Vorratskammer in einem ganz bestimmten Muster lagern. Die Nüsse sollen in einem " + str(square.dim) + "x" + str(square.dim) + " Raster liegen. In jedem Feld soll eine andere Anzahl an Nüssen liegen und in jeder Zeile und Spalte sollen insgesamt genau " + str(square.sum) + " Nüsse liegen. Bei korrekter Antwort gibt Eichhörnchen einen weiteren Hinweis zum Verbleib der Einhörner heraus.</p>"
        ]
        hints = [
            "Die Summe der Nüsse ist immer ungerade",
            "Baue ein magisches Quadrad",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solutionLevel2(), "data": "TEST"}

    def create_level3(self):
        task_messages = [
            ""
        ]
        hints = [
            ""
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_functions": self.solutionLevel3(), "data": "TEST"}


    ## BEGIN LEVEL 1 ##
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

    def decrypt(self, text, key):
        key = key * -1
        return self.encrypt(text, key)
    ## END LEVEL 1 ##

    ### SOLUTIONS ###

    ## BEGIN LEVEL 1 ##
    def solutionLevel1(self, text):
        return self.decrypt(text, 2)
    ## END LEVEL 1 ##

    ## BEGIN LEVEL 2 ##
    def solutionLevel2(self):
        return 1
    ## END LEVEL 2 ##

    ## BEGIN LEVEL 3 ##
    def solutionLevel3(self):
        return 1
    ## END LEVEL 3 ##
