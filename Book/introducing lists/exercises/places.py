from audioop import reverse


visit_places= ["kivu lake", "akagera national park", "musanze volcanoes", "zanzibar lake"]
print(visit_places)
sort_visit_places = sorted(visit_places)
print(visit_places)
reverse_sorted_visit_places = sorted(sort_visit_places, reverse=True)
print(reverse_sorted_visit_places)
print(visit_places)
visit_places.reverse()
print(visit_places)
visit_places.reverse()
print(visit_places)
visit_places.sort()
print(visit_places)
visit_places.sort(reverse=True)
print(visit_places)