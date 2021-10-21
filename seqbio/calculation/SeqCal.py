# SeqCal module
def gcContent(seq):
    # G+C/(A+T+G+C)
    return (countBase(seq.upper(), 'G') + countBase(seq.upper(), 'C'))/len(seq.upper())

def atContent(seq):
    # A+T/(A+T+G+C)
    return (countBase(seq.upper(), 'A') + countBase(seq.upper(), 'T'))/len(seq.upper())

def countBase(seq, base):
    seq = seq.upper()
    return seq.count(base.upper())

def countBasesDict(seq):
    seq = seq.upper()
    basesM = {}
    for base in seq:
        basesM[base] = basesM.get(base, 0)+1
    return basesM

# print(__name__)
# if __name__ == '__main__':
#     seq = "ATGGGccGTAGAATTCTTGCaaGCCCGT"
#     print("test: countBase G", countBase(seq, 'G'))
#     print("test: countBase C", countBase(seq, 'C'))
#     print("test: length", len(seq))
#     print("test: gc Content:", gcContent(seq))
#     print("test: Count Bases:" ,countBasesDict(seq))