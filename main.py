import re

from seqbio.calculation.SeqCal import gcContent, atContent, countBase, countBasesDict
from seqbio.pattern.SeqPattern import enzTargetsScan, cpgSearch
from seqbio.seqMan.dnaconvert import dna2rna, reverseComplementSeq, dna2protein, reverseSeq, complementSeq, loadCodons

# Input
# seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
# seq = seq.upper()

# print("Transcription: ", dna2rna(seq))
# print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
# print("Translation: ", dna2protein(seq))
# print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
# print("GC Content:", gcContent(seq))
# print("Count Bases: ", countBasesDict(seq))
# print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
# print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
# print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))

def test():
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    seq = seq.upper()

    print("Transcription: ", dna2rna(seq))
    print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
    print("Translation: ", dna2protein(seq))
    print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
    print("GC Content:", gcContent(seq))
    print("Count Bases: ", countBasesDict(seq))
    print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
    print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
    print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:' ,
        dest='command'
    )
    
    subparsers.required = True

    #first command is gcContent
    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                            help="Provide sequence")

    #second command is countBases
    cbase_command = subparsers.add_parser('countBases', help='Count number of each base')
    cbase_command.add_argument("-s", "--seq", type=str, default=None, 
                            help="Provide Sequence")
    cbase_command.add_argument("-r", "--revcomp", action ='store_true', default=False, 
                            help="Convet DNA to reverse-complementary")

    #third command is transcription
    transc_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transc_command.add_argument("-s", "--seq", type=str, default=None, 
                            help="Provide Sequence")
    transc_command.add_argument("-r", "--revcomp", action ='store_true', default=False, 
                            help="Convet DNA to reverse-complementary")

    #fouth command is translation
    transl_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    transl_command.add_argument("-s", "--seq", type=str, default=None, 
                            help="Provide Sequence")
    transl_command.add_argument("-r", "--revcomp", action ='store_true', default=False, 
                            help="Convet DNA to reverse-complementary")

    #fifth command is enzTargetsScan
    renz_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    renz_command.add_argument("-s", "--seq", type=str, default=None, 
                            help="Provide Sequence")
    renz_command.add_argument("-e", "--enz", type=str, default=None, 
                            help="Provide Enzyme name")
    renz_command.add_argument("-r", "--revcomp", action ='store_true', default=False, 
                            help="Convet DNA to reverse-complementary")


    # parser.print_help()

    return parser

def main():
    parser = argparserLocal()
    args = parser.parse_args()
    # print(args)
    
    if args.command == 'gcContent':
        if args.seq == None:
            print("------------------------------------------------------\nError: Invalid input (You do not provide -s or --seq)\n------------------------------------------------------\n")
            exit(parser.parse_args(['gcContent','-h']))
        # print("line 96", args.seq.upper())
        # print("line 97", countBase(args.seq, 'G'))
        # print("line 98", countBase(args.seq, 'c'))
        # print("line 99", len(args.seq))
        # print("line 100", float(gcContent(args.seq)))
        print("Input ", args.seq, "GC Content = ", gcContent(args.seq.upper()))

    elif args.command == 'countBases':
        if args.seq == None:
            print("------------------------------------------------------\nError: Invalid input (You do not provide -s or --seq)\n------------------------------------------------------\n")
            exit(parser.parse_args(['countBases','-h']))
        elif args.revcomp:
            print("Input ", args.seq, "countBases = ", countBasesDict(reverseComplementSeq(args.seq.upper())))
        else:
            print("Input ", args.seq, "countBases = ", countBasesDict(args.seq.upper()))
    
    elif args.command == 'transcription':
        if args.seq == None:
            print("------------------------------------------------------\nError: Invalid input (You do not provide -s or --seq)\n------------------------------------------------------\n")
            exit(parser.parse_args(['transcription','-h']))
        elif args.revcomp:
            print("Input ", args.seq, "Transcription = ", dna2rna(reverseComplementSeq(args.seq.upper())))
        else:
            print("Input ", args.seq, "Transcription = ", dna2rna(args.seq.upper()))

    elif args.command == 'translation':
        if args.seq == None:
            print("------------------------------------------------------\nError: Invalid input (You do not provide -s or --seq)\n------------------------------------------------------\n")
            exit(parser.parse_args(['translation','-h']))
        elif args.revcomp:
            print("Input ", args.seq, "Translation = ", dna2protein(reverseComplementSeq(args.seq.upper())))
        else:
            print("Input ", args.seq, "Translation = ", dna2protein(args.seq.upper()))

    elif args.command == 'enzTargetsScan':
        if args.seq == None or args.enz == None:
            print("--------------------------------------------------------\nError: Invalid input (You do not provide --seq or --enz)\n--------------------------------------------------------\n")
            exit(parser.parse_args(['enzTargetsScan','-h']))
        elif args.revcomp:
            print("Input ", args.seq, args.enz, "sites = ", enzTargetsScan(reverseComplementSeq(args.seq.upper()), args.enz))
        else:
            print("Input ", args.seq, args.enz, "sites = ", enzTargetsScan(args.seq.upper(), args.enz))

    # print(args.seq, gcContent(args.seq))
    # print(args.seq, enzTargetsScan(args.seq, args.enz))


if __name__ == "__main__":
    # test()
    main()
    