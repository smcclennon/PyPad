# PyPad
# smcclennon.github.io

import random, string


def random_string(max_length):
    # Decide how long the string should be
    length = random.randint(1, max_length)
    # Return final string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


# Generate sample test data for testing the padding function
# length = how many lines of data to produce
# string_length = maximum length generated strings in test data should be (default: 20)
def test_data(length, string_length=20):
    # Store generated columns of data in this variable
    """
    data = [
        [  # Column 1 of data, for example incrementing numbers
            "1.", "2.", "3"
        ],
        [  # Column 2 of data, for example music genres
            "EDM", "Jazz", "Rock"
        ],
        [ # Column 3 of data, for example a border character
            "|", "|", "|"
        ],
        [ # Column 4 of data, for example links to playlists for the music genres
            "playlist.com/EDM", "playlist.com/Jazz", "playlist.com/Rock"
        ]
    ]
    """
    data = [[]]
    for i in range(length):
        data[0].append(f'{i}.')  # Example: "1."

    # Create new column and add random strings to it
    data.append([])
    for _ in range(length):
        data[1].append(random_string(string_length))  # Example: "FSjxRamuYvws"

    # Create new column and add decorative separators
    data.append([])
    for _ in range(length):
        data[2].append('|')

    # Create new column and add more random strings
    data.append([])
    for _ in range(length):
        data[3].append(random_string(string_length))  # Example: "FSjxRamuYvws"

    return data

# Pad a list of columns
# Parses the same format output by test_data()
# column_list = unpadded list
# spacing = spaces to add between columns after padding
# pad_char = optionally substitute spaces for a different padding character
def pad(column_list, spacing=1, pad_char=' '):
    # List to insert padded columns and values in to
    padded_list = []
    # Iterate through each column in the list
    for index, column in enumerate(column_list):
        # Determine the longest value in the list
        longest_value = max(column, key=len)
        # Get the length of that longest value
        longest_value_len = len(longest_value)

        # Initialise a 2nd dimension (creating a column) so we can insert padded column values in to it
        padded_list.append([])
        # Iterate through each unpadded value in the column
        for item in column:
            # Take in to account extra spacing for the padding size
            pad_size = longest_value_len + spacing
            # Pad the value with "ljust", using the correct pad size and pad character
            padded_item = item.ljust(pad_size, pad_char)
            # Insert the padded item in to the current column in the parent for loop
            padded_list[index].append(padded_item)

    # Return the padded list in the same format as the unpadded list input
    return padded_list


# Parse the 2d list structure for columns and output/print data
# column_list = multi-column list
def output_data(column_list):
    # Get the length of the first column in the list
    # (All columns should be the same size)
    length = len(column_list[0])
    # Increment through each number from 0 to "length"
    for item in range(length):
        # For each column in column_list
        for column in column_list:
            # Print the value at index "item", and do not line-break
            # This is used to iterate through each column, printing
            # the same index in each column, on the same line
            # TLDR: Parse each column at the same index to print a row of related content/data
            print(column[item], end='')
        # Once a row of data has been printed on the same line, print a new line
        print('')


sample_data = test_data(10, 30)
padded_data = pad(sample_data)
output_data(sample_data)
output_data(padded_data)