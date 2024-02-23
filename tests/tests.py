import sys
sys.path.append('C:/Users/aaggu/mypackage')

from mypackage import myModule

def test_top_n():
    try:
        assert myModule.top_n([8,3,2,7,4],3) == [8,7,4], "assersion failed"
    except AssertionError:
        print(f"assersion failed: given [8,3,2,7,4], expected  [8,7,4] but got {myModule.top_n([8,3,2,7,4],3)}")
    
    try:
        assert myModule.top_n([10,1,12,9,2],2) == [12,10], "assersion failed"
    except AssertionError:
        print(f"assersion failed: given [10,1,12,9,2], expected  [12,10] but got {myModule.top_n([10,1,12,9,2],2)}")

    try:
        assert myModule.top_n([1,2,3,4,5],5) == [5,4,3,2,1], "assersion failed"
    except AssertionError:
        print(f"assersion failed: given [1,2,3,4,5], expected  [5,4,3,2,1] but got {myModule.top_n([1,2,3,4,5],5)}")


        
    
def main():
    test_top_n()


if __name__ == "__main__":
    main()
