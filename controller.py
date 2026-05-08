import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        if modality == "default":

                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

        if modality == "lineare":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

        if modality =="dicotomica":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
        else:
                return None
        return


    def handleLanguageSelection(self, e):
        self._view.lvOut.controls.append(
            ft.Text(value="Lingua correttamente selezionata:" + self._view.ddLanguage.value)
        )
        self._view.update()

    def handleSearchSelection(self, e):
        self._view.lvOut.controls.append(
            ft.Text(value="Modalità correttamente selezionata:" + self._view.ddSearch.value)
        )
        self._view.update()

    def handleSpellCheck(self, e):
        txtIn = self._view.txtInput.value
        if txtIn == "":
            self._view.lvOut.controls.clear()
            self._view.lvOut.controls.append(
                ft.Text(value="Inserire una frase!")
            )
            return

        language = self._view.ddLanguage.value
        print(language)
        modality = self._view.ddSearch.value
        print(modality)

        if language == "":
            self._view.lvOut.controls.clear()
            self._view.lvOut.controls.append(
                ft.Text(value="Inserire una lingua!")
            )
            return

        if modality == "":
            self._view.lvOut.controls.clear()
            self._view.lvOut.controls.append(
                ft.Text(value="Inserire una modalità!")
            )
            return

        parole , elapsedTime = self.handleSentence(txtIn , language , modality)

        self._view.lvOut.controls.clear()
        self._view.lvOut.controls.append(
            ft.Text(value="Frase inserita:" + txtIn)
        )
        self._view.lvOut.controls.append(
            ft.Text(value="Parole errate:" + parole)
        )
        self._view.lvOut.controls.append(
            ft.Text(value="Tempo richiesto dalla ricerca:" + str(elapsedTime))
        )
        self._view.update()


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
