from itertools import product
# this import is the key to Petrick's
# the product function is a cartesian product that will
# allow us to do distributivity of POS    

def calc_petricks(rows, cols):
    pos_terms = []
    for m in cols:
        if len(cols[m]) > 0:
            pos_terms.append(cols[m])
    if len(pos_terms) == 0:
        return set()

    # cartesian product
    distributed = product(*pos_terms)
    min_length = len(cols)+1
    best_imps = set()

    for sop_term in distributed:
        sop_term = set(sop_term) # idempotency
        if len(sop_term) < min_length:
            min_length = len(sop_term)
            best_imps = sop_term

    return best_imps