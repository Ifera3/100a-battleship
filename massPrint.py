#!python3

for i in range(1,11):
    for I in range(1,11):
        print(f"    boatshow{i}{I}2 = StringVar(window)")
        print(f"    showlist2.append(boatshow{i}{I}2)")
        print(f"    boat{i}{I}2 = Button(window, textvariable=boatshow{i}{I}2, command=lambda m=[{i-1},{I-1}]: gogrt2(m))")
        #print(f"    boat{i}{I}.grid(row={12-i}, column={I+1}, padx=3)")
        print(f"    buttonlist2.append(boat{i}{I}2)")
