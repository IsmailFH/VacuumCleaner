import random
import time


class VacuumCleaner:
    def __init__(self):
        self.location = random.choice(["A","B"])
        self.performance_measure = 0

    def perceive(self, environment):
        location_state = environment[self.location]
        return (self.location, location_state)

    def action(self, location_state):
        if location_state == 'dirty':
            self.performance_measure += 1
            return 'suck'
        else:
            return 'move'

    def run(self, environment, runtime=60, perception_interval=2, evaluation_interval=15):
        print('Starting simulation...')
        cumulative_performance_measure = 0
        start_time = time.time()
        next_evaluation_time = start_time + evaluation_interval
        while time.time() - start_time < runtime:
            # print environment state
            print(f'Environment state: {environment}')

            # perceive environment
            location, location_state = self.perceive(environment)
            print(f'Perception: location={location}, state={location_state}')

            # act on environment
            action = self.action(location_state)
            print(f'Action: {action}')

            # update environment
            if action == 'suck':
                environment[location] = 'clean'
            else:
                other_location = 'B' if location == 'A' else 'A'
                environment[other_location] = random.choice(['clean', 'dirty'])

            # evaluate performance measure
            if time.time() >= next_evaluation_time:
                performance_measure = self.performance_measure
                cumulative_performance_measure += performance_measure
                print(f'Performance measure: {performance_measure}')
                print(f'Cumulative performance measure: {cumulative_performance_measure}')
                next_evaluation_time += evaluation_interval

            # wait for perception interval
            time.sleep(perception_interval)

        print('Simulation complete.')

environment = {'A': random.choice(["dirty","clean"]), 'B':  random.choice(["dirty","clean"])}
vc = VacuumCleaner()
vc.run(environment)
