import car_maze as cm
import time

env = cm.CarMazeEnv()

#################################################
# Observation space value meanings by list index:
# 0 - up       (values: 0 - road blocked,  1 - road available)
# 1 - down
# 2 - left
# 3 - right
# 4 - ID position of car
# 5 - ID position of gold
# 6 - roads / possible moves of the maze. Tuple of two ID values (from, to)
#
###########################
# Action space values
# 0 - up
# 1 - down
# 2 - left
# 3 - right

#####################################
# You code starts here
#####################################

def get_neighbours( x, y, observation):
    neighbours = []

    # left
    if observation[2]:
        neighbours.append(str(x - 1) + '-' + str(y))
    # down
    if observation[1]:
        neighbours.append(str(x) + '-' + str(y - 1))
    # up
    if observation[0]:
        neighbours.append(str(x) + '-' + str(y + 1))
    # right
    if observation[3]:
        neighbours.append(str(x + 1) + '-' + str(y))
    return neighbours





for i_episode in range(1):

    observation = env.reset()
    path = []
    visited = []
    visited.append(observation[4])
    current = observation[4]

    for t in range(200000):
        env.render()
        print(observation)
        # --------------------------------------------
        # example code
        # --------------------------------------------
        x = int(observation[4].split('-')[0])
        y = int(observation[4].split('-')[1])

        all_used = True
        for neighbour in get_neighbours(x, y, observation):

            if neighbour not in visited:
                current = neighbour
                all_used = False

        if all_used:
            path.pop()
            current = path.pop()

        path.append(current)
        visited.append(current)

        x_new = current.partition("-")[0]
        y_new = current.partition("-")[2]

        # moving
        if int(x_new) > int(x):
            action = 3
        elif int(x_new) < int(x):
            action = 2
        elif int(y_new) > int(y):
            action = 0
        elif int(y_new) < int(y):
            action = 1

        time.sleep(0.1)

        observation, reward, done, info = env.step(action)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print("Reward - " + reward)
            break
        # --------------------------------------------
        # end of example code
        # --------------------------------------------

#####################################
# You code ends here
#####################################


env.close()
