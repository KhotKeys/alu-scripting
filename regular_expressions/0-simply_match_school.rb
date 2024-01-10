#!/usr/bin/env ruby
# match_school.rb

def match_school(input)
  # Regular expression to match "School"
  regex = /\bSchool\b/

  # Check if the input matches the regular expression
  if input.match?(regex)
    puts "The input contains the word 'School'."
  else
    puts "The input does not contain the word 'School'."
  end
end

# Check if a command line argument is provided
if ARGV.empty?
  puts "Please provide a string as a command line argument."
else
  # Get the first command line argument
  input_string = ARGV[0]

  # Call the match_school method with the input string
  match_school(input_string)
end
