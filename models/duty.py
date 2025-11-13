class Duty:
  def __init__(self, description, number, ksbs):
    self._description = description
    self._number = number 
    self._ksbs = ksbs
    self._complete = False

  @staticmethod
  def get_duty():
    return Duty("Random Duty", "", "",)


  def get_name(self):
    return f"Duty {self._number}"
  

  def get_ksbs(self):
    return self._ksbs
  
  def save(duty):
    pass

  def complete(self):
    self._complete = True
  
  def is_complete(self):
    if self._complete:
      return "Duty Complete!"
    else:
      return "Duty Not Completed!"
  
  