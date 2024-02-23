import copy
def top_n(items_l,n):
    """ returns the top n items of a list in descending order 
    Args:
        items (array): list or array-like object
        n (int): num of items to return

    Return:
        array: top n items, in descending order 
    
    """
    items = copy.deepcopy(items_l)
    top_n_list = []
    for i in range(n):
        current_max = max(items)
        top_n_list.append(current_max)
        items.remove(current_max)
    return  top_n_list[::-1]


def main():
    items = [99,50,88,40,77,66,90,11,22,90,33,44,80,55]
    print(top_n(items,5))

if __name__ == "__main__":
    main()