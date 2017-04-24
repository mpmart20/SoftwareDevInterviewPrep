import unittest
import math

def palindrome_pairs(words):

    wordict = {}
    rtn = []
    for x,y in enumerate(words):
        wordict[y] = x
    for num,word in enumerate(words):
        for j in range(len(word)+1):
            #split the word by an indice
            tmp1 = word[:j]
            tmp2 = word[j:]
            #if the anagram complement of our current tmp1 is not ourselves
            #if we find the anagram complement to our tmp1 and tmp2 is a anagra
            if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=num and tmp2 == tmp2[::-1]:
                rtn.append([num,wordict[tmp1[::-1]]])
            #otherwise if the tmp2 complement of our word is in dict and tmp1 is an anagam
            if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]]!=num and tmp1 == tmp1[::-1]:
                rtn.append([wordict[tmp2[::-1]],num])
    return rtn

def AlienDict(words):
    less = []
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                less += a + b,
                break
    chars = set(''.join(words))
    order = []
    while less:
        free = chars - set(zip(*less)[1])
        if not free:
            return ''
        order += free
        less = filter(free.isdisjoint, less)
        chars -= free
    return ''.join(order + list(chars))
    #return alphaOrder(head)

def two_sum(nums, target):
    nums_Dict = {}
    for x in range(0,len(nums)):
        rtn = nums_Dict.get(nums[x])
        if not rtn is None:
            return [rtn,x]
        else:
            nums_Dict[abs(target - nums[x])] = x
    return rtn

def textJustification(words, L):
    """
        [
       "This    is    an",
       "example  of text",
       "justification.  "
        ]
    """
    #format words by adding spaces in between:
    def line_formatter(line,space):
        count = sum(map(lambda x: len(x), line))
        while count != space:
            if len(line) < 2:
                whiteSpace = [" "] * (space-count)
                return line[0] + "".join(whiteSpace)
            for y in range(0,len(line)-1):
                count +=1
                line[y] = line[y] + " "
                if count == space:
                    break
        return "".join(line)

    #### Divides the words into appropriate lines
    lines,curr,count = [],[],0
    for x in words:
        if len(x) + count > L:
            count = len(x) + 1
            lines.append(curr)
            curr = [x]
        else:
            curr.append(x)
            count += len(x) +1
    if lines[-1] != curr:
        lines.append(curr)



    return map(lambda x: line_formatter(x,L),lines)

def legos(n):
    def numways(n):
        if n==0:
            return 1
        elif n < 0:
            return 0
        return numways(n-4) + numways(n-3) + numways(n-2) + numways(n-1)


    def calculateInvalid(n,h,dictT):
        return sum(map(lambda x,y : (y ** h)*math.factorial(n-x+1),dictT.keys(),dictT.values()))
        #sum(map(lambda x,y : (y ** h) * math.factorial(n-x+1),dictT.keys(),dictT.values()))
        #math.factorial(n-(n-1)+1)*(dictT.get(n-1)**h)
        #sum(map(lambda x,y : (y ** h)* math.factorial(n-x+1),dictT.keys(),dictT.values()))

    def factsum(n):
        if n == 0:
            return 0;
        else:
            return math.factorial(n) + factsum(n-1)
    n = 4; h = 4;

    tot = numways(n); totDict = {};



    for x in range(1,n):
        totDict[x] = numways(x)



    print  tot, tot**h, totDict

    return tot**h-calculateInvalid(n,h,totDict)

