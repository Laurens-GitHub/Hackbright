"""Restaurant rating lister."""


# put your code here


def restaurant_ratings(input_file):
    input_file = open(input_file)
    rating_dic = {}
    rating_list = []
    for line in input_file:
        line = line.rstrip()
        words = line.split(":")
        for word in words:
            rating_dic[word] = rating_dic.get(words[0], words[1])
    for items in rating_dic:
        rating_list.append(items)
    rating_list.sort()
    for rating in rating_list:
        print(f'{rating} is rated at {rating_dic[rating]}.')

    rest_input = input("")
restaurant_ratings('scores.txt')
