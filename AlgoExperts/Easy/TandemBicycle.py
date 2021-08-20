"""

  A tandem bicycle is a bicycle that's operated by two people: person A and
  person B. Both people pedal the bicycle, but the person that pedals faster
  dictates the speed of the bicycle. So if person A pedals at a speed of <span>5</span>
  , and person B pedals at a speed of <span>4</span>
  , the tandem
  bicycle moves at a speed of <span>5</span>
  <span>tandemSpeed = max(speedA, speedB)</span>

  You're given two lists of positive integers: one that contains the speeds of
  riders wearing red shirts and one that contains the speeds of riders wearing
  blue shirts. Each rider is represented by a single positive integer, which is
  the speed that they pedal a tandem bicycle at. Both lists have the same
  length, meaning that there are as many red-shirt riders as there are
  blue-shirt riders. Your goal is to pair every rider wearing a red shirt with a
  rider wearing a blue shirt to operate a tandem bicycle.

  Write a function that returns the maximum possible total speed or the minimum
  possible total speed of all of the tandem bicycles being ridden based on an
  input parameter, <span>fastest</span> . If <span>fastest = true</span> , your
  function should return the maximum possible total speed; otherwise it should
  return the minimum total speed.

  "Total speed" is defined as the sum of the speeds of all the tandem bicycles
  being ridden. For example, if there are 4 riders (2 red-shirt riders and 2
  blue-shirt riders) who have speeds of <span>1, 3, 4, 5</span>
  , and if they're
  paired on tandem bicycles as follows:
  <span>[1, 4], [5, 3]</span>
  , then the
  total speed of these tandem bicycles is
  <span>4 + 5 = 9</span>
"""


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    arrayLength = len(redShirtSpeeds)
    totalSpeed = 0
    i = 0
    j = arrayLength - 1
    if fastest:
        while i < arrayLength:
            totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[j])
            i += 1
            j -= 1

    else:
        while i < arrayLength:
            totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
            i += 1
    return totalSpeed
