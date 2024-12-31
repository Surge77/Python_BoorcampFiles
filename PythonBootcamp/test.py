tell_me_why = {
'You': 56,
'Are': 23,
'My': 43,
'Fire': 78,
'The': 11,
"One":10,
'Desire':8,
'Belive':6,
'When':134,
'I':1234,
'Say':77,
"I Want":123,
'It':12345,
"That":123211,
'Way':12345
}
#make the keys a list
tell_me_why_keys = list(tell_me_why.keys())
#print the list of the keys
print(tell_me_why_keys)
#print certain key
print(tell_me_why_keys[5])
#print certain key value
print(tell_me_why[tell_me_why_keys[5]])