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
    temp_value = self.value
    for index in ["!", "?"]:
      temp_value = temp_value.replace(index, ".")
    sentence_list = [sentence for sentence in temp_value.split(".") if sentence]
    return len(sentence_list)
      