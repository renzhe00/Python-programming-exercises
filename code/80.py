subjects, verbs, objects = ["I", "You"], ["Play", "Love"], ["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = '{0} {1} {2}'.format(subjects[i], verbs[j], objects[k])
            print(sentence)