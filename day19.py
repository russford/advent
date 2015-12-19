import re

with open("day19.txt", "r") as f:
    replacements = [d.strip('\n').split(" => ") for d in f.readlines()]

input_molecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

mol_in = set([r[0] for r in replacements])
mol_out = set([r[1] for r in replacements])


def make_subs (input_molecule):
    outputs = []
    for r in replacements:
        for m in re.finditer(r[0], input_molecule):
            output_molecule = input_molecule[:m.start()] + r[1] + input_molecule[m.end():]
            outputs.append(output_molecule)
    return list(set(outputs))

print (len(make_subs(input_molecule)))

mol = input_molecule
repl_order = sorted(replacements, key=lambda e: len(e[1]), reverse=True)
len1 = 0
subs = 0
while len1 != len(mol):
    len1 = len(mol)
    for r in repl_order:
        while r[1] in mol:
            n = mol.index(r[1])
            mol = mol[:n] + r[0] + mol[n+len(r[1]):]
            print ("got sub {} => {}; len now {}".format(r[0], r[1], len(mol)))
            subs += 1
    print (len1-len(mol))
print (mol, subs)
