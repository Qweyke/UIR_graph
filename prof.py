from collections import deque

graph = {
    "you": {"connections": ["Bob", "Claire", "Alice"], "profession": "other"},
    "Bob": {"connections": ["Anuj", "Peggi"], "profession": "other"},
    "Claire": {"connections": ["Tom", "Jonny"], "profession": "other"},
    "Peggi": {"connections": ["Bob"], "profession": "other"},
    "Alise": {"connections": ["Peggi", "Jonny"], "profession": "other"},
    "Jonny": {"connections": ["Alise"], "profession": "other"},
    "Tom": {"connections": [], "profession": "other"},
    "Anuj": {"connections": [], "profession": "other"},
    "Alice": {"connections": [], "profession": "seller"}

}


def check_profession(name, target_profession):
    return graph[name]["profession"] == target_profession


def search_by_profession(start, target_profession):
    search_queue = deque()
    search_queue.append(start)
    searched = set()

    while search_queue:
        person_name = search_queue.popleft()

        if person_name not in searched:
            if check_profession(person_name, target_profession):
                print(person_name + " is a " + target_profession + "!")
                return True
            else:
                search_queue.extend(graph[person_name]["connections"])
                searched.add(person_name)

    return False


search_by_profession("you", "seller")
