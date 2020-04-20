# Print out all of the strings in the following array that represent a number divisible by 3:
# [
#   "five",
#   "twenty six",
#   "nine hundred ninety nine,
#   "twelve",
#   "eighteen",
#   "one hundred one",
#   "fifty two",
#   "forty one",
#   "seventy seven",
#   "six",
#   "twelve",
#   "four",
#   "sixteen"
# ]
# The expected output for the above input is:
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# start by defining a dictionary that changes string numbers to 
# integers (string integers but still integers)

places = {'hundred': 100}
tens_places = {'twenty':20,"thirty":30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90}
ones = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
tens = {'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19}
text_num_dict = {}
dicts = [places,tens_places,ones,tens]
for i in dicts:
    text_num_dict.update(i)

input_list = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]

for item in input_list:
    word_list = item.split()
    output = []
    for word in word_list:
        number = text_num_dict[word]
        if number == 100:
            output[-1] = 100 * output[-1]
        else:
            output.append(number)
    check_number = sum(output)
    if check_number%3 == 0:
        print(item)


# for every item in list
    # word_list =  string.split()
    # for every word in word_list
        # start appending values to an output list
    # str.join outputlist
    # if int(joined output_list) %3 == 0:
        # print item
    # else continue

# output list functionality
# whenever I see "hundred" multiply the previous number in the output list by
# 100 and then replace the previous value. so instead of appending 
# output[-1] = 100 * output[-1]
# then sum up the output array to get my solution.
