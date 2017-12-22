index = 0
state = [0]

for i in range(1, 2018):
    index += 329
    index %= len(state)

    state = state[:index + 1] + [i] + state[index + 1:]
    index += 1
    index %= len(state)

print(state[state.index(2017) + 1])
