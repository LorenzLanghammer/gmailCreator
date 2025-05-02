
Run('C:\\Users\\stefa\\OneDrive\\Desktop\\PyMacroRecord')
WinWaitActive('PyMacroRecord')
Send('^l')
Sleep(500)
Send('openPage')
Sleep(500)
Send('{Enter}')
Sleep(500)
Click(87, 105, 'Left')
Sleep(5000)
WinClose('PyMacroRecord')
WinWaitClose('PyMacroRecord')

