import sys
import time

from tabulation import tabulate
from pit import prune_table, createPIT
from petrick import calc_petricks

def get_minimal_SOP(minterms):
    if len(minterms) == 0:
        return set()
    terms = set()
    n = len(minterms[0])
    rows, cols = createPIT(tabulate(n, minterms))
    terms.update(prune_table(rows,cols))
    if len(rows) > 0 or len(cols) > 0:
        terms.update(calc_petricks(rows,cols))
    
    return terms    

if __name__ == "__main__":
    minterms = []

    for line in sys.stdin:
        bitstring = line.strip()
        if bitstring == '':
            break
        minterms.append(bitstring)
    
    start = time.perf_counter()
    sop_terms = get_minimal_SOP(minterms)
    end = time.perf_counter()
    print(sop_terms)
    print("Time taken for Quine McCluskey: ", end-start)