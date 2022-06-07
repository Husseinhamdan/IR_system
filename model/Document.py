from services.text_processing import *

class Document:
    def __init__(self):
        self._I = ""
        self._T = ""
        self._B = ""
        self._A = ""
        self._N = ""
        self._K = ""
        self._X = ""
        self._W = ""
        self._Content = ""





    def _get_I(self):
        return self._I
    def _set_I(self, new_I):
        self._I = new_I
        
    def _get_T(self):
        return self._T
    def _set_T(self, new_T):
        self._T = new_T
        
    def _get_B(self):
        return self._B
    def _set_B(self, new_B):
        self._B = new_B
        
    def _get_A(self):
        return self._A
    def _set_A(self, new_A):
        self._A = new_A
        
    def _get_K(self):
        return self._K
    def _set_K(self, new_K):
        self._K = new_K
        
    def _get_N(self):
        return self._N
    def _set_N(self, new_N):
        self._N = new_N
        
    def _get_W(self):
        return self._W
    def _set_W(self, new_W):
        self._W = new_W

    def _get_X(self):
        return self._X

    def _set_X(self, new_X):
        self._X = new_X

    def _get_Content(self):
        return self._Content

    def _set_Content(self, new_Content):
        self._Content = new_Content

    def processing_content(self,stopWord):
        lower = lower_text(self._Content)
        token = text_to_wordtoken(lower)
        filter = filter_stopWord(token,stopWord)
        stem = stemWord(filter)
        lemm = lemmWord(stem)
        return " ".join(lemm)

    def to_dict(self):
        return {
            "Id": self.I,
            "Title": self.T,
            "Authors":self.A,
            "Abstract":self.W,
            "Date" :self.B
        }


    I = property(_get_I, _set_I)
    T = property(_get_T, _set_T)
    B = property(_get_B, _set_B)
    A = property(_get_A, _set_A)
    K = property(_get_K, _set_K)
    W = property(_get_W, _set_W)
    N = property(_get_N, _set_N)
    X = property(_get_X, _set_X)
    Content = property(_get_Content, _set_Content)
