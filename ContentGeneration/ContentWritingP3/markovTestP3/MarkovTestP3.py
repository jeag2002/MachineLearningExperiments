import markovify

# Get raw text as string.
# include errors='ignore', encoding='utf-8' if you are working in windows
with open("84-0.txt", errors='ignore', encoding='utf-8') as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text, state_size=3)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))