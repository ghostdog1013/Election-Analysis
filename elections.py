# Name: Yilun Liu, Katrina Li
# Course Instructor: Aaron Bauer
# Course Name: CS111 Intro to Computer Science
# HW3 Data Analysis regarding voting
# Date: 2019/10/12





# Opening the file and reading the information
data_file = open("district_overall_2018.csv")
first_line = data_file.readline()                                               # returns a string of the next line in the file (in this case the first)
data_lines = data_file.readlines()                                              # returns a list of all remaining lines in the file
data_file.close()                                                               # you should always close a file when you're done with it

for i in range(len(data_lines)):
    data_lines[i] = data_lines[i].split(",")
# Finish reading the csv file and formatting it.









#Question 1
out_file = open("report.txt","w")
candidates = []
for line in data_lines:
    if line[1] == "Minnesota" and line[7] == "District 2" and line[10] != "NA":
       candidates.append(line[10])                                              # append adds an element to the end of a list

out_file.write("\nQ1\n")
out_file.write("The following candidates ran to represent Northfield in the House in 2018:\n")
for c in candidates:
    out_file.write(c + "\n")
out_file.write("\n")                                                            # add a blank line to separate this from the answer to the next question
#Question 1 finished






# Question2
out_file.write("\nQ2" + "\n")
current_state_rep = 0
state_and_rep = []
current_state = "Alabama"
index = 0
for line in data_lines:
    index = index + 1
    if line[1] == current_state:
        current_state_rep = current_state_rep + 1                               # Create an empty list called state_and_rep and append every state with
        if index == len(data_lines):                                            # its corresponding number of representatives. Then, loop over the list
            state_and_rep.append(current_state + " " + str(current_state_rep))  # to write it to the txt file.
    else:
        state_and_rep.append(current_state + " " + str(current_state_rep))

        current_state = line[1]
        current_state_rep = 1


out_file.write("The number of representatives from each state:\n")
for c in state_and_rep:
    out_file.write(c + "\n")
#Question 2 finished








# Question 3/4
out_file.write("\nQ3" + "\n")
def get_state(line):
    return line[1]

def get_district(line):
    return line[7]

def get_vote(line):
    return (line[14])

def get_state_district(line):
    return (line[1] + " " + line[7])                                            #   First extract the candidate votes from the House race in 2018.

state_districts = []

for line in data_lines:
    if get_state_district(line) not in state_districts:
        state_districts.append(get_state(line) + " " + get_district(line))


max_diff = 1
min_diff = 999999
for state_district in state_districts:
    vote = []
    for line in data_lines:
        if state_district == get_state_district(line):
            vote.append(int(get_vote(line)))

        vote_sorted = sorted(vote)
        vote_sorted.append(state_district)                                      # Append the corresponding name of the district so that it is easier later for print out
                                                                                # print(vote_sorted)
    length = len(vote_sorted)
    possible_max_diff = vote_sorted[length-2] - vote_sorted[0]
    if length != 2:
        possible_max_diff = vote_sorted[length-2] - vote_sorted[length-3]
    else:
        possible_max_diff = 1
    if length != 2:
        possible_min_diff = vote_sorted[length-2] - vote_sorted[length-3]       # The conditionals serve to extract the maximum and minumum difference between districts.
    else:                                                                       # The max_diff is between the most voted candidate and the least one, whereas the min_diff
        possible_min_diff = 999999                                              # is between the first and second voted candidates.
    if possible_max_diff > max_diff:
        max_diff = possible_max_diff
        max_state_district = state_district
    if possible_min_diff < min_diff:
        min_diff = possible_min_diff
        min_state_district = state_district
out_file.write("The closest House race is " + min_state_district + " with " + str(min_diff) + " votes " + "\n")
out_file.write("\nQ4\n")
out_file.write("The most lopsided House race is " + max_state_district + " with " + str(max_diff) + " votes " + "\n")
#Question 3/4 finished








#Question 5
out_file.write("\nQ5" + "\n" + "The following Houses are competitive:" + "\n\n")
def get_total_vote(line):
    return (line[15])

                                                                # to keep track of the number of competitve Houses

state_district_vote = []
sdv_line =[]
count = 0
#just_votes = []
for line in data_lines:
    if get_state_district(line) not in sdv_line:
        sdv_line = []
        sdv_line.append(get_state_district(line))
        sdv_line.append(get_total_vote(line))
        state_district_vote.append(sdv_line)
    if get_state_district(line) in sdv_line:
        sdv_line.append(get_vote(line))

