class PipelineAdapter():
  def __init__(self, next):
    self.next = next

  def output(self, data):
    self.next.send_data(data)