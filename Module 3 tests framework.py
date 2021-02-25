from selenium import webdriver
import time
import math
import unittest
#first task
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
import os



def test_input_text(expected_result, actual_result):
  result1 = expected_result == actual_result
  assert  result1, f"expected {expected_result}, got {actual_result}"

'''''
def test_substring(full_string, substring):  
    s = substring in full_string
    assert s, f"expected '{substring}' to be substring of '{full_string}'"
def test_0007():
    test_substring("почта  шарик почта", "шарик")
    '''''
def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

    if __name__ == "__main__":
        test_abs1()
        print("All tests passed!")