print(state_district_vote)


print(state_district_vote)
for line in state_district_vote:
    just_votes =[]

    for l in range(1,len(line)):
        just_votes.append(int(line[l]))
    just_votes = sorted(just_votes)


    print(just_votes)
    #     state_district_vote(line) = sorted(line(1:len(line)))
    if len(just_votes) > 2:
        margin = just_votes[-2] - just_votes[-3]
    else:
        margin = 9999999
    if (10 * margin) < int(just_votes[-1]):
        out_file.write(line[0] +"\n")
        count = count + 1
out_file.write("\n \n number of competitive houses: " + str(count))
    #print(state_district_vote)









# Question 6

out_file.write("\nQ6")
data_file1 = open("state_overall_2018.csv")
first_line1 = data_file1.readline()                                             # returns a string of the next line in the file (in this case the first)
data_lines1 = data_file1.readlines()                                            # returns a list of all remaining lines in the file
data_file1.close()                                                              # you should always close a file when you're done with it

count = 0

for i in range(len(data_lines1)):
    data_lines1[i] = data_lines1[i].split(",")


for line in data_lines1:
    if line[1] == "Minnesota" and line[7] == "statewide" and line[10] != "NA":                       # The conditionals make sure that counts are within Minnesota, statewide, and in case
        count = count + 1                                                       # if a candidate double runs, we count him twice.
        if "&" in line[6]:
            count = count + 1

#print(count)
out_file.write("\nThe number of statewide candidates running in Minnesota in 2018 was " + str(count) + ".\n")

# Question 6 finished










# Question 7

count1 = 0
office = []
for line in data_lines1:
    if line[1]== "Minnesota" and line[12] == "TRUE":
        possible_count = int(line[14])
        possible_office = line[6]                                               # We use an empty list and an index starting at zero to trace every write-in voter.
        if count1 < possible_count:                                             # If a write-in voter receive more votes than the prior one, the office will replace
            count1 = possible_count                                             # the prior one with the current one.
            office = possible_office                                            # The "office" variable will be printed to indicate which write-in voter receive the highest votes.

#print(office, count1)

out_file.write("\nQ7\n")
out_file.write("The Minnesota election with the most write-in votes comes from " + office + " with " + str(count1) + " votes.")

# Question 7 finished











# Question 8
def str_to_bool(s):
    if s == "TRUE":
        return True
    elif s == "FALSE":
        return False
def is_contest(office):
    write_in = []
    contest = True
    for line in data_lines1:
        if line[1] == "Minnesota" and office == line[6]:
            write_in.append(str_to_bool(line[12]))
    for b in write_in:
        if b == True:
            del write_in[b]                                                      # we deleted one False element so that we can use "and" to figure out if there are more "False" in write_in
            break
    for c in write_in:                                                           # c and the increment variable contest return True only when both are true.
        contest = contest and c                                                  # if there is only one False element in write_in, is_contest returns "uncontested"
    if contest == True:                                                          # otherwise this function returns "contested"
        return "uncontested"
    elif contest == False:
        return "contested"

office_and_vote = []
office8 = []
uncontested_num = 0
uncontested_total = 0
contested_num = 0
contested_total = 0
vote8 = 0
for line in data_lines1:

    if line[1] == "Minnesota" and line[7] == "statewide":
        if line[6] not in office8:
            # office8 = line[6]
            office8.append(line[6])
            if is_contest(line[6]) == "contested":
                contested_total = contested_total + int(line[15])
                contested_num = contested_num + 1
            elif is_contest(line[6]) == "uncontested":
                uncontested_total = uncontested_total + int(line[15])
                uncontested_num = uncontested_num + 1
                                                                                #elif line[6] == office8:
                                                                                # print(contested_total)
                                                                                # print(contested_num)
                                                                                # print(uncontested_total)
contested_average = contested_total / contested_num
uncontested_average = uncontested_total / uncontested_num


out_file.write("\n\nQ8\n")
out_file.write("The average total votes for contested statewide elections in Minnesota is " + str(round(contested_average,2)) + "\n")
out_file.write("The average total votes for uncontested statewide elections in Minnesota is " + str(round(uncontested_average,2)))

# Close the file
out_file.close()
