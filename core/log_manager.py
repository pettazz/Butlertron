from fluent import sender
from fluent import event
sender.setup('butlr', host='localhost', port=24224)
event.Event('follow', {
  'from': 'userA',
  'to':   'userB'
})