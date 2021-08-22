"""

  Write a function that takes in a "special" array and returns its product sum.


  A "special" array is a non-empty array that contains either integers or other
  "special" arrays. The product sum of a "special" array is the sum of its
  elements, where "special" arrays inside it are summed themselves and then
  multiplied by their level of depth.

  The depth of a "special" array is how far nested it is. For instance, the
  depth of
  <span>[]</span>
   is
   <span>1</span>
   ; the depth of the inner array in
  <span>[[]]</span>
   is
   <span>2</span>
   ; the depth of the innermost array in
  <span>[[[]]]</span> is 3


  Therefore, the product sum of
  <span>[x, y]</span> is
  <span>x + y</span>
  ; the
  product sum of
  <span>[x, [y, z]]</span> is
  <span>x + 2 * (y + z)</span>
  ; the
  product sum of
  <span>[x, [y, [z]]]</span>
  is
  <span>x + 2 * (y + 3z)</span>

"""


# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    return productSumHelper(array, 1)


def productSumHelper(array, level):
    runningSum = 0
    for item in array:
        if type(item) is int:
            runningSum += item
        else:
            runningSum += productSumHelper(item, level + 1)

    return runningSum * level