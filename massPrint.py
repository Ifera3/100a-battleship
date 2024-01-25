#!python3

for i in range(1,11):
    for I in range(1,11):
        print(f"    boatshow{i}{I} = StringVar(window)")
        print(f"    boatshow{i}{I}.set('   ')")
        print(f"    boat{i}{I} = Button(window, textvariable=boatshow{i}{I})")
        print(f"    boat{i}{I}.grid(row={11-i+1}, column={I+1}, padx=3)")
