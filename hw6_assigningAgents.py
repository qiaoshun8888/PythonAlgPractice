# coding=UTF-8

__author__ = 'johnqiao'

'''
    There are n agents and m tasks (n ≥ m).
    Denote an agent as Ai (i is the agent id from 1 to n) and a task as Tj (j is the task id from 1 to m).
    Each agent has a capability Ai.capability. Each task has a difficulty Tj.difficulty.
    Agent Ai can solve task Tj if Ai ≥ Tj. Each agent can solve at most one task.

    Now your job is to assign the agents so that all tasks can be solved.
    If you assign one task to agent Ai, you need to pay Ai.capability dollars.
    However, you have only a limited budget of k dollars.
    Design an algorithm that does the assignment, given all the agent and task information, along with your budget k.
'''


def assigning_agents(agents, tasks, k):
    agents = sorted(agents)
    tasks = sorted(tasks)

    result = []

    # n   -  current cost
    # ai  -  index of the agents array
    # ti  -  index of the tasks array
    n = ai = ti = 0
    possible = True

    while True:
        if tasks[ti] > agents[ai]:
            ai += 1
        else:
            result.append(agents[ai])

            n += agents[ai]
            ai += 1
            ti += 1

        if ti == len(tasks):
            possible = True
            break
        if ai == len(agents):
            possible = False
            break

    return n <= k and possible, result


if __name__ == '__main__':
    A = [1, 2, 2, 3, 5, 7, 15, 20]
    T = [2, 4, 3, 6, 2]
    k = 20

    is_possible, res = assigning_agents(A, T, k)
    if is_possible:
        print 'Possible'
        print res
    else:
        print 'Impossible Assignment'