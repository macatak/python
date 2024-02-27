from streamz import Stream

# Define a simple function to process the data
def process_data(x):
    return x * 2

# Create a Stream object
source_stream = Stream()

# Apply the processing function to the stream
processed_stream = source_stream.map(process_data)

# Define a callback function to print the results
def print_result(x):
    print("Processed Result:", x)

# Subscribe the print_result function to the processed_stream
processed_stream.sink(print_result)

# Emit some data into the source_stream
source_stream.emit(1)
source_stream.emit(2)
source_stream.emit(3)
source_stream.emit(4)
source_stream.emit(5)



'''

import streamz

# Create a stream object from a list of numbers
numbers = [1, 2, 3, 4, 5]
stream = streamz.Stream(numbers)

# Map each value in the stream to its square
squared_values = stream.map(lambda x: x**2)

# Filter out any values that are not divisible by 2
even_values = squared_values.filter(lambda x: x % 2 == 0)

# Print each value in the stream
for value in even_values:
    print(value)

'''

'''from streamz import Stream

# Create a stream
stream = Stream()

# Define a function to square the incoming values
def square(x):
    return x ** 2

# Apply the transformation to the stream
squared_stream = stream.map(square)
print(squared_stream)
# Define another transformation function
def add_one(x):
    return x + 1

# Chain the transformations
transformed_stream = stream.map(square).map(add_one)

print("squared: {}".format(squared_stream))
print("--- : {}".format(stream.emit(1)))
stream.emit(2)
stream.emit(3)

# Define a function to print the incoming values
def print_value(x):
    print(x)

# Subscribe to the stream
transformed_stream.sink(print_value)

'''