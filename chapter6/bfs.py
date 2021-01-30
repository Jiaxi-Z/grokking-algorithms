from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []  # suppose is the one we want to find
graph["jonny"] = []


def person_is_find(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_find(person):
                print("Well done, "+person.upper()+" is the right one!")
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
