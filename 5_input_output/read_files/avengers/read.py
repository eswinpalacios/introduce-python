# read
file_movies = open("file_movies.txt", "rt")
file_movies_data = file_movies.read()
print(file_movies_data)
file_movies.close()

# save
file_movies_for_write = open("new_file_movies.txt", "wt")
data_for_file = "Ironman 3"
file_movies_for_write.write(data_for_file)
file_movies_for_write.close()