def longestPath(target):
    """

    Longest path
    Params:
        The name of a file contains at least a . and an extension.
        The name of a directory or sub-directory will not contain a .

    """

    longest, curr_path = 0,None

    #create class to store curr path and its parents/children/level
    class path():
        def __init__(self,name,depth):
            self.name = name
            self.parent = None
            self.children = [] #should be other paths
            self.isFile = "." in name
            if self.parent:
                self.path_len = len(parent.name)+ len(name)
            else:
                self.path_len = len(name)
            self.depth = depth

        def update_parent(self, currPath,longest,curr_path):
            #only updates is we have found a larger path
            if (currPath.path_len + len(self.name)) > self.path_len:
                self.parent = currPath
                self.parent.children.append(self)
                self.path_len = self.parent.path_len + len(self.name)
                if self.path_len > longest and self.isFile:
                    return self.path_len, self
            return longest,curr_path

        def commonDir(self,targ):
            curr = targ
            while not curr.depth == self.depth:
                curr = curr.parent
            return curr.parent

    #parse
    def pathParse(arg):
        "\t\t\t\tfile1.ext --> ['\\file1.ext',4]"
        depth,currName = 0, "/"
        for x in arg.split("\t"):
            if x == "":
                depth += 1
            else:
                currName += x
        if not depth:
            return [arg,depth]
        return [currName, depth]

    #TODO: \n\t --> indicates child; filter out extra \t(depth) --> convert appropriately to just \+path/filename
    myQ = target.split("\n")
    currDepth,last = 0, path(pathParse(myQ[0])[0],0)

    for p in  myQ[1:]:
        parsed =  pathParse(p)
        thisPath = path(parsed[0],parsed[1])
        print "thisPath is: ", thisPath.name, thisPath.depth

        if currDepth < parsed[1]:
            currDepth = parsed[1]
            longest, curr_path = thisPath.update_parent(last,longest,curr_path)
        else:
            currDepth = parsed[1]
            #assign common ancestor as parent
            longest, curr_path = thisPath.update_parent(thisPath.commonDir(last),longest,curr_path)
        last = thisPath

    #prepare rtn to return path
    rtn = ""
    while curr_path:
        rtn = curr_path.name + rtn
        print curr_path.name
        curr_path = curr_path.parent
    return rtn

class myMatrix():

    def __init__(self, contents):
        self.contents = contents
        self.height = len(contents)
        self.width = len(contents[0])

    def update(self, row, column, val):
        self.contents[row][column] = val

    def sumRegion(self, TL,TR,BL,BR):
        rtn = 0
        for y in range(TL, BL+1):
            rtn += sum(self.contents[y][TR:BR+1])
        return rtn

def longestUniqueKString(target, k):
    pass

def fizzBuzz(num):
    """
    fizzbuzz where 3 = foo, 5 = bar, 3/5 = buzz
    """
    rtn = []
    for x in range(1, num+1):
        if x % 3 == 0:
            if x % 5 == 0:
                rtn.append("buzz")
            else:
                rtn.append("foo")
        elif x % 5 == 0:
            rtn.append("bar")
        else:
            rtn.append(x)
    return rtn

def commonalityBtwString(cString):
    """
    commonality between strings
    1) ignore non alphanumeric characters
    2) preserve spaces
    3) keep earlier version
    4) not case sensitive
    5) is contained
    """
    #str.isalnum() -> used to tell if str is alpha numeric
    def conversion(targetStr):
        """
        strips strings down into words while conserving white spaces in between them
        """
        myStr = ""
        lstStr = []
        for x in list(targetStr.lower()):
            if x.isalnum():
                myStr+= x
            if (x == " ") and (myStr != ""):
                lstStr.append(myStr)
                myStr = ""
        if not (myStr == ""):
            lstStr.append(myStr)
        return lstStr

    convertedLst = []   #text stripped down
    for y in cString:
        convertedLst.append(conversion(y))

    ### q2 text analysis ###
    currRtn = []    #args that match our params
    accounted = []  #args that we have ruled out based on params
    for z in range(0,len(convertedLst)):
        curr = z
        if z in accounted:
            continue
        for i in range(z+1, len(convertedLst)):
            ### set([a]) <= set([b]) a is contained in b
            ### checks if curr is contained within a and should be overwritten by b
            if (set(convertedLst[curr]) <= set(convertedLst[i])) and (len(convertedLst[curr])<len(convertedLst[i])):
                curr = i
                accounted.append(i)

            ### b is contained in a and a should overwrite b ###
            elif ((convertedLst[i]) == (convertedLst[curr])):
                accounted.append(i)
        if not curr in currRtn:
            currRtn.append(curr)
    return map(lambda x: cString[x], currRtn)

