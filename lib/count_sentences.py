#!/usr/bin/env python3
import re
class MyString:
  def __init__(self,value=None):
    self._value =value
  
  def get_val(self):
    return self._value
  def set_val(self,value):
    if type(value) == str:
      self._value = value
    else:
      print('The value must be a string.')

  value = property(get_val,set_val)

  def is_sentence(self):
    if(self.value.endswith('.')):
      return True
    else:
      return False
  def is_question(self):
    if(self.value.endswith('?')):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if(self.value.endswith('!')):
      return True
    else:
      return False

  def count_sentences(self):
   my_str = re.sub('',) 

    

