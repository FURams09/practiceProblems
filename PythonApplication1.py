#Given a string pattern of 0s, 1s, and ?s (wildcards), generate all 0-1 strings that match this pattern. 
#e.g. 1?00?101 -> [10000101, 10001101, 11000101, 11001101]. 

def stringPermutations(pattern):
    nextQ = pattern.find('?');
    if nextQ < 0:
        return pattern
    nextPattern = stringPermutations(pattern[nextQ + 1:]);
    if nextPattern != '':
        zeroBranch = [(pattern[:nextQ] + '0' + '{0}').format(i) for i in nextPattern];
        oneBranch = [(pattern[:nextQ] + '1' + '{0}').format(i)  for i in nextPattern];
    else:
        zeroBranch = [pattern[:nextQ] + '0' ];
        oneBranch = [pattern[:nextQ] + '1'];
    
    return zeroBranch + oneBranch;
   
#print(stringPermutations('?00?110?'))


def stringPermutationBrute(pattern):
    permQueue = [];
    currentStaticString = '';
    
    for i in range(0, len(pattern) ):
        if (pattern[i] == '0') or (pattern[i] == '1'):
            currentStaticString += pattern[i];
        else:
            newQueue = []
            if len(permQueue) == 0:
                permQueue = ['0', '1'];
            else:
                for j in xrange(len(permQueue)):
                    newQueue.append(permQueue[j] + currentStaticString + '0');
                    newQueue.append(permQueue[j] + currentStaticString + '1');
                currentStaticString = '';
                permQueue = newQueue;
    if currentStaticString != '':
        for j in xrange(len(permQueue)):
                if j % 2 == 0:
                    permQueue[j] += currentStaticString;
                else:
                    permQueue[j] += currentStaticString;
    return permQueue;
print(stringPermutationBrute('?00?110?'))