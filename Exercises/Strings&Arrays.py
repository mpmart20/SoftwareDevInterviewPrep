import unittest

def stringIsUnique(targetStr):
    """
    Implement an algorithm to determine if a string has all unique characters
    """
    pass

def stringIsUniqueInPlace(targetStr):
    """
    Implement an algorithm to determine if a string has all unique characters
    Do not use additional data structures
    """
    pass

def reverseStrInPlace(targetStr):
    """
    Reverse string in place

    """
    pass

def isPermutation(arg1,arg2):
    """
    Given two strings, write a method to decide if one is a permutation of the other
    """
    pass

def replaceSpace(targetStr):
    """
    Write a method to replace all spaces in a string with %20
    You may assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the true length of the string
    Input:"My John Smith  ",13
    Output:"Mr%20John%20Smith"

    """
    pass

def stringCompression(targetStr):
    """
    Implement a method to perform basic string compression using the counts of repeated characters. For example, te string aabccccccaa would become a$2b$1c$6a$2
    """
    pass

def rotateImage(image):
    """
    Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Try this in place --> not sure jsut yet
    """
    pass

def setToZero(matrix):
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its enture row and column are set to 0
    """

    pass


def isSubstring():
    """
    assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write the code to check if s2 is a rotation of s1 using only one call to isSubstring
    waterbottle
    erbottlewat
    """
    pass

class  StringAndArraysTest(unittest.TestCase):

    def test_q1(self):
        target = "abcd"
        self.assertEqual(stringIsUnique(target),True)
        target = "AbC"
        self.assertEqual(stringIsUnique(target),True)
        target = "12345"
        self.assertEqual(stringIsUnique(target),True)
        target = "aabbcc"
        self.assertEqual(stringIsUnique(target),False)
        target = "12355"
        self.assertEqual(stringIsUnique(target),False)
        target = ""
        self.assertEqual(stringIsUnique(target),True)

        target = "abcd"
        self.assertEqual(stringIsUniqueInPlace(target),True)
        target = "AbdC"
        self.assertEqual(stringIsUniqueInPlace(target),True)
        target = "12345"
        self.assertEqual(stringIsUniqueInPlace(target),True)
        target = "aabbcc"
        self.assertEqual(stringIsUniqueInPlace(target),False)
        target = "12355"
        self.assertEqual(stringIsUniqueInPlace(target),False)
        target = ""
        self.assertEqual(stringIsUniqueInPlace(target),True)

    def test_q2(self):
        target = "abc"
        self.assertEqual(reverseStrInPlace(target),"cba")
        target = ""
        self.assertEqual(reverseStrInPlace(target),"")
        target = "AaBbCc"
        self.assertEqual(reverseStrInPlace(target),"cCbBaA")
        target = "12345"
        self.assertEqual(reverseStrInPlace(target),"54321")
        target = "a"
        self.assertEqual(reverseStrInPlace(target),"a")

    def test_q3(self):
        self.assertEqual(isPermutation("abc","abc"),True)
        self.assertEqual(isPermutation("aabbcc","abccba"),True)
        self.assertEqual(isPermutation("",""),True)
        self.assertEqual(isPermutation("12c","c21"),True)
        self.assertEqual(isPermutation("Aa12cC!","!21aAcC"),True)
        self.assertEqual(isPermutation("abc","ac"),False)
        self.assertEqual(isPermutation("aaaaa","AAAA"),False)
        self.assertEqual(isPermutation("a","a"),True)

    def test_q4(self):
        self.assertEqual(replaceSpace("Mr John Smith  "),"Mr%20John%20Smith")

    def test_q5(self):
        self.assertEqual(stringCompression("aabbcc"), "a$2b$2c$2")
        self.assertEqual(stringCompression("AaBbCc"), "A$1a$1B$1b$1C$1c$1")
        self.assertEqual(stringCompression(""),"")
        self.assertEqual(stringCompression(None), None)
        self.assertEqual(stringCompression("112233"), "1$22$23$2")

    def test_q6(self):
        # m = [[1,2,3],[4,5,6],[7,8,9]]
        # n = [[7,4,1],[8,5,2],[9,6,3]]
        # self.assertEqual(rotateImage(m),n)
        # m = [[1,2],[3,4]]
        # n = [[3,1],[4,2]]
        # self.assertEqual(rotateImage(m),n)
        pass

    def test_q7(self):
        m = [[0]]
        n = [[0]]
        self.assertEqual(setToZero(m),n)
        m = [[1]]
        n = [[1]]
        self.assertEqual(setToZero(m),n)
        m = [[0,1],[1,1]]
        n = [[0,0],[0,1]]
        self.assertEqual(setToZero(m),n)
        m = [[1,1,1],[1,0,1],[1,1,1]]
        n = [[1,0,1],[0,0,0],[1,0,1]]
        self.assertEqual(setToZero(m),n)

    def test_q8(self):
        pass
