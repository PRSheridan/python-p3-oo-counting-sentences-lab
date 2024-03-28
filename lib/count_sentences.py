#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self.value = value
  
  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    temp = len(self.value)
    if self.value[temp-1] == ".": return True
    else: return False

  def is_question(self):
    temp = len(self.value)
    if self.value[temp-1] == "?": return True
    else: return False

  def is_exclamation(self):
    temp = len(self.value)
    if self.value[temp-1] == "!": return True
    else: return False

  def count_sentences(self):
    counter = 0
    sentence_list = []
    punctuation_list = [".", "?", "!"]

    for index in self.value:
      if index in punctuation_list:
        index_of_punctuation = self.value.index(index)
        temp_sentence = self.value[0:index_of_punctuation+1]
        sentence_list += [temp_sentence]
        self.value.replace(temp_sentence, "")
        self.value.strip()
        print(self.value)
        print(sentence_list)
      