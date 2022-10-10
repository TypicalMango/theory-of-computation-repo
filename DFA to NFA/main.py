def nfa_to_dfa_rec(states, ip, trans, curr, final, fin_states, dfa, trap, all_states):
    temp_dfa = {}
    all_states.add(curr)
    fin = False
    for x in ip:
        string = ""
        for y in curr:
            temp = ''.join((trans[y + x]).split())
            string += temp
            stg = sorted(set(string))
            for i in stg:
                for j in final:
                    if i == j:
                        fin = True
            string = ''.join(str(e) for e in stg)
        while (string.find("%") != -1) and (string != "%"):
            string = string.replace("%", "")
        temp_trans = {curr + x: string}
        dfa.update(temp_trans)
        temp_dfa.update(temp_trans)
        if fin:
            fin_states.add(curr)

    for x in temp_dfa:
        for z in ip:
            if dfa[x] + z == "%":
                trap = True
        flag = True
        keys = dfa.keys()
        for y in keys:
            for z in ip:
                if dfa[x] + z == y:
                    flag = False
                    break
        if flag:
            nfa_to_dfa_rec(states, ip, trans, dfa[x], final, fin_states, dfa, trap, all_states)


def nfa_to_dfa(states, ip, trans, start, final):
    temp_dfa = {}
    all_states = {start}
    dfa = {}
    fin_states = set([])
    trap = False
    for x in ip:
        temp = ''.join((trans[start + x]).split())
        temp_trans = {start + x: temp}
        dfa.update(temp_trans)
        temp_dfa.update(temp_trans)
    for x in temp_dfa:
        if temp_dfa[x] != start:
            nfa_to_dfa_rec(states, ip, trans, dfa[x], final, fin_states, dfa, trap, all_states)
    if trap:
        dfa.update({"%0": "%", "%1": "%"})
    print("-----------------------------------------------------")
    print("all states: ", all_states)
    print("all inputs: ", ip)
    print("transition", dfa)
    print("start state: {", start, "}")
    print("final state: ", fin_states)
    print("-----------------------------------------------------")


states = input("Enter all states separated by spaces: ")
states = states.split()
ip = input("Enter all inputs separated by spaces: ")
ip = ip.split()
trans = {"%0": "%", "%1": "%"}
print("Enter transitions separated by white spaces, use % symbol for null transition: ")

for x in states:
    for y in ip:
        temp = input("(" + x + ", " + y + ") = ")
        temp_trans = {x+y: temp}
        trans.update(temp_trans)
    print()

start = input("Enter start state: ")
final = input("Enter all final states separated by spaces: ")

nfa_to_dfa(states, ip, trans, start, final)
