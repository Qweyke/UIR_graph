from collections import deque

graph = {
    "you": ["Bob", "Claire", "Alice"],
    "Bob": ["Anuj", "Peggi"],
    "Claire": ["Tom, Jonny"],
    "Peggi": ["Bob"],
    "Alise": ["Peggi"],
    "Jonny": ["Alise"],
    "Tom": ["Tom"],
    "Tom": [],
}


def check(name):
    return name[-1] == "e"


def search(name):
    search_queue = deque()
    search_queue.extend(graph[name])
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if check(person):
                print(person + " продавец манго!")
                return True
            else:
                search_queue.extend(graph[person])
                searched.append(person)

    return False


search("you")
