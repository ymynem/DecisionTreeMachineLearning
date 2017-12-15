import monkdata as m
import dtree as d

import random
def partition(data, fraction):
        ldata = list(data)
        random.shuffle(ldata)
        breakPoint = int(len(ldata) * fraction)
        return ldata[:breakPoint], ldata[breakPoint:]

def getBestTree(bestTree, bestTreeError, monkVal):
        while True:
                trees = d.allPruned(bestTree)
                newCandidate = False
                for tree in trees:
                        newError = 1-d.check(tree, monkVal)
                        if newError < bestTreeError:
                                bestTree = tree
                                bestTreeError = newError
                                newCandidate = True
                if not newCandidate:
                        break
        return bestTree, bestTreeError

subsets = []
subsets.append(d.select(m.monk1, m.attributes[4], 1))
subsets.append(d.select(m.monk1, m.attributes[4], 2))
subsets.append(d.select(m.monk1, m.attributes[4], 3))
subsets.append(d.select(m.monk1, m.attributes[4], 4))

print(d.buildTree(m.monk1, m.attributes, 3))

"""for subset in subsets:
        for attri in m.attributes:
                print(d.averageGain(subset, attri))
        print()
"""

t = d.buildTree(m.monk1, m.attributes, 2)
print(t)
#t = d.buildTree(m.monk3, m.attributes)
#print(1 - d.check(t, m.monk3test))

fractions = [0.3,0.4,0.5,0.6,0.7,0.8]
runs = 1000
datasets = [(m.monk1, m.monk1test),(m.monk3,m.monk3test)]

for train, test in datasets:
        for fraction in fractions:
                errorSum = 0
                for i in range(runs):
                        monkTrain, monkVal = partition(train, fraction)
                        bestTree = d.buildTree(monkTrain, m.attributes)
                        bestTreeError = 1-d.check(bestTree, monkVal)
                        bestTree, bestTreeError = getBestTree(bestTree, bestTreeError, monkVal)
                        errorSum += 1-d.check(bestTree, test)
                print("best tree for fraction", fraction, ":",round(errorSum/runs,3))   
        print()

