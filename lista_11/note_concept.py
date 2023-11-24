#Function that given a note converts to a concept between A anf F
def note_concept(note):
    if note > 90:
        return "A"
    elif note > 80:
        return "B"
    elif note > 70:
        return "C"
    elif note > 60:
        return "D"
    else:
        return "F"
note = float(input("Enter a note, and I will convert to a concept between A and F: "))
print(note_concept(note))