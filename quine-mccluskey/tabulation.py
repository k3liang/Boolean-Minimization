# minterm: "1001" --> output: 2
def count_ones(minterm):
    return minterm.count('1')

# n = number of variables
# minterms; eg ["1001", "1111", etc.]
def bucket_sort(n, minterms):
    buckets = [[] for i in range(n+1)]
    for minterm in minterms:
        buckets[count_ones(minterm)].append(minterm)
    return buckets

# can two implicants be merged?
# so, merge them
def merge(m1, m2):
    diff_seen = False
    diff_index = -1
    index = -1
    for a,b in zip(m1, m2):
        index += 1

        # check dash alignment!
        if a == '-' and a != b:
            return ""
        if b == '-' and a != b:
            return ""
        
        if a != b:
            if diff_seen:
                return ""
            diff_seen = True
            diff_index = index
    if not diff_seen:
        return m1
    return m1[:diff_index] + '-' + m1[diff_index + 1:]

def tabulate(n, minterms):
    buckets = bucket_sort(n, minterms)
    merged = set()
    implicants = set(minterms)
    for i in range(n+1, 0, -1):
        # i is the current number of buckets in the column
        new_buckets = [[] for k in range(i - 1)]

        for j in range(len(buckets) - 1):
            for imp in buckets[j]:
                for imp2 in buckets[j+1]:
                    merged_imp = merge(imp, imp2)
                    if merged_imp:
                        if merged_imp not in implicants:
                            new_buckets[j].append(merged_imp)
                            implicants.add(merged_imp)
                        merged.add(imp)
                        merged.add(imp2)

        buckets = new_buckets
                    
    return implicants.difference(merged)

