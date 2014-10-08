from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

def constrainedMatchPair(firstMatch, secondMatch, length):
    return ()
    
def subStringMatchExact(target, key):
    keyLoc = find(target, key)
    locations = ()
    while keyLoc > -1:
        locations = locations + (keyLoc, )
        keyLoc = find(target, key, keyLoc + 1)
            
    return (locations)
        
        
def runPerms():
    target = 1
    key = 0

    while target < 3:
        while key < 4:
            print(str(target) + ' '  + str(key + 10))
            if target == 1:
                if key == 0:
                    print(subStringMatchExact(target1, key10))
                elif key ==1:
                    print(subStringMatchExact(target1, key11))
                elif key ==2:
                    print(subStringMatchExact(target1, key12))
                elif key ==3:
                    print(subStringMatchExact(target1, key13))
            else:
                if key == 0:
                    print(subStringMatchExact(target2, key10))
                elif key ==1:
                    print(subStringMatchExact(target2, key11))
                elif key ==2:
                    print(subStringMatchExact(target2, key12))
                elif key ==3:
                    print(subStringMatchExact(target2, key13))
            key += 1
        key = 0
        target += 1
                

    
        
