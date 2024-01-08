# Load the necessary libraries
library(readr)
library(purrr)

# Define the number of smaller files
num_files <- 10  # replace with your desired number of files

# Read the large CSV file
data <- read_csv("osm-osm-roads-2020-na.csv")

# Calculate the number of rows for each smaller file
rows_per_file <- ceiling(nrow(data) / num_files)

# Split the large file into smaller data frames
split_data <- split(data, rep(1:num_files, each = rows_per_file, length.out = nrow(data)))

# Write each smaller data frame to a separate CSV file
iwalk(split_data, ~ write_csv(.x, paste0("osm-map", .y, ".csv")))