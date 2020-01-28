from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('84-0.txt', num_epochs=4)
textgen.generate(3, temperature=1.0)