"""

  You're given a non-empty array of positive integers representing the amounts
  of time that specific queries take to execute. Only one query can be executed
  at a time, but the queries can be executed in any order.

  A query's <b>waiting time</b>  is defined as the amount of time that it must
  wait before its execution starts. In other words, if a query is executed
  second, then its waiting time is the duration of the first query; if a query
  is executed third, then its waiting time is the sum of the durations of the
  first two queries.

"""


def minimumWaitingTime(queries):
    queries.sort()
    totalSum = 0
    runningSum = 0
    for i in range(len(queries) - 1):
        runningSum += queries[i]
        totalSum += runningSum
    return totalSum
