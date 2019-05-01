import tkinter as tk


def choice(choices, default=0, SubmitText="Submit", title="Questionaire"):
	ChoiceWin = tk.Tk()
	ChoiceWin.iconbitmap("./res/choice.ico")
	ChoiceWin.title(title)


	ChoiceVar = tk.IntVar(ChoiceWin)
	ChoiceVar.set(default)


	counter = 0
	for choice in choices:
		ChoiceButton = tk.Radiobutton(ChoiceWin, text=choice, variable=ChoiceVar, value=counter)
		ChoiceButton.pack(side=tk.TOP, anchor=tk.NW)

		counter += 1

	SubmitButton = tk.Button(ChoiceWin, text=SubmitText, command=ChoiceWin.destroy)
	SubmitButton.pack(side=tk.BOTTOM)
	
	while True:
		try:
			ChoiceWin.update()
		except tk.TclError:
			return ChoiceVar.get()


if __name__ == "__main__":
	print("Chose one:", choice([chr(num) for num in range(32, 127)]))
	input()
