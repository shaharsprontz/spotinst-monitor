from firebase import firebase


firebase = firebase.FirebaseApplication('https://pushtest-eb14f.firebaseio.com/')

array = ["Umi", "Turdakulov"]

arraywitoutbrackets = (", ".join(repr(e) for e in array))
stringarray = str(arraywitoutbrackets)
result = firebase.patch('/apps', {'condition': str(stringarray)})


print stringarray
print type(stringarray)