def employees(inputStr):
    """
    given two employees, return common ancestor
    """
    class employee():
        """
        employee nodes for building tree
        """
        def __init__(self,name):
            self.name = name
            self.manager = None
            self.team = []

        def add_team(self,person):
            self.team.append(person)

        def assign_manager(self,person):
            self.manager = person

    def parseTeams(dirtyStr):

        """
        parses input string into a dictionary of people
        """
        dictofPeople = {}
        for x in dirtyStr:
            manager, teamMember = x.split("->")
            if dictofPeople.get(manager):
                manager = dictofPeople.get(manager)
            else:
                manager = employee(manager)
            if dictofPeople.get(teamMember):
                teamMember = dictofPeople.get(teamMember)
            else:
                teamMember = employee(teamMember)
            manager.add_team(teamMember)
            teamMember.assign_manager(manager)
            dictofPeople[teamMember.name] = teamMember
            dictofPeople[manager.name] = manager
        return dictofPeople

    def findCommonAncestor(employee1, employee2,dictOfR):
        if (employee1.manager is None) or (employee2.manager is None):
            raise ValueError('Both employees must have a manger')
        seen = [employee1.name] #everything we've looked at
        queue = [employee1.manager]  #potential common ancestor
        curr_manager = employee1.manager
        while len(queue) > 0:
            curr = queue.pop()
            seen.append(curr.name)
            if curr.name == employee2:
                return employee2.manager.name
            if curr.team:
                if employee2 in curr.team:
                    return curr_manager.name
                for x in curr.team:
                    if not x.name in seen:
                        queue.insert(0,x)
            if not curr_manager.manager is None:
                curr_manager = curr_manager.manager
                queue.insert(0,curr_manager)
        return curr_manager.name


    p1,p2 = inputStr[-1],inputStr[-2]
    dictOfRelations = parseTeams(inputStr[:-2])
    return findCommonAncestor(dictOfRelations.get(p1),dictOfRelations.get(p2),dictOfRelations)

def longestAbsPath(target):
    """
    find the longest path to a file
    size of the str is how we are measuring
    """
    longest, curr_path = 0,None

    #create class to store curr path and its parents/children/level
    class path():
        def __init__(self,name,depth):
            self.name = name
            self.parent = None
            self.children = [] #should be other paths
            self.isFile = "." in name
            if self.parent:
                self.path_len = len(parent.name)+ len(name)
            else:
                self.path_len = len(name)
            self.depth = depth

        def update_parent(self, currPath,longest,curr_path):
            #only updates is we have found a larger path
            if (currPath.path_len + len(self.name)) > self.path_len:
                self.parent = currPath
                self.parent.children.append(self)
                self.path_len = self.parent.path_len + len(self.name)
                if self.path_len > longest and self.isFile:
                    return self.path_len, self
            return longest,curr_path

        def commonDir(self,targ):
            curr = targ
            while not curr.depth == self.depth:
                curr = curr.parent
            return curr.parent

    #parse
    def pathParse(arg):
        "\t\t\t\tfile1.ext --> ['\\file1.ext',4]"
        depth,currName = 0, "/"
        for x in arg.split("\t"):
            if x == "":
                depth += 1
            else:
                currName += x
        if not depth:
            return [arg,depth]
        return [currName, depth]

    #TODO: \n\t --> indicates child; filter out extra \t(depth) --> convert appropriately to just \+path/filename
    myQ = target.split("\n")
    currDepth,last = 0, path(pathParse(myQ[0])[0],0)

    for p in  myQ[1:]:
        parsed =  pathParse(p)
        thisPath = path(parsed[0],parsed[1])
        print "thisPath is: ", thisPath.name, thisPath.depth

        if currDepth < parsed[1]:
            currDepth = parsed[1]
            longest, curr_path = thisPath.update_parent(last,longest,curr_path)
        else:
            currDepth = parsed[1]
            #assign common ancestor as parent
            longest, curr_path = thisPath.update_parent(thisPath.commonDir(last),longest,curr_path)
        last = thisPath

    #prepare rtn to return path
    rtn = ""
    while curr_path:
        rtn = curr_path.name + rtn
        print curr_path.name
        curr_path = curr_path.parent
    return rtn

def licenseKeyFormat(licenseKey, k):
    """
    evenly distribute the license key of k,
    note that the first part of the key can be =< the length of the other segments
    """
    clean = "".join(licenseKey.split("-"))
    segment = len(clean)
    parts = []
    if segment % k == 0:
        for x in range(0,segment/k):
            parts.append(clean[x*k:(x*k)+k])
    else:
        diff = segment % k
        parts.append(clean[:diff])
        counter = k
        for x in range(0,segment/k):
            parts.append(clean[(x*k)+diff:(x*k)+k+diff])
    return "-".join(parts)

