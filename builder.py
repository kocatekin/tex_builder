import sys
ALPHABET = ["A.","B.","C.","D.","E.","F."]

def main(questions):
    mystack = []
    state = ""
    f = open(questions,"r")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if state == "MCQ":
            mystack.append(line)
        if state == "TF":
            mystack.append(line)
        if state == "ONEWORD":
            mystack.append(line)
        if line == "MCQ":
            state = "MCQ"
        if line == "TF":
            state = "TF"
        if line == "ONEWORD":
            state = "ONEWORD"
        if line == "END":
            if state == "MCQ":
                mcq(mystack)
                mystack = []
                print("\\end{parts}")
                print("")
            if state == "TF":
                tf(mystack)
                mystack = []
                print("\\end{parts}")
                print("")
            if state == "ONEWORD":
                oneword(mystack)
                mystack = []
                print("\\end{parts}")
                print("")
                

def oneword(input):
    #print(input)
    print("\\question Fill in the blanks with words from the list below. There are more in the list than needed, be careful and choose correct words.")
    print("\\begin{parts}")
    for elm in input:
        if elm != "END" and elm != "ONEWORD":
            q = elm.split(":")[0]
            a = elm.split(":")[1]
            print(f"    \\part {q} \\ow[{a}]")
    return

def tf(input):
    #print(input)
    print("\\question True/False Questions. Write T or F in the blank line.")
    print("\\begin{parts}")
    for elm in input: 
        if elm != "END" and elm != "TF":
            q = elm.split(":")[0]
            ans = elm.split(":")[1]
            print(f"  \\part \\tf[{ans}] {q}")
    return

def mcq(input):
    #print(input)
    answers = []
    print("\\question Please answer the multiple questions below. There is only one right answer.")
    print("\\begin{parts}")
    print(f"\\part {input[0:1][0]}")
    print("\\begin{choices}")
    for elm in input[1::]:
        #print(elm)
        if elm == "END":
            return
        if elm[0:2] == "AN":
            #print(elm)
            ans = elm.split(": ")[1] #A B or C etc.
            i = ord(ans) % 65
            for idx, answer in enumerate(answers):
                if idx == i:
                    print(f"    \\CorrectChoice{answer}")
                else:
                    print(f"    \\choice{answer}")
            answers=[]
            print("  \\end{choices}")
            continue
        if elm[0:2] not in ALPHABET:
            print(f"\\part {elm}")
            print("  \\begin{choices}")
        elif elm[0:2] in ["A.","B.","C.","D.","E."]:
            #print(f"    \\choice{elm[2::]}")
            answers.append(elm[2::])

if __name__ == "__main__":
    main(sys.argv[1])
