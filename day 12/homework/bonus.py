
read_pages = int(input("put here how much pages you have read: "))
free_time = input("did l had a free time? (True/False): ") 


free_time = free_time.lower() == 'true'


productive = read_pages >= 20 and free_time


if productive:
    print("მოსწავლე იყო productive!")
else:
    print("მოსწავლე არ იყო productive.")