def longestKSubstring(target, k):
    """
    in a string find the longest segment with k unique characters
    """
    p1, p2 = 0,1
    charMap = {target[p1]:p1}
    longestSeg,uniqueChars = "", 1
    while p2 < len(target):
        lastCharLoc = charMap.get(target[p2])
        if target[p1] != target[p2]:
            if uniqueChars < k:
                if not lastCharLoc:
                    uniqueChars += 1
            elif uniqueChars == k:
                if not lastCharLoc or lastCharLoc < p1:
                    if len(target[p1:p2]) > len(longestSeg):
                        longestSeg = target[p1:p2]
                    p1 = charMap.get(target[p1]) + 1
        charMap[target[p2]] = p2
        p2 += 1
    if len(target[p1:p2]) > len(longestSeg):
        longestSeg = target[p1:p2]
    return longestSeg

def rangeSum2DArray(arr,topX,topY,bottomX,bottomY):
    """
    find the sm of elements inside the rectangle defined by the given corners
    """
    rtn = 0
    for x in range(topX,bottomX+1):
        rtn += sum(arr[x][topY:bottomY+1])
    return rtn

def screenFitting(text, rows, cols):
    """
    given a row x cols screen and a sentence represented by a list of non empty words find how many times the given sentence can be fitted on the screen
    """
    pass

def longestConsecutiveSequence(BST):
    """
    Given a binary tree, find the length of the longest consecutive sequence path

    must be from parent to child (aka no traveling upwards)
    """
    def helper(node,currLongest,curr):
        if node == None:
            return currLongest

        if not node.parent:
            curr += 1
        elif node.parent.val == node.val - 1:
            curr += 1
        if curr > currLongest:
            currLongest = curr
        return max(helper(node.left,currLongest,curr),helper(node.right, currLongest,curr))

    return helper(BST, 0 , 0)

def wordSquares(words):
    """
    Given a set of words(without duplicates), find all word squares you can build from them

    a sequence of words forms a valid word square if the kth row and column read the exact same string, where 0<= k< max(numRows, numCols)

    params:
        1 < num words <1001
        all words have the exact same length
        word length is at least 1 and at most 5

    """
    pass

from collections import deque

class zigzagIterator():
    """
    given n 1D vectors, create an iterator to return their elements alternately
    """
    def __init__(self, arrays):
        self.content = [deque(arr) for arr in arrays]
        self.curr = 0


    def next(self):
        pointer1 = None
        print self.curr
        while True:
            print self.curr
            currArr = self.content[self.curr]
            if currArr:
                if self.curr < len(self.content)-1:
                    self.curr += 1
                else:
                    self.curr = 0
                return currArr.popleft()
            else:
                if pointer1 == None:
                    pointer1 = self.curr
                elif self.curr == pointer1:
                    return None
                if self.curr < len(self.content)-1:
                    self.curr += 1
                else:
                    self.curr = 0

def bombEnemy(gameBoard):
    """
    Given a 2d grid, each cell is either a wall 'W', an enemy 'E', or empty '0', return the max number of enemies you can kill using one bomb

    The bomb kills all the enemies in the same row and cloumn from the planted point until it hits the wall since the wall is too string to be destroyed

    Note that you can only put the bomb at an empty cell
    """
    pass


def textJustification(words,L):

    def line_formatter(line,space):
        #gets me the current line size
        count = sum(map(lambda x: len(x), line))
        #while my line size is not == my L
        while count != space:
            if len(line) < 2:
                whiteSpace = [" "] * (space-count)
                return line[0] + "".join(whiteSpace)
            for y in range(0,len(line)-1):
                count +=1
                line[y] = line[y] + " "
                if count == space:
                    break
        return "".join(line)

    #### Divides the words into appropriate lines
    lines,curr,count = [],[],0
    for x in words:
        if len(x) + count > L:
            count = len(x) + 1
            lines.append(curr)
            curr = [x]
        else:
            curr.append(x)
            count += len(x) +1
    if lines[-1] != curr:
        lines.append(curr)

    return map(lambda x: line_formatter(x,L),lines)

def uniqueElement(arr1,arr2):
    unique,norm = None,None
    if len(arr1) < len(arr2):
        unique,norm = arr2,arr1
    else:
        unique,norm = arr1,arr2
    dictN = dict(map(lambda x: (x, True),norm))
    for x in unique:
        if not dictN.get(x):
            return x
    raise ValueError("ValueError: Malformed Arrays")

