from collections import defaultdict # Dictionaries that take a default for missing entries
from itertools import product # will help with a sort of "cartesian product" for {0,1} x {0,1} x ...

# iterative approach
# using itertools product to enumerate cases
def minterms(imp):
    dash_index = [i for i,c in enumerate(imp) if c =='-']

    # base case
    if not dash_index:
        return {imp}
    
    all_minterms = set()
    for case in product('01', repeat=len(dash_index)):
        case_minterm = list(imp)
        for i in range(len(dash_index)):
            case_minterm[dash_index[i]] = case[i]
        all_minterms.add("".join(case_minterm))

    return all_minterms

def createPIT(primes):
    rows = defaultdict(set) # prime implicant is the key
    cols = defaultdict(set) # minterm is the key

    for prime in primes:
        minterms_ = minterms(prime)
        rows[prime].update(minterms_)

        for m in minterms_:
            cols[m].add(prime)

    return (rows,cols)

def essential(rows, cols):
    epi = set()
    for minterm in cols:
        if len(cols[minterm]) == 1:
            epi.update(cols[minterm])

    return epi

def simplify_table(rows, cols, imps):
    covered_minterms = set()
    for imp in imps:
        covered_minterms.update(rows[imp])
        rows.pop(imp)
    for imp in rows:
        rows[imp].difference_update(covered_minterms)
    for m in covered_minterms:
        cols.pop(m)

def elim_dominated_rows(rows, cols):
    imps = [imp for imp in rows.keys()]
    dominated_imps = set()
    for i in range(len(imps)):
        imp1set = rows[imps[i]]
        for j in range(i+1, len(imps)):
            if imp1set.issuperset(rows[imps[j]]):
                dominated_imps.add(imps[j])
            elif imp1set.issubset(rows[imps[j]]):
                dominated_imps.add(imps[i])
                break
    for imp in dominated_imps:
        rows.pop(imp)
    for m in cols:
        cols[m].difference_update(dominated_imps)

def elim_dominating_cols(rows, cols):
    minterms_ = [m for m in cols.keys()]
    dominating_cols = set()
    for i in range(len(minterms_)):
        col1set = cols[minterms_[i]]
        for j in range(i+1, len(minterms_)):
            if col1set.issubset(cols[minterms_[j]]):
                dominating_cols.add(minterms_[j])
            elif col1set.issuperset(cols[minterms_[j]]):
                dominating_cols.add(minterms_[i])
                break
    for m in dominating_cols:
        cols.pop(m)
    for imp in rows:
        rows[imp].difference_update(dominating_cols)

def prune_table(rows, cols):
    minimal_imps = set()
    while True:
        initial_len_rows = len(rows)
        initial_len_cols = len(cols)
        if initial_len_rows == 0 or initial_len_cols == 0:
            break

        # step 1: essentiality and table simplification
        epi = essential(rows, cols)
        minimal_imps.update(epi)
        simplify_table(rows, cols, epi)

        # step 2: row dominance
        elim_dominated_rows(rows, cols)

        # step 3: column dominance
        elim_dominating_cols(rows, cols)

        if len(rows) == initial_len_rows and len(cols) == initial_len_cols:
            break

    return minimal_imps 