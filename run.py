import itertools
from ahpy_functions import ahpy
from table import val


def m(elements, judgments):
    return dict(zip(elements, judgments))
 

cri = ('Opportunity', 'Salary', 'Reputation', 'Flexibility')
c_cri = list(itertools.combinations(cri, 2))
cri_val=(3, 7, 3, 9, 1, 1 / 7)
criteria = ahpy.Compare('Criteria', m(c_cri, cri_val), 3)
print("Criteria table")
val(cri,cri_val)

alt = ('Company A', 'Company B', 'Company C', 'Company D', 'Company E', 'Company F')
pairs = list(itertools.combinations(alt, 2))

opportunities = ('Salary Potential', 'Top Level Position', 'Training', 'Overseas')
opp_val= (2, 5, 3, 2, 2, .5)
c_pairs = list(itertools.combinations(opportunities, 2))
opportunity = ahpy.Compare('Opportunity', m(c_pairs, opp_val), precision=3)
print("Opportunity table")
val(opportunities,opp_val)


## opportinitiess tables
salary_m = (9, 9, 1, 0.5, 5, 1, 1 / 9, 1 / 9, 1 / 7, 1 / 9, 1 / 9, 1 / 7, 1 / 2, 5, 6)
salary_p = ahpy.Compare('Salary Potential', m(pairs, salary_m), 3)
print("Salary Potential table")
val(alt,salary_m)

top_level_position_m = (1/1.13, 1.41, 1.15, 1.24, 1.19, 1.59, 1.3, 1.4, 1.35, 1/1.23, 1/1.14, 1/1.18, 1.08, 1.04, 1/1.04)
#top_level_position_m = (31, 35, 22, 27, 25, 26)
top_level_position = ahpy.Compare('Top Level Position', m(pairs, top_level_position_m), 3)
#top_level_position = ahpy.Compare('Top Level Position', m(alt, top_level_position_m), 3)
print("Top Level Position table")
val(alt,top_level_position_m)

overseas_m = (3, 4, 1 / 2, 2, 2, 2, 1 / 5, 1, 1, 1 / 6, 1 / 2, 1 / 2, 4, 4, 1)
#overseas_m = (0.52, 0.46, 0.44, 0.55, 0.48, 0.48)
overseas = ahpy.Compare('Overseas', m(pairs, overseas_m), 3)
#overseas = ahpy.Compare('Overseas', m(alt, overseas_m), 3)
print("Overseas table")
val(alt,overseas_m)

training_m = (1.5, 4, 4, 4, 5, 4, 4, 4, 5, 1, 1.2, 1, 1, 3, 2)
training = ahpy.Compare('Training', m(pairs, training_m), 3)
print("Training table")
val(alt,training_m)


#--------------------------------------------------------
# for salaryyy
salary_m = (1, 5, 7, 9, 1 / 3, 5, 7, 9, 1 / 3, 2, 9, 1 / 8, 2, 1 / 8, 1 / 9)
salary = ahpy.Compare('Salary', m(pairs, salary_m), 3)
print("Salary table")
val(alt,salary_m)
#--------------------------------------------------------
# for reputation
reputation_m = (1, 7, 5, 9, 6, 7, 5, 9, 6, 1 / 6, 3, 1 / 3, 7, 5, 1 / 5)
reputation = ahpy.Compare('Reputation', m(pairs, reputation_m), 3)
print("Reputation table")
val(alt,reputation_m)
#--------------------------------------------------------
# for flexibility
flexibility = ahpy.Compare('Flexibility', {('Time', 'Location'): 0.2})

# location
flexibility_loc_m = (1, 1 / 2, 1, 3, 1 / 2, 1 / 2, 1, 3, 1 / 2, 2, 6, 1, 3, 1 / 2, 1 / 6)
#flexibility_loc_m = (5, 5, 8, 5, 4, 8)
flexibility_loc = ahpy.Compare('Location', m(pairs, flexibility_loc_m), 3)
#flexibility_loc = ahpy.Compare('Location', m(alt, flexibility_loc_m), 3)
print("Location table")
val(alt,flexibility_loc_m)
#------------------------------------
# time
flexibility_time_m = (1, 1 / 2, 1 / 2, 1 / 2, 1 / 3, 1 / 2, 1 / 2, 1 / 2, 1 / 3, 1, 1, 1 / 2, 1, 1 / 2, 1 / 2)
#flexibility_time_m = (14, 14, 87.6, 72.9, 74.6, 147.4)
flexibility_time = ahpy.Compare('Time', m(pairs, flexibility_time_m), precision=3)
#flexibility_time = ahpy.Compare('Time', m(alt, flexibility_time_m), precision=3)
print("Time table")
val(alt,flexibility_time_m)


opportunity.add_children([salary_p, top_level_position, training, overseas])
flexibility.add_children([flexibility_time, flexibility_loc])
criteria.add_children([opportunity, salary, reputation, flexibility])

# print(criteria.target_weights)
# print(criteria.consistency_ratio)
report = criteria.report(show=True, verbose=True)
print(report)