def maxNums(arr,num):

    def insertNum(arrCur,curr):
        #delete smallest element
        #[a,b,c,d,e,f,g]
        count = len(arrCur)/2
        while True:
            if curr == arrCur[count] or curr == arrCur[count-1] or ((curr >arrCur[count]) and (count <= 0)) or (curr > arrCur[count] and (curr < arrCur[count-1])):
                arrCur.insert(count,curr)
                return arrCur[:-1]
            elif curr < arrCur[count]:
                count = count + (count/2)
                print("hmm")
            else:
                count = count - (count/2)
                if count == 1:
                    count = 0

                print("lol")

            print "count",count,count/2,curr, arrCur


    runningMax = sorted(arr[:num])[::-1]
    for element in arr[num:]:
        small = runningMax[-1]
        print small
        print "runningMax", runningMax
        if element > small:
            runningMax = insertNum(runningMax,element)
    return runningMax


    pass

def uniqueInt(arr1,arr2):
    return abs(sum(arr1)-sum(arr2))



class interviewTest(unittest.TestCase):

    def test_palindrome(self):
        words = ["bat", "tab", "cat"]
        self.assertEqual(palindrome_pairs(words), [[0, 1], [1, 0]])
        words = ["abcd", "dcba", "lls", "s", "sssll"]
        #self.assertEqual(palindrome_pairs(words), [[0, 1], [1, 0], [3, 2], [2, 4]])

    def test_alien(self):
        #self.assertEqual(AlienDict(["wrt","wrf","er","ett","rftt"]), "werft")
        pass

    def test_twoSum(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(two_sum(nums,target), [0, 1])

    def test_textJustification(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        L = 16
        self.assertEqual(textJustification(words,L), ["This    is    an","example  of text","justification.  "])

    def test_Legos(self):
        self.assertEqual(legos(4),3375)

    def test_LongestFilePath(self):
        arg1 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        target = "dir/subdir2/subsubdir2/file2.ext"
        self.assertEqual(q1(arg1), target)

    def test_MatrixRegion(self):
        content = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],[1, 0, 3, 0, 5]]
        matrix = myMatrix(content)
        self.assertEqual(matrix.sumRegion(2, 1, 4, 3), 8)
        matrix.update(3, 2, 2)
        self.assertEqual(matrix.sumRegion(2, 1, 4, 3), 10)

    def test_longestUniqueKString(self):
        pass

    def test_q1(self):
        self.assertEqual(q1(15), [1,2,"foo",4,"bar","foo",7,8,"foo","bar",11,"foo",13,14,"buzz"])
        self.assertEqual(q1(2), [1,2])

    def test_q2(self):
        self.assertEqual(q2(["computer  science is bomb!", "computer science is bomb", "computer science is bomb though!","computer-science-is-dope"]), ["computer science is bomb though!","computer-science-is-dope"])

        self.assertEqual(q2(["computer science is bomb!", "computer science is bomb","computer-science-is-dope"]), ["computer science is bomb!","computer-science-is-dope"])

        self.assertEqual(q2(["computer      science is bomb!", "computer science is bomb","computer-science-is-dope"]), ["computer      science is bomb!","computer-science-is-dope"])

        self.assertEqual(q2(["computer science is bomb!", "computer science        is bomb","computer-science-is-dope"]), ["computer science is bomb!","computer-science-is-dope"])

    def test_q3(self):
        self.assertEqual(q3(["Andrew->Jon", "Andrew->Will", "Jon", "Will"]), "Andrew")
        self.assertEqual(q3(["Andrew->Jon", "Andrew->Will", "Jack->Andrew", "Jon", "Andrew"]), "Jack")
        self.assertEqual(q3(["Andrew->Jon", "Andrew->Will", "Jack->Andrew","Jack->Lauren","Lauren->Marc","Jon", "Marc"]), "Jack")
        self.assertEqual(q3(["Andrew->Jon", "Jon->Will", "Jon", "Will"]), "Andrew")
    def test_q1(self):
        path = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        sol = "dir/subdir2/subsubdir2/file2.ext"
        self.assertEqual(longestAbsPath(path),sol)

    #finshed
    def test_q2(self):
        val = "2-4A0R7-4K"
        k  = 4
        output = "24A0-R74K"

        self.assertEqual(licenseKeyFormat(val, k), output)

        val = "2-4A0R7-4K"
        k = 3
        output = "24-A0R-74K"

        self.assertEqual(licenseKeyFormat(val, k), output)

    #finished
    def test_q3(self):
        val = "eceba"
        k = 2
        out = "ece"
        self.assertEqual(longestKSubstring(val,k), out)

    #finished
    def test_q4(self):
        matrix = [
          [3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
        ]
        self.assertEqual(rangeSum2DArray(matrix, 2,1,4,3), 8)
        matrix[3][2] = 2
        self.assertEqual(rangeSum2DArray(matrix, 2,1,4,3), 10)

    def test_q5(self):
        sentence = ["hello", "world"]
        rows = 2
        cols = 8
        self.assertEqual(screenFitting(sentence, rows, cols),1)

        sentence = ["a", "bcd", "e"]
        rows = 3
        cols = 6
        self.assertEqual(screenFitting(sentence, rows, cols),2)

    #finsished
    def test_q6(self):
        class BST():
            def __init__(self, value):
                self.val = value
                self.right = None
                self.left = None
                self.parent = None

            def update_child(self,key, node):
                if key == "R":
                    self.right = node
                else:
                    self.left = node
                node.parent = self


        root = BST(1)
        r = BST(3)
        l = BST(2)
        root.update_child("R",r)
        root.right.update_child("L",l)
        root.right.update_child("R",BST(4))
        root.right.right.update_child("R",BST(5))
        self.assertEqual(longestConsecutiveSequence(root), 3)

    def test_q7(self):
        words = ["area","lead","wall","lady","ball"]
        sol = [
          [ "wall",
            "area",
            "lead",
            "lady"
          ],
          [ "ball",
            "area",
            "lead",
            "lady"
          ]
        ]
        self.assertEqual(wordSquares(words), sol)

        words = ["abat","baba","atan","atal"]
        sol = [
          [ "baba",
            "abat",
            "baba",
            "atan"
          ],
          [ "baba",
            "abat",
            "baba",
            "atal"
          ]
        ]
        self.assertEqual(wordSquares(words),sol)

    #finished
    def test_q8(self):
        v1,v2,v3 = [1,2,3],[4,5,6,7],[8,9]
        myI = zigzagIterator([v1,v2,v3])
        nxt = myI.next()
        rtn = []
        while nxt:
            rtn.append(nxt)
            nxt = myI.next()
            print(nxt)
        self.assertEqual(rtn, [1,4,8,2,5,9,3,6,7])

    def test_q9(self):
        matrix = [[0,"E",0,0],["E",0,"W","E"],[0,"E",0,0]]
        self.assertEqual(bombEnemy(matrix),3)



def test_justify(self):
    """
    Write a function that justifies a string given the maximum number of characters per line.
    """

    words = ["This", "is", "an", "example", "of", "text", "justification."]
    L = 16
    self.assertEqual(textJustification(words,L), ["This    is    an","example  of text","justification.  "])

def test_rotationCount(self):
    """
    Knowing that you start off with a sorted array of numbers which you don't know what the content is, that array is rotated an unknown number of times, and you end up with another array. Find out how many times you have to rotate it back to put it back like how it was.
    """

    pass

def test_uniqueElement(self):
    """
    You have 2 unsorted arrays of integers that only differ by one element. Find that element in the most efficient way.
    """
    arr1 = [1,2,3,4,5,6,7,8,9,10]
    arr2 = [10,2,3,4,1,32,5,6,7,8,9]
    self.assertEqual(uniqueElement(arr1,arr2),32)

def test_maxNums(self):
    """
    Find the max k elements in an unsorted array.
    """
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    arr = arr[::-1] + arr
    num = 5
    self.assertEqual(maxNums(arr, num),[13,13,12,12,11])
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    arr = arr + arr[::-1]
    num = 4
    self.assertEqual(maxNums(arr, num),[13,13,12,12])

def test_uniqueInt(self):
    """
    Given two lists of integers that are exactly the same except that one of them has one extra element added, find the added element
    """
    arr1 = [1,2,3,4,5,6,7,8,9,10]
    arr2 = [10,2,3,4,1,32,5,6,7,8,9]
    self.assertEqual(uniqueInt(arr1,arr2),32)

def test_wordCount(self):
    """
    Write a program that reads a file and counts the number of times each word in the file appears and at which lines.
    """
    pass
