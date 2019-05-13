def reverse(sentence):
    words=sentence.split(" ")
    newWords=[i[::-1] for i in words]
    newSentence=" ".join(newWords)
    print(newSentence)



sentence=input()
reverse(sentence)